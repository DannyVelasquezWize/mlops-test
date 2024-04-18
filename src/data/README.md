# Data origins
File was downloaded from Kaggle page: [dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

## Data Dictionary:

1. INTEGER - id (Unique id for each patient)
2. INTEGER - age (Age of the patient in years)
3. STRING - sex (Male/Female)
4. STRING - dataset (place of study)
5. STRING - cp chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic])
6. INTEGER - trestbps resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital))
7. INTEGER - chol (serum cholesterol in mg/dl)
8. BOOL - fbs (if fasting blood sugar > 120 mg/dl)
9. STRING - restecg (resting electrocardiographic results) -- Values: [normal, stt abnormality, lv hypertrophy]
10. INTEGER - thalach: maximum heart rate achieved
11. BOOL - exang: exercise-induced angina (True/ False)
12. FLOAT - oldpeak: ST depression induced by exercise relative to rest
13. STRING - slope: the slope of the peak exercise ST segment
14. INTEGER ca: number of major vessels (0-3) colored by fluoroscopy
15. STRING - thal: [normal; fixed defect; reversible defect]
16. INTEGER - num: the predicted attribute - target [0=no heart disease; 1,2,3,4 = stages of heart disease ]