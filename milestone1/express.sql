CREATE TYPE THours AS (
    monOpen  TIME,
    monClose TIME,
    tueOpen  TIME,
    tueClose TIME,
    wedOpen  TIME,
    wedClose TIME,
    thuOpen  TIME,
    thuClose TIME,
    friOpen  TIME,
    friClose TIME,
    satOpen  TIME,
    satClose TIME,
    sunOpen  TIME,
    sunClose TIME
);

CREATE TABLE Diners(
    did     INTEGER         NOT NULL PRIMARY KEY,
    name    VARCHAR(256)    NOT NULL UNIQUE,
    loc     VARCHAR(256)    NOT NULL,
    hours   THours          NOT NULL
);

CREATE TABLE Items(
    iid         INTEGER         NOT NULL,
    did         INTEGER         NOT NULL REFERENCES Diners(did),
    name        VARCHAR(256)    NOT NULL,
    price       INTEGER         NOT NULL,
    timeToCook  time            NOT NULL,
    hours       THours          NOT NULL,
    -------------------------------------
    PRIMARY KEY (iid, did)
);

CREATE TABLE Users(
    cardid  INTEGER         NOT NULL PRIMARY KEY,
    name    VARCHAR(256)    NOT NULL,
    phone   VARCHAR(30)     NOT NULL,
    email   VARCHAR(256)    NOT NULL
);

CREATE TABLE Orders(
    oid                 INTEGER NOT NULL PRIMARY KEY,
    cardid              INTEGER NOT NULL REFERENCES Users(cardid),
    did                 INTEGER NOT NULL REFERENCES Diners(did),
    timePlaced          TIMESTAMP NOT NULL,
    scheduledPickUpTime TIMESTAMP NOT NULL,
    stat                VARCHAR(8) CHECK(
        stat = 'pending' OR stat = 'accepted' OR stat = 'ready' OR stat = 'picked'
    )
);

CREATE TABLE Includes(
    oid INTEGER NOT NULL REFERENCES Orders(oid),
    iid INTEGER NOT NULL,
    did INTEGER NOT NULL,
    --------------------------------------------------
    FOREIGN KEY (iid, did) REFERENCES Items(iid, did),
    PRIMARY KEY (oid, iid, did)
);
