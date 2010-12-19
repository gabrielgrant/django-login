from django.test import TestCase

class SimpleTest(TestCase):
	urls = 'login.test_urls'
	def test_get_login(self):
		response = self.client.get('/admin/')
		self.assertEqual(response.status_code, 200)
		print response.content
		#for k,v in response:
		#	print '\n\n',k,':',v,'\n\n'

