# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tenant
import mysql.connector
from mysql.connector import errorcode

@receiver(post_save, sender=Tenant)
def create_tenant_database(sender, instance, created, **kwargs):
    if created:
        try:
            # Connect to MySQL server
            cnx = mysql.connector.connect(
                user='root',  # Replace with your MySQL root user
                password='',  # Replace with your MySQL root password
                host=instance.db_host,
                port=instance.db_port
            )
            cursor = cnx.cursor()

            # Create database
            cursor.execute(f"CREATE DATABASE {instance.db_name}")

            # Create user and grant privileges
            cursor.execute(f"CREATE USER '{instance.db_user}'@'{instance.db_host}' IDENTIFIED BY '{instance.db_password}'")
            cursor.execute(f"GRANT ALL PRIVILEGES ON {instance.db_name}.* TO '{instance.db_user}'@'{instance.db_host}'")
            cursor.execute("FLUSH PRIVILEGES")

            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
