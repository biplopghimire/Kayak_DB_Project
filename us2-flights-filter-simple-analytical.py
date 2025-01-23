from common import *

us='''
* Simple US

   As a:  Traveler
 I want:  To filter flights by destination.
So That:  I can see flights to my desired destination.
'''

print(us)

def list_flights_sorted_by_departure_date(dest):
    cols = 'fnum departure_date departure_airport destination_airport airline_name'
    
    tmpl = f'''
SELECT {c(cols)}
  FROM Flights
 WHERE destination_airport = %s
'''
    cmd = cur.mogrify(tmpl, (dest,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_flights_sorted_by_departure_date('JFK International')
