from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QDateEdit, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QComboBox,QDateTimeEdit,QCompleter
from PyQt5.QtCore import Qt
from booking_appointement import *
from PyQt5.QtCore import QDate
from datetime import datetime


# Global variable to hold the appointment window
appointment_window = None
past_appointments_window = None
lab_test_window = None
medical_history_window = None

def create_after_login_page(patient_id):
    # Create the main widget
    window = QWidget()

    # Main layout as QVBoxLayout
    main_layout = QVBoxLayout()

    # Top HBoxLayout for the welcome message
    welcome_layout = QHBoxLayout()
    welcome_label = QLabel(f"Welcome!--{patient_id}")  # Replace [User] with dynamic username if needed
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_layout.addWidget(welcome_label)

    # Vertical layout for buttons
    button_layout = QVBoxLayout()

    # "Book Appointment" Button
    book_appointment_button = QPushButton("Book Appointment")
    book_appointment_button.clicked.connect(lambda: open_book_appointment_ui(patient_id))
    button_layout.addWidget(book_appointment_button)

    # "Know My Past Appointments" Button
    past_appointment_button = QPushButton("Know My Past Appointments")
    past_appointment_button.clicked.connect(lambda: open_past_appointments_ui(patient_id))
    button_layout.addWidget(past_appointment_button)

    # "Add Medical History" Button
    add_medical_button = QPushButton("Add Medical History")
    add_medical_button.clicked.connect(lambda: add_medical_history_funct(patient_id))
    button_layout.addWidget(add_medical_button)

    # "Book LAB Test" Button
    lab_book_button = QPushButton("Book LAB Test")
    lab_book_button.clicked.connect(lambda: book_lab_test(patient_id))
    button_layout.addWidget(lab_book_button)

    # Adding layouts to the main layout
    main_layout.addLayout(welcome_layout)
    main_layout.addStretch()
    main_layout.addLayout(button_layout)
    main_layout.addStretch()

    # Set the main layout
    window.setLayout(main_layout)
    window.setGeometry(100, 100, 1800, 900)  # Adjust size to your preference
    window.setWindowTitle("User Dashboard")

    return window


def open_book_appointment_ui(patient_id):
    print(f"Booking appointment for Patient ID: {patient_id}")
    global appointment_window  # Declare it as a global variable

    # Create the main widget for booking an appointment
    appointment_window = QWidget()
    appointment_window.setWindowTitle("Book Appointment")
    
    # Main layout for the booking form
    appointment_layout = QVBoxLayout()
    
    # Scheduled Date input
    date_layout = QHBoxLayout()
    date_label = QLabel("Scheduled Date:")
    date_label.setFixedSize(120, 30)
    date_input = QDateEdit()
    date_input.setCalendarPopup(True)
    date_input.setFixedSize(200, 30)
    
    # Set default date to the present date
    date_input.setDate(QDate.currentDate())
    
    date_layout.addWidget(date_label)
    date_layout.addWidget(date_input)
    date_layout.addStretch(1)  # Add stretch to push elements to the left
    
    # Doctor ID dropdown with search functionality
    doctor_id_layout = QHBoxLayout()
    doctor_id_label = QLabel("Doctor ID:")
    doctor_id_label.setFixedSize(120, 30)
    
    # Create the ComboBox
    doctor_id_input = QComboBox()
    doctor_id_input.setFixedSize(200, 30)
    
    # Add "Select" as the default, unselectable item
    doctor_id_input.addItem("Select")
    doctor_id_input.model().item(0).setEnabled(False)  # Disable the "Select" option

    # Populate the ComboBox with Doctor IDs
    doctor_ids = doctor_id_list_get()
    doctor_id_input.addItems(doctor_ids)
    
    # Add search functionality
    completer = QCompleter(doctor_ids)
    doctor_id_input.setCompleter(completer)
    
    doctor_id_layout.addWidget(doctor_id_label)
    doctor_id_layout.addWidget(doctor_id_input)
    doctor_id_layout.addStretch(1)  # Add stretch to push elements to the left
    
    # Comment input
    comment_layout = QHBoxLayout()
    comment_label = QLabel("Comment:")
    comment_label.setFixedSize(120, 30)
    comment_input = QTextEdit()
    comment_input.setFixedSize(400, 100)
    comment_layout.addWidget(comment_label)
    comment_layout.addWidget(comment_input)
    comment_layout.addStretch(1)  # Add stretch to push elements to the left
    
    # Add all layouts to the main layout
    appointment_layout.addLayout(date_layout)
    appointment_layout.addSpacing(20)
    appointment_layout.addLayout(doctor_id_layout)
    appointment_layout.addSpacing(20)
    appointment_layout.addLayout(comment_layout)
    
    # Status message label
    status_message = QLabel("")
    status_message.setFixedSize(400, 30)
    appointment_layout.addWidget(status_message, alignment=Qt.AlignCenter)
    
    # Submit button
    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(120, 40)

    # Function to handle submission
    def handle_submission():
        date = date_input.date().toString("yyyy-MM-dd")  # Get the selected date
        doctor_id = doctor_id_input.currentText()        # Get the selected Doctor ID
        comment = comment_input.toPlainText()            # Get the comment
        
        # Ensure the user has selected a doctor ID other than "Select"
        if doctor_id == "Select":
            status_message.setText("Please select a valid Doctor ID.")
            return
        
        success = insert_data_into_redshift(date, doctor_id, comment, patient_id)  # Insert data into Redshift
        
        # Update status message based on insertion result
        if success:
            status_message.setText("Booked Successfully")
        else:
            status_message.setText("Booking Failed")

    # Connect button click to submission handler
    submit_button.clicked.connect(handle_submission)
    
    appointment_layout.addWidget(submit_button, alignment=Qt.AlignCenter)  # Center the button
    
    appointment_window.setLayout(appointment_layout)
    appointment_window.setGeometry(100, 100, 600, 400)
    appointment_window.show()

