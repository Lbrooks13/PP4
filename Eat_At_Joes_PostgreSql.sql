-- /*******************************************************************************
--    Create Tables
-- ********************************************************************************/
CREATE TABLE "Customers"
(
    "CustomerId" INT NOT NULL,
    "FirstName" VARCHAR(40) NOT NULL,
    "LastName" VARCHAR(40) NOT NULL,
    "PhoneNumber" VARCHAR(15),
    "EmailAddress" VARCHAR(40),
    CONSTRAINT "PK_Customers" PRIMARY KEY  ("CustomerId")
);

CREATE TABLE "Tables"
(
    "TableId" INT NOT NULL,
    "TableNumber" INT NOT NULL,
    "Capacity" INT NOT NULL,
    "Location" VARCHAR(20),
    "AvaliabiltyStatus" BOOLEAN,
    CONSTRAINT "PK_Tables" PRIMARY KEY  ("TableId")
);

CREATE TABLE "Reservations"
(
    "ReservationId" INT NOT NULL,
    "CustomerId" INT NOT NULL,
    "TableId" INT NOT NULL,
    "ReservationDate" DATE NOT NULL,
    "ReservationTime" TIME NOT NULL,
    "NumberOfGuests" INT NOT NULL,
    CONSTRAINT "PK_Reservations" PRIMARY KEY  ("ReservationId")
);

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
ALTER TABLE "Reservations" ADD CONSTRAINT "FK_CustomerId"
    FOREIGN KEY ("CustomerId") REFERENCES "Customers" ("CustomerId") ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX "IFK_ReservationsCustomerId" ON "Reservations" ("CustomerId");

ALTER TABLE "Reservations" ADD CONSTRAINT "FK_TableId"
    FOREIGN KEY ("TableId") REFERENCES "Tables" ("TableId") ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX "IFK_ReservationsTableId" ON "Reservations" ("TableId");

/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (1, 01, 4, 'Front', true);
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (2, 02, 4, 'Front', true);
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (3, 03, 10, 'Front', true);
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (4, 04, 10, 'Front', true);
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (5, 05, 5, 'Front', true);
INSERT INTO "Tables" ("TableId", "TableNumber", "Capacity", "Location", "AvaliabiltyStatus") VALUES (6, 06, 5, 'Front', true);
