# IMPORTING LIBRARIES
import requests
import datetime as dt
import time
import smtplib
import os

# CONSTANTS
ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"
DEGREE_OFFSET = 5

# DUMMY COORDINATES
MY_LATITUDE = -134.0852
MY_LONGITUDE = 18.2345

# DUMMY CREDENTIALS
TO_MAIL = os.environ.get("TO_MAIL")
FROM_MAIL = os.environ.get("FROM_MAIL")
PASSWORD = os.environ.get("PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SUBJECT = "Subject:Lookout for ISS.\n"

# GET ISS REQUEST
iss_response = requests.get(ISS_API_ENDPOINT)
iss_response.raise_for_status()

# ISS JSON DATA
iss_data = iss_response.json()
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

while True:
    time.sleep(60)
    if (abs(iss_latitude - MY_LATITUDE) <= DEGREE_OFFSET) and (
        abs(iss_longitude - MY_LONGITUDE) <= DEGREE_OFFSET
    ):

        sunset_sunrise_parameters = {
            "lat": MY_LATITUDE,
            "lng": MY_LONGITUDE,
            "formatted": 0,
        }

        # GET SUNSET-SUNRISE(SS) REQUEST
        ss_response = requests.get(
            SUNSET_SUNRISE_API_ENDPOINT, params=sunset_sunrise_parameters
        )
        ss_response.raise_for_status()

        #  SS JSON DATA
        ss_data = ss_response.json()

        sunrise = ss_data["results"]["sunrise"]
        sunset = ss_data["results"]["sunset"]

        sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
        sunset_hour = int(sunset.split("T")[1].split(":")[0])

        current_hour = dt.datetime.now().hour

        message = SUBJECT + "ISS is above you. Go out and check the night sky."

        if current_hour > sunset_hour or current_hour < sunrise:
            try:
                with smtplib.SMTP(FROM_SMTP_SERVER) as connection:
                    connection.starttls()
                    connection.login(user=FROM_MAIL, password=PASSWORD)
                    connection.sendmail(
                        from_addr=FROM_MAIL, to_addrs=TO_MAIL, msg=message
                    )
                print("Mail sent.")
            except:
                print("Mail could not be sent.")
