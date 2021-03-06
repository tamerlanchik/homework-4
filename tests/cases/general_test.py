from tests.cases.base import TestAuthorized
from tests.pages.general import GeneralPage
from tests.pages.pin import PinDetailsPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = GeneralPage(self.driver)

    def test_open_pin(self):
        name, link = self.page.form.click_first_pin()
        page = PinDetailsPage(self.driver, False)
        real_name = page.form.get_title()
        self.assertEqual(real_name, name, "Opened wrong pin")
        self.assertEqual(self.driver.current_url, link, "Wrong page got from router")
