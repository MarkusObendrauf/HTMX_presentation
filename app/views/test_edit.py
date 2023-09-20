from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from time import sleep

from app import models


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_edit_row(self):
        models.Contact2(
            first_name="Test", last_name="Tester", email="test.tester@example.com"
        ).save()
        self.selenium.get(f"{self.live_server_url}/edit-demo")

        edit_button = self.selenium.find_element(By.XPATH, '//button[text()="Edit"]')
        edit_button.click()

        first_name = self.selenium.find_element(By.NAME, "first_name")
        first_name.clear()
        first_name.send_keys("new_first_name")

        last_name = self.selenium.find_element(By.NAME, "last_name")
        last_name.clear()
        last_name.send_keys("new_last_name")

        email = self.selenium.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("new_email@example.com")

        confirm_button = self.selenium.find_element(
            By.XPATH, '//button[text()="Confirm"]'
        )
        confirm_button.click()

        contact = models.Contact2.objects.first()

        self.assertEqual(contact.first_name, "new_first_name")
        self.assertEqual(contact.last_name, "new_last_name")
        self.assertEqual(contact.email, "new_email@example.com")

    def test_delete_row(self):
        models.Contact2(
            first_name="Test", last_name="Tester", email="test.tester@example.com"
        ).save()
        self.selenium.get(f"{self.live_server_url}/edit-demo")

        delete_button = self.selenium.find_element(
            By.XPATH, '//button[text()="Delete"]'
        )
        delete_button.click()
        Alert(self.selenium).accept()

        # Give the db some time to make changes
        sleep(1)
        contacts = models.Contact2.objects.all()

        self.assertEqual(len(contacts), 0)
