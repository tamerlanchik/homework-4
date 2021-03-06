from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class EditPinPage(Page):
    PATH = "/pin_change/{0}"

    ROOT = {
        "method": By.XPATH,
        "key": Page.get_xpath_visible('//div[@id="pinediting-page"]'),
    }

    def __init__(self, driver, pin_id):
        Page.__init__(self, driver)
        self.open(pin_id)

    @property
    def form_list(self):
        return FindEditPinForm(self.driver)

    @property
    def form_concrete(self):
        return ConcreteUserMessagesForm(self.driver)


class FindEditPinForm(FormComponent):
    pin_name = '//input[@id="pinname"]'
    pin_content = '//input[@id="pincontent"]'
    edit_pin_button = '//input[@class="createpin__buttons__button-save createpin__buttons__button-save_pos"]'
    boards_list = '//select[@id="createPinBoardSelect"]'
    change_pin_button_click = '//div[@id="createPinBoardSelect"]'

    def set_pin_name(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.pin_name), query)

    def set_pin_content(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.pin_content), query)

    def edit_pin(self):
        self.driver.find_element_by_xpath(self.edit_pin_button).click()

    def get_error(self, pin_id):
        error_line = '//div[@id="createPinError/pin_change/' + str(pin_id) + '"]'
        return self.driver.find_element_by_xpath(error_line).text

    def set_select_board(self, board_id):
        select = self.driver.find_element_by_name("board-select")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == board_id:
                option.click()
                return

    def go_back(self, pin_id):
        back_button = '//a[@id="pinEditingButtonsExit/pin_change/' + str(pin_id) + '"]'
        self.driver.find_element_by_xpath(back_button).click()

    def delete_pin(self, pin_id):
        back_button = '//div[@id="PinDel/pin_change/' + str(pin_id) + '"]'
        self.driver.find_element_by_xpath(back_button).click()


class ConcreteUserMessagesForm(FormComponent):
    section_name = '//div[@id="profilePinsBoardsView"]'
    boards_list = '//div[@class="board-for-user-view__content"]'

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)

    def get_boards_list(self):
        return self.driver.find_elements_by_xpath(self.boards_list)
