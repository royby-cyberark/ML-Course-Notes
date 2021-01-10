All course colabs:
https://drive.google.com/drive/folders/1UxSm3L3hlHXF7ZWTKzl0EbQxbhok7akj

Intro to data science links - https://devarea.com/introduction-to-data-science/#.X_qxaOkzabu

--------------------------------

Short summary:
class. vs. regr. - is our target column a true/false or a numeric value?
1. is our problem classigication or regression?

## Regression
we are interested in things like the distribution of values
We would then use metric like the following to look at the results:

import sklearn.linear_model as slin
model = slin.LinearRegressions()
model.fit(X_train, y_train)
LogisticRegression()
model.score(X_test, y_test)

import sklearn.metrics as mt

mt.mean_absolute_error(y_test, y_pred)
mt.mean_squared_error(...)
mt.mean_squared_log_error(...)

read about these in the docs.
  
## Classification
We could do something very similar with classification
...
model = slin.LogisticRegression(max_iter=1000)
but not the target won't be price, but rather something like "high_price" that we added if the prices gt something

here we will test for something else:

mt.confusion_matrix(y_test, y_pred)
print(mt.classificatoin_report(y_test, y_pred))

----------------------------


ML
* Unsupervised
* Supervised
  * Regression - Linear, SVR (Support vector regressor), DTR (descision tree regressor), RFR (random forest regressor)
  * Classification
    * Multiclass - a, b or c (e.g dog breed, type of custoemr between several types) - DT (Decisoin tree), RF (random forest), KNN (K nearest neighbor), NB (Naive Bayes)
    * Binary - yes/no - Logistic, SVC (support verctor)
  

----------------------------

ALL MODELS THAT FIT REGRESSION ALSO FIT CLASSIFICATION


## Support vector machine model

given two (or more) classes of values, the model find the broadest stip to seperate between the groups. then find the middle of it.
it doesnt have the be linear. 


See support vector machine, SVM demo - https://drive.google.com/file/d/1W3lPhE0h8KFW4NBEqGIeb31I8ZRHcWg3/view?usp=sharing\\

K-fold c.v (cross validation)

Tools for model selection:
https://scikit-learn.org/stable/model_selection.html
https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics

We can implemeted our own score calculator, ingeriting the base classes. 

Optional exercise:
See LinearRegression - Dim reduce (seee solution also)

TODO - complete power outage - around 01:50 at 11:00am

Go over all supervised models that are here:
https://scikit-learn.org/stable/supervised_learning.html

## Decision tree
for non-linear problems

!(destree)[https://github.com/royby-cyberark/ml-course/blob/main/day4/Screen%20Shot%202021-01-10%20at%2011.07.51.png]

always add pairplot
if the features are very mixed then SVM wont work (unless we do some transformation)

Overfit - when creating training data, we might make this data fit, let's say to a 100%, but this doesn't have to be right.
We need to balance between bias and variance.
the **Bias and variance tradeoff**
Bias - error compared to our data
variance - 

When we make our model more complex we get less error until a min point, after which our train data get less errors, but the test results get more errors.
we are looking for this min point.

DescisionTreeClassifier has hyperparams that we can use, 
min_samples_split - change it to find the min point
and other params.

**Always check for overfitting, underfitting** - in any model

TODO - read about underfitting

We can create the desicion tree in many way.
the randomness according to which we build our tree will affect our results

Which have the option of building many trees. 

## Random forests
We build many trees for the same data
run your prediction on all trees, and pick the result according to the majority.
this cancels our problem of random picking.

See Ensemble methods under scikit learn
https://scikit-learn.org/stable/modules/ensemble.html

for example, there's randomForestRegressor, and many more, there's the classifier which you init and then you use the regressor.

in my notebook see "Bootstrap Aggregation" and "Random Forests"

in random forest, for example, we can ask what ware the more important features.


* We could use the decision tree to solve linear and other problems also, e.g. the iris problem that is sovled in the SVM examples
in the notebooks here
https://drive.google.com/drive/folders/1UxSm3L3hlHXF7ZWTKzl0EbQxbhok7akj

## Naive Bayes
conditional probability. 
There are academic courses, like this: https://www.coursera.org/learn/bayesian-methods-in-machine-learning

TODO, task:
run 

df = sb.load_dataset("diamonds")
liranbh@gmail.com

instructor gmail: liranbh



# Nearest neighbors

K Nearest neighbors is a classification algorithm
calc distance to all points in your data

the problem - there's no fit here. the prediction takes time.

We need to use scalers, see in preprocessing in scikit which will turn everything into one scale
e.g. turn all between 0-1

https://scikit-learn.org/stable/modules/preprocessing.html

see standardisation or normalization
we can for example use rehshape(-1, 1)

TODO - read this:
https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py


**NOTE:** If we're using a distance algorithm, you MUST normalize/standarize the data

# Multiclass and Multilabel

Turn this into a binary problem

* 1 vs all
* 1 vs 1 (or all vs all)

# Multilabel
e.g. suggest tags, understand if its related to python, linux, web, android etc.


TODO
see exe_multi class classification

exercise: in the ML zip, under Naive Bayes, use the class_exe.csv

* Use random forest classifier
* do 1 vs 1
* 1 vs 2
* 1 vs 3





