import pandas as pd
from database.snowflake_db import get_connection

def load_sensor_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM SENSOR_DATA")

    rows = cursor.fetchall()

    columns = [col[0].lower() for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    cursor.close()

    conn.close()

    return df