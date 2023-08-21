import os
from selene import browser
from selene import have
from tests.conftest import path_picture


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._fill_gender(user.gender)
        self.fill_mobile_number(user.mobile_number)
        self._fill_date_of_birth(user, user.date_of_birth)
        self._fill_subjects(*user.subjects)
        self._fill_hobbies(*user.hobbies)
        self._upload_picture(user.picture)
        self._fill_current_address(user.current_address)
        self._fill_state_and_city(user.state, user.city)
        self._submit()

    def should_have_registered(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.mobile_number}',
            f'{user.date_of_birth:%d} {user.date_of_birth:%B},{user.date_of_birth.year}',
            f'{", ".join(user.subjects)}',
            f'{", ".join(user.hobbies)}',
            f'{user.picture}',
            f'{user.current_address}',
            f'{user.state} {user.city}'
        ))

    def _fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)

    def _fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)

    def _fill_email(self, value):
        browser.element('[id="userEmail"]').type(value)

    def _fill_gender(self, value):
        if value in ('Male', 'Female', 'Other'):
            browser.all('#genterWrapper .custom-control').element_by(have.exact_text(value)).click()

    def fill_mobile_number(self, value):
        browser.element('[id="userNumber"]').type(str(value))

    def _fill_date_of_birth(self, user, date):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{date.year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{int(date.month) - 1}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{user.date_of_birth:%d}"]').click()

    def _fill_subjects(self, *args):
        for arg in args:
            if arg in ('Maths',
                       'Accounting',
                       'Arts',
                       'Social Studies',
                       'Biology',
                       'Physics',
                       'Computer Science',
                       'Chemistry',
                       'Commerce',
                       'Economics',
                       'Civics',
                       'English',
                       'Hindi',
                       'History'):
                browser.element('[id="subjectsInput"]').type(arg).press_enter()
            else:
                continue

    def _fill_hobbies(self, *args):
        for arg in args:
            if arg in ('Sports', 'Reading', 'Music'):
                browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text(arg)).click()
            else:
                continue

    def _upload_picture(self, url):
        browser.element('[id="uploadPicture"]').send_keys(os.path.join(path_picture, url))

    def _fill_current_address(self, text):
        browser.element('[id="currentAddress"]').type(text)

    def _fill_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(city)).click()

    def _submit(self):
        browser.element('[id="submit"]').click()
