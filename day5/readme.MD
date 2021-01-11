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
* cheat sheet:
https://github.com/royby-cyberark/DS/blob/master/models-CS.ipynb

* data:
https://github.com/royby-cyberark/DS/blob/master/ds1.csv

* My work: 
https://colab.research.google.com/drive/14s7pbkkJ-OBTRjEMowHa5RrLq8on6v2K

We can't really get good results without some transformation - feature engineering

in such problems we must transform the data somehow
The history might matter here. 

* See timestamp problems
google UCI datasets
you can see timeseries datasets:
https://archive.ics.uci.edu/ml/datasets.php?format=&task=&att=&area=&numAtt=&numIns=&type=ts&sort=nameUp&view=table


# Deep learning

Neural networks no longer uses scikit. instead there is Keras, integrated into tensorflow (from google)
The alternative is pytorch (from facebook)
After learning machine learning, the next step is learning tensorflow (or pytorch)

NN are dealing with many features (we don't need to have a lot of data, but at least in the order or magnitutde of the features, or maybe one more)

Chaining of machine learning problems
This model is called "Nueral network", based loosely on the human brain
if we have a large amount of features, its hard to find the important features

It learns how to break into the right sub-problems

The human brain is made of a lot of neurons, each of which is connected with synaps to 10k neurons.
a simple descision usess 200-300 neurons

In deep learning, we build a network, like a graph.
we give it the input.
let's say X, Y, Z
each neuron is connected to all neurons in the next level. 
at the far side we have the target.
each vertex in the graph has a weight.

we doing some linear calc on the inputs and the vertices and then we run some mathematical operation on the input and get the output.
see image

![Deep learning]("https://raw.githubusercontent.com/royby-cyberark/ml-course/main/day5/Screen%20Shot%202021-01-11%20at%2014.22.54.png")

To decide on the actual numner we need to train the network.
which means to find the weights on the vertices
this isn't trivial. it takes time and it might not sure that we can actually train it properly, depending on the way that we've built it.

## Benefits: 
* It can solve ANY machine learning problems - regression, classification and ..
each neuron is its own linear regression

* Here we don't need to understand how to seperate into sub-problems. the learning process decides what's best, which is represented by the vertices weight


The trainers are called Optimizers
after we go over all data we get epoc1
each time we tweaq the data a bit according to what we're trying to find (there's some calculus here)
then we need to go over all data many more times epoc2, 3, etc.

database for images:
http://yann.lecun.com/exdb/mnist/

See Mnist-NN notebook

MLPClassifier - multi layer preceptron classfier (neuron network classifier)

## Drawbacks
Very hard to set up.
many many parameters

Google **Activation Functions** fot the neural networks functions that we can use

* Learning rate - too small - might take a lot, too large - might miss the minimum

## Other NN types
* Auto encoders
  for example, compressions.
  we get 10k input features, we require an hidden layer of lower number, and at the result, the same 10k results.
  this can be used for compressions for example.
  see example notebook:
  https://colab.research.google.com/drive/1-dzKQbIplTUFktWQN8FtlF-4TAVQK2CN
  
  the examples also has images with noise and after that it results in clean number. 
  since it learned how the number are supposed to look.
  
  from this deep fake started.
  
  *  A generator for people that do not exist:
  https://thispersondoesnotexist.com/
  
  * Generate songs - lyrics, melody, vocals
  https://openai.com/blog/jukebox/
  
  * GuaGAN - sketches into fake scenary on youtube
  
  
* SOM
* Convolutional NN - math operation on pics, a kind of filter. using algorithms to build the network
  import scipy.signal as scisig
  scisig.convole2d(tab1, fil)
  see Mnist-NN vs MNIST_CNN notebook results
  
* Boltzmann machines


# Text analysis
we got a lot of text - documents
1. build a BOW - bag of words - a bag of each **unique** words
2. filtered some words (stop words), like "on", "the" etc - lowers the dims
   also conjugation - stop, stopping, stopped. there are tricks for doing that.
3. let's say we are left with 10k words. we will build a table with the word as features
4. the rows are the docs - doc1, doc2, etc.
5. we want to decide on the % handycap 
6. tfidf - term freq (count the term), inverse doc freq - 

# Natural language processing

## NLTK - natural language took kit 
a must library for NLP
helps with feature prep, etc. 
see examples in the notebook: "Text Processing\NPL Demo" 
spam filter by words

you can use things like:
python string poncuation, 
nltk have packages like corpus which you can get words from, stopwords

we can build a pipeline with this:
sklearn.pipeline import Pipeline

# Next learning
for deep learning its best to get some match backgroung first from 
e.g. Deep Learning Specialization in Coursera
also there are heb lectures in youtube

There are ready models in aws, google, etc. 





