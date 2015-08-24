from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from hello.models import Devinfo

"""TESTING VZ SELENIUM"""
class HelloTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(HelloTests, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(HelloTests, cls).tearDownClass()
        
    def test_devinfo_displayed(self):
    
        # create a test record into base
        Devinfo.objects.create(name='Roma', lastname='Shevchuk', email='wrongman@gmail.com', birthdate='1985-05-17', bio='All good', jabber='jabber-ID', othcontacts='+380989682061')

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(self.selenium.find_elements_by_css_selector('.field_name-decor-class-0')[0].text,'Roma')
