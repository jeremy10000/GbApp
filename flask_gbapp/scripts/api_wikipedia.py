"""

"""
import wikipedia


class ApiWikipedia:
	"""

	"""

	def __init__(self):
		wikipedia.set_lang("fr")

	def find(self, keywords):
		"""
		"""

		#print(wikipedia.summary(keywords))
		page = wikipedia.search(keywords, results=1)
		page = page[0]

		#url = "https://fr.wikipedia.org/wiki/" + page

		#print(page, url)
		url = wikipedia.page(page).url

		#print(wikipedia.summary(page))
		#print(wikipedia.page(page).url)

		return {
			"summary": wikipedia.summary(page),
			"url": url
		}