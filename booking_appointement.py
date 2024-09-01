import random
import string
import psycopg2

def generate_random_id():
    #prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    
    return f"APT{digits}"
def booking_appointed(Scheduled_date,Doctor_ID,Additional_comments,Patient_ID):
    
    Appointment_data = {
        "Scheduled_date": Scheduled_date,
        "Doctor_ID": Doctor_ID,
        "Additional_comments": Additional_comments,
        "Patient_ID": Patient_ID,
        "Appointment_ID": generate_random_id(),
        
    }
    return Appointment_data
 
def load_redshift_config(filepath='redshift_config.txt'):
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config
 
def insert_data_into_redshift(Scheduled_date,Doctor_ID,Additional_comments,Patient_ID):
    Appointment_data = booking_appointed(Scheduled_date,Doctor_ID,Additional_comments,Patient_ID)
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
        INSERT INTO user_data.NEW_APPOINTMENT
        (Scheduled_date, Doctor_ID, diagnosis,Patient_ID,Appt_ID,APPOINTMENT_CHARGES)
        VALUES (%s, %s, %s, %s, %s,300)
        """
        cursor.execute(insert_query, (
            Appointment_data["Scheduled_date"],
            Appointment_data["Doctor_ID"],
            Appointment_data["Additional_comments"],
            Appointment_data["Patient_ID"],
            Appointment_data["Appointment_ID"]
        ))
        
        # Commit the transaction
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting data into Redshift: {e}")
        return False
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()
            
            
def past_appointments(Patient_ID):
    config = load_redshift_config()
    
    try:
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            database=config['dbname'],
            user=config['user'],
            password=config['password']
        )
 
        cursor = conn.cursor()
        cursor.execute("select * from user_data.NEW_APPOINTMENT where Patient_ID = %s",(Patient_ID,))
    
        result: tuple = cursor.fetchall()   
        print(result)
        conn.commit()
        return result
    
    except Exception as e:
        print(f"Error running query Redshift: {e}")
    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()

######################################--MEDICAL---HISTORY##########################################################
def generate_record_ID():
    #prefix = .join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"RE{digits}"

def medical_history(Patient_ID,Allergies,Pre_conditions):
    Record_ID = generate_record_ID()
    Patient_ID = Patient_ID
    Allergies = Allergies
    Pre_conditions = Pre_conditions

    config = load_redshift_config()
    
    try:
        conn = psycopg2.connect(
        host = config['host'],
        port = config['port'],
        dbname = config['dbname'],
        user = config['user'],
        password = config['password']
        )
        cursor = conn.cursor()
        
        print(Record_ID,Patient_ID,Allergies,Pre_conditions)
        insert_medical_history= """
        INSERT INTO user_data.MEDICAL_HISTORY
        (RECORD_ID,PATIENT_ID,Allergies,Pre_conditions)
        VALUES(%s,%s,%s,%s)
        """
        #cursor.execute(insert_medical_history(Record_ID,Patient_ID,Allergies,Pre_conditions)
        cursor.execute(insert_medical_history,(Record_ID, Patient_ID, Allergies, Pre_conditions))
   
        conn.commit()
        
    except Exception as e:
        print(f"Error inserting data into redshift.{e}")
        
    finally:
        if conn:
            cursor.close()
            conn.close()
    
    
################################LAB-- TEST ###############################

# Test_ID,TEST_NAME,PATIENT_ID,DOCTOR_ID,DATE,TEST_COST

def generate_Test_ID():

    digits = ''.join(random.choices(string.digits, k=6))
    return f"TE{digits}"



def test_name(TEST_NAME):
    query = "SELECT TESTCOST FROM user_data.LABTestReference WHERE TestName = %s"
    config = load_redshift_config()
    try:
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        )
        cursor = conn.cursor()
        # Using parameterized query to prevent SQL injection
        cursor.execute(query, (TEST_NAME,))
        result = cursor.fetchone()
        if result:
            print(result[0])  # Print the cost
            return result[0]  # Return only the TESTCOST value
        
    except Exception as e:
        print(f"Error fetching data from Redshift: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    
    return None  # Return None explicitly if no result found
 
def Lab_test(TEST_NAME,PATIENT_ID,DOCTOR_ID,DATE):
    
    TEST_ID = generate_Test_ID()
    print(TEST_ID)
    TEST_NAME = TEST_NAME
    print(TEST_NAME)
    PATIENT_ID= PATIENT_ID
    print(PATIENT_ID)
    DOCTOR_ID = DOCTOR_ID
    print(DOCTOR_ID)
    DATE = DATE
    print(DATE)
    TEST_COST = test_name(TEST_NAME)
    print(TEST_COST)
    config =  load_redshift_config()
    try:
        conn = psycopg2.connect(
          host = config['host'], 
          port = config['port'], 
          dbname = config['dbname'],
          user = config['user'],
          password = config['password']
        )
        cursor = conn.cursor()
        insert_lab_test = """
        INSERT INTO user_data.Lab_test(TEST_ID,TEST_NAME,PATIENT_ID,DOCTOR_ID,test_DATE,TEST_COST)
        VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert_lab_test,(TEST_ID,TEST_NAME,PATIENT_ID,DOCTOR_ID,DATE,TEST_COST))
        
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting data into redshift:{e}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
    
