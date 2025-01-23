from common import *

us='''
* Compelx US

   As a:  Manager
 I want:  To see which airlines appear in the most searches.
So That:  I can promote airlines that are most popular.
'''

print(us)

def list_airlines_by_searches():
    cols = 'f.airline_name COUNT(fs.sid)'
    
    tmpl = f'''
SELECT {c(cols)}
  FROM FlightsInSearches AS fs
       JOIN Flights AS f ON fs.fnum = f.fnum AND fs.departure_date = f.departure_date
 GROUP BY f.airline_name
 ORDER BY COUNT(fs.sid) DESC;
'''
    cmd = cur.mogrify(tmpl,)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_airlines_by_searches()
