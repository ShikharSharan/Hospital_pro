from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QDateEdit, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from booking_appointement import *

# Global variable to hold the appointment window
appointment_window = None
past_appointments_window = None

def create_after_login_page(patient_id):
    # Create the main widget
    window = QWidget()

    # Main layout as QVBoxLayout
    main_layout = QHBoxLayout()

    # Top HBoxLayout for the welcome message
    welcome_layout = QHBoxLayout()
    welcome_label = QLabel(f"Welcome!--{patient_id}")  # Replace [User] with dynamic username if needed
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_layout.addWidget(welcome_label)

    # HBoxLayout for "Book Appointment"
    book_appointment_layout = QHBoxLayout()
    book_appointment_button = QPushButton("Book Appointment")
    book_appointment_button.clicked.connect(lambda: open_book_appointment_ui(patient_id))
    book_appointment_layout.addWidget(book_appointment_button)

    # HBoxLayout for "Know My Past Appointments"
    past_appointment_layout = QVBoxLayout()
    past_appointment_button = QPushButton("Know My Past Appointments")
    past_appointment_button.clicked.connect(lambda: open_past_appointments_ui(patient_id))
    past_appointment_layout.addWidget(past_appointment_button)
    
    add_medical_history  = QVBoxLayout()
    add_medical_button = QPushButton("Add Medical History")
    #add_medical_button.clicked.connect()
    add_medical_history.addWidget(add_medical_button)

    # Adding HBoxLayouts to the main VBoxLayout
    main_layout.addLayout(welcome_layout)
    main_layout.addStretch()
    main_layout.addLayout(book_appointment_layout)
    main_layout.addStretch()
    main_layout.addLayout(past_appointment_layout)
    main_layout.addLayout(add_medical_history)

    # Set the main layout
    window.setLayout(main_layout)
    window.setGeometry(100, 100, 1800, 900)
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
    date_layout.addWidget(date_label)
    date_layout.addWidget(date_input)
    date_layout.addStretch(1)  # Add stretch to push elements to the left
    
    # Doctor ID input
    doctor_id_layout = QHBoxLayout()
    doctor_id_label = QLabel("Doctor ID:")
    doctor_id_label.setFixedSize(120, 30)
    doctor_id_input = QLineEdit()
    doctor_id_input.setFixedSize(200, 30)
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
    
    # Submit button
    submit_button = QPushButton("Submit")
    submit_button.setFixedSize(120, 40)
    
    submit_button.clicked.connect(lambda: insert_data_into_redshift(date_input.text(), doctor_id_input.text(), comment_input.toPlainText(), patient_id))  # Connect to submission functionality
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
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(["Scheduled Date", "Doctor ID", "Comments", "Patient Id", "Appointement Id"])
    
    # Populate the table with data
    for row, appointment in enumerate(appointments):
        # Extract values from each tuple
        scheduled_date, doctor_id, patient_id, appointment_id, comments = appointment

        # Add data to the table
        table.setItem(row, 0, QTableWidgetItem(scheduled_date.strftime("%Y-%m-%d")))  # Format date
        table.setItem(row, 1, QTableWidgetItem(doctor_id))
        table.setItem(row, 2, QTableWidgetItem(patient_id))
        table.setItem(row, 3, QTableWidgetItem(appointment_id))
        table.setItem(row, 4, QTableWidgetItem(comments))
    
    # Add the table to the layout
    layout.addWidget(table)
    
    # Set the layout and show the window
    past_appointments_window.setLayout(layout)
    past_appointments_window.setGeometry(100, 100, 800, 400)
    past_appointments_window.show()
