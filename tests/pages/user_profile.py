from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.solarsunrise_urls import SettingsPage


class ProfilePage(Page):
    PATH = '/profile'
    ROOT = {
        'method': By.ID,
        'key': 'profile-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def form(self):
        return ProfileForm(self.driver)


class ProfileForm(FormComponent):
    question_btn = '//img[@id="buttonForAsk"]'
    question_field = '//textarea[@id="profileMessageTextArea"]'
    submit_button = '//input[@class="feedback__form__button"]'

    settings_profile_btn = '//img[@data-section="/settings"]'
    menu_btn = '//img[@id="headerView"]'
    settings_menu_btn = '//a[@href="/settings"]'

    def set_question(self, question):
        self.fill_input(self.driver.find_element_by_xpath(self.question_field), question)

    def submit(self, name):
        self.driver.find_element_by_xpath(name).click()

    def create_message(self, question):
        self.submit(self.question_btn)
        self.set_question(question)
        self.submit(self.submit_button)
        self.submit(self.question_btn)
        self.submit(self.question_btn)
        assert self.get_value_elem_text(self.question_field) == '', 'Error sending message'

    def go_to_settings_from_menu(self):
        self.submit(self.menu_btn)
        self.submit(self.settings_menu_btn)
        SettingsPage(self.driver, open=False).wait_for_load()

    def go_to_settings_from_profile(self):
        self.submit(self.settings_profile_btn)
        SettingsPage(self.driver, open=False).wait_for_load()
