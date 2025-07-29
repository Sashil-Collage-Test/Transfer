import numpy as np
import pandas as pd
playtennis=pd.read csv("D:\sumitp\STUDENT\TYCS_10\AI\AI Collage")
print("PlayTennis,"/n/n)
from sklearn.preprocessing import labelEncoder
le=LabelEncoder()
playtennis['Outlook']=le.fit_transform(playtennis['Temperature'])
