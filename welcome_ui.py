from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt

def create_after_login_page():
    # Create the main widget
    window = QWidget()

    # Main layout as QVBoxLayout
    main_layout = QVBoxLayout()

    # Top HBoxLayout for the welcome message
    welcome_layout = QHBoxLayout()
    welcome_label = QLabel("Welcome!")  # Replace [User] with dynamic username if needed
    welcome_label.setAlignment(Qt.AlignCenter)
    welcome_layout.addWidget(welcome_label)

    # HBoxLayout for "Book Appointment"
    book_appointment_layout = QHBoxLayout()
    book_appointment_button = QPushButton("Book Appointment")
    book_appointment_layout.addWidget(book_appointment_button)

    # HBoxLayout for "Know My Past Appointments"
    past_appointment_layout = QHBoxLayout()
    past_appointment_button = QPushButton("Know My Past Appointments")
    book_appointment_layout.addWidget(past_appointment_button)

    # Adding HBoxLayouts to the main VBoxLayout
    main_layout.addLayout(welcome_layout)
    main_layout.addStretch()
    main_layout.addLayout(book_appointment_layout)
    main_layout.addStretch()
    main_layout.addLayout(past_appointment_layout)

    # Set the main layout
    window.setLayout(main_layout)
    window.setWindowTitle("User Dashboard")

    return window

def welcome_ui():
    app = QApplication([])
    window = create_after_login_page()
    window.setGeometry(100, 100, 1800, 900)
    window.show()
    app.exec_()

welcome_ui() 