def open_past_appointments_ui(patient_id):
    print(f"Fetching past appointments for Patient ID: {patient_id}")
    global past_appointments_window  # Declare it as a global variable

    # Create the main widget for displaying past appointments
    past_appointments_window = QWidget()
    past_appointments_window.setWindowTitle("Past Appointments")
    
    # Main layout for the table of past appointments
    layout = QVBoxLayout()
    
    # Fetch appointment data
    appointments = past_appointments(patient_id)  # Call your function to get past appointments
    print(appointments)
    # Create a table to show the data
    table = QTableWidget()
    table.setRowCount(len(appointments))
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels(["Scheduled Date", "Doctor ID", "Ptient ID", "Appointement ID","Comments" ,"Charges"])
    
    # Populate the table with data
    for row, appointment in enumerate(appointments):
        # Extract values from each tuple
        appointment_id,scheduled_date, doctor_id,patient_id , comments,charges = appointment
        print("shssbdjs",charges)
        # Add data to the table
        table.setItem(row, 0, QTableWidgetItem(scheduled_date.strftime("%Y-%m-%d")))  # Format date
        table.setItem(row, 1, QTableWidgetItem(doctor_id))
        table.setItem(row, 2, QTableWidgetItem(patient_id))
        table.setItem(row, 3, QTableWidgetItem(appointment_id))
        table.setItem(row, 4, QTableWidgetItem(comments))
        table.setItem(row, 5, QTableWidgetItem(str(charges)))
    
    # Add the table to the layout
    layout.addWidget(table)
    
    # Set the layout and show the window
    past_appointments_window.setLayout(layout)
    past_appointments_window.setGeometry(100, 100, 800, 400)
    past_appointments_window.show()
    
    
    
def add_medical_history_funct(patient_id):
    print(f"Adding Medical History for Patient ID: {patient_id}")
    global medical_history_window  # Declare it as a global variable

    # Create the main widget for medical history
    medical_history_window = QWidget()
    medical_history_window.setWindowTitle("Add Medical History")
    
    # Main layout for the medical history form
    medical_history_layout = QVBoxLayout()
    
    # Allergies input
    allergy_layout = QHBoxLayout()
    allergy_label = QLabel("Allergies:")
    allergy_input = QLineEdit()
    allergy_input.setFixedSize(200, 30)
    allergy_layout.addWidget(allergy_label)
    allergy_layout.addWidget(allergy_input)
    
    # Precondition input
    precondition_layout = QHBoxLayout()
    precondition_label = QLabel("Precondition:")
    precondition_label.setFixedSize(120, 30)
    precondition_input = QLineEdit()
    precondition_input.setFixedSize(200, 30)
    precondition_layout.addWidget(precondition_label)
    precondition_layout.addWidget(precondition_input)
    
    # Add all layouts to the main layout
    medical_history_layout.addLayout(allergy_layout)
    medical_history_layout.addSpacing(20)
    medical_history_layout.addLayout(precondition_layout)
    
    # Submit button
    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(120, 40)
    submit_button.clicked.connect(lambda: medical_history(patient_id, allergy_input.text(), precondition_input.text()))  # Connect to submission functionality
    medical_history_layout.addWidget(submit_button, alignment=Qt.AlignCenter)  # Center the button
    
    medical_history_window.setLayout(medical_history_layout)
    medical_history_window.setGeometry(100, 100, 600, 400)
    medical_history_window.show()

    
    
