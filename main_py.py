import psycopg2


def load_redshift_config(filepath='redshift_config.txt'):
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config



def insert_data_into_redshift(patient_data):
    config = load_redshift_config()

    try:
        # Establish a connection to the Redshift database
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        )
        cursor = conn.cursor()
        
        # SQL query to insert data
        insert_query = """
        INSERT INTO user_data.NEW_USER
        (Patient_ID, Patient_FName, Patient_LName, Phone, Blood_Type, Email, Gender, Password, Admission_Date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            patient_data["Patient_ID"],
            patient_data["Patient_FName"],
            patient_data["Patient_LName"],
            patient_data["Phone"],
            patient_data["Blood_Type"],
            patient_data["Email"],
            patient_data["Gender"],
            patient_data["Password"],
            patient_data["Admission_Date"]
        ))

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(f"Error inserting data into Redshift: {e}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()



    # Insert data into Redshift
    #insert_data_into_redshift(patient_data)

def verify_login(patient_id, password):
    config = load_redshift_config()

    try:
        # Establish a connection to the Redshift database
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        )
        cursor = conn.cursor()

        # SQL query to verify login
        select_query = """
        SELECT Patient_ID, Password FROM user_data.NEW_USER 
        WHERE Patient_ID = %s AND Password = %s
        """
        cursor.execute(select_query, (patient_id, password))
        result = cursor.fetchone()

        if result:
            print("Login Successful!")
        else:
            print("Login Failed: Invalid Patient ID or Password.")

    except Exception as e:
        print(f"Error verifying login: {e}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()
    















'''
def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def collect_data():
    if male_button.isChecked():
        gender = "Male"
    elif female_button.isChecked():
        gender = "Female"
    elif others_button.isChecked():
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




if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())'''








'''
import sys
import random
import string
from datetime import datetime
import psycopg2
from PyQt5.QtWidgets import QApplication
from ui import (app, window, fname_input, lname_input, phone_input, blood_type_input, 
                email_input, gender_input, password_input, submit_button)

def load_redshift_config(filepath='redshift_config.txt'):
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def push_to_redshift(patient_data):
    config = load_redshift_config()

    try:
        # Establish a connection to the Redshift database
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        )
        cur = conn.cursor()
        
        # Insert data into the Redshift table
        insert_query = 
        #INSERT INTO Patient (Patient_ID, Patient_FName, Patient_LName, Phone, Blood_Type, 
         #                    Email, Gender, Condition, Admission_Date, Discharge_Date)
        #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL);
        
        cur.execute(insert_query, (
            patient_data['Patient_ID'],
            patient_data['Patient_FName'],
            patient_data['Patient_LName'],
            patient_data['Phone'],
            patient_data['Blood_Type'],
            patient_data['Email'],
            patient_data['Gender'],
            patient_data['Password'],  # Assuming Condition is mapped to Password (Adjust accordingly)
            patient_data['Admission_Date'],
        ))

        # Commit the transaction
        conn.commit()

        # Close the connection
        cur.close()
        conn.close()

        print("Data pushed to Redshift successfully")

    except Exception as e:
        print(f"Error pushing data to Redshift: {e}")

def collect_data():
    patient_data = {
        "Patient_ID": generate_random_id(),
        "Patient_FName": fname_input.text(),
        "Patient_LName": lname_input.text(),
        "Phone": phone_input.text(),
        "Blood_Type": blood_type_input.text(),
        "Email": email_input.text(),
        "Gender": gender_input.text(),
        "Password": password_input.text(),
        "Admission_Date": generate_current_date(),
    }
    
    # Push the collected data to Redshift
    push_to_redshift(patient_data)

#submit_button.clicked.connect(collect_data)

if __name__ == "__main__":
    sys.exit(app.exec_())'''
