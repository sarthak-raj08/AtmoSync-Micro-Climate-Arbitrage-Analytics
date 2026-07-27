import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()


def get_connection():

    conn = snowflake.connector.connect(

        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")

    )

    return conn


if __name__ == "__main__":

    try:

        conn = get_connection()

        print("✅ Connected Successfully!")

        conn.close()

    except Exception as e:

        print("❌ Connection Failed")
        print(e)