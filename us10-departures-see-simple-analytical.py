from common import *

us = '''
* Simple US

   As a:  Airline
 I want:  To see the frequency of flights departing from certain airports.
So That:  I know which airports the airline should service more in the future.
'''

print(us)

def list_departures_by_airline(airline_name):
    cols = 'departure_airport,  count'

    tmpl = f'''
SELECT departure_airport AS departure_airport, COUNT(fnum) AS count
  FROM Flights
 WHERE airline_name = %s
 GROUP BY departure_airport
 ORDER BY count DESC;
    '''
    cmd = cur.mogrify(tmpl, (airline_name,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_departures_by_airline('Delta Airlines')

