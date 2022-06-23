# Automated-ISS-Coordinates

### [twitter](https://twitter.com/achte_te)

## Description
An application that checks the realtime coordinates of International Space Station. The coordinates can be checked at [coordinate_checker](https://www.latlong.net/Show-Latitude-Longitude.html).

If the ISS is above the specified location coordinates and if the sun has set in the location on the ground, an email is sent using the SMTP protocol.  

This code is running on [pythonanywhere](https://www.pythonanywhere.com/) servers.  

## Requirements

[Python](https://www.python.org/)

```sh
$ python3 --version
Python 3.9.12
```

[requests](https://pypi.org/project/requests/)

[datetime](https://docs.python.org/3/library/datetime.html)

[ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

[SUNSET-SUNRISE-API](https://sunrise-sunset.org/api)

## Install

```sh
$ git clone git@github.com:achte-2022/ISS-Coordinates.git
```

## Run

```sh
$ cd ISS-Coordinates
$ python3 main.py
```
