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

### Phase 2: 
- Engineered 2 new features with Crash/Inspection data from USDOT

### Phase 3:
Performed a Hierarchical Clustering Algorithm on the 3 features to Engineer Labels for Non-Chameleon and Chameleon

## Methodology
- The first algorithm used is the K Nearest Neighbour,an instance based learning algorithm.
![Image of KNN](https://github.com/raedjamw/Unsupervized-KNN-for-matching-Pairs-Chamleon-Trucking-Project/blob/master/KNN.JPG)

The KNN  Works by finding the K(specified number,3 in my case) of 'in service carriers(truckers)' which are closest to an 'out of service carriers(trucker)'.The distance
used is the standard euclidian distance(straight line).It is an instance based algorithm because it constructs hypotheses directly from the training instances themselves. This why KNN is unsupervizied because we do not have any labels, the result we get are actually a new factor and not a label.Additionally, there is no need to consider in such specifics as the 'driving distance' etc. We are trying to determine the labels(legitimate or chameleon) at the end of this entire project.

- The second algorithm used is the Hierarchical Clustering Algorithm.

Hierarchical cluster analysis involves creating clusters that have predominant ordering from top to bottom, i.e., a datapoint starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy, as seen below.

<p align="center">
 <img width="460" height="650" src="https://user-images.githubusercontent.com/39776292/90050461-36c74e00-dca4-11ea-93cf-f6138fcc1ff8.gif">
</p>


## Next Steps
- Locate financial data
- Peform Perform appropriate classification algorithms to predict for new data
 
## References

For More info on Chameleon Trucking,See the following Link
https://www.atlantainjurylawblog.com/uncategorized/what-is-a-chameleon-trucking-company-and-how-does-it-keep-doing-dangerous-stuff.html

https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn

https://en.wikipedia.org/wiki/Instance-based_learning

https://gfycat.com/somelonelycaterpillar

https://www.kdnuggets.com/2019/09/hierarchical-clustering.html

NOTE:SOME OF THE GEOCORDINATES DID NOT MATCH UP CORRECTLY WHEN PLOTTED.THIS IS DUE TO INACCURACIES IN THE FREE VERSION OF THE ARCGIS API.I DID MULTIPLE ITERATIONS OF DATA CLEANING AND THE PLOTS REMAINED THE SAME.

#Python #Logistics #MySQL #Geopandas #MachineLearning #KNN #ArcGIS #Basemap
