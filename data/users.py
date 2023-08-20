from dataclasses import dataclass
import enum
import datetime

"""
class Gender(enum.Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class State(enum.Enum):
    NCR = 'NCR'
    UP = 'Uttar Pradesh'
    HARYANA = 'Haryana'
    RAJASTHAN = 'Rajasthan'


class City(enum.Enum):
        DELHI = 'Delhi'
        GURGAON = 'Gurgaon'
        NOIDA = 'Noida'
        AGRA = 'Agra'
        LUCKNOW = 'Lucknow'
        MERRUR = 'Merrut'
        KARNAL = 'Karnal'
        PANIPAT = 'Panipat'
        JAIPUR = 'Jaipur'
        JAISELMER = 'Jaiselmer'
"""
@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: int
    date_of_birth: datetime.date
    subjects: tuple
    hobbies: tuple
    picture: str
    current_address: str
    state: str
    city: str




