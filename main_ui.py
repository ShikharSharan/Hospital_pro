def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def collect_data():
    if male_radio.isChecked():
        gender = "Male"
    elif female_radio.isChecked():
        gender = "Female"
    elif others_radio.isChecked():
        gender = "Others"
    else:
        gender = "Not specified"
    
    blood_group = blood_group_dropdown.currentText()

    patient_data = {
        "Patient_ID": generate_random_id(),
        "Patient_FName": Patient_Fname_input.text(),
        "Patient_LName": Patient_lname_input.text(),
        "Phone": Phone_number_input.text(),
        "Blood_Type": blood_group,
        "Email": email_input.text(),
        "Gender": gender,
        "Password": create_password_input.text(),
        "Admission_Date": generate_current_date(),
    }
    print(patient_data)
