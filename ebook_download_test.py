import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class SalesManagoTest(unittest.TestCase):

    def setUp(self):
        print('Start of the test!')
        self.driver = webdriver.Firefox()

    def test_get_ebook(self):
        driver = self.driver
        print('Lets go to the site')
        driver.get("https://www.salesmanago.com/")
        time.sleep(5)
        self.assertIn(driver.title, 'SALESmanago – AI Customer Data Platform with Omnichannel Execution')

        # print('Lets get rid off the pop-up.')
        # driver.switch_to.frame(driver.find_element_by_id('bhr-iframe-consent-form'))
        # time.sleep(5)
        # not_now_button = driver.find_element_by_css_selector('button.wpc_w_f_c_b-n')
        # not_now_button.click()
        # time.sleep(5)

        print('Lets get to the site with ebooks')
        resources_btn = driver.find_element_by_link_text('resources')
        action = ActionChains(driver)
        hover = action.move_to_element(resources_btn)
        hover.perform()
        ebook_button = driver.find_element_by_link_text('Ebooks')
        ebook_button.click()
        time.sleep(4)

        print('Lets choose the ebook')
        ebook_title = 'definitive-guide-to-email-deliverability'
        chosen_ebook = driver.find_element_by_xpath(f"//a[@href='https://www.salesmanago.com/info/{ebook_title}.htm']")
        chosen_ebook.click()
        time.sleep(5)

        print('Lets switch the tab')
        driver.switch_to.window(driver.window_handles[-1])

        input_name = driver.find_element_by_name('name')
        input_email = driver.find_element_by_name('email')
        input_company = driver.find_element_by_name('company')
        input_url = driver.find_element_by_name('url')
        input_phone = driver.find_element_by_name('phoneNumber')
        submit_button = driver.find_element_by_xpath("//form[@id='uspForm']/div/div/button")

        print('Lets fill out the form')
        time.sleep(2)
        input_name.send_keys('Test')
        time.sleep(2)
        input_email.send_keys('olga.lepecka.benhauer+test@salesmanago.com')
        time.sleep(2)
        input_company.send_keys('Testing comp.')
        time.sleep(2)
        input_url.send_keys('www.test.pl')
        time.sleep(2)
        input_phone.send_keys('510510510')
        time.sleep(2)
        submit_button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()