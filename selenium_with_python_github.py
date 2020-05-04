from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import os
import time


class TestSuit(unittest.TestCase):

    def setUp(self):
        webdriver_location = 'C:\\WebDrivers\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = webdriver_location
        self.driver = webdriver.Chrome(webdriver_location)
        self.adress_location = "http://automationpractice.com/index.php"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_by_xpath(self):
        self.driver.get(self.adress_location)
        
        #ruhadarab kereses es hozzaadas
        Blouse_Block = self.driver.find_element_by_xpath(" //ul[@id='homefeatured']//li[2]//div[1]//div[1]//div[1]//a[1]//img[1]") 
        Blouse_Block.click()
     
        Add_to_card = self.driver.find_element_by_xpath("//button[@name='Submit']")
        Add_to_card.click()
        
        Checkout_button = self.driver.find_element_by_xpath("//div[@id='layer_cart']//div//div//div//a")
        Checkout_button.click()

        Proceed_to_checkout = self.driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']")
        Proceed_to_checkout.click()
        
        #regisztracio
        email_address = self.driver.find_element_by_xpath("//input[@id='email_create']")
        email_address.send_keys("proba7@gmail.com")

        create_account = self.driver.find_element_by_xpath("//button[@id='SubmitCreate']")
        create_account.click()

        radio_button = self.driver.find_element_by_xpath("//div[@class='clearfix']//div[1]//label[1]")
        radio_button.click()

        first_name = self.driver.find_element_by_xpath("//input[@id='customer_firstname']")
        first_name.send_keys("Reka")

        last_name = self.driver.find_element_by_xpath("//input[@id='customer_lastname']")
        last_name.send_keys("Marton")

        email_box = self.driver.find_element_by_xpath("//input[@id='email']")
        email_box.click()

        password_box = self.driver.find_element_by_xpath("//input[@id='passwd']")
        password_box.send_keys("Password231")

        date_of_birth = self.driver.find_element_by_xpath("//div[@id='uniform-days']//option[2]")
        date_of_birth.click()

        date_of_birth = self.driver.find_element_by_xpath("//option[contains(text(),'January')]")
        date_of_birth.click()

        date_of_birth = self.driver.find_element_by_xpath("//option[contains(text(),'2004')]")
        date_of_birth.click()
        
        #szamlazasi cim 
        address_first_name = self.driver.find_element_by_xpath("//input[@id='firstname']")
        address_first_name.send_keys("Reka")

        address_last_name = self.driver.find_element_by_xpath("//input[@id='lastname']")
        address_last_name.send_keys("Marton")

        address_company = self.driver.find_element_by_xpath("//input[@id='company']")
        address_company.send_keys("Codespring")

        address = self.driver.find_element_by_xpath("//p[4]//input[1]")
        address.send_keys("str.Frunzisului nr.29")

        address_city = self.driver.find_element_by_xpath("//p[6]//input[1]")
        address_city.send_keys("Cluj-Napoca")

        address_state = self.driver.find_element_by_xpath("//option[contains(text(),'Alaska')]")
        address_state.click()

        address_postal_code = self.driver.find_element_by_xpath("//input[@class='form-control uniform-input text']")
        address_postal_code.send_keys("42701")

        address_state = self.driver.find_element_by_xpath("//option[contains(text(),'United States')]")
        address_state.click()

        address_mobilephone = self.driver.find_element_by_xpath("//p[13]//input[1]")
        address_mobilephone.send_keys("0742425252")

        address = self.driver.find_element_by_xpath("//p[14]//input[1]")
        address.send_keys("str.Frunzisului nr.29")
        
        #regisztracio megerositese
        register_button = self.driver.find_element_by_xpath("//button[@class='btn btn-default button button-medium']")
        register_button.click()
        
        #Cim megerosites
        check = self.driver.find_element_by_xpath("//button[@class='button btn btn-default button-medium']//span[contains(text(),'Proceed to checkout')]")
        check.click()
        self.driver.implicitly_wait(20)
        
        #kiszallitas feltetel elfogadasa
        checkbox = self.driver.find_element_by_xpath("//div[@class='checker']//span//input")
        checkbox.click()

        check = self.driver.find_element_by_xpath("//button[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]")
        check.click()

        #fizetesmod kivalasztasa
        check_pay = self.driver.find_element_by_xpath("//a[@class='cheque']")
        check_pay.click()

        #megerosites
        confirm = self.driver.find_element_by_xpath("//span[contains(text(),'I confirm my order')]")
        confirm.click()

        #assert
        confirmation_box = self.driver.find_element_by_xpath("//p[@class='alert alert-success']")
        print(confirmation_box.text)
        self.assertEqual(confirmation_box.text,"Your order on My Store is complete.")

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)
    time.sleep(1000)
