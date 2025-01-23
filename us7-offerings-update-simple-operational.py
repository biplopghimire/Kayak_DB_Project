from common import *

us = '''
* Simple US

   As a:  Airline
 I want:  To update offerings of flights available to travelers.
So That:  I can provide travelers an accurate listing of all flights.
'''

print(us)

def list_and_update_flights(flight_number, date, new_destination):
    cols = 'f.fnum, f.departure_date, f.departure_airport, f.destination_airport, f.airline_name'
    tmpl_list = f'''
SELECT {cols}
  FROM Flights as f
 ORDER BY f.departure_date ASC
    '''
    cmd_list = cur.mogrify(tmpl_list, ())
    cur.execute(cmd_list)
    rows = cur.fetchall()
    show_table(rows, "fnum departure_date departure_airport destination_airport airline_name")
    tmpl_update_flights = '''
UPDATE Flights
   SET departure_date = %s, destination_airport = %s
 WHERE fnum = %s
    '''
    cmd_update_flights = cur.mogrify(tmpl_update_flights, (date, new_destination, flight_number))
    cur.execute(cmd_update_flights)

    tmpl_update_searches = '''
UPDATE FlightsInSearches
   SET departure_date = %s
 WHERE fnum = %s
    '''
    cmd_update_searches = cur.mogrify(tmpl_update_searches, (date, flight_number))
    cur.execute(cmd_update_searches)

    print(f"Flight {flight_number} departure date {date} updated to new destination {new_destination}.")

def list_flights():
    cols = 'fnum departure_date departure_airport destination_airport airline_name'
    
    tmpl = f'''
SELECT {c(cols)}
  FROM Flights
  ORDER BY departure_date ASC
'''
    cmd = cur.mogrify(tmpl, ())
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_and_update_flights("101", "2024-12-05", "T21T") #update new destination!!
list_flights()
