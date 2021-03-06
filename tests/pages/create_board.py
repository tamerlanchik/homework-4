from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class CreateBoardPage(Page):
    PATH = "/create_board"

    ROOT = {
        "method": By.XPATH,
        "key": Page.get_xpath_visible('//div[@id="createboard-page"]'),
    }

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form_list(self):
        return FindCreateBoardForm(self.driver)

    @property
    def form_concrete(self):
        return ConcreteUserMessagesForm(self.driver)


class FindCreateBoardForm(FormComponent):
    board_name = '//input[@id="boardname"]'
    board_content = '//input[@id="boardcontent"]'
    error_line = '//div[@id="createBoardError"]'
    create_button = (
        '//input[@class="createboard-form__button-save create-form__button-save_pos"]'
    )
    back_button = '//a[@id="createBoardViewButtonsExit"]'

    def set_board_name(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.board_name), query)

    def set_board_content(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.board_content), query)

    def create_board(self):
        self.driver.find_element_by_xpath(self.create_button).click()

    def go_back(self):
        self.driver.find_element_by_xpath(self.back_button).click()

    def get_error(self):
        return self.driver.find_element_by_xpath(self.error_line).text


class ConcreteUserMessagesForm(FormComponent):
    section_name = '//div[@id="profilePinsBoardsView"]'
    boards_list = '//div[@class="board-for-user-view__content"]'
    boards_href_list = '//div[@class="board-for-user-view"]'

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)

    def get_id_by_board_name(self, board_name):
        for board in self.get_href_boards_list():
            board_text = board.find_element_by_tag_name("div")
            if board_text.text == board_name:
                return board.find_element_by_tag_name("a").get_attribute("href")[30:]

    def get_boards_list(self):
        return self.driver.find_elements_by_xpath(self.boards_list)

    def find_board(self, board_name):
        board_list = self.get_boards_list()
        for board in board_list:
            if board.text == board_name:
                return True
        return False

    def get_href_boards_list(self):
        return self.driver.find_elements_by_xpath(self.boards_href_list)
