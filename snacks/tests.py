from django.test import TestCase
from django import urls
from django.test import TestCase , SimpleTestCase
from django.urls import reverse
# Create your tests here.

class SnacksTest(SimpleTestCase) : 
    def test_home_page(self): 
        url=reverse('home')
        actual_status_code = self.client.get(url).status_code
        expected_status_code=200

        self.assertEqual(actual_status_code,expected_status_code) 


    def test_about_page(self): 
        url=reverse('about')
        actual_status_code = self.client.get(url).status_code
        expected_status_code=200

        self.assertEqual(actual_status_code,expected_status_code)


    def test_template_home(self): 
        url=reverse('home')
        actual_status_code = self.client.get(url)
        expected_status='home.html'

        self.assertTemplateUsed(actual_status_code,expected_status)

    def test_template_about(self): 
        url=reverse('about')
        actual_status_code = self.client.get(url)
        expected_status='about.html'

        self.assertTemplateUsed(actual_status_code,expected_status)