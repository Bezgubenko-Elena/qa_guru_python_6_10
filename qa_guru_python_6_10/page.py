import os
from selene import browser
from selene import have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)

    def fill_email(self, value):
        browser.element('[id="userEmail"]').type(value)

    def fill_gender(self, value):
        if value in ('Male', 'Female', 'Other'):
            browser.all('#genterWrapper .custom-control').element_by(have.exact_text(value)).click()

    def fill_mobile_number(self, value):
        browser.element('[id="userNumber"]').type(str(value))

    def fill_date_of_birth(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{int(month) - 1}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    def fill_subjects(self, *args):
        for arg in args:
            if arg in (
                    'Maths',
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
                    'History'
            ):
                browser.element('[id="subjectsInput"]').type(arg).press_enter()
            else:
                continue

    def fill_hobbies(self, *args):
        for arg in args:
            if arg in ('Sports', 'Reading', 'Music'):
                browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text(arg)).click()
            else:
                continue

    def upload_picture(self, url):
        browser.element('[id="uploadPicture"]').send_keys(os.path.abspath(url))

    def fill_current_address(self, text):
        browser.element('[id="currentAddress"]').type(text)

    def fill_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('[id="submit"]').click()


    def should_values(self, *args):
        for i in range(len(args)):
            browser.all('.table-responsive .table tbody tr')[i].should(have.text(args[i]))