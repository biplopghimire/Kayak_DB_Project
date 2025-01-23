from common import *

us='''
* Complex US

   As a:  Manager
 I want:  To view feature requests from only our registered users.
So That:  I can cater the website more towards our registered users.
'''

print(us)

def list_feature_requests_for_registered_users():

    cols = 'f.f_iid feed.comment f.votes u.uid r.name r.email'

    tmpl =  f'''
SELECT {c(cols)}
  FROM Features as f
       JOIN Feedback as feed on f.f_iid = feed.iid
       JOIN Users as u ON feed.uid = u.uid
       JOIN Registered as r ON u.uid = r.r_uid
 WHERE r.r_uid IS NOT NULL
 ORDER BY f.votes DESC    
'''
    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    # pp(rows)
    show_table(rows, cols)

list_feature_requests_for_registered_users()