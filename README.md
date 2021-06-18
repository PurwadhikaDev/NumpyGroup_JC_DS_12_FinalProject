# NumpyGroup_JC_DS_12_FinalProject
Team Members: 
- **Fajar Setiawan** (jarbling@gmail.com)
- **Fransiskus Alvin Andriyanto** (fransiskusalvin@yahoo.com)
- **Panji Agdiwijaya** (agdiwijaya@gmail.com)

# CREDIT CARD CUSTOMER CLUSTERING OPTIMIZED WITH MULTICLASS MACHINE LEARNING MODELLING

## BACKGROUND
Almost every American, it seems, gets a new credit card offer in the mail almost every week. Credit cards are highly profitable, but only if the customers stays around for a while. It **costs about 80 dollars** to **acquire a new credit card customer** who **returns about 120 dollars per year** in profit, but **only if the customers keeps the card**. If customers **drops the card after a few weeks, or doesn’t use the card**, the issuer will **lose that 80 dollars, plus some more money spent trying to reactivate them**.

[Source](https://www.dbmarketing.com/articles/Art175.htm)

## WORKFLOW PROCESS 

![image](https://user-images.githubusercontent.com/78836373/120300137-d9b18d00-c2f5-11eb-9f5c-56fe6224274f.png)

## 1. BUSINESS PROBLEMS
- **Customer loyalty** is one of the **key** to survive in this credit card business competition [(source)](https://www.dbmarketing.com/articles/Art175.htm)
- The **cost of acquiring new customers** is estimated at **five times** the rate of **retaining existing ones** [(source)](https://www.fpsc.com/the_cost_of_customer_churn.pdf)
- In order to retain customers, we must first understanding our **Customers Type and Customers Behaviour**
- Previously, our bank **only has 1 product of credit card**, resulting **low customer loyalty** because **inaccurate marketing program**
- After do long research, our management decides to make 3 different products: **Business Unlimited (High), Business Cash (Medium), and Performance Business (Low)**
- In other hand, the company **doesn't know which customers belongs to which products**

## 2. GOALS SETTINGS
- Understanding **Customers Type** and **Customer Behaviour** through **Customer Data Clustering**
- **Define product details** based on **Clustering Results** to ensure that customers get the proper product
- **Help Marketing Team** to define new Customers Type through **Multiclass Clasification Machine Learning Technique**

## 3. DATA EXTRACTION, DATA LOAD, AND DATA UNDERSTANDING
- Our data set is taken from [Kaggle](https://www.kaggle.com/arjunbhasin2013/ccdata)
- Below is the small part of our dataset which consists of **18 Features** and **8950 data**

CUST_ID | BALANCE | BALANCE_FREQUENCY | PURCHASES | ONEOFF_PURCHASES | INSTALLMENTS_PURCHASES | CASH_ADVANCE | PURCHASES_FREQUENCY | ONEOFF_PURCHASES_FREQUENCY | PURCHASES_INSTALLMENTS_FREQUENCY | CASH_ADVANCE_FREQUENCY | CASH_ADVANCE_TRX | PURCHASES_TRX | CREDIT_LIMIT | PAYMENTS | MINIMUM_PAYMENTS | PRC_FULL_PAYMENT | TENURE
-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----
C10001 | 40.900749 | 0.818182 | 95.4 | 0 | 95.4 | 0 | 0.166667 | 0 | 0.083333 | 0 | 0 | 2 | 1000 | 201.802084 | 139.509787 | 0 | 12
C10002 | 3202.467416 | 0.909091 | 0 | 0 | 0 | 6442.945483 | 0 | 0 | 0 | 0.25 | 4 | 0 | 7000 | 4103.032597 | 1072.340217 | 0.222222 | 12
C10003 | 2495.148862 | 1 | 773.17 | 773.17 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 12 | 7500 | 622.066742 | 627.284787 | 0 | 12
C10004 | 1666.670542 | 0.636364 | 1499 | 1499 | 0 | 205.788017 | 0.083333 | 0.083333 | 0 | 0.083333 | 1 | 1 | 7500 | 0 |  | 0 | 12
C10005 | 817.714335 | 1 | 16 | 16 | 0 | 0 | 0.083333 | 0.083333 | 0 | 0 | 0 | 1 | 1200 | 678.334763 | 244.791237 | 0 | 12

Below is the definition of each features:
- `CUST_ID` - Identification of Credit Card Holder
- `BALANCE` - Balance amount left in their account to make purchases
- `BALANCE_FREQUENCY` - How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated)
- `PURCHASES` - Amount of purchases made from account 
- `ONEOFF_PURCHASES` - Maximum purchase amount done in one-go
- `INSTALLMENTS_PURCHASES` - Amount of purchase done in installment
- `CASH_ADVANCE` - Amount of Cash Money user take from credit card
- `PURCHASES_FREQUENCY` - How frequent the Purchases are being made, score between 0 and 1 (1 = frequently purchased, 0 = not frequently purchased)
- `ONEOFF_PURCHASES_FREQUENCY` - How frequent Purchases are happening in one-go (1 = frequently purchased, 0 = not frequently purchased)
- `PURCHASES_INSTALLMENTS_FREQUENCY` - How frequent purchases in installments are being done (1 = frequently done, 0 = not frequently done)
- `CASH_ADVANCE_FREQUENCY` - How frequent user take money from credit card
- `CASH_ADVANCE_TRX` - Number of Transactions made with "Cash in Advanced" 
- `PURCHASES_TRX ` - Number of purchase transactions made 
- `CREDIT_LIMIT` - Limit of Credit Card for user
- `PAYMENTS` - Amount of Payment done by user
- `MINIMUM_PAYMENTS` - Minimum amount of payments made by user
- `PRC_FULL_PAYMENT` - Percent of full payment paid by user
- `TENURE` - Tenure of credit card service for user

## 4. DATA CLEANING
#### MISSING VALUE HANDLING
- From our dataset, we got several missing value which most of them are **MINIMUM_PAYMENTS**

![image](https://user-images.githubusercontent.com/78836373/120305580-1f248900-c2fb-11eb-9dfe-8a22e64e4605.png)

- Missing Value on **MINIMUM_PAYMENTS** is filled with 0 assuming the customers haven't made any PAYMENTS (PAYMENTS = 0)
- Missing Value on **MINIMUM_PAYMENTS** is filled with same value of PAYMENTS because the customers have PAYMENTS data recorded 
- Missing Value on **CREDIT_LIMIT** is dropped because there is only 1 CREDIT_LIMIT data that has null value

#### REMOVE UNECESSARY COLUMNS:
- Since **CUST_ID** has object and has **no relation for analysis**, we will **drop CUST_ID**

## 5. DATA CLUSTERING
Based on **problems** and added by **research results**, we **utilize 3 features** that might be the factors for **customer segmentation**:
- **BALANCE**
- **PURCHASES**
- **CREDIT_LIMIT**

Source :
- [Research 1](https://creditcards.chase.com/)
- [Research 2](https://www.mckinsey.com/~/media/mckinsey/dotcom/client_service/Financial%20Services/Latest%20thinking/Payments/MoP19_New%20frontiers%20in%20credit%20card%20segmentation.ashx)

For clustering we use **three algorithm**: 
1. **KMeans**
2. **AHC** 
3. **Gaussian Mixture**  

[For further details please refer to Clustering Notebook](https://github.com/PurwadhikaDev/NumpyGroup_JC_DS_12_FinalProject/blob/main/1_Clustering_CreditCardCustomerSegmentation.ipynb) 

Below is our **Silhouette Score** comparison for each algorithm and each number segment:

![image](https://user-images.githubusercontent.com/78836373/120307310-07e69b00-c2fd-11eb-93fd-353f5520b6a4.png)

- From the Silhouette Score using three different methods (KMeans, AHC, Gaussian Mixsture), the best number of clusters obtained is 2.
- Nevertheless, we choose to use **3 clustering** due to **Business Demand and Simulation**.
- Within 3 clustering, AHC method has better Silhouette Score (0.52) compared to KMeans (0.48). However, we choose **KMeans** method because has **better seperation of grouping** 

Below is our **Clustering Visualization** Result using KMeans Algorithm: 

![image](https://user-images.githubusercontent.com/78836373/120307620-6449ba80-c2fd-11eb-988c-320f4e0d3370.png)
![image](https://user-images.githubusercontent.com/78836373/120307642-6c095f00-c2fd-11eb-96c9-8585c2551ca6.png)
![image](https://user-images.githubusercontent.com/78836373/120307667-73c90380-c2fd-11eb-866a-3a744e126aa7.png)

![](https://github.com/PurwadhikaDev/NumpyGroup_JC_DS_12_FinalProject/blob/main/Media/VID-20210602-WA0000_1_1_3.gif)

From Insight Above we can conclude:
* **SEGMENT 0 : LOW CUSTOMERS** This customer group indicates a large group of customers who have **LOW BALANCES**, **small spenders (LOW PURCHASES**) with the **LOWEST CREDIT LIMIT**. 

* **SEGMENT 1 : MEDIUM CUSTOMERS** This customer group indicates a small group of customers who have **LOW-MEDIUM BALANCES**, **intermediate spenders (LOW-MEDIUM PURCHASES)** with **intermediate CREDIT LIMIT**.

* **SEGMENT 2 : HIGH CUSTOMERS** This customer group indicates a small group of customers who have **LOW-HIGH BALANCES**, **high spenders (LOW-HIGH PURCHASES)** with **HIGH CREDIT LIMIT**.

## 6. EXPLORATORY DATA ANALYSIS

For EDA we do the following steps below:
- **Binning**
- **Aggregating Columns**
- **Visualization**
- **Insight & Conclusion**

**BUSINESS QUESTIONS** 
- What features which have impact to SEGMENT?

**EDA SUMMARY:**
- **BALANCE** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120447971-4b044500-c3b5-11eb-8619-54da4177e6cb.png)

- **PURCHASES** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448059-60796f00-c3b5-11eb-8b4f-091f4992655c.png)

- **ONEOFF_PURCHASES** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448156-7a1ab680-c3b5-11eb-809a-d553261ba84d.png)

- **INSTALLMENT_PURCHASES** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448210-8acb2c80-c3b5-11eb-82c3-a385c055485c.png)

- **CASH_ADVANCE_PURCHASES** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448285-9dddfc80-c3b5-11eb-8e92-33c6420cc96a.png)

- **CREDIT_LIMIT** has significant impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448353-b1896300-c3b5-11eb-8fb2-e06c45f0451a.png)

- **PAYMENTS** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448859-29f02400-c3b6-11eb-85b3-519573d29a3f.png)

- **MINIMUM_PAYMENTS** has low impact to SEGMENT

![image](https://user-images.githubusercontent.com/78836373/120448900-35434f80-c3b6-11eb-82cb-0e35153d21ff.png)

- Customer SEGMENTATION influenced by many Features

[For Further details please refer EDA Notebook](https://github.com/PurwadhikaDev/NumpyGroup_JC_DS_12_FinalProject/blob/main/2_EDA_CreditCardCustomerSegmentation.ipynb)

**EDA RECOMMENDATION:**
- Based on our analysis, we recommend to use **all features for Machine Learning**

## 7. MACHINE LEARNING MODELLING

Since our dataset have 3 SEGMENT/**Multiclass** where:
- **SEGMENT 0**: LOW CUSTOMERS      
- **SEGMENT 1**: MEDIUM CUSTOMERS       
- **SEGMENT 2**: HIGH CUSTOMERS 
  
With **SEGMENT Composition** down below:

![image](https://user-images.githubusercontent.com/78836373/120308724-9ad40500-c2fe-11eb-9dae-a923c2e2c64b.png)

We will **focus** to obtain Machine Learning Model with the best **Accuracy Score**

**Features Selection:**
- For this model we will use all features, because from EDA results, the customer segmentation is affected by all features from dataset

For Machine Learning modelling we utilize all data features and utilize 3 different algorithm:
1. **Random Forest**
3. **Logistic Regression**
4. **KNN Classifier**

Below we provided table to **Compare Accuracy Score** based on our choosen algorithm

![image](https://user-images.githubusercontent.com/78836373/120584921-0501bc80-c45b-11eb-93bc-abeeb097c4df.png)

- **Random Forest** result accuracy is already **good**, in other hand, this model is categorized as **Strong Learner** model which causing the model might be only memorizing the data, and not learning the pattern. So we want to decrease accuracy score to get a **Good Learner** and get more suitable confusion matrix through Hyper Parameter Tuning.

[For Further details please refer Machine Learning Notebook](https://github.com/PurwadhikaDev/NumpyGroup_JC_DS_12_FinalProject/blob/main/3_ML_CreditCardCustomerSegmentation.ipynb)

**MACHINE LEARNING SUMMARY**:
- From the initial machine learning modelling, there are **no overfit result** on all over model algorithm
- We **suggest** to use **Random Forest Tuned**, because after analysis it has the best accuracy score 93% (not so high) with the most suitable confusion matrix 
- How this model will help bank company?
    - This model will allow bank marketing team to take actions on identified as "customer segment", furthermore the development of these model should contribute to bank revenue management.
    - These prediction models enable marketing teams to mitigate profit loss derived from customer churn caused by unsuitable marketing program

**MACHINE LEARNING RECOMMENDATION**:
- This Machine Learning could be used for **customer segmentation based on their credit card usage behaviour**.
- The result from this project could be used by **marketing team** to offer suitable product for new customers based on their segmentation which is predict through Machine Learning Model

## PROJECT RECOMENDATION 
DETAIL PRODUCT SUGGESTION:

- **PERFORMANCE CREDIT CARD** DETAIL PRODUCT:
    - GET REWARDS with Monthly **Minimum Purchases 500 dollars**
    - **CREDIT_LIMIT: 5000 dollars**

- **BUSINESS CASH CREDIT CARD** DETAIL PRODUCT:
    - GET REWARDS with Monthly **Minimum Purchases 1200 dollars**
    - **CREDIT_LIMIT: 13000 dollars**
    
- **BUSINESS UNLIMITED CREDIT CARD** DETAIL PRODUCT:
    - GET REWARDS with Monthly **Minimum Purchases 3500 dollars**
    - **CREDIT_LIMIT: 30000 dollars**
    
We Suggest:
- Offer **LOW CUSTOMERS SEGMENT** with **PERFORMANCE CREDIT CARD**
- Offer **MEDIUM CUSTOMERS SEGMENT** with **BUSINESS CASH CREDIT CARD**
- Offer **HIGH CUSTOMERS SEGMENT** with **BUSINESS UNLIMITED CREDIT CARD**

## BUSINESS IMPACT

From our [research](https://www.statista.com/statistics/816735/customer-churn-rate-by-industry-us/), current **credit card churn is about 25%**.
With the help of our Clustering and Multiclass Machine Learning Modeling, we simulate that credit card churn **will drop into 7%**.

Assuming number of customers and lost per customers as down below:

![image](https://user-images.githubusercontent.com/78836373/120530327-96dfda00-c407-11eb-9c26-c6d8b7a32664.png)

Attached below is **rough calculation** Lost Customer Cost Without Machine Learning vs Lost Customer Cost with Machine Learning

![image](https://user-images.githubusercontent.com/78836373/120474772-cc1e0500-c3d2-11eb-9aec-b115f0cb2cd8.png)

Using our Multiclass Machine Learning Modelling, our company **could save money** around **14,400,000 dollars!!**

![image](https://user-images.githubusercontent.com/78836373/120474804-d6400380-c3d2-11eb-83de-177e78c84353.png)

## FURTHER RESEARCH (NEXT ACTION)
- For further research information, customer behaviour (Payment history, Length of credit history, New credit, The variety of credit products you have, including credit cards, installment loans, finance company accounts, mortgage loans and so on) could be included into the dataset in hope to improve the models and measure the importance of these features

## 8. MODEL DEPLOYMENT PREVIEW (FLASK DASHBOARD)

### HOME PAGE

![image](https://user-images.githubusercontent.com/78836373/122417753-ebf91f80-cfb3-11eb-99ff-bc08b5901ad8.png)


### ABOUT PAGE

![image](https://user-images.githubusercontent.com/78836373/122417922-0fbc6580-cfb4-11eb-9ab4-60f5301b5335.png)
![image](https://user-images.githubusercontent.com/78836373/122417980-1a76fa80-cfb4-11eb-9d30-253df5dfcdd4.png)


### DATA PAGE

![image](https://user-images.githubusercontent.com/78836373/122418552-7ccffb00-cfb4-11eb-992f-65a83acae508.png)
![image](https://user-images.githubusercontent.com/78836373/122418606-85c0cc80-cfb4-11eb-8755-a06560ca6fe4.png)


### INPUT NEW DATA PAGE

![image](https://user-images.githubusercontent.com/78836373/122418694-97a26f80-cfb4-11eb-866a-5aeb941f744c.png)


### CUSTOMER SEGMENTATION PREDICTION

![image](https://user-images.githubusercontent.com/78836373/122418752-a2f59b00-cfb4-11eb-9c68-97b3aa935803.png)

[For Further details please refer Dashboard File](https://github.com/PurwadhikaDev/NumpyGroup_JC_DS_12_FinalProject/tree/main/Dashboard)
