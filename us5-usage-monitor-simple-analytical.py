from common import *

us='''
* Simple US

   As a:  Manager
 I want:  To rank which hours each user is the most active.
So That:  I can promote personalized ads to users at the peak times.
'''

print(us)

def list_hour_by_traffic():
    cols = 'user hour_of_day searches_in_hour activity_rank'
    
    tmpl = f'''
SELECT 
    uid AS user,
    DATE_PART('hour', timestamp) AS hour_of_day,
    COUNT(sid) AS searches_in_hour,
    RANK() OVER w AS activity_rank
  FROM Searches
 GROUP BY uid, DATE_PART('hour', timestamp)
WINDOW w AS (PARTITION BY uid ORDER BY COUNT(sid) DESC);


'''
    cmd = cur.mogrify(tmpl,)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_hour_by_traffic()
