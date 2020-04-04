from WebCrawler import WebCrawler
from selenium import webdriver
from unittest import TestCase
import os


# https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#
# https://docs.python.org/2/library/unittest.html#


class TestWebCrawler(TestCase):
    def setUp(self):
        webdriver_options = webdriver.chrome.options.Options()
        webdriver_options.add_argument('--headless')
        webdriver_options.add_argument('--no-sandbox')
        webdriver_options.add_argument('--disable-dev-shm-usage')
        webdriver_test = webdriver.Chrome(options=webdriver_options)
        self.crawler = WebCrawler(webdriver_test)
        # https://stackoverflow.com/a/53347438/9351796
        html_file = os.getcwd() + "//" + "test_WebPage.html"
        self.crawler.open_url("file:///" + html_file, load_time=0)

    def tearDown(self):
        self.crawler.driver.quit()


class TestOpenUrl(TestWebCrawler):
    def test_open_url(self):
        self.assertEqual(self.crawler.driver.title, "MyFirstUnitTestInPython")


# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

# https://selenium-python.readthedocs.io/locating-elements.html
class TestFindItemBy(TestWebCrawler):
    def test_find_item_by_id_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["id", "list_item_0001"]))

    def test_find_item_by_id_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["id", "not_in_my_html"]))

    def test_find_item_by_xpath_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["xpath", "//button[contains(@data-user-id, '0001') and contains(.//div, 'Follow')]"]))

    def test_find_item_by_xpath_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["xpath", "//button[contains(@data-user-id, '0011') and contains(.//div, 'Follow')]"]))

    def test_find_item_by_link_text_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["link text", "user_0001"]))

    def test_find_item_by_link_text_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["link text", "user_0011"]))

    def test_find_item_by_partial_link_text_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["partial link text", "0001"]))

    def test_find_item_by_partial_link_text_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["partial link text", "0011"]))

    def test_find_item_by_name_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["name", "follower-list"]))

    def test_find_item_by_name_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["name", "following-list"]))

    def test_find_item_by_tag_name_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["tag name", "ol"]))

    def test_find_item_by_tag_name_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["tag name", "h1"]))

    def test_find_item_by_class_name_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["class name", "some-info"]))

    def test_find_item_by_class_name_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["class name", "some-more-info"]))

    def test_find_item_by_css_selector_ok(self):
        self.assertTrue(self.crawler.find_item_by(item=["css selector", "span.follow"]))

    def test_find_item_by_css_selector_nok(self):
        self.assertFalse(self.crawler.find_item_by(item=["css selector", "span.follow-the-white-rabbit"]))


class TestFindItemsBy(TestWebCrawler):
    def test_find_items_by_id_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["id", "list_item_0001"]))

    def test_find_items_by_id_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["id", "not_in_my_html"]))

    def test_find_items_by_xpath_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["xpath", "//button[contains(@data-user-id, '0001') and contains(.//div, 'Follow')]"]))

    def test_find_items_by_xpath_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["xpath", "//button[contains(@data-user-id, '0011') and contains(.//div, 'Follow')]"]))

    def test_find_items_by_link_text_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["link text", "user_0001"]))

    def test_find_items_by_link_text_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["link text", "user_0011"]))

    def test_find_items_by_partial_link_text_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["partial link text", "0001"]))

    def test_find_items_by_partial_link_text_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["partial link text", "0011"]))

    def test_find_items_by_name_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["name", "follower-list"]))

    def test_find_items_by_name_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["name", "following-list"]))

    def test_find_items_by_tag_name_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["tag name", "ol"]))

    def test_find_items_by_tag_name_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["tag name", "h1"]))

    def test_find_items_by_class_name_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["class name", "some-info"]))

    def test_find_items_by_class_name_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["class name", "some-more-info"]))

    def test_find_items_by_css_selector_ok(self):
        self.assertTrue(self.crawler.find_items_by(item=["css selector", "span.follow"]))

    def test_find_items_by_css_selector_nok(self):
        self.assertFalse(self.crawler.find_items_by(item=["css selector", "span.follow-the-white-rabbit"]))


