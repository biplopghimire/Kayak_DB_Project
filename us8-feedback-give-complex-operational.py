from common import *

#this is a pretty complicated US so i have comments below kinda explaning it as it looks more complicated that it is.

us = '''
* Simple US

   As a:  Traveler
 I want:  To give feedback for my searches.
So That:  I can express my desire for a specific feature.
'''

print(us)

def create_feature_votes_trigger(): #update the votes trigger function
    drop_trigger_and_function = '''
    DROP TRIGGER IF EXISTS update_feature_votes_trigger ON Feedback;
    DROP FUNCTION IF EXISTS update_feature_votes();
    '''
    cur.execute(drop_trigger_and_function)

    create_votes_function = '''
    CREATE FUNCTION update_feature_votes()
    RETURNS TRIGGER AS $$ 
    BEGIN
        UPDATE Features
           SET votes = votes + 1
         WHERE f_iid = NEW.iid;

        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    '''
    cur.execute(create_votes_function)

    create_votes_trigger = '''
    CREATE TRIGGER update_feature_votes_trigger
    AFTER INSERT ON Feedback
    FOR EACH ROW
    EXECUTE FUNCTION update_feature_votes();
    '''
    cur.execute(create_votes_trigger)

def give_feedback(fid, comment, uid, sid, iid):
    tmpl_check_issue = '''
SELECT COUNT(*)
  FROM Issues
 WHERE iid = %s
    '''
    cur.execute(tmpl_check_issue, (iid,))
    issue_exists = cur.fetchone()[0] > 0 #https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchone.html

    if not issue_exists: #it checks if the issue already exists if not it adds it to issues
        tmpl_create_issue = '''
INSERT INTO Issues (iid, status)
VALUES (%s, 'new')
        '''
        cur.execute(tmpl_create_issue, (iid,))

    tmpl_check_feature = '''
SELECT COUNT(*)
  FROM Features
 WHERE f_iid = %s
    '''
    cur.execute(tmpl_check_feature, (iid,))
    feature_exists = cur.fetchone()[0] > 0

    if not feature_exists: #same thing as ealier but now with features table.
        tmpl_create_feature = '''
INSERT INTO Features (f_iid, votes)
VALUES (%s, 0)
        '''
        cur.execute(tmpl_create_feature, (iid,))

    tmpl_insert_feedback = '''
INSERT INTO Feedback (fid, comment, uid, sid, iid)
VALUES (%s, %s, %s, %s, %s)
    '''
    cmd_insert_feedback = cur.mogrify(
        tmpl_insert_feedback,
        (fid, comment, uid, sid, iid)
    )
    cur.execute(cmd_insert_feedback)

def list_feedback(): #just used to show the result of what the trigger function did
    cols = 'fid comment uid iid sid'
    tmpl =  f'''
SELECT {c(cols)}
  FROM Feedback
'''
    cmd = cur.mogrify(tmpl, ())
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

def list_features(): #just used to show the result of what the trigger function did
    cols = 'Features.f_iid Features.votes'

    tmpl =  f'''
SELECT {c(cols)}
  FROM Features as Features
'''
    cmd = cur.mogrify(tmpl, ())
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, cols)

create_feature_votes_trigger()

give_feedback(
    26912,  # insert RANDOM unique NUMBER for Feedback ID
    "This feature is really NEEDED!",  # the comment
    uid=10,  # needs to be a EXISTING UID as users can only give feedback
    sid=202,  # needs to be a EXISTING SID as you need a search to give feedback
    iid=12  # either a existing or new Feature ID (checks Issues or creates it)
)

#this is just to show the result of the function that ran
list_feedback()
list_features()