def book_lab_test(patient_id):
    print(f"Booking Lab Test for: {patient_id}")
    global lab_test_window  # Declare it as a global variable

    # Create the main widget for booking a lab test
    lab_test_window = QWidget()
    lab_test_window.setWindowTitle("Book LAB Test")

    # Main layout for the booking form
    book_lab_test_layout = QVBoxLayout()

    # Feedback message label
    feedback_label = QLabel("")
    feedback_label.setFixedSize(400, 30)
    feedback_label.setAlignment(Qt.AlignCenter)  # Center the text

    # Test Name input using QComboBox
    test_name_layout = QHBoxLayout()
    test_name_label = QLabel("Test Name:")
    test_name_label.setFixedSize(120, 30)
    test_name_dropdown = QComboBox()
    test_name_dropdown.setFixedSize(200, 30)
    test_name_dropdown.addItem("Select")
    test_name_dropdown.model().item(0).setEnabled(False)  # Make "Select" unselectable
    test_name_dropdown.addItems(["Lipid Profile", "X-Ray", "MRI", "CT Scan"])  # Add more test options as needed
    test_name_layout.addWidget(test_name_label)
    test_name_layout.addWidget(test_name_dropdown)

    # Doctor ID input using QComboBox with search functionality
    doctor_id_layout = QHBoxLayout()
    doctor_id_label = QLabel("Doctor ID:")
    doctor_id_label.setFixedSize(120, 30)
    doctor_id_dropdown = QComboBox()
    doctor_id_dropdown.setFixedSize(200, 30)

    # Add "Select" as the default, unselectable item
    doctor_id_dropdown.addItem("Select")
    doctor_id_dropdown.model().item(0).setEnabled(False)  # Disable the "Select" option

    # Populate the ComboBox with Doctor IDs
    doctor_ids = doctor_id_list_get()  # Assuming this function returns a list of doctor IDs
    doctor_id_dropdown.addItems(doctor_ids)

    # Add search functionality to Doctor ID dropdown
    doctor_id_search_edit = QLineEdit()
    completer = QCompleter(doctor_ids)
    completer.setCaseSensitivity(Qt.CaseInsensitive)  # Make the search case insensitive
    doctor_id_search_edit.setCompleter(completer)
    doctor_id_dropdown.setEditable(True)
    doctor_id_dropdown.setLineEdit(doctor_id_search_edit)
    
    doctor_id_layout.addWidget(doctor_id_label)
    doctor_id_layout.addWidget(doctor_id_dropdown)

    # Date selection input using QDateEdit
    date_layout = QHBoxLayout()
    date_label = QLabel("Select Date:")
    date_label.setFixedSize(120, 30)
    date_input = QDateEdit()
    date_input.setFixedSize(200, 30)
    date_input.setCalendarPopup(True)  # Enables the calendar popup
    date_input.setDate(QDate.currentDate())  # Set current date as default
    date_layout.addWidget(date_label)
    date_layout.addWidget(date_input)

    # Add all layouts to the main layout
    book_lab_test_layout.addSpacing(40)
    book_lab_test_layout.addLayout(test_name_layout)
    book_lab_test_layout.addSpacing(20)
    book_lab_test_layout.addLayout(doctor_id_layout)
    book_lab_test_layout.addSpacing(20)
    book_lab_test_layout.addLayout(date_layout)
    book_lab_test_layout.addSpacing(20)
    book_lab_test_layout.addWidget(feedback_label)

    # Submit button
    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(120, 40)

    # Function to handle submission
    def handle_submission():
        test_name = test_name_dropdown.currentText()
        doctor_id = doctor_id_dropdown.currentText()
        test_date = date_input.date().toString("yyyy-MM-dd")

        # Ensure the user has selected valid options
        if test_name == "Select" or doctor_id == "Select":
            feedback_label.setText("Please select valid Test Name and Doctor ID.")
            return

        # Handle lab test booking
        success = Lab_test(test_name, patient_id, doctor_id, test_date)

        if success:
            feedback_label.setText("Lab Test Booked Successfully")
        else:
            feedback_label.setText("Booking Failed")

    # Connect button click to submission handler
    submit_button.clicked.connect(handle_submission)
    book_lab_test_layout.addWidget(submit_button, alignment=Qt.AlignCenter)  # Center the button
    book_lab_test_layout.addSpacing(30)

    lab_test_window.setLayout(book_lab_test_layout)
    lab_test_window.setGeometry(100, 100, 600, 400)
    lab_test_window.show()


    
    

