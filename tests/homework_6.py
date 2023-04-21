import datetime


def test_dark_theme_by_time():
    current_time = datetime.time(hour=23)
    real_time = datetime.datetime.now()
    if 22 <= current_time.hour <= 23 or 0 <= current_time.hour <= 6:
        is_dark_theme = True
        print(f"dark theme enabled, current time {real_time.strftime('%H:%M:%S')}")
    else:
        is_dark_theme = False
        print(f"Light theme enabled, current time {real_time.strftime('%H:%M:%S')}")
    assert is_dark_theme is True


if __name__ == '__main__':
    print(test_dark_theme_by_time())


def test_dark_theme_by_time_and_user_choice():
    current_time = datetime.time(hour=23)
    dark_theme_enabled_by_user = True
    real_time = datetime.datetime.now()
    is_dark_theme = True
    if dark_theme_enabled_by_user == True:
        is_dark_theme = True
        print(f"dark theme enabled, current time {real_time.strftime('%H:%M:%S')}")
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = False
        print(f"dark theme is off, current time {real_time.strftime('%H:%M:%S')}")

    elif dark_theme_enabled_by_user == None:
        if 22 <= current_time.hour <= 23 or 0 <= current_time.hour <= 6:
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


if __name__ == '__main__':
    print(test_dark_theme_by_time_and_user_choice())


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = list(filter(lambda x: x.get('name') == 'Olga', users))[0]
    assert suitable_users == {"name": "Olga", "age": 45}
    suitable_users = list(filter(lambda x: x.get('age') < 20, users))
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


if __name__ == '__main__':
    print(test_find_suitable_user())


def hello_decorator(func, *args):
    separated_tuple = ', '.join(args)
    result = string.capwords(f'{func.__name__.replace("_", " ")}') + f' [{separated_tuple}]'
    print(result, end='\n')
    return result


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = hello_decorator(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = hello_decorator(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = hello_decorator(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
