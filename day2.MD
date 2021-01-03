
* supervised-unsupervised-learning
https://blogs.nvidia.com/blog/2018/08/02/supervised-unsupervised-learning/

We genrally seperate ML into two categories: 
1. Supervised - marked data
   we have info on the target, e.g. is the pic a dog or a cat
   
   1.1 classification problems - tell me if its a dog or a cat
   
   1.2 regression - we have the target values, and we want to predict some value. for example, we want to predict grades, avg, etc. with the data that we have for studends (e.g. age, where they live, etc.)

2. Unsupervised - unmarked data. we don't have the target value. e.g. 
   we're taking a group, e.g. a successful fertilization. 
   then, according to the parameters, we will try to infer for something we don't know.
   usually for recommendations. e.g. product recommendation.
   e.g. user is a studend, certain age, etc. then recommend a tv show. 
   
   
   
* Python sci packages
https://scipy.org/


|    Scikits   |     Seaborn  |
| SciPy | Pandas | Matplotlib |
|            NumPy            |

Numpy - low level math, structures impl. in c
Pandas - data processing, uses numpy
SciPy - math, built on Numpy
Seaborn - http://seaborn.pydata.org/#

* More on Numpy, pandas with examples - [colab](https://colab.research.google.com/drive/1kr2RX0Ffz01JYhG6p7LS1AVduyxQe2qN?usp=sharing), [in this repo](https://github.com/royby-cyberark/ml-course/blob/main/ml_course_day2_sci_libs.ipynb)

* Data types
  * Matrix data - a design matrix x and label vector y
  * text
  * images
  * set data, e.g. items purchased together
  * sequence data 0 clickstream, purcahse histroy
  * time seriese (e.g stock prices, audio, video)
  * grpah/network
  
## Data processing
When we're going data processing we have 3 options for filling in missing data
  * Ignore them (bad idea usually)
  * Delete it, but then we're missing the rest of the data
  * Usually we will opt to fill in the missing data so that we don't lose the entire record
  
  
## Exercise 1, day2
* See github - https://github.com/dev-area/DS
* [data understanding cheat-sheet](https://github.com/royby-cyberark/ml-course/blob/main/Data%20Understanding%20CS.ipynb)
* do Lab-diamonds: loads the diamonds dataset
* df = sb.load_dataset('diamonds')
* df.head()
* run until data-prep
* https://github.com/dev-area/DS/blob/master/Lab%20-%20diamonds.ipynb


## Creating the model in supervised 
target can be a number or a category (dog/cat)

let's say we want to predict apt. price
x is all params - location, rooms, floor, etc. y is that target - price

* We start by seperating the dataset into train and test:
70% of the data - train (x.train, y.train)
30% of the data - test (x.test, y.test)

* Fit
x_train, y_train into fit -> which give us the model

fit will take the x_train and y_train and will try to find the model (the calculation that will bring us to y from x)

* Then we take the model, and feed it with x_test, and predict it. it outputs with y_predict.
* compare y_test with y_predict and see how they fit.

See: https://colab.research.google.com/drive/1kr2RX0Ffz01JYhG6p7LS1AVduyxQe2qN#scrollTo=rT-86niaL32v
for examples of using scipy

# Linear regression
params = x, y, z, target = t
LR find a line that is closeset to all points.
something like x* c1 + y * c2 + y * c3 = t

in code we can get those by calling:

```
model.coef_
```





