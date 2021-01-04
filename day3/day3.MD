Notebook: https://colab.research.google.com/drive/15acX6WSC-MrK95KEx1KyHz3-HElBK2yA?usp=sharing

* Bias varianve tradeoffs - 

# Classification
The simplest model here is called "Logistic regression" - confusing name, see:
https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

We are trying to find a seperation between data points.
We will find a line that seperates them. 
the "Logistics regression" function - f(x) = 1 / (1 + e^-x)
is also called sigmoid
This function gives you 0-1 values.

Above 0.5 - we will consider it true for our model, below -false.

our model will do:

y = 1 / (1 + e^-(A*x1 + B*x2 + C*x3 ... + P1) )

then test for the result vs 0.5

Fitting: 
* Binary classification - cat or dog

Example, see Titanic notenook in the course archive file

TODO: 
1. Logistics regression lab
2. practice dummy vars: real_estate.csv - build a regression model, when you keep the type, or turn it into dummy vars and compare results
3. take any dateset from fraggle and try everything we did there

## Titanic
See titanic notebook - my notes at the top

## classification reports
see "classification reports.ipynb"



