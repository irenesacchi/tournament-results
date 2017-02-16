#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
import bleach
import psycopg2
import itertools


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE from matches;')
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute('DELETE FROM players;')
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT count(*) FROM players;')
    registered_players =  c.fetchone()[0]
    db.commit()
    db.close()
    return registered_players


def registerPlayer(name):
    """Adds a player to the tournament database."""
    db = connect()
    c = db.cursor()
    bleached_name = bleach.clean(name, strip=True)
    c.execute('INSERT INTO players (name) VALUES (%s)', (bleached_name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT * FROM standings;')
    player_standings = c.fetchall()
    db.close()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO matches (winner, loser)'
        'VALUES (%s, %s)', (winner, loser,))
    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match."""
    db = connect()
    c = db.cursor()
    c.execute('SELECT * FROM standings;')
    results = c.fetchall()
    pairings = []
    count = len(results)

    for x in range(0, count - 1, 2):
        paired_list = (results[x][0],
                    results[x][1],
                    results[x + 1][0],
                    results[x + 1][1])
        pairings.append(paired_list)

    c.close()
    return pairings
