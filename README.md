# Classification_Project
Individual Classification project for Codeup

# Project Description

Retention of customers is a prime motivator for companies. This is particularly salient for firms that focus on a subscription model, as is the norm in telecommunications. Consequently, understanding what drives customer attrition is important to the bottom line of such businesses. 

The following project is intended to unearth the factors contributing to customer attrition, referred to as "churn", for Telco Systems patrons. In pursuit of this end, I utilized the Telco dataset provided by Codeup. This dataset provides information on customers including demographics, contract status, payment information, and service add-ons. I will be exploring these variables to determine which ones may provide insight into what drives customer churn.

# Project Goal

* Discover drivers of churn for customers of Telco
* Utilize these drivers to develop a machine learning model to classify customers as likely to imminently churn or not churn
* The information derived from this model can subsequently be used on data from new or existing customers to predict imminent churn


# Initial Thoughts

My initial hypothesis states that primary drivers of churn will be derived from financial and contract based variables.

# Planning Process

* Acquire dataset from Codeup database

* Prepare data:
  * Clean columns to account for null values
  * Create dummy variables for categorical strings
  * Create new Billing Type column from Payment Type column, determining if client's payment was manual or automatic

* Explore data for variables driving upset
  * Answer the following initial questions:
      * How do monthly charges affect the likelihood of customer churn?
      * How does the type of customer contract drive churn?
      * Does the way in which customers pay their bills affect likelihood of attrition?
      * Does having dependents, a demographic category nominally unrelated to finance or contract, affect churn?

* Develop a model to predict client attrition
  * Use variables identified as drivers to build predictive models
  * Evaluate models on train and validate data
  * Select the best model based on highest accuracy
  * Evaluate the best model on test data

# Data Dictionary 

The following dictionary only defines columns used in analysis for this dataset.

| Feature | Definition |
|:--------|:-----------|
|Churn| True or False, Displays if a customer has churned or not|
|Monthly Charges| The amount in dollars a customer is charged each month|
|Billing Type| Way in which a customer pays bills: Automatic billing or Manual billing |
|Dependents| Yes or no category, does client have dependents?|

# Reproduction Instructions


 1. Clone this repo.
 2. Acquire the data from codeup
 3. Put the data in the file containing the cloned repo.
 4. Run notebook.


# Takeaways and Conclusions

* Higher monthly charges seem to be a driver of churn
* Customers with automatic billing seem to churn at a lower rate than those who pay manually
* The longer the contract, the less likely a customer will churn
* Having dependents does seem to affect churn, indicating that nor only financial factors can be good predictors


# Recommendations

* Focus on incentivising long term contracts with customers
* Push family plans to draw in those with dependents
