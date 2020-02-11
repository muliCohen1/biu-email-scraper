from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import input_output

class BIUEmailScraper:

    driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        
    def login(self, user_name, user_password):
        self.driver.get("https://lemida.biu.ac.il/")
        # time.sleep(2)  #sleeping prevents element latency creation problems. muliCohen
        username = self.driver.find_element_by_id("login_username")
        password = self.driver.find_element_by_id("login_password")
        username.send_keys(user_name)
        password.send_keys(user_password)
        self.driver.find_element_by_css_selector("input[type='submit']").click()

    def get_emails(self, students_sum, course_url, element_path):
        counter = 0
        while counter < students_sum:
            self.driver.get(course_url)
            self.driver.find_element_by_xpath(element_path + str(counter) + "_c0']/a").click()
            element = self.driver.find_element_by_xpath("//*[@id='adaptable_profile_tree']/div[1]/div/div/section/ul/li[4]/span").text
            input_output.write_file(element)
            print(element)
            counter += 1

email_scrpaper = BIUEmailScraper()
email_scrpaper.login('*********', '*********')
email_scrpaper.get_emails(57, "https://lemida.biu.ac.il/user/index.php?contextid=1347096&id=48684&perpage=100", "//*[@id='user-index-participants-48684_r") #changeable arguments. muliCohen