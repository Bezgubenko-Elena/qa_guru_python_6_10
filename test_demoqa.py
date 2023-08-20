import datetime
from data.users import User
from qa_guru_python_6_10.page import RegistrationPage


def test_success_registration():
    registration_page = RegistrationPage()

    user1 = User(
        first_name='Helen',
        last_name='Bezgubenko',
        email='eb@gmail.com',
        gender='Female',
        mobile_number=9011111111,
        date_of_birth=datetime.date(1993, 11, 1),
        subjects=('Maths', 'Arts', 'Commerce', 'Economics'),
        hobbies=('Music', 'Sports', 'Reading'),
        picture='resources\h.jpg',
        current_address='Istr Street, 17, 21',
        state='NCR',
        city='DELHI'
    )

    registration_page.open()

    registration_page.register(user1)

    registration_page.should_have_registered(user1)
