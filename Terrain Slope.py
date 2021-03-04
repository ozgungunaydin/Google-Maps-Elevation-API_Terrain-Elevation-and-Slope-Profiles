import pandas as pd

# list of file paths with elevation and slope (calculated in qgis) data of corresponding points
df_paths = [
'lanciano_coordinates.csv',
'san vito chietino_coordinates.csv'
]

# iterate through the file paths
for path in df_paths:
	# create a list for id's
	ID = []
	# create a list for elevations
	Elevation = []
	# create a list for distances
	Distance = []
	# create a list for slopes
	Slope_Python = []
	# read the file
	df = pd.read_csv(path)
	# rearrange list without 'Unnamed' columns and assign to same variable
	df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

	# iterate through id's
	for i in df['ID']:
		# append each id to ID list
		ID.append(i)

	# iterate through elevations
	for i in df['Elevation']:
		# append each elevation to elevation list
		Elevation.append(i)

	# iterte through distances between two points
	for i in df['distance']:
		# append each distance to distance list
		Distance.append(i)

	# iterate through the range of ID list length
	for i in range(len(ID)):
		# if it is the first item in the range
		if i == 0:
			# add None to the list because no slope can be calculated
			Slope_Python.append(None)
		# if the item is not the first one in the range
		if i > 0:
			# calculate slope
			slope = (abs(Elevation[i] - Elevation[i - 1]) / Distance[i]) * 100
			# append slope values to Slope_Python list
			Slope_Python.append(slope)

	# create 'Slope_Python' column in dataframe and attach it to Slope_Python list
	df['Slope_Python'] = Slope_Python
	# rewrite new dataframe to the csv file without an index column
	df.to_csv(path, index=False)

print('Done!')