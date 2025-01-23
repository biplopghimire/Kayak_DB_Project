from common import *

us='''
* Complex US

   As a:  Manager
 I want:  To see the number of guest users vs registered users.
So That:  I can determine if we need more incentive to get people to register.
'''

print(us)

def list_registered_guest():

    cols = 'registered_users guest_users'

    tmpl =  f'''
SELECT COUNT(r.r_uid) as registered_users,
       COUNT(g.g_uid) as guest_users
  FROM Registered as r
       FULL JOIN Guests as g ON r.r_uid = g.g_uid   
'''
    cmd = cur.mogrify(tmpl, ())
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

list_registered_guest()