# Logistic Regression Loan Prediction Application
 
 
 ## Quick Start Guide
 The application can be downloaded from here: https://drive.google.com/drive/folders/1QNbtPltEAwr5TWPEaajnwg6eAw20xOd. It can be executed by double clicking on the “main” file in that directory.  To limit the overall filesize, I only included about 10% of the original SBA data.  This subset is fairly representative of the original dataset.  The accuracy of the model is slightly lower, but still above 80%.
The original data file is included with the source code in the ‘src’ directory.  To run the program from source you may follow these instructions:
1.	Open the code file in the PyCharm Python IDE.
2.	Set the Python interpreter to 3.9: 
a.	Hold ‘ctrl + alt + s’ to open the settings
b.	Click the Project:src tab
c.	Select Python Interpreter
d.	Select Python 3.9 from the dropdown
3.	Use pip to install the following libraries:
•	Pandas
•	PyQt5
•	PyQtChart
•	sklearn
•	statsmodels
4.	Hold Shift + f10 to run the program.

Warning: The SBA loan data file is quite large and machine learning algorithms can be computationally complex. The program may become unresponsive for periods of time on a computer with an older or low-end CPU.
With the project installed, users can immediately begin using it.  Clicking on the New Loan prediction button will open a dialog with multiple inputs.  Users can enter an applicant’s information and receive the predicted chance of loan payback.
The Data Visualization button will open a dialog with multiple graphs.  The user can use a combo box to choose which data they want to view.  The Model Statistics button opens a dialog with information on the regression model itself.  Users can view statistics like accuracy, model coefficients, and mean values of the data.

## Problem Summary
The Small Business Administration is tasked with aiding small businesses in securing the loans they require to grow and prosper. This is primarily achieved through partnerships with banks, credit unions, and development agencies. The SBA encourages lending by guaranteeing a small percentage of the total disbursement amount. Although the agency’s efforts have helped create and sustain many companies, it does not have a perfect track record. In 2006, 6.24% of all SBA loans resulted in default. That number increases to 19.51% for its direct loan program (SBA Loss Report, 2006). This equals a loss of billions for taxpayers but also harms the businesses and entrepreneurs that the loans were meant to assist. 
Machine learning and data science can be used to increase the success of the SBA’s loan program and help even more Americans prosper.  My proposed solution will use data from the SBA’s loan program to “train” a model that will predict the default chances of applicant businesses.  New data visualizations will also help SBA employees understand how company information affects their likelihood to repay loans.

## Customer Benefits
As an organization whose primary purpose is to support the nation’s small businesses, the Small Business Administration must be capable of determining where their resources are best directed. Greater accuracy in loan payback predictions will reduce the waste of taxpayer money as well as the burden of debt on the businesses receiving the loans. With less waste, the SBA will be able to support more businesses in a time of great economic uncertainty and turmoil.
Through a relatively minor investment in machine learning technologies, the SBA will gain greater insights into their own, historical loan data. With this newfound knowledge, the agency will benefit more businesses and safeguard taxpayer investments.

## Data Product Outline
The data product will consist of a Python 3.9 desktop application built using the PyQt5 GUI framework.  The program will also use external libraries such as pandas, sklearn, and statsmodels to create a logistic regression model.  It will include the following capabilities:
•	Historical SBA loan data will be imported and “cleaned” for use in the data product.
•	The loan data will be used to train and test a logistic regression machine learning model.
•	SBA Employees will be able to input new applicant information and receive a quick and accurate response on the likelihood of loan default.
•	SBA Employees will be able to view key indicators and their impact on creditworthiness using data visualization tools.
•	SBA employees will be able to view metrics on the accuracy and reliability of the machine learning model.

