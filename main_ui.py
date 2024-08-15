import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

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
username_label = QLabel('Username:')
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
Blood_group_input = QLineEdit()
Blood_group_input.setFixedSize(300, 20)
Blood_group_layout.addWidget(Blood_group_input)
signup_layout.addLayout(Blood_group_layout)
signup_layout.addSpacing(20)

Gender_layout = QHBoxLayout()
Gender_label = QLabel('Gender')
Gender_layout.addWidget(Gender_label)
Gender_input = QLineEdit()
Gender_input.setFixedSize(300, 20)
Gender_layout.addWidget(Gender_input)
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

window.setLayout(main_layout)

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())
