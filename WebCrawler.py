print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

from time import sleep
from selenium import webdriver
from selenium.webdriver.common import by as BY
from selenium.webdriver.remote.webelement import WebElement
# from random import uniform

# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"


class WebCrawler:
    driver: webdriver

    def __init__(self,
                 driver: webdriver):
        print("__init__()")
        self.driver = driver

    def open_url(self, url: str, load_time: float = 5):
        self.driver.get(url)
        if load_time > 0:
            sleep(load_time)

    def scroll_to_bottom_by(self, reload_time: float = 1, **by_identifier_dict) -> bool:
        print(type(by_identifier_dict))
        print(f'scroll_to_bottom_by -> (reload_time={reload_time})')
        try:
            scroll_box = self.get_item_by(by_identifier_dict)
            last_height, current_height = 0, 1
            while last_height != current_height:
                last_height = current_height
                if reload_time > 0 and last_height > 0:
                    sleep(reload_time)
                current_height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        except Exception as ex:
            print(f'failed to scroll to bottom => {ex}')
        return False

    def find_item_by(self, **by_identifier_dict) -> bool:
        print(f'find_item_by')
        try:
            item = self.get_item_by(by_identifier_dict)
            return bool(item)
        except Exception as ex:
            print(f'failed to find item => {ex}')
        return False

    def find_items_by(self, **by_identifier_dict) -> bool:
        print(f'find_items_by')
        try:
            items = self.get_items_by(by_identifier_dict)
            return len(items) > 0
        except Exception as ex:
            print(f'failed to find items => {ex}')
        return False

    def fill_item_by(self, content: str, **by_identifier_dict) -> bool:
        print(f'fill_item_by -> ({content})')
        try:
            item = self.get_item_by(by_identifier_dict)
            item.send_keys(content)
            return True
        except Exception as ex:
            print(f'failed to fill item with \"{content}\" => {ex}')
        return False

    def click_item_by(self, use_js_click: bool = False, **by_identifier_dict) -> bool:
        print(f'click_item_by -> ("use_js_click="{use_js_click})')
        try:
            item = self.get_item_by(by_identifier_dict)
            if item:
                if use_js_click:
                    self.driver.execute_script("arguments[0].click();", item)
                else:
                    item.click()
                return True
        except Exception as ex:
            print(f'failed to click item => {ex}')
        return False

    def get_attributes_by(self,  attribute: str, validator, **by_identifier_dict) -> list:
        print(f'get_attributes_by -> ({by_identifier_dict}, {attribute})')
        try:
            items = self.get_items_by(by_identifier_dict)
            if items:
                return [attr for attr in (item.get_attribute(attribute) for item in items) if validator(attr)]
        except Exception as ex:
            print(f'failed to get attributes \"{attribute}\" => {ex}')
        return []

    def get_item_by(self, by_identifier_dict: dict):
        print(f'get_item_by -> ({by_identifier_dict})')
        try:
            iterations: int = 0
            for by, identifier in by_identifier_dict.items():
                iterations += 1
                if iterations > 1:
                    item = item.find_element(identifier[0], identifier[1])
                else:
                    item = self.driver.find_element(identifier[0], identifier[1])
            return item
        except Exception as ex:
            print(f'failed in iteration {iterations} to find item by {by_identifier_dict} => {ex}')
        return False

    def get_items_by(self, by_identifier_dict: dict):
        print(f'get_items_by -> ({by_identifier_dict})')
        try:
            iterations: int = 0
            last_iteration = len(by_identifier_dict)
            for key, by_identifier in by_identifier_dict.items():
                iterations += 1
                if iterations > 1:
                    if iterations == last_iteration:    # other steps on dict with 1 item
                        item = item.find_elements(by_identifier[0], by_identifier[1])
                        return item
                    else:                               # other steps on dict with n items
                        item = item.find_element(by_identifier[0], by_identifier[1])
                else:
                    if iterations == last_iteration:    # first step on dict with 1 item
                        item = self.driver.find_elements(by_identifier[0], by_identifier[1])
                        return item
                    else:                               # first step on dict with n items
                        item = self.driver.find_element(by_identifier[0], by_identifier[1])
        except Exception as ex:
            print(f'failed in iteration {iterations} to find items by {by_identifier_dict} => {ex}')
        return False