## Data Description
The data used for this proposal is released by the Small Business Administration itself. It contains approximately one million records of small businesses that received loans from the SBA between the years 1966 and 2014.  The data was obtained directly from the Small Business Administration by Li, M…, et al (Li, Mickel, & Taylor, 2018).  The authors formatted the data in a convenient manner with clearly defined attributes.  
For logistic regression to function, there needs to be a binary output variable. The “MIS_Status” attribute will serve as that variable, as it represents the default status of the loan record.  There are 27 attributes in total including information on the firm's geographic location, loan amounts, industry type, and the timeframe of the loan.
To use the data in a regression model, it will need to undergo formatting.  Certain missing values will be dropped from the set completely. There are a small number of empty “MIS_Status” records, which will be purged.  Additionally, “dummy variables” will need to be created for certain attributes. Rural versus urban, to name one example, needs to be separated into two different columns. Each column will contain either a one or a zero representing the Boolean value. This will allow our regression model to analyze those columns.

## Objectives & Hypotheses
This proposal has the following objectives:
•	To create a logistic regression machine learning application for predicting default on SBA-backed loans
•	The application must achieve an accuracy rating of at least 80%
•	The application must return a default probability in less than ten seconds
•	The application must generate data visualizations based on key indicators
•	The application must display information about the reliability of the regression model
I hypothesize that a logistic regression model will discover relationships between various attributes that relate to the probability of loan default. I believe the term length, disbursements, and geographic region are some of the indicators that can lead to reliable predictions of loan outcomes.  Some predictors may be obvious to the SBA, such as larger subsidized disbursements leading to higher rates of full payback.  Others may be less intuitive, however.  With these predictors, the Small Business Administration should be able to avoid high-risk loans and save taxpayers and businesses from the detrimental effects of bad debt.

## Project Methodology
I will use the waterfall method for developing the application. I have chosen to use this method as I have already created a rough outline of the requirements of the project. This will allow me to separate the development into specific tasks, each having a start and end date.
The first task will be holding discussions with stakeholders about their requirements for the project.  These talks will lead into the design phase, where the data will be explored, and technical specifications will be created.  Next, the development of the application will begin.  The model and GUI application will be created. Finally, testing will be done to verify the correct functionality of the program.

## Solution Impact
Organizations with large amounts of business data can oftentimes struggle to fully comprehend its meaning.  Machine learning offers a way for these organizations to gain insights into their information in relatively short periods of time.  The proposed project will allow the SBA to use their data to more accurately determine what firms are worthy of receiving subsidized loans.  By identifying key indicators of loan defaults, the SBA will reduce the burden of unsustainable debt on the small businesses they are trying to help. They will, at the same time, reduce the waste of taxpayer dollars, and ensure they can continue their founding mission.

## Ethical & Legal Considerations
It is important to protect individuals’ privacy when working with their data. Many big data systems use large amounts of sensitive data that could cause harm, especially in the financial industry. For this reason, there are precautions that need to be taken when working with such data.  A common action is to anonymize certain attributes, such as names, account numbers, and addresses. In our case, we are working with government data, which has already been made available to the public. There are no individual names or private addresses, only company information. As a result, we do not need to alter the data to protect anyone’s privacy.

## Creator’s Expertise
With several years of experience in the machine learning field as well as a degree in computer science, I am confident in my ability to create this data product. I have implemented logistic regression models in the public health realm and those skills will easily transfer to a financial setting. I have made extensive use of the Python programming language and the relevant libraries, including pandas, sklearn, and PyQt5.
In addition to my technical skills, I am knowledgeable in project management, having achieved both the CompTIA Project+ and the AXELOS ITIL Foundation certifications. This will aid me in planning for the project and seeing it through to completion.

## Assessment of Accuracy
Python libraries such as “sklearn” gave us a number of means to determine the accuracy of our regression model. The metrics module in particular offered many tools. Using its score methods, our model received the following results:

1. Accuracy: 0.8242380468318086
2. Precision: 0.826697366708408
3. Recall: 0.9956215979545835


This is accuracy and precision of around 82%, which is satisfactory for a machine learning model.  
