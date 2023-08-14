import datetime
import os
from selene import browser
from selene import have

from data.users import Gender, State, User, City
from qa_guru_python_6_10.page import RegistrationPage

user1 = User(
        first_name='Helen',
        last_name='Bezgubenko',
        email='eb@gmail.com',
        gender=Gender.FEMALE,
        mobile_number=9011111111,
        date_of_birth=datetime.date(1993, 11, 1),
        subjects=('Maths', 'Arts', 'Commerce', 'Economics'),
        hobbies=('Music', 'Sports', 'Reading'),
        picture='resources\h.jpg',
        current_address='Istr Street, 17, 21',
        state=State.NCR,
        city=City.GURGAON
    )

def test_success_registration(browser_open):
    registration_page = RegistrationPage()
    # fill form
    registration_page.fill_mobile_number(9011111111)
    registration_page.fill_date_of_birth('1993', '11', '01')
    registration_page.fill_subjects('Maths', 'Arts', 'Commerce', 'Economics')
    registration_page.fill_hobbies('Music', 'Sports', 'Reading')
    registration_page.upload_picture('resources\h.jpg')
    registration_page.fill_current_address('Spark Street, 17')
    registration_page.fill_state_and_city('NCR', 'Delhi')
    registration_page.submit()

    # check form
    registration_page.should_values('Helen Bezgubenko',
                                    'eb@gmail.com',
                                    'Female',
                                    '9011111111',
                                    '01 November,1993',
                                    'Maths, Arts, Commerce, Economics',
                                    'Music, Sports, Reading',
                                    'h.jpg',
                                    'Spark Street, 17',
                                    'NCR Delhi'
                                    )
