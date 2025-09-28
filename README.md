
play and have fun
#HR Attrition Prediction App – Summary Report

Purpose:
The HR Attrition Prediction App is designed to help organizations identify employees who are at risk of leaving. By predicting attrition likelihood, HR teams can take proactive steps to improve retention through targeted interventions, such as mentorship programs, workload management, or incentives.

Data Used:
The app uses the IBM HR Analytics Employee Attrition Dataset, which includes employee demographic information, job roles, salary, satisfaction scores, performance ratings, and other workplace metrics. The dataset is cleaned and preprocessed, including:

Dropping irrelevant columns (EmployeeCount, Over18, StandardHours, EmployeeNumber).

Handling categorical features using One-Hot Encoding.

Addressing class imbalance with SMOTE to ensure fair model training.

Machine Learning Models:
The app implements three models for attrition prediction:

Logistic Regression – predicts the probability of an employee leaving and identifies key features influencing attrition.

Decision Tree – provides an interpretable model showing how different employee attributes affect attrition.

Random Forest – an ensemble model that improves prediction accuracy and identifies the top 10 most important features impacting employee attrition.

Functionality:

User Input: HR personnel can input employee details such as age, job role, department, satisfaction scores, and overtime status.

Prediction Output: The app provides:

Probability of attrition (e.g., 0.24 → 24% chance of leaving).

Classification: Likely to stay or leave.

Feature Importance: Shows which factors most influence attrition for informed HR decision-making.

Visualization:
The app includes interactive charts for data exploration:

Distribution of employees by department, job role, gender, and education field.

Attrition patterns across categorical and numerical features.

Feature importance charts from Random Forest and Logistic Regression.

Impact:
This app allows HR teams to:

Identify high-risk employees in real-time.

Make data-driven decisions for retention programs.

Track employee risk scores for strategic workforce management