class TestFillItemBy(TestWebCrawler):
    def test_fill_item_by_id_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["id", "username"], content="test"))

    def test_fill_item_by_id_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["id", "email"], content="test"))

    def test_fill_item_by_xpath_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["xpath", "//*[@name='email']"], content="test"))

    def test_fill_item_by_xpath_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["xpath", "//*[@id='zip']"], content="test"))

    def test_fill_item_by_name_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["name", "email"], content="test"))

    def test_fill_item_by_name_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["name", "username"], content="test"))

    def test_fill_item_by_tag_name_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["tag name", "input"], content="test"))

    def test_fill_item_by_tag_name_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["tag name", "textbox"], content="test"))

    def test_fill_item_by_class_name_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["class name", "pass"], content="test"))

    def test_fill_item_by_class_name_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["class name", "password"], content="test"))

    def test_fill_item_by_css_selector_ok(self):
        self.assertTrue(self.crawler.fill_item_by(item=["css selector", "input.username"], content="test"))

    def test_fill_item_by_css_selector_nok(self):
        self.assertFalse(self.crawler.fill_item_by(item=["css selector", "input.address"], content="test"))


class TestClickItemBy(TestWebCrawler):
    def test_click_item_by_id_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["id", "login-btn"]))

    def test_click_item_by_id_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["id", "logout-btn"]))

    def test_click_item_by_xpath_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["xpath", "//button[contains(@class, 'button-sidebar')]"]))

    def test_click_item_by_xpath_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["xpath", "//button[contains(@class, 'button-headline')]"]))

    def test_click_item_by_link_text_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["link text", "Forgot Password"]))

    def test_click_item_by_link_text_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["link text", "Restore Password"]))

    def test_click_item_by_partial_link_text_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["partial link text", "Passw"]))

    def test_click_item_by_partial_link_text_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["partial link text", "Pssw"]))

    def test_click_item_by_name_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["name", "login"]))

    def test_click_item_by_name_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["name", "logout"]))

    def test_click_item_by_tag_name_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["tag name", "button"]))

    def test_click_item_by_tag_name_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["tag name", "h1"]))

    def test_click_item_by_class_name_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["class name", "button-sidebar"]))

    def test_click_item_by_class_name_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["class name", "button-headline"]))

    def test_click_item_by_css_selector_ok(self):
        self.assertTrue(self.crawler.click_item_by(item=["css selector", "button.button-sidebar"]))

    def test_click_item_by_css_selector_nok(self):
        self.assertFalse(self.crawler.click_item_by(item=["css selector", "button.button-headline"]))


class TestGetAttributesBy(TestWebCrawler):
    def test_get_attributes_by_id_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["id", "first-user"])))

    def test_get_attributes_by_id_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["id", "second-user"]))

    def test_get_attributes_by_xpath_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["xpath", "//a[contains(text(), 'user_0001')]"])))

    def test_get_attributes_by_xpath_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["xpath", "//a[contains(text(), 'not_in_my_html')]"]))

    def test_get_attributes_by_link_text_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["link text", "user_0001"])))

    def test_get_attributes_by_link_text_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["link text", "user_0011"]))

    def test_get_attributes_by_partial_link_text_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["partial link text", "user_"])))

    def test_get_attributes_by_partial_link_text_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["partial link text", "users_"]))

    def test_get_attributes_by_name_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["name", "first-user"])))

    def test_get_attributes_by_name_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["name", "second-user"]))

    def test_get_attributes_by_tag_name_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["tag name", "a"])))

    def test_get_attributes_by_tag_name_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["tag name", "h1"]))

    def test_get_attributes_by_class_name_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["class name", "some-username"])))

    def test_get_attributes_by_class_name_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["class name", "another-username"]))

    def test_get_attributes_by_css_selector_ok(self):
        self.assertTrue(bool(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["css selector", "a.some-username"])))

    def test_get_attributes_by_css_selector_nok(self):
        self.assertFalse(self.crawler.get_attributes_by(
            attribute="href",
            validator=lambda attr: attr is not None,
            item=["css selector", "a.another-username"]))

    """        
class TestScrollToBottom(TestWebCrawler):
    def test_scroll_to_bottom_by(self):
        self.fail()

class TestGetItemBy(TestWebCrawler):
    def test_get_item_by(self):
        self.fail()

class TestGetItemsBy(TestWebCrawler):
    def test_get_items_by(self):
        self.fail()
    """