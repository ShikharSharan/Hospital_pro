from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QDateEdit
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from booking_appointement import prescription, doctor_id_list_get, medicine_id_list_get, patient_id_list_get  # Assuming these functions are available

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('ADMIN PAGE')
window.setGeometry(100, 100, 1800, 900)
main_layout = QHBoxLayout()

login_layout = QVBoxLayout()
login_layout.addStretch()

label = QLabel('BILLING')
label.setAlignment(Qt.AlignCenter)
login_layout.addWidget(label)

# Dropdown for Patient ID
username_layout = QHBoxLayout()
username_label = QLabel('Patient_ID:')
username_layout.addWidget(username_label)

patient_id_combo = QComboBox()
patient_id_combo.addItem('Select Patient ID')
patient_id_combo.addItems(patient_id_list_get())  # Populating the dropdown with patient IDs
username_layout.addWidget(patient_id_combo)

login_layout.addLayout(username_layout)
login_layout.addSpacing(40)

button_layout = QHBoxLayout()
login_button = QPushButton("Login")
button_layout.addWidget(login_button)

login_layout.addLayout(button_layout)
login_layout.addStretch()

prescription_layout = QVBoxLayout()
prescription_layout.addStretch()

label2 = QLabel("Prescription")
label2.setAlignment(Qt.AlignCenter)
prescription_layout.addWidget(label2)

# Patient ID Dropdown
Patient_fname_layout = QHBoxLayout()
patient_id_label = QLabel('Patient_ID')
Patient_fname_layout.addWidget(patient_id_label)
Patient_id_combo = QComboBox()
Patient_id_combo.addItem('Select Patient ID')
Patient_id_combo.addItems(patient_id_list_get())  # Populating the dropdown with patient IDs
Patient_fname_layout.addWidget(Patient_id_combo)
prescription_layout.addLayout(Patient_fname_layout)
prescription_layout.addSpacing(20)

# Medicine ID Dropdown
medicine_layout = QHBoxLayout()
medicine_id_label = QLabel('MedicineID:')
medicine_layout.addWidget(medicine_id_label)
medicine_id_combo = QComboBox()
medicine_id_combo.addItem('Select Medicine ID')
medicine_id_combo.addItems(medicine_id_list_get())  # Populating the dropdown with medicine IDs
medicine_layout.addWidget(medicine_id_combo)
prescription_layout.addLayout(medicine_layout)
prescription_layout.addSpacing(20)

# Date Input
Date_layout = QHBoxLayout()
Date_label = QLabel('Date')
Date_layout.addWidget(Date_label)

Date_input = QDateEdit()
Date_input.setDisplayFormat("yyyy-MM-dd")
Date_input.setFixedSize(190, 20)
Date_input.setCalendarPopup(True)
Date_input.setDate(QDate.currentDate())

Date_layout.addWidget(Date_input)
prescription_layout.addLayout(Date_layout)
prescription_layout.addSpacing(20)

# Dosage Input
dosage_layout = QHBoxLayout()
dosage_label = QLabel('Dosage')
dosage_layout.addWidget(dosage_label)
dosage_input = QLineEdit()
dosage_input.setFixedSize(200-10, 20)
dosage_layout.addWidget(dosage_input)

prescription_layout.addLayout(dosage_layout)
prescription_layout.addSpacing(20)

# Doctor ID Dropdown
doctorid_layout = QHBoxLayout()
doctor_id_label = QLabel('Doctor ID:')
doctorid_layout.addWidget(doctor_id_label)
doctor_id_combo = QComboBox()
doctor_id_combo.addItem('Select Doctor ID')
doctor_id_combo.addItems(doctor_id_list_get())  # Populating the dropdown with doctor IDs
doctorid_layout.addWidget(doctor_id_combo)
prescription_layout.addLayout(doctorid_layout)
prescription_layout.addSpacing(20)

# Blank QLabel for displaying success or failure message
result_label = QLabel('')
result_label.setAlignment(Qt.AlignCenter)
prescription_layout.addWidget(result_label)
prescription_layout.addSpacing(20)

# Create Button
create_button_layout = QHBoxLayout()
create_button = QPushButton("Create")
create_button_layout.addWidget(create_button)
prescription_layout.addLayout(create_button_layout)
prescription_layout.addStretch()

main_layout.addStretch()
main_layout.addLayout(login_layout)
main_layout.addStretch()
main_layout.addLayout(prescription_layout)
main_layout.addStretch()

# Connect the create button to the function
def on_create_button_clicked():
    result = prescription(
        Patient_id_combo.currentText(),
        doctor_id_combo.currentText(),
        medicine_id_combo.currentText(),
        dosage_input.text(),
        Date_input.text()
    )
    if result:  # Assuming the function returns True for success
        result_label.setText("Prescription added successfully.")
    else:
        result_label.setText("Failed to add prescription.")

create_button.clicked.connect(on_create_button_clicked)

window.setLayout(main_layout)

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())
