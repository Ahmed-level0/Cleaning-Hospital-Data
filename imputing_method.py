import pandas as pd

def imputer(row, grouped_data):
    doctor = row['Doctor']
    age = row['patient_age']
    gender = row['patient_gender']

    doctor_group = grouped_data.get_group(doctor)


    gender_filter = doctor_group[doctor_group['patient_gender'] == gender]


    gender_filter = doctor_group  # fallback if no same-gender data

    dept_avg_age = gender_filter.groupby('department_referral')['patient_age'].mean()

    age_difference = []
    for dept, avg_age in dept_avg_age.items():
        difference = abs(age - avg_age)
        age_difference.append((dept, difference))

    age_difference.sort(key=lambda x: x[1])

    return age_difference[0][0]  # closest department