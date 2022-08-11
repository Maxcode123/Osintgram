
from datetime import datetime
from typing import Dict, List, Optional
from geopy.geocoders import Nominatim
from .dtos import Comment, PostAddress, User, UserInfo

from instagram_wrapper import InstagramWrapper



class Osintgram:

    def __init__(
        self,
        instagram_wrapper: InstagramWrapper,
        geolocator: Nominatim
        ) -> None:
        self.wrapper = instagram_wrapper
        self.geolocator = geolocator

    def change_target(self, target_username: str) -> None:
        self.wrapper.set_user(target_username)

    def get_addrs(self) -> List[PostAddress]:
        addrs = []
        geodata = self.wrapper.get_post_geodata()
        for g in geodata:
            address = self.geolocator.reverse(f"{g['coordinates']['lat'], g['coordinates']['long']}")
            dt = datetime.fromtimestamp(g['timestamp'])
            addrs.append({'address': address, 'timestamp': dt})
        return addrs

    def clear_cache(self):
        pass

    def get_captions(self) -> List[str]:
        return self.wrapper.get_post_captions()

    def get_comment_data(self) -> List[Comment]:
        return self.wrapper.get_comments()

    def get_total_comments(self) -> Dict[str, int]:
        posts = self.wrapper.get_posts()
        t_comments = {'comment_counter': 0, 'posts': 0}
        for p in posts:
            t_comments['comment_counter'] += p['comment_count']
            t_comments['posts'] += 1
        return t_comments

    def get_followers(self) -> List[User]:
        return self.wrapper.get_followers()

    def get_followings(self) -> List[User]:
        return self.wrapper.get_followings()

    def get_fwersemail(self):
        pass

    def get_fwersnumber(self):
        pass

    def get_followers_subset(self):
        pass

    def get_fwingsemail(self):
        pass

    def get_fwingsnumber(self):
        pass

    def get_followings_subset(self):
        pass

    def get_hashtags(self) -> Optional[Dict[str, int]]:
        captions = self.wrapper.get_post_captions()
        hashtags = []
        for c in captions:
            for s in c.split():
                if s.startswith('#'):
                    hashtags.append(s.encode('UTF-8'))
        if len(hashtags) > 0:
            hashtag_counter = {}
            for i in hashtags:
                if i in hashtag_counter:
                    hashtag_counter[i] += 1
                else:
                    hashtag_counter[i] = 1
            ssort = sorted(hashtag_counter.items(), key=lambda tpl: tpl[1], reverse=True)
            return ssort
        return None

    def get_user_info(self) -> UserInfo:
        return self.wrapper.get_user_info()

    def get_total_likes(self):
        pass

    def get_media_type(self):
        pass

    def get_photo_description(self):
        pass

    def get_user_photo(self):
        pass

    def get_user_propic(self):
        pass

    def get_user_stories(self):
        pass

    def get_people_tagged_by_user(self):
        pass

    def change_target(self):
        pass

    def get_people_who_commented(self):
        pass

    def get_people_who_tagged(self):
        pass