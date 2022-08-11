from datetime import datetime
from typing import TypedDict


class Post(TypedDict):
    id: str
    comment_count: int

class PostAddress(TypedDict):
    address: str
    timestamp: datetime

class User(TypedDict):
    id: int
    username: str
    fullname: str
    is_private: bool

class UserInfo(TypedDict):
    user: User
    biography: str
    follower_count: int
    following_count: int
    business_account: bool
    business_category: str
    verified_account: bool
    email: str
    profile_pic_url: str
    fb_page: str
    whatsapp_number: str
    city_name: str
    address_street: str
    contact_phone_number: str

class Coordinates(TypedDict):
    lat: float
    long: float

class GeoData(TypedDict):
    coordinates: Coordinates
    timestamp: int

class Comment(TypedDict):
    post_id: str
    by_user: User
    text: str
