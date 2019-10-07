from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time


class TwitterBot:
	def __init__(self,username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()
		email = bot.find_element_by_class_name('email-input')
		password = bot.find_element_by_name('session[password]')
		email.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(keys,RETURN)
		time.sleep(3)

	def like_tweet(self, hashtag):
		bot = sef.bot
		bot.get('https://twitter.com/search?q='+ hashtag+ '&src=tyd')
		time.sleep(3)




	def login(self):
		bot = self.bot
		bot.get('https://twitter.com')
		time.sleep(3)


ed = TwitterBot('delosedira@yahoo.com','Jesus4life')
ed.login()