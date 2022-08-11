from datetime import datetime
from typing import TypedDict


class Post(TypedDict):
    id: str

class User(TypedDict):
    id: int
    is_private: bool

class Coordinates(TypedDict):
    lat: float
    long: float

class GeoData(TypedDict):
    coordinates: Coordinates
    timestamp: int

class Comment(TypedDict):
    post_id: str
    user_id: int
    username: str
    text: str
