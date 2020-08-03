from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from model import Question
import time
class ProgHubParser():

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_tests_page()
        self.parse_question_page()


    def go_to_tests_page(self):
        self.driver.get("https://proghub.ru/tests")
        carousel_card = self.driver.find_elements_by_class_name("carousel__card")

        for card in carousel_card:
            lang_link = card.get_attribute("href")
            # print(lang_link)

            if self.lang in lang_link:
                # language = lang_link.split("/")[-1]
                # self.driver.get("https://proghub.ru/q/00edd5/")
                self.driver.get("https://proghub.ru/t/python-3-basic")
                btn_elem = self.driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[1]/div[3]/div/div[2]/div[2]/a")
                btn_elem.click()
                time.sleep(2)
                break

    def parse_question_page(self):
        question = Question()
        self.fill_question_text(question)
        self.fill_question_code(question)
        self.fill_question_answer(question)
        print(question)

    def fill_question_text(self, question):
        try:
            question_text_elm = self.driver.find_element_by_class_name("title")
            question.text = question_text_elm.text
        except NoSuchElementException:
            print("Question text missing")

    def fill_question_code(self, question):
        try:
            code_elm = self.driver.find_element_by_class_name("code")
            question.code = code_elm.text
        except NoSuchElementException:
            pass

    def fill_question_answer(self, question):
        try:
            answer_elm = self.driver.find_elements_by_xpath("//*[@id='__next']/div[2]/div[3]/div[2]/div[2]")
            for elm in answer_elm:
                question.answer = elm.text
        except NoSuchElementException:
            pass



def main():
    driver = webdriver.Chrome()
    parser = ProgHubParser(driver, "python")
    parser.parse()


if __name__ == "__main__":
    main()
