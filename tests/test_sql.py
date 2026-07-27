import unittest
import os
import sqlite3
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestSQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.sql_folder = os.path.join(PROJECT_ROOT, "sql")
        cls.database = os.path.join(PROJECT_ROOT, "data", "atmosync.db")

    # --------------------------------------------------
    # SQL Folder Exists
    # --------------------------------------------------

    def test_sql_folder_exists(self):
        self.assertTrue(os.path.exists(self.sql_folder))

    # --------------------------------------------------
    # SQL Files Exist
    # --------------------------------------------------

    def test_sql_files_exist(self):

        required = [
            "01_create_database.sql",
            "02_create_tables.sql",
            "03_insert_sample_data.sql",
            "04_data_validation.sql",
            "05_views.sql",
            "06_joins.sql",
            "07_kpi_queries.sql",
            "08_materialized_views.sql"
        ]

        for file in required:
            path = os.path.join(self.sql_folder, file)
            self.assertTrue(
                os.path.exists(path),
                f"{file} not found"
            )

    # --------------------------------------------------
    # SQL Files Are Not Empty
    # --------------------------------------------------

    def test_sql_files_not_empty(self):

        for file in os.listdir(self.sql_folder):

            if file.endswith(".sql"):

                path = os.path.join(self.sql_folder, file)

                with open(path, "r", encoding="utf-8") as f:

                    content = f.read().strip()

                self.assertGreater(
                    len(content),
                    0,
                    f"{file} is empty"
                )

    # --------------------------------------------------
    # SQLite Database Opens
    # --------------------------------------------------

    def test_database_connection(self):

        if not os.path.exists(self.database):
            self.skipTest("SQLite database not created yet.")

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("SELECT sqlite_version();")

        version = cursor.fetchone()

        self.assertIsNotNone(version)

        conn.close()


if __name__ == "__main__":

    print("=" * 60)
    print("Running SQL Tests")
    print("=" * 60)

    unittest.main(verbosity=2)