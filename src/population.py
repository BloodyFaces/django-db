import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta, date
from flights.models import Airport, Plane, Flight

def airport_fill():
    sheet = pd.read_excel('airportsupd.xlsx')
    for index, row in sheet.iterrows():
        airport = Airport(name=row['Name'], country=row['Country'], city=row['City'])
        print(row['Name'], '-', row['City'], '-', row['Country'])
        airport.save()

def plane_fill():
    sheet = pd.read_excel('planesupd.xlsx')
    for index, row in sheet.iterrows():
        sits = row['Sits']
        plane = Plane(name=row['Name'], number_of_sits=sits)
        print(row['Name'], '-', sits)
        plane.save()


def get_random_date(year):
    try:
        return datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')
    except ValueError:
        get_random_date(year)


def get_random_airports(airports, dep=None):
    if dep is None:
        dep_index = random.randint(1, airports.count())
        dep = airports.get(pk=dep_index)
    dest_index = random.randint(1, airports.count())
    dest = airports.get(pk=dest_index)
    if dep.country == dest.country:
        return get_random_airports(airports, dep=dep)
    return dep, dest


def flights_fill(count):
    airports = Airport.objects.all()
    planes = Plane.objects.all()
    for i in range(count):
        year = random.randint(2018, 2025)
        flight_datetime = get_random_date(year)
        flight_date = flight_datetime.date()
        hour = random.randint(3, 23)
        flight_time = timedelta(hours=hour)
        dep, dest = get_random_airports(airports)
        plane_index = random.randint(1, planes.count())
        plane = planes.get(pk=plane_index)
        flight = Flight(duration=flight_time, date=flight_date, departure=dep, destination=dest, plane=plane)
        flight.save()

#airport_fill()
#plane_fill()
flights_fill(50000)