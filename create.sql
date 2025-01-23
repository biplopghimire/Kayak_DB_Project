-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-12-05 19:11:20.68

-- tables
-- Table: Airlines
CREATE TABLE Airlines (
    airline_name text  NOT NULL,
    headquarters text  NOT NULL,
    CONSTRAINT Airlines_pk PRIMARY KEY (airline_name)
);

-- Table: Bugs
CREATE TABLE Bugs (
    b_iid int  NOT NULL,
    severity text  NOT NULL,
    CONSTRAINT Bugs_pk PRIMARY KEY (b_iid)
);

-- Table: Features
CREATE TABLE Features (
    f_iid int  NOT NULL,
    votes int  NOT NULL,
    CONSTRAINT Features_pk PRIMARY KEY (f_iid)
);

-- Table: Feedback
CREATE TABLE Feedback (
    fid int  NOT NULL,
    comment text  NOT NULL,
    uid int  NOT NULL,
    iid int  NOT NULL,
    sid int  NOT NULL,
    CONSTRAINT Feedback_pk PRIMARY KEY (fid)
);

-- Table: Flights
CREATE TABLE Flights (
    fnum int  NOT NULL,
    departure_date date  NOT NULL,
    departure_airport text  NOT NULL,
    destination_airport text  NOT NULL,
    airline_name text  NOT NULL,
    CONSTRAINT Flights_pk PRIMARY KEY (fnum,departure_date)
);

-- Table: FlightsInSearches
CREATE TABLE FlightsInSearches (
    sid int  NOT NULL,
    fnum int  NOT NULL,
    departure_date date  NOT NULL,
    CONSTRAINT FlightsInSearches_pk PRIMARY KEY (sid,fnum,departure_date)
);

-- Table: Guests
CREATE TABLE Guests (
    g_uid int  NOT NULL,
    login_ip text  NOT NULL,
    timestamp timestamp  NOT NULL,
    CONSTRAINT Guests_pk PRIMARY KEY (g_uid)
);

-- Table: Issues
CREATE TABLE Issues (
    iid int  NOT NULL,
    status text  NOT NULL,
    CONSTRAINT Issues_pk PRIMARY KEY (iid)
);

-- Table: Registered
CREATE TABLE Registered (
    r_uid int  NOT NULL,
    name text  NOT NULL,
    phone_number text  NOT NULL,
    email text  NOT NULL,
    CONSTRAINT Registered_pk PRIMARY KEY (r_uid)
);

-- Table: Searches
CREATE TABLE Searches (
    sid int  NOT NULL,
    timestamp timestamp  NOT NULL,
    uid int  NOT NULL,
    CONSTRAINT Searches_pk PRIMARY KEY (sid)
);

-- Table: Users
CREATE TABLE Users (
    uid int  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (uid)
);

-- foreign keys
-- Reference: Features_Issues (table: Features)
ALTER TABLE Features ADD CONSTRAINT Features_Issues
    FOREIGN KEY (f_iid)
    REFERENCES Issues (iid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Feedback_Issues (table: Feedback)
ALTER TABLE Feedback ADD CONSTRAINT Feedback_Issues
    FOREIGN KEY (iid)
    REFERENCES Issues (iid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Feedback_Searches (table: Feedback)
ALTER TABLE Feedback ADD CONSTRAINT Feedback_Searches
    FOREIGN KEY (sid)
    REFERENCES Searches (sid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Feedback_Users (table: Feedback)
ALTER TABLE Feedback ADD CONSTRAINT Feedback_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: FlightsInSearches_Flights (table: FlightsInSearches)
ALTER TABLE FlightsInSearches ADD CONSTRAINT FlightsInSearches_Flights
    FOREIGN KEY (fnum, departure_date)
    REFERENCES Flights (fnum, departure_date)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: FlightsInSearches_Searches (table: FlightsInSearches)
ALTER TABLE FlightsInSearches ADD CONSTRAINT FlightsInSearches_Searches
    FOREIGN KEY (sid)
    REFERENCES Searches (sid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Flights_Airlines (table: Flights)
ALTER TABLE Flights ADD CONSTRAINT Flights_Airlines
    FOREIGN KEY (airline_name)
    REFERENCES Airlines (airline_name)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guests_Users (table: Guests)
ALTER TABLE Guests ADD CONSTRAINT Guests_Users
    FOREIGN KEY (g_uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Issues_Bugs (table: Bugs)
ALTER TABLE Bugs ADD CONSTRAINT Issues_Bugs
    FOREIGN KEY (b_iid)
    REFERENCES Issues (iid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Registered_Users (table: Registered)
ALTER TABLE Registered ADD CONSTRAINT Registered_Users
    FOREIGN KEY (r_uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Searches_Users (table: Searches)
ALTER TABLE Searches ADD CONSTRAINT Searches_Users
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.