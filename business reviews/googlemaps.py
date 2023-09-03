import google maps

#Replace with your google places API key
API_KEY = 'AIzaSyCarzeHE0kHHWYLPbydipS8bhn30Vc1b2Y'

#Initialize the Google Places Client
gmaps = googlemaps.cliemt(Key=API_KEY)

# Place ID of the business you want to fetch reviews for
place_id ='21370 HOMESTEAD ROAD CUPERTINO, CA 95014'

# fetch reviews for the business
place_details = gmaps.place("21370 HOMESTEAD ROAD CUPERTINO, CA 95014 " ,fields=['Homestead High School','#384','https://www.google.com/search?q=Homestead+high+school+rating&oq=Homestead+high+school+rating&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDc2NTdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#'])

# Extract reviews from the response
if 'reviews' in place_details:
    reviews = place_details['reviews']
else:
    reviews = []