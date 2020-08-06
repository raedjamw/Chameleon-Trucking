# Chameleon Trucking Project
![Image of Chameleon](https://github.com/raedjamw/Chameleon-Trucking/blob/master/Chameleon-branch-Madagascar.jpg)


## Background
These Notebooks are an ongoing Project to determine 'Chameleon Trucking' Companies.
This a A potentially deadly trend where trucking Companies with poor records, for various
reasons such as dangerous driving,DUI's etc. shut down their companies and reopen under a new 
name to clean up their records. This covers North and Central America,over 1.2 million companies.
I hope to help determine these companies using machine learning method methods.

### Phase 1:
- Webscraping location Data into MySQL and then python.
- Preprocessing:Feature Engineering,removing NaNs,other stopwords 
- Geocoding via Googlemaps API platform,ArcGIS.
- Vizualizations: Geographic visualizations via Basemap,Geopandas
- Run KNN algorithm in Sklearn to match up companies 
- Perform unit testing to validate the accuracy of the NN algorithm

### Phase 2: Currently
- Engineer new feature with Crash/Inspection data from USDOT

## Methodology
- The algorithm used is the K Nearest Neighbour,an instance based learning algorithm.
![Image of KNN](https://github.com/raedjamw/Unsupervized-KNN-for-matching-Pairs-Chamleon-Trucking-Project/blob/master/KNN.JPG)

The KNN  Works by finding the K(specified number,3 in my case) of 'in service carriers(truckers)' which are closest to an 'out of service carriers(trucker)'.The distance
used is the standard euclidian distance(straight line).It is an instance based algorithm because it constructs hypotheses directly from the training instances themselves. This why KNN is unsupervizied because we do not have any labels, the result we get are actually a new factor and not a label.Additionally, there is no need to consider in such specifics as the 'driving distance' etc. We are trying to determine the labels(legitimate or chameleon) at the end of this entire project.


## Next Steps
- Locate financial data
- Peform an appropriate clustering algorithm to classify and generate labels
 
## References

For More info on Chameleon Trucking,See the following Link
https://www.atlantainjurylawblog.com/uncategorized/what-is-a-chameleon-trucking-company-and-how-does-it-keep-doing-dangerous-stuff.html

https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn

https://en.wikipedia.org/wiki/Instance-based_learning

NOTE:SOME OF THE GEOCORDINATES DID NOT MATCH UP CORRECTLY WHEN PLOTTED.THIS IS DUE TO INACCURACIES IN THE FREE VERSION OF THE ARCGIS API.I DID MULTIPLE ITERATIONS OF DATA CLEANING AND THE PLOTS REMAINED THE SAME.

#Python #Logistics #MySQL #Geopandas #MachineLearning #KNN #ArcGIS #Basemap
