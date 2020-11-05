PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE records (
domain varchar(255) NOT NULL PRIMARY KEY,
ip varchar(255) NOT NULL
);
INSERT INTO "records" VALUES('bank.com','127.0.0.1');
COMMIT;
