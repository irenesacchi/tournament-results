# ==Irene’s Tournament Results==

Project Specification

Develop a Python module that uses the PostgreSQL database to keep track of players and matches in a Swiss-style game tournament.

Files

tournament.py

    Implementation for the Swiss tournament

tournament.sql

    SQL queries to create the database, tables and views

tournament_test.py

    Test cases for tournament.py

# ==To run the module on your VM==

-Start Vagrant

Open Terminal or cmd and browse to the vagrant folder

Type vagrant up

In the same terminal type vagrant ssh

-Change to the correct folder

Type cd /vagrant/tournament

-Open PSQL and run the tournament.sql

type psql

inside the psql you should see:

vagrant==> tipe: “CREATE DATABASE tournament”

write SQL in the tournament.sql file to create tables, or copy and paste it from the tournment.sql file.

copy the contents of tournament.sql and paste in to the terminal window

-Run the tests

In the terminal type python tournament_test.py

#==Success! All tests pass!==
