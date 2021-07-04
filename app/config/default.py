import os


DEBUG = True

SECRET_KEY = os.getenv("APP_SECRET_KEY")

MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_PORT = 3306
MYSQL_DB = os.getenv("MYSQL_DB")

LOGGING_LEVEL = "DEBUG"
LOGGIN_FILE = "activity.log"
LOGGING_BACKUPS = 2
LOGGING_MAXBYTES = 1024

TIMEZONE = "America/Montreal"

STORE_SCREENSHOT_URI = "https://marketvault-bucket.s3.ca-central-1.amazonaws.com/screenshots/"