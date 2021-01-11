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

See "ML/Unsuper/K Means Clustering Demo" notebook
or this:
https://colab.research.google.com/drive/10KWdg8e4FmeOVeKz8FwDJs53tVVpTlby
You can try to change the numnber of groups (centers) and see the diff it makes

## Gaussian Mixture Models (GMMs)

Let's assume we decided on the centers like in K-means and let's say we draw ellipses around them.
If we look at a data-point that is on the boundary of one of the centers. how can we tell to which group the point belongs?

GMM also looks at the distribution to decide to what center it belongs. 
What is the chance by distribution to belong to this or that group/center?
 
```
from sklearn.mixture import GaussianMixture
```
and we use itinstead of kmeans
we get much better results, since this takes into account the "density"

We will usually use Gaussian in addition to k-means model.

## Hierarchical clustering

## Density-based clustering 
Based not only on distances but also on the density
No need to decide on number of clusters ahead of time

Params - 
number of min points in a cluster

* pick a point, look around it up to an epsilon and mark these points
* for each such point, look up to the epsilon and mark points. 
* until you have no more points to mark.
* is the number of points < min, then its a cluster. if not, ignore the points or something.

There are several algos, like:
### DBScan
if we have a lot of points, then it takes a long time. there are optimizations

see Clustering notebook
https://colab.research.google.com/drive/1osu0aivItwPh7NNCQEe4OfT3omHnJpbV

```
from sklearn.datasets import make_circles
X,y = make_circles(n_samples=400, factor=.3, noise=.05)
circle = pd.DataFrame(X)
DB_clusters = DBSCAN(eps=0.5,min_samples=80).fit_predict(circle)
circle["clusters"] = DB_clusters
sns.pairplot(circle,hue="clusters",vars=list(circle.columns)[:-1])
```

Play with the epsilon and see, for example 0.3, some points cannot be clustered

DBScan model has no predict, only fit_predict, you must provide all data to it. so you have to fit and predict.

## Association rules
Marketing analysis - e.g. what are people buying.

### apriori algorithm (for data analysis)
Give it 10k reciepts for shopping and you create a table where you mark each product bought. 
you can learn what items are bought together, and for what items you can offer sales for.

* Define thresholds - for example:
1. only look at items that are bought in more than 200 reciepts
2. for ANY pair of items, use only paris that were bought in more than 50 reciepts
3. look at any three items, only look at those that are bought in more than 5 reciepts

**See "dataframe corr" notebook**
https://colab.research.google.com/drive/1XBtF3oCq2ed665unXc6etX711X1M2u4v
you do corrwith(m1) for example to see what it correlates with the best.
Those can be movies for example.

We can use dataset from imdb
see "Recommender systems with python" notebook
see https://colab.research.google.com/drive/1Oh656WtJP0fomYcKqhZA_2wlc-XFGtQE

we used a pivot table:
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')

in the example we look for corr to start wars, the results are not very good.
simply looking at the rating is no enough. 
we need some math understanding here.
we also need to look at the ratings (how many ratings did it get).
The next example taking rating into account and get better results.

# Semi Supervised
we have 10k records, but only a small portion are "marked" 
The strategy is to lower the number of dimentions

See "Dimentionatily reduction" in scikit 
https://scikit-learn.org/stable/modules/unsupervised_reduction.html

See ensemble methods to do that.

See kaggle notebook for examples with a lot of explanations

Take a look at the following algos:
## Bagging (bootstap aggregation)

## Boosting 
you build weak learners

Real life problems will not simply be solved by running one model, but by running multiple models, breaking the problem into sub problems and so on.

# Imbalanced data
for example with a target of true/false and we have 98% true
this data isn't balanced. 
one option is taking a smaller part of the true


**TODO Exercise**

In repo see DS1.csv with data
try to build a supervised model for it to understand if its true or false































 
 






