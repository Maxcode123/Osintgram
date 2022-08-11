from typing import Dict, List, Optional

from instagram_private_api import (
    Client,
    ClientCookieExpiredError,
    ClientLoginRequiredError,
    ClientError,
    ClientThrottledError,
)

from dtos import Comment, Coordinates, GeoData, Post, User

def following_validator(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            if self._following_user:
                result = func(*args, **kwargs)
                return result
            else:
                raise Exception('Not following user')
        return wrapper

class InstagramWrapper:
    _feed: Optional[List[Post]] = None
    _user: Optional[User] = None
    _following_user: bool = False
    _tokens: Optional[Dict[str, str]] = None

    def __init__(self, instagram_client: Client, username: str) -> None:
        self.instagram_client = instagram_client
        self._init_user(username)

    def set_user(self, username: str) -> None:
        self._init_user(username)

    @following_validator
    def get_post_geodata(self) -> List[GeoData]:
        geodata = []
        for post in self._feed:
            if 'location' in post and post['location'] is not None:
                if 'lat' in post['location'] and 'lng' in post['location']:
                    geodata.append(GeoData(
                        coordinates=Coordinates(
                            lat=post['location']['lat'],
                            long=post['location']['lng'],
                            ),
                        timestamp=post.get('taken_at')
                    ))
        return geodata

    @following_validator
    def get_post_captions(self) -> List[str]:
        captions = []
        for post in self._feed:
            if 'caption' in post and post['caption'] is not None:
                captions.append(post['caption']['text'])
        return captions

    @following_validator
    def get_comments(self) -> List[Comment]:
        comments = []
        for post in self._feed:
            post_id = post.get('id')
            post_comments = self.instagram_client.media_n_comments(post_id)
            for c in post_comments:        
                comments.append(Comment(
                    post_id=post_id,
                    user_id=c.get('user_id'),
                    username=c.get('user').get('username'),
                    text=c.get('text')
                ))
        return comments

    @following_validator
    def get_followers(self) -> List[User]:
        followers = []
        next_max_id = 1
        while next_max_id:
            results = self.instagram_client.user_followers(str(self._user['id']), self._tokens['followers'])
            users = [User(id=r['pk'], is_private=r['is_private']) for r in results.get('users', [])]
            followers.extend(users, [])
            next_max_id = results.get('next_max_id')
        return followers

    @following_validator
    def get_followings(self) -> List[User]:
        followings = []
        next_max_id = 1
        while next_max_id:
            results = self.instagram_client.user_following(str(self._user['id']), self._tokens['followings'])
            users = [User(id=r['pk'], is_private=r['is_private']) for r in results.get('users', [])]
            followings.extend(users, [])
            next_max_id = results.get('next_max_id')
        return followings    

    def _init_user(self, username: str) -> None:
        content = self.instagram_client.username_info(username)
        self._user = User(
            id=content['user']['pk'],
            is_private=content['user'['is_private']],
            )
        self._feed = self._get_feed(self._user['id'])
        self._tokens = self._generate_tokens()
        self._following_user = self._check_following()
    
    def _get_feed(self, user_id: int) -> List[Post]:
        feed = []
        next_max_id = 1
        while next_max_id:
            result = self.instagram_client.user_feed(str(user_id))
            feed.extend(result.get('items', []))
            next_max_id = result.get('next_max_id')
        return feed

    def _generate_tokens(self) -> Dict[str, str]:
        t = {
            "followers": Client.generate_uuid(),
            "followings": Client.generate_uuid(),
        }
        return t

    def _check_following(self) -> bool:
        if str(self._user['id']) == self.instagram_client.authenticated_user_id:
            return True
        endpoint = 'users/{user_id!s}/full_detail_info/'.format(**{'user_id': self._user['id']})
        user_info = self.instagram_client._call_api(endpoint)
        following = user_info['user_detail']['user']['friendship_status']['following']
        return following
