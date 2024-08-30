import random
import string
import psycopg2

def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    
    return f"{prefix}{digits}"
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
        (Scheduled_date, Doctor_ID, Additional_comments,Patient_ID,Appointment_ID)
        VALUES (%s, %s, %s, %s, %s)
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
 
    except Exception as e:
        print(f"Error inserting data into Redshift: {e}")
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
