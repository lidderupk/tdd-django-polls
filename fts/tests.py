from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userFactory import UserFactory

class PollsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.user = UserFactory.create()


    def tearDown(self):
        self.browser.quit()

    def test_can_create_new_poll_via_admin_site(self):
        self.browser.get(self.live_server_url+'/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys(self.user.username)

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.ENTER)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        polls_links = self.browser.find_elements_by_link_text('Polls')
        self.assertEqual(len(polls_links), 2)


        polls_links[1].click()

        #the user is taken to the polls listing page, which shows no polls yet
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 polls', body.text)

        # the user clicks on add to add a new poll
        new_poll_link = self.browser.find_element_by_link_text('Add poll')
        new_poll_link.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Question:', body.text)
        self.assertIn('Date published:', body.text)


        question_field = self.browser.find_element_by_name('question')
        question_field_text = 'How awesome is test driven development'
        question_field.send_keys(question_field_text)
        date_field = self.browser.find_element_by_name('pub_date_0')
        date_field.send_keys('01/01/12')
        time_field = self.browser.find_element_by_name('pub_date_1')
        time_field.send_keys('00:00')

        # user adds choices to the newly created poll. 
        choice_1 = self.browser.find_element_by_name('choice_set-0-choice')
        choice_1.send_keys('Great')

        choice_2 = self.browser.find_element_by_name('choice_set-1-choice')
        choice_2.send_keys('Good')

        choice_3 = self.browser.find_element_by_name('choice_set-2-choice')

        choice_3.send_keys('Nice')


        # save_button = self.browser.find_element_by_css_selector("input[value='save']")
        save_button = self.browser.find_element_by_name('_save')
        save_button.click()

        new_poll_links = self.browser.find_elements_by_link_text(question_field_text)
        self.assertEqual(len(new_poll_links), 1)


        # self.fail('Finish the test!')

    def test_voting_on_a_new_poll(self):

        # First, the user logs into the admin site and 
        # creates a couple of new Polls, and their response choices

        # Now a regular user goes to the homepage of the site and sees the list of polls

        # he clicks the link to the first poll, which is called ""
        pass