General cheat sheet:
https://github.com/dev-area/DS/blob/master/models-CS.ipynb

In scikit learning they have good examples for clustering:
https://scikit-learn.org/stable/modules/clustering.html

We pair-plot, and if we see one of the patterns that is shown on the clustering overview page (link above)

the black are data that it can't fit anywhere. didn't find any relatioship to any of the clusters.

We usually cluster by the geometry.

## K-Means
Simple clustering algo - gets the number of groups
For example, we got data points and we want to cluster into 3 groups
we pick 3 random points k1, k2, k3
* First iteration: for each data point we assign it to one of the k's (nearest). so we have 3 groups.
  Imagine we have an ellipse around all data points in each group.
* Move the kn to the center of each ellipse 
This algo is sensitive to outliers, it considers weight so that one far data point doesnt move the center
* 2nd iteration: go over all points and match each point to the nearest center.
  * Move centers again
* Anther iteration
* Finish when no point changed color.
You can now throw the points and keep only the centers and also also calc mean distance of data points from centers.
So you have:

1. centers
2. mean distance from centers

When you get a new point match it with the right center. 


