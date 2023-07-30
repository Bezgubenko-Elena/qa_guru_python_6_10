from dataclasses import dataclass
import enum


class Gender(enum.Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

class State(enum.Enum):
    NCR = 'NCR'
    UT = 'Uttar Pradesh'
    Haryana = 'Haryana'
    Rajasthan = 'Rajasthan'

class City(enum.Enum):
    Delhi
    Gurgaon
    Noida

    Agra
    Lucknow
    Merrut

    Karnal
    Panipat

    Jaipur
    Jaiselmer


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: int
    date_of_birth: datetime    #????
    subjects: tuple
    hobbies: tuple
    picture: str #????
    current_address: str
    state: str
    city: str