#Lab_test("laboraratory","C1107","D1107","22 August 2024")

###############- LAB- TEST --- DATA LOAD DONE------#############################


################ - PRESCRIPTION----#########################################

def generate_prescription_ID():
    digits =''.join(random.choices(string.digits, k=6))
    return f"PE{digits}"
def prescription(Patient_ID,Doctor_ID,Medicine_ID,Dosage,Date):
    Prescription_ID = generate_prescription_ID()
    Patient_ID = Patient_ID
    Doctor_ID = Doctor_ID
    Medicine_ID = Medicine_ID
    Dosage = Dosage
    Date= Date

    config = load_redshift_config()
    try:
        conn = psycopg2.connect(
            host = config['host'],
            port = config['port'],
            dbname = config['dbname'],
            user = config['user'],
            password = config['password']
        )
        cursor = conn.cursor()
        insert_prescription_details = """
        INSERT INTO user_data.Prescription( Prescription_ID,Patient_ID,Doctor_ID,Medicine_ID,Dosage,prescription_Date)
        VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert_prescription_details,(Prescription_ID,Patient_ID,Doctor_ID,Medicine_ID,Dosage,Date))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error loading data in redshift:{e}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
    
#########PRESCRIPTION LOADED SUCCESSFULLY ##############################

################--BILL-GENERATED--###########################

def generate_bill_ID():
    digits = ''.join(random.choices(string.digits,k=6))
    return f"BI{digits}"

    
def Bill_generated(Patient_ID):
    Bill_ID = generate_bill_ID()
    Patient_ID = Patient_ID
    DATE= DATE
    APPOINTMENT_CHARGES = APPOINTMENT_CHARGES
    TEST_COST = TEST_COST
    M_COST = M_COST
    TOTAL_COST = APPOINTMENT_CHARGES+TEST_COST+M_COST

    config = load_redshift_config()
    try:
        conn= psycopg2.connect(
            host = config['host'],
            port = config['port'],
            dbname = config['dbname'],
            user = config['user'],
            password = config['password']
        )
        cursor = conn.cursor()
        insert_bill_information = """
        INSERT INTO user_data.Bill_Generated(Bill_ID,Patient_ID,DATE,APPOINTMENT_CHARGES,TEST_COST,M_COST,TOTAL_COST)
        VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        
        cursor.execute(insert_bill_information(Bill_ID,Patient_ID,DATE,APPOINTMENT_CHARGES,TEST_COST,M_COST,TOTAL_COST))
        conn.commit()
    except Exception as e:
        print(f"Error loading data in redshit:{e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            

###############################The function for getting Doctor id from redshift table###############        
            
def doctor_id_list_get():
    # Example function to get the list of Doctor IDs
    return ['D001', 'D002', 'D003', 'D004']


def medicine_id_list_get():
    return ['DOLO','ZOLO']

def patient_id_list_get():
    return ['PT323028','SL53636']