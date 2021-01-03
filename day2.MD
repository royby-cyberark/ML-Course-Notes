
* supervised-unsupervised-learning
https://blogs.nvidia.com/blog/2018/08/02/supervised-unsupervised-learning/

We genrally seperate ML into two categories: 
1. Supervised - marked data
   we have info on the target, e.g. is the pic a dog or a cat
   1.1 classification problems - tell me if its a dog or a cat
   1.2 req - ?
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
* 
