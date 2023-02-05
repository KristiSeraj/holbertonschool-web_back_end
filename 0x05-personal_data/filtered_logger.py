#!/usr/bin/env python3
"""Regex-ing module"""
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "password", "ssn")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter datum that returns the log message obfuscated"""
    for el in fields:
        message = re.sub(fr'{el}=.*?{separator}',
                         f'{el}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Returns info logging"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to a secure database"""
    userName = os.getenv('PERSONAL_DATA_DB_USERNAME')
    localHost = os.getenv('PERSONAL_DATA_DB_HOST')
    if userName is None or localHost is None:
        os.environ['PERSONAL_DATA_DB_USERNAME'] = "root"
        os.environ['PERSONAL_DATA_DB_HOST'] = "localhost"
    db = mysql.connector.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )

    return db


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor function"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def main():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')
    for row in cursor:
        msg = f"name={row[0]}; email={row[1]}; " +\
                f"phone={row[2]}; ssn={row[3]}; " +\
                f"password={row[4]}; ip={row[5]}; " +\
                f"last_login={row[6]}; user_agent={row[7]}; "
        log_record = logging.LogRecord("user_data", logging.INFO, None,
                                       None, msg, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(log_record))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
