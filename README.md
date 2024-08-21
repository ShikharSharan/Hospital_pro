# Hospital_pro

def collect_data():
    # Assuming you have radio buttons for gender
    if male_radio.isChecked():
        gender = "Male"
    elif female_radio.isChecked():
        gender = "Female"
    elif others_radio.isChecked():
        gender = "Others"
    else:
        gender = "Not specified"
    
    # Assuming the blood group is selected from a dropdown
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









![image](https://github.com/user-attachments/assets/651c7b9d-5dd9-48ce-962e-1ba0919e2118)
