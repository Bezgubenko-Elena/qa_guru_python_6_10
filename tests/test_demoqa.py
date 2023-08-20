from qa_guru_python_6_10.page import RegistrationPage


def test_success_registration(browser_open):
    registration_page = RegistrationPage()
    # fill form
    registration_page.open()
    registration_page.fill_first_name('Helen')
    registration_page.fill_last_name('Bezgubenko')
    registration_page.fill_email('eb@gmail.com')
    registration_page.fill_gender('Female')
    registration_page.fill_mobile_number(9011111111)
    registration_page.fill_date_of_birth('1993', '11', '01')
    registration_page.fill_subjects('Maths', 'Arts', 'Commerce', 'Economics')
    registration_page.fill_hobbies('Music', 'Sports', 'Reading')
    registration_page.upload_picture('h.jpg')
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
