\c kayak

\echo 'Displaying contents of the Users table: Contains unique user identifiers.'
SELECT * FROM Users;

\echo 'Displaying contents of the Features table: Tracks feature issues and their vote counts.'
SELECT * FROM Features;

\echo 'Displaying contents of the Bugs table: Lists bug issues with their severity levels.'
SELECT * FROM Bugs;

\echo 'Displaying contents of the Issues table: General issues with their current status.'
SELECT * FROM Issues;

\echo 'Displaying contents of the Feedback table: User feedback on issues and searches.'
SELECT * FROM Feedback;

\echo 'Displaying contents of the Registered table: Information about registered users.'
SELECT * FROM Registered;

\echo 'Displaying contents of the Guests table: Details about guest users, including login IPs and timestamps.'
SELECT * FROM Guests;

\echo 'Displaying contents of the Searches table: Search activity records with timestamps and user IDs.'
SELECT * FROM Searches;

\echo 'Displaying contents of the Airlines table: Airline name and headquarters.'
SELECT * FROM Airlines;

\echo 'Displaying contents of the FlightsInSearches table: Flights displayed in a certain search.'
SELECT * FROM FlightsInSearches;

\echo 'Displaying contents of the Flights table: Information about individual flights.'
SELECT * FROM Flights;