**Project overview:**
The research was focused on developing a data-driven approach to predict the success of bank telemarketing using a case study of a Portuguese banking institution. 

**Dataset:**
The dataset utilized is bank-additional-full.csv.There is a total of 41,888 records with 20 inputs (independent variables) and one output (term deposit accepted or not as dependent variable). The goal is to predict if the client will subscribe a term deposit. 

**Model:**
The Model adopted for this intial code stage is Logistic Regression model.

*******Code:******

***A: Banking_Data_set_intial_code_ST.ipynb** code starts with Univariate Analysis,  Bivariate analysis, Analyzing the relationship between numerical variables and understanding the relationship between the independent variable and categorical depandent variable. To utilize the python based Logestic regression model , encoding of Categorical variable is done. Then the dataset is split between the train and test sets. Finally the model is run and it's AOC is checked.

***B: Banking_Data_set_Final_code_28_Mar_2022** code starts with Univariate Analysis,  Bivariate analysis, Analyzing the relationship between numerical variables and understanding the relationship between the independent variable and categorical depandent variable. To implment various ML models, encoding of Categorical variable is done. One of the Categorical variable 'duration is dropped'. The the dataset is split between the train, test and validation sets. Then the model is run for Logistic regression , Neural network and Decison tree. Each of those model is evaluated in terms of Recall, precison, accuracy , time taken to execute, stability, mean and standard deviation of the cross validation score.


******Technical Report:******

*A: Banking_Data_set_intial_code_ST.pdf consists of the compiled version of the code and the approach.

*B: Banking_Data_set_Final_code_28_Mar_2022.pdf consists of the compiled version of the final code.
