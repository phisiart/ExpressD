INSERT INTO Diners VALUES
(1, 'Au Bon Pain', 'Bryan Center', (
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59',
    '07:00:00', '11:59:59'
));

INSERT INTO Diners VALUES
(2, 'Cafe Edens', 'McClendon Tower', (
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59',
    '00:00:00', '11:59:59'
));

-- Au Bon Pain
INSERT INTO Items VALUES
(1, 1, 'Chicken Cobb with Avocado', 300, '00:05:00', (
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '10:00:00', '11:59:59',
    '11:00:00', '11:59:59'
)),
(2, 1, 'Vegetarian Deluxe', 300, '00:05:00', (
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '08:00:00', '11:59:59',
    '10:00:00', '11:59:59',
    '11:00:00', '11:59:59'
));

-- Cafe Edens
INSERT INTO Items VALUES
(1, 2, 'Chicken Pommes Frites', 1300, '00:05:00', (
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00'
)),
(2, 2, 'Spaghetti And Meatballs', 1200, '00:05:00', (
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00',
    '17:00:00', '11:00:00'
));

-- add a user
INSERT INTO Users VALUES
(
    12345678,                   -- cardid
    'Alex',                     -- name
    '9190000000',               -- phone
    'alexisthebest@spam.com'    -- email
);

-- add an order
INSERT INTO Orders VALUES
(
    1,                      -- oid
    12345678,               -- cardid
    1,                      -- did
    '2014-01-01 00:00:00',  -- timePlaced
    '2014-01-01 10:00:00',  -- scheduledPickUpTime
    'pending'              -- stat
);

-- add item in order
INSERT INTO Includes VALUES
(
    1, -- oid
    1, -- iid
    1  -- did
),
(
    1, -- oid
    2, -- iid
    1  -- did
);

-- see the items in an order
-- see the items in an order
SELECT Orders.oid, Users.name, Diners.name, Items.name
FROM Includes, Orders, Users, Items, Diners
WHERE   Orders.oid = Includes.oid
    AND Orders.cardid = Users.cardid
    AND Includes.iid = Items.iid
    AND Includes.did = Items.did
    AND Diners.did = Includes.did;
    