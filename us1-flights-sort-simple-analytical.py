from common import *

us='''
* Simple US

   As a:  Traveler
 I want:  To sort flights by departure date.
So That:  I can see when the earliest flight is.
'''

print(us)

def list_flights_sorted_by_departure_date():
    cols = 'fnum departure_date departure_airport destination_airport airline_name'
    
    tmpl = f'''
SELECT {c(cols)}
  FROM Flights
 ORDER BY departure_date ASC
'''
    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_flights_sorted_by_departure_date()
