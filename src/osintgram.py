
from datetime import datetime
from geopy.geocoders import Nominatim

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

    def get_addrs(self):
        geodata = self.wrapper.get_post_geodata()
        for g in geodata:
            address = self.geolocator.reverse(f"{g['coordinates']['lat'], g['coordinates']['long']}")
            dt = datetime.fromtimestamp(g['timestamp'])

    def clear_cache(self):
        pass

    def get_captions(self):
        captions = self.wrapper.get_post_captions()

    def get_comment_data(self):
        data = self.wrapper.get_comments()

    def get_total_comments(self):
        pass

    def get_followers(self):
        pass

    def get_followings(self):
        pass

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

    def get_hashtags(self):
        pass

    def get_user_info(self):
        pass

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