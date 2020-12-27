import os
import sqlite3
from sqlite3 import Error
import random
import config as cf

role = [
    "Quality Assurance Specialist",
    "Tester",
    "Software Engineer",
    "Software Developer",
    "Quality Analyst",
    "Business Analyst",
    "Business Associate",
    "Junior Assitant",
    "Senior Assistant",
    "Data Scientist"
]

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def dummy_db(type_job, location="Pune"):
    n = random.randint(0, 9)
    template = "Hi, Cognologix is looking for "+role[n]+". This role requires you to be proficient in software as well as testing side." \
                                                        " If you would like to apply please say apply for the job."
    return template


"""
if __name__ == '__main__':
    create_connection(os.path.join(cf.db_path, "information.db"))
"""

