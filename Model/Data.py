import pandas as pd

# A class for handling the data used for creating a regression model
class Data:
    def __init__(self, filepath):
        self.data = None
        self.data_file_path = filepath

    # Load data from a csv file at filepath
    def load_data(self):
        # Read csv file
        self.data = pd.read_csv(self.data_file_path,
                               dtype={'LoanNr_ChkDgt': str, 'NAICS': str, 'Zip': str, 'FranchiseCode': str,
                                      'UrbanRural': str, }, parse_dates=True, low_memory=False)

    # Format the data so it can be used for regression modeling
    def clean_data(self):
        # Only take data with non-null MIS_Status
        self.data = self.data[self.data['MIS_Status'].notna()]
        # Use the mean for any missing values
        self.data['State'] = self.data['State'].fillna('CA')
        self.data['NewExist'] = self.data['NewExist'].fillna(1.0)
        self.data = self.data.rename(columns={"UrbanRural": "Area", "NewExist": "Business"})
        # Format Dates and Money Values
        self.data['ApprovalDate'] = pd.to_datetime(self.data['ApprovalDate'], dayfirst=True)
        self.data['ChgOffDate'] = pd.to_datetime(self.data['ChgOffDate'], dayfirst=True)
        self.data['DisbursementDate'] = pd.to_datetime(self.data['DisbursementDate'], dayfirst=True)
        self.data['DisbursementGross'] = self.data['DisbursementGross'].replace('[\$,]', '', regex=True).astype(float)
        self.data['BalanceGross'] = self.data['BalanceGross'].replace('[\$,]', '', regex=True).astype(float)
        self.data['GrAppv'] = self.data['GrAppv'].replace('[\$,]', '', regex=True).astype(float)
        self.data['SBA_Appv'] = self.data['SBA_Appv'].replace('[\$,]', '', regex=True).astype(float)
        self.data['ApprovalFY'] = self.data['ApprovalFY'].replace('1976A', '1976', regex=True).astype(float)
        # Format data for dummying
        self.data['Area'] = self.data['Area'].replace('0', 'Urban', regex=True).astype(str)
        self.data['Area'] = self.data['Area'].replace('1', 'Urban', regex=True).astype(str)
        self.data['Area'] = self.data['Area'].replace('2', 'Rural', regex=True).astype(str)
        self.data['Business'] = self.data['Business'].replace('1.0', 'Existing', regex=True).astype(str)
        self.data['Business'] = self.data['Business'].replace('2.0', 'New', regex=True).astype(str)
        self.data['Business'] = self.data['Business'].replace('0.0', 'Existing', regex=True).astype(str)
        self.data['Business'] = self.data['Business'].replace('1.0', 'Existing', regex=True).astype(str)
        # Only keep first two NAICS characters for the general industry field
        self.data['NAICS'] = self.data['NAICS'].str[:2]

    # Create dummy variables for UrbanRural, MIS_Status and NewExist
    def dummy_data(self):
        self.data = pd.get_dummies(self.data, prefix=None, columns=['Area', 'Business', 'MIS_Status'])
        return self.data

    def get_data(self):
        return self.data

