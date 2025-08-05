import pandas as pd

def imputer(row, grouped_data):
    doctor = row['Doctor']
    age = row['patient_age']
    gender = row['patient_gender']

    doctor_group = grouped_data.get_group(doctor) # get the Group of the doctor


    gender_filter = doctor_group[doctor_group['patient_gender'] == gender]  # Filter the result by the gender of the patient 


    dept_avg_age = gender_filter.groupby('department_referral')['patient_age'].mean()   # Calculate the mean age of the gender in the each department

    age_difference = []

    for dept, avg_age in dept_avg_age.items():
        difference = abs(age - avg_age)
        age_difference.append((dept, difference))

    age_difference.sort(key=lambda x: x[1])

    return age_difference[0][0]  # closest department


def sat_imputer(row, grouped_data):
    doctor = row['Doctor']

    doctor_group = grouped_data.get_group(doctor)

    mode_sat_score = doctor_group['patient_sat_score'].value_counts()[0]
    
    return float(mode_sat_score)

    