# Setup instructions

Using **Python 3.7.9** (python 3 should work fine in general):
1. Initialize virtual environment (`CS3103_FINAL/app`) <br>
```python3 -m venv .```
2. Run ```pip install -r requirements.txt```
3. Run ```python app.py``` to start the local development server

# Accessing the SQLite database
1. Simply run `sqlite3 database/dns.db` from `CS3103_FINAL/app`
2. To quit, simply type `.quit`

# Installing MySQL Server

Linux Guide: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04
MacOs Guide: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html

Note: Only tested on linux machine, will be tested from GNS3 soon
1. sudo apt update
2. sudo apt install mysql-server
3. sudo mysql_secure_installation
4. sudo apt-get install libmysqlclient-dev
5. sudo apt-get install python3-dev
6. enter root as password
7. mysql -u root -p
8. Enter root as password
9. CREATE DATABASE IF NOT EXIST dns;
10. USE dns;
11. CREATE TABLE IF NOT EXISTS records (domain varchar(255) NOT NULL PRIMARY KEY, ip varchar(255) NOT NULL);
12. INSERT INTO records (domain, ip) VALUES ('www.bank.com', '127.0.0.1');

## Project Structure

`Python` code should be contained inside `app.py`. If the project gets large enough, we can have multiple `.py` files.

`HTML` pages must be in `/templates`.
