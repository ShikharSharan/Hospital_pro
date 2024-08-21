
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
        INSERT INTO patient_records 
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
