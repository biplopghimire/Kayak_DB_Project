-- drop the trax database if it exists
DROP database if EXISTS kayak;

-- create it afresh
CREATE database kayak;
\c kayak

\i create.SQL

-- load the data

\copy Users(uid) FROM data/users.csv csv header;
\copy Issues(iid, status) FROM data/issues.csv csv header;
\copy Features(f_iid, votes) FROM data/features.csv csv header;
\copy Bugs(b_iid, severity) FROM data/bugs.csv csv header;
\copy Searches(sid, timestamp, uid) FROM data/searches.csv csv header;
\copy Feedback(fid, comment, uid, iid, sid) FROM data/feedback.csv csv header;
\copy Registered(r_uid, name, phone_number, email) FROM data/registered.csv csv header;
\copy Guests(g_uid, login_ip, timestamp) FROM data/guests.csv csv header;
\copy Airlines(airline_name, headquarters) FROM data/airlines.csv csv header;
\copy Flights(fnum, departure_date, departure_airport, destination_airport, airline_name) FROM data/flights.csv csv header;
\copy FlightsInSearches(sid, fnum, departure_date) FROM data/flights_in_searches.csv csv header;




