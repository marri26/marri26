# Suggested code may be subject to a license. Learn more: ~LicenseLog:3914135866.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1374013346.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:413862720.
import pandas as pd
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3918647975.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import statsmodels.api as sm

# create a random data with fields name and age and save to a dataframe called user_details
user_details = pd.DataFrame({'name': np.random.choice(['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'], size=100),
                            'age': np.random.randint(18, 65, size=100)})
print(user_details.head())
