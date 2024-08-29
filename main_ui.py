import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QRadioButton,QComboBox
from PyQt5.QtCore import Qt
import random
from datetime import datetime
import string
#from email_validator import validate_email, EmailNotValidError
import re
from main_py import *
from welcome_ui import create_after_login_page

def on_login_button_click():
    patient_id = username_input.text()
    password = password_input.text()

    if not patient_id or not password:
        nortification_label.setText("Input Error: Both fields are required.")
        return

    if verify_login(patient_id, password):
        print("yesssss")
        nortification_label.setText("Login Successful!")
        # Close the current login window
        window.close()
        # Launch the new welcome UI
        welcome_window = create_after_login_page(patient_id)
        welcome_window.show()
        app.active_window = welcome_window
    else:
        nortification_label.setText("Login Failed: Invalid Patient ID or Password.")


def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def collect_data():
    if Male_button.isChecked():
        gender = "Male"
    elif Female_button.isChecked():
        gender = "Female"
    elif Other_button.isChecked():
        gender = "Others"
    else:
        gender = "Not specified"
    
    blood_group = Blood_group_input.currentText()

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
    insert_data_into_redshift(patient_data)
#create_button.clicked.connect(on_create_button_click)

def on_create_button_click():
    # Check if any field is empty
    if not (Patient_Fname_input.text() and Patient_lname_input.text() and Phone_number_input.text() and 
            Blood_group_input.currentText()  #and email_input.text()
            and 
            create_password_input.text() and confirm_password_input.text()):
        space_button.setText("Input Error: All fields are required.")
        return
    
    # Check if phone number is 10 digits
    if len(Phone_number_input.text()) != 10 or not Phone_number_input.text().isdigit():
        space_button.setText("Input Error:  Phone number must be 10 digits.")
        return

    # Check if passwords match
    if create_password_input.text() != confirm_password_input.text():
        space_button.setText("Input Error:  Passwords do not match.")
        return
    
    #email validation
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email_input.text())):
        pass
 
    else:
        space_button.setText("Invalid email")
        return
    #if not check(email_input.text()):
    
    #create_button.clicked.connect(collect_data)
    collect_data()
    space_button.setText("Success:  Account created successfully!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('LOGIN PAGE')
window.setGeometry(100, 100, 1800, 900)
main_layout = QHBoxLayout()

login_layout = QVBoxLayout()
login_layout.addStretch()

label = QLabel('LOGIN')
label.setAlignment(Qt.AlignCenter)
login_layout.addWidget(label)

username_layout = QHBoxLayout()
username_label = QLabel('Patient_ID:')
username_layout.addWidget(username_label)

username_input = QLineEdit()
username_layout.addWidget(username_input)

login_layout.addLayout(username_layout)
login_layout.addSpacing(40)

password_layout = QHBoxLayout()
password_label = QLabel('Password:')
password_layout.addWidget(password_label)

password_input = QLineEdit()
password_layout.addWidget(password_input)

login_layout.addLayout(password_layout)
login_layout.addSpacing(40)

nortification_layout = QHBoxLayout()
nortification_label = QLabel("")
nortification_layout.addWidget(nortification_label)
login_layout.addLayout(nortification_layout)


button_layout = QHBoxLayout()
login_button = QPushButton("Login")
button_layout.addWidget(login_button)

login_layout.addLayout(button_layout)
login_layout.addStretch()

signup_layout = QVBoxLayout()
signup_layout.addStretch()

label2 = QLabel("SignUP")
label2.setAlignment(Qt.AlignCenter)
signup_layout.addWidget(label2)

Patient_fname_layout = QHBoxLayout()
Patient_first_name_label = QLabel('Patient_FName')
Patient_fname_layout.addWidget(Patient_first_name_label)
Patient_Fname_input = QLineEdit()
Patient_Fname_input.setFixedSize(300, 20)
Patient_fname_layout.addWidget(Patient_Fname_input)
signup_layout.addLayout(Patient_fname_layout)
signup_layout.addSpacing(20)

Patient_lname_layout = QHBoxLayout()
Patient_lname_name_label = QLabel('Patient_LName')
Patient_lname_layout.addWidget(Patient_lname_name_label)
Patient_lname_input = QLineEdit()
Patient_lname_input.setFixedSize(300, 20)
Patient_lname_layout.addWidget(Patient_lname_input)
signup_layout.addLayout(Patient_lname_layout)
signup_layout.addSpacing(20)

Phone_number_layout = QHBoxLayout()
Phone_number_label = QLabel('Phone')
Phone_number_layout.addWidget(Phone_number_label)
Phone_number_input = QLineEdit()
Phone_number_input.setFixedSize(300, 20)
Phone_number_layout.addWidget(Phone_number_input)
signup_layout.addLayout(Phone_number_layout)
signup_layout.addSpacing(20)

Blood_group_layout = QHBoxLayout()
Blood_group_label = QLabel('Blood Group')
Blood_group_layout.addWidget(Blood_group_label)
Blood_group_input = QComboBox()
Blood_group_input.addItems(['','O+','O-','A+','A-','B+','B-','AB+','AB-'])
Blood_group_input.setFixedSize(300,20)
Blood_group_layout.addWidget(Blood_group_input)
signup_layout.addLayout(Blood_group_layout)
signup_layout.addSpacing(20)

Gender_layout = QHBoxLayout()
Gender_label = QLabel('Gender')
Gender_layout.addWidget(Gender_label)
Male_button = QRadioButton('Male')
Gender_layout.addWidget(Male_button)
Female_button = QRadioButton('Female')
Gender_layout.addWidget(Female_button)
Other_button = QRadioButton('Others')
Gender_layout.addWidget(Other_button)
signup_layout.addLayout(Gender_layout)

signup_layout.addSpacing(20)

email_layout = QHBoxLayout()
email_label = QLabel('Email :')
email_layout.addWidget(email_label)
email_input = QLineEdit()
email_input.setFixedSize(300, 20)
email_layout.addWidget(email_input)
signup_layout.addLayout(email_layout)
signup_layout.addSpacing(20)

create_passworrd_layout = QHBoxLayout()
create_password_label = QLabel('CreatePassword:')
create_passworrd_layout.addWidget(create_password_label)
create_password_input = QLineEdit()
create_password_input.setEchoMode(QLineEdit.Password)
create_password_input.setFixedSize(300, 20)
create_passworrd_layout.addWidget(create_password_input)
signup_layout.addLayout(create_passworrd_layout)
signup_layout.addSpacing(20)

confirm_password_layout = QHBoxLayout()
confirm_password_label = QLabel('Confirm_Password:')
confirm_password_layout.addWidget(confirm_password_label)
confirm_password_input = QLineEdit()
confirm_password_input.setEchoMode(QLineEdit.Password)
confirm_password_input.setFixedSize(300, 20)
confirm_password_layout.addWidget(confirm_password_input)
signup_layout.addLayout(confirm_password_layout)
signup_layout.addSpacing(20)

space_layout = QHBoxLayout()
space_button = QLabel(" ")
space_layout.addWidget(space_button)
signup_layout.addLayout(space_layout)
signup_layout.addSpacing(20)

create_button_layout = QHBoxLayout()
create_button = QPushButton("create")
create_button_layout.addWidget(create_button)
signup_layout.addLayout(create_button_layout)
signup_layout.addStretch()

main_layout.addStretch()
main_layout.addLayout(login_layout)
main_layout.addStretch()
main_layout.addLayout(signup_layout)
main_layout.addStretch()

create_button.clicked.connect(on_create_button_click) #signup here
login_button.clicked.connect(on_login_button_click)  #login function here
window.setLayout(main_layout)

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())
