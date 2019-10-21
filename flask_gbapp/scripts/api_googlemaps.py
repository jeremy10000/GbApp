import requests

class ApiGoogleMap:

	def __init__(self):
		self.url = "https://maps.googleapis.com/maps/api/geocode/json?"

	def find(self, keywords):
		params = {
        	'address': keywords,
        	'key': ''
    	}
		api_request = requests.get(url=self.url, params=params)
		response = api_request.json()
		data = response["results"]

		route = str()
		point_of_interest = None
		locality = str()

		# dico (key) for : list comprehension
		try:
			for component in data[0]["address_components"]:
				if 'route' in component['types']:
					#print(" ### route : ", component['long_name'])
					route = component['long_name']

				if 'point_of_interest' in component['types']:
					point_of_interest = component['long_name']

				if 'locality' in component['types']:
					#print(" ### locality : ", component['long_name'])
					locality = component['long_name']

			formatted_address = data[0]['formatted_address']
			#print("*********** : formatted_address : ", formatted_address)
			lat = data[0]['geometry']['location']['lat']
			lng = data[0]['geometry']['location']['lng']
		except IndexError:
			return False

		if point_of_interest is not None:
			print("### : route = ", route)
			route = point_of_interest
			print("### : route (changement?) = ", route)


		return {
			"formatted_address": formatted_address,
			"route": route + " " + locality,
			"lat": lat,
			"lng": lng
		}
