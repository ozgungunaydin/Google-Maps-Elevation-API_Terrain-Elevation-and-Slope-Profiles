the following excerpt is from my own master's thesis completed at Architecture (Conservation) department of Sapienza University of Rome which was co-supervised by Politecnico di Milano.

thesis:
An Urban Regeneration Project for Lanciano (Utilizing GIS and Data Analysis Tools): The Disused Sangritana Railway Line Between Mobility and Historic Networks
March 2021

" terrain elevation and slope profiles to examine proposed cycle paths

in this section two proposed cycle paths12 in Lanciano and San Vito Chietino are examined within their elevation and slope contexts.

methodology

method I: 1 - digital elevation model (dem) of the terrain with 10x10m resolution which was taken from Abruzzo Open Data platform is reprojected to relevant projection in QGIS that is EPSG:7794 in this case

2 - drape (set Z value from raster) process is run to extract elevation data from dem raster

3 - using ‘field calculator’ following functions are calculated: length: $length start point: z(start_point($geometry)) end_point: z(end_point($geometry)). slope: (abs(start_point - end_point) / length) * 100

please note that this methodology might not be resulting with a correct slope but rather a distorted one for following reasons:

1 - 10x10m dem resolution is still too far away from being 100% accurate.

2 - the firsthand dem might be problematic when it comes to anthropogenic features such as underpasses, road embankments, bridges, etc..

at this points, it is worthwhile to mention that a different method of landscape modelling13 has been discussed by D’Uva et al. (2020) which might result with a more accurate slope analysis of the proposed paths.

method II: 1 - using ‘extract specific vertices’ in QGIS with “0, -1” as vertex indices, points are produced on proposed lines at the beginning and end of each line parts both in Lanciano and San Vito Chietino

2 - thanks to ‘remove duplicate vertices’ processing tool overlapping points are deleted

3 - point vector layer is reprojected to WGS84 to be able to extract coordinates of each point

4 - ‘add geometry attributes’ is run in QGIS to get x and y coordinates

5 - point vector with coordinates is extracted to CSV file where ycoord is latitude and xcoord is longtitude

6 - a Python algorithm is run to extract elevation data of each point from Google Maps Elevation API

7 - slope value of each point is calculated using Python with the following expression: slope = ((Elevation[i] - Elevation[i - 1]) / Distance[i]) * 100

this method also seem problematic considering fluctuations in elevation data which make the slope in Lanciano narrower while in San Vito Chietino quite wider than the previous one.

method III: komoot.com is used to get the screenshot of elevation and slope profiles. since it seems the most reliable among all the methods mentioned. darker colours represent steeper terrain. "
