import unittest

from scripts.parser import Parser
from scripts.api_googlemaps import ApiGoogleMap
from scripts.api_wikipedia import ApiWikipedia
from unittest.mock import patch


class TestParser(unittest.TestCase):

	def test_parser(self):
		parser = Parser()

		question = "Indique moi ou est le musée du louvre!"

		result = parser.extract(question)

		self.assertEqual(result, "musée louvre ")

	# QUand tu vois requests.get dans api_googlemaps tu le remplaces par mock_json (qui est l'attribut)
	@patch("scripts.api_googlemaps.requests.get")
	def test_api_gmaps(self, mock_json):
		mock_json.return_value.json.return_value = {'results': [{'address_components': [{'long_name': 'Place Jacques Rueff', 'short_name': 'Place Jacques Rueff', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Arrondissement de Paris', 'short_name': 'Arrondissement de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'Île-de-France', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75007', 'short_name': '75007', 'types': ['postal_code']}], 'formatted_address': 'CONNAID Jacques Rueff, 75007 Paris, France', 'geometry': {'location': {'lat': 48.858257, 'lng': 2.2946056}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 48.85960598029151, 'lng': 2.295954580291502}, 'southwest': {'lat': 48.85690801970851, 'lng': 2.293256619708498}}}, 'place_id': 'ChIJ____vx9w5kcRg3gQZBz71Ag', 'plus_code': {'compound_code': 'V75V+8R Paris, France', 'global_code': '8FW4V75V+8R'}, 'types': ['establishment', 'museum', 'point_of_interest']}], 'status': 'OK'}

		data = mock_json.return_value.json.return_value["results"]

		api_googlemaps = ApiGoogleMap()
		data_googlemaps = api_googlemaps.find("adresse tour mo")

		r = {
			"formatted_address": data[0]['formatted_address'],
			"route": data[0]['address_components'][0]["long_name"] + " " + data[0]['address_components'][1]["long_name"],
			"lat": data[0]['geometry']["location"]["lat"],
			"lng": data[0]['geometry']["location"]["lng"]
		}
		print("RR : ", api_googlemaps.find("adresse tour mo"), r)

		self.assertEqual(api_googlemaps.find("adresse tour mo"), r)
		
	@patch("scripts.api_wikipedia.wikipedia.search")
	@patch("scripts.api_wikipedia.wikipedia.summary")
	@patch("scripts.api_wikipedia.wikipedia.page")
	def test_api_wiki(self, mock_search, mock_summary, mock_page):
		"""
		#mock_search.return_value = "Eiffel"
		print("m :", mock_page) # search
		print("m :", mock_search) # page
		print("m :", mock_summary) #summary"""
		
		api_wikipedia = ApiWikipedia()
			

		mock_page.return_value = "Eiffel"
		mock_search().url = "http://"
		mock_summary.return_value = "La tour eiffel blablabla"

		"""
		print("m :", mock_search)
		print("m :", mock_summary)
		print("m :", mock_page)"""


		

		r = {
			"summary": mock_summary.return_value,
			"url": mock_search().url
		}
		print("DD", api_wikipedia.find("Eiffel"), r)	

		self.assertEqual(api_wikipedia.find("Eiffel"), r)
		

if __name__ == '__main__':
    unittest.main()
