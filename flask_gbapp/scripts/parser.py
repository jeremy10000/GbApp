import re
from . import stopwords


class Parser:
	""" Parser """

	def generator(self, string):
		""" generator """
		for word in string:
			if word not in stopwords.STOPWORDS:
				yield word + " "

	def extract(self, string):
		""" Extract all the words that are not in the list """
		
		# lowercase
		string = string.lower()

		# no symbols
		string = re.sub("[,?@#!&.<>^\"""]"," ", string)
		
		string = string.split()
		generator = self.generator(string)

		# All the words that are not in the list (stopwords).
		place = str()

		for word in generator:
			place += word

		return place
