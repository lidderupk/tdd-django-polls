from django.test import TestCase
from django.utils import timezone
from polls.models import Poll, Choice

class PollModelTest(TestCase):

	question = "What's up"
	pub_date = timezone.now()


	def test_creating_a_new_poll_and_saving_it_to_database(self):
		poll = Poll()
		poll.question = self.question
		poll.pub_date = self.pub_date
		poll.save()

		all_polls_in_database = Poll.objects.all()
		self.assertEquals(len(all_polls_in_database), 1)
		only_poll_in_db = all_polls_in_database[0]
		self.assertEquals(only_poll_in_db, poll)

		self.assertEquals(only_poll_in_db.question, self.question)
		self.assertEquals(only_poll_in_db.pub_date, self.pub_date)


	def test_verbose_name_for_pub_date(self):
		for field in Poll._meta.fields:
			if field.name == 'pub_date':
				self.assertEquals(field.verbose_name, 'Date published')

	def test_poll_objects_are_named_after_their_question(self):
		# the model shows the unicode value in the admin panel
		p = Poll()
		question_text = 'How are you doing?'
		p.question = question_text
		self.assertEquals(unicode(p), question_text)

class ChoiceModelTest(TestCase):
	def test_creating_some_choices_for_a_poll(self):
		poll = Poll()
		poll.question = "what's up?"
		poll.pub_date = timezone.now()
		poll.save()

		choice = Choice()
		choice.poll = poll
		choice.choice = 'alright then ...'
		choice.votes = 3
		choice.save()

		# check the database
		poll_choices = poll.choice_set.all()
		self.assertEquals(poll_choices.count(), 1)
		self.assertEquals(poll_choices[0].choice, choice.choice)

	def test_choice_defaults(self):
		choice = Choice()
		self.assertEquals(choice.votes, 0)