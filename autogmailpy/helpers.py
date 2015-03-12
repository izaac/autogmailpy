import os
from functools import wraps
import datetime

config = dict(
    email='nstest739@gmail.com',
    passwd_key='password',
)


def screenshot_on_error(test):

    @wraps(test)
    def wrapper(*args, **kwargs):
        try:
            test(*args, **kwargs)
        except:
            test_object = args[0]
            screenshot_dir = './screenshots'
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            date_string = datetime.datetime.now().strftime('%m%d%y-%H%M%S')
            filename = '{0}/SS-{1}-{2}.png'.format(screenshot_dir, test.__name__, date_string)
            test_object.driver.get_screenshot_as_file(filename)
            raise AssertionError
    return wrapper