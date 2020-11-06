PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE records (
domain varchar(255) NOT NULL PRIMARY KEY,
ip varchar(255) NOT NULL
);
INSERT INTO records VALUES('bank.com','127.0.0.0');
INSERT INTO records VALUES('google.com','127.217.194.138');
INSERT INTO records VALUES('luminus.com','18.182.99.238');
INSERT INTO records VALUES('youtube.com','74.125.68.91');
INSERT INTO records VALUES('listent.app','34.232.170.120');
INSERT INTO records VALUES('instagram.com','34.232.170.120');
INSERT INTO records VALUES('coursemology.org','163.47.8.92');
INSERT INTO records VALUES('facebook.com','157.240.218.35');
INSERT INTO records VALUES('twitch.tv','151.101.130.167');
INSERT INTO records VALUES('nusmods.com','139.59.222.196');
COMMIT;
