__author__ = 'Jorge'


class HomePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = None

    def quit(self):
        self.driver.quit()

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, obj):
        self._driver = obj

    @property
    def wait(self):
        return self._wait

    @wait.setter
    def wait(self, obj):
        self._wait = obj