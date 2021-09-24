# Loan Default Prediction Machine Learning Application
 
 
 ## Quick Start Guide
 The product includes an executable file in the “Application” subdirectory. It can be executed by double clicking on the “main” file in that directory.  In order to meet the 200MB file size limit for submissions, I only included about 10% of the original SBA data.  This subset is fairly representative of the original dataset.  The accuracy of the model is slightly lower, but still above 80%.
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

## Assessment of Accuracy
Python libraries such as “sklearn” gave us a number of means to determine the accuracy of our regression model. The metrics module in particular offered many tools. Using its score methods, our model received the following results:

Accuracy: 0.8242380468318086
Precision: 0.826697366708408
Recall: 0.9956215979545835


This is accuracy and precision of around 82%, which is satisfactory for a machine learning model.  
