# Import External Libs
import statsmodels.api as sm
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.rc("font", size=14)


class LogRegModel:
    # Class Constructor
    def __init__(self):
        self.data = None
        # Features/Inputs in to our model to predict loan default
        # Final list of potential features to include in the model
        self.loan_default_features = ['Area_Urban', 'Area_Rural', 'Business_New', 'Business_Existing', 'Term', 'NoEmp',
                                      'CreateJob', 'RetainedJob', 'DisbursementGross', 'GrAppv', 'SBA_Appv',
                                      'ApprovalFY']

    def make_pred_target(self, data):
        self.data = data
        # Prediction Target
        self.y = self.data['MIS_Status_P I F']
        self.X = self.data[self.loan_default_features]

    # Use statsmodels to ceate a Logistic Regression prediction model.
    # Statsmodels creates a better summary of the results.
    def make_sm_model(self):
        # Statsmodels version
        self.sm_model = sm.Logit(self.y, self.X.astype(float))
        self.sm_result = self.sm_model.fit(maxiter=200, method='newton')

    def set_sm_model(self, sm_model):
        self.sm_result = sm_model

    # Display the results of the statsmodels LogisticRegression.
    def get_sm_results(self):
        return self.sm_result.summary2()

    # Split data into training and testing data sets.
    def train_test_split(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.25,
                                                                                random_state=0)

    def get_mean(self):
        return self.data.groupby('MIS_Status_P I F').mean()

    # Create a Logistic Regression model with scikit-learn.
    def make_skl_model(self):
        # instantiate the LogisticRegression class
        self.logreg = LogisticRegression()
        # fit the model with the training data
        self.logreg.fit(self.X_train, self.y_train)
        # create a prediction for the test data
        self.y_pred = self.logreg.predict(self.X_test)
        return self.get_metrics()

    def make_y_pred(self):
        self.y_pred = self.logreg.predict(self.X_test)

    def get_lr_model(self):
        return self.logreg

    def set_lr_model(self, model):
        self.logreg = model

    # Create a Confusion Matrix of Results
    def create_conf_matrix(self):
        return metrics.confusion_matrix(self.y_test, self.y_pred)

    # Print metrics of the logreg model.
    def get_metrics(self):
        # Evaluate Metrics
        return {"Accuracy": metrics.accuracy_score(self.y_test, self.y_pred),
                "Precision": metrics.precision_score(self.y_test, self.y_pred, pos_label=1),
                "Recall": metrics.recall_score(self.y_test, self.y_pred, pos_label=1)}

    # Use model to make a prediction based on input business data. Returns array - [0] = probability of default.
    def make_pred(self, bus_data):
        return self.logreg.predict_proba(bus_data)[0][1] * 100
