import requests
import json
import pandas as pd

# create an elevation list to extract elevation data using google maps elevation api later on
elevation = []

# list of file paths with coordinates (calculated in qgis) of corresponding points
paths = ['csv_file_path_1',
'csv_file_path_2']

# insert your google maps elevation api key here
apikey='your_api_key'

# iterate through list of paths
for path in paths:
	# read csv file
	df = pd.read_csv(path)

	# iterate through each row in dataframe
	for i in range(len(df)):
		# set latitude variable to latitude info from lat column in dataframe
		latitude = str(df.loc[i, 'lat'])
		# set longitude variable to longitude info from long column in dataframe
		longitude = str(df.loc[i, 'long'])

		# create an identical url for each latitude longitude pair with your personal api key:
		url = "https://maps.googleapis.com/maps/api/elevation/json?locations="+latitude+" "+longitude+"&key="+apikey

		# request information from the url
		data = requests.get(url)
		# json.loads() is used to convert json data into python dictionary to parse it
		data_json = json.loads(data.text)
		print(data_json)
		# for each result in json
		for result in data_json['results']:
			# get elevation data to append elevation list created at the beginning
			elevation.append(result['elevation'])

	# add list of elevation data to a new column in previously add data frame
	df['Elevation'] = elevation
	# write updated dataframe to the same file
	df.to_csv(path, index=False)

print('Done!')