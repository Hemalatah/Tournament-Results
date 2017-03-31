#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2



def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def query_pattern(query):
    """ connect to database, grab cursor, execute, commit,
    close and returns the database object"""
    DB = connect()
    c = DB.cursor()
    c.execute(query)
    DB.commit()
    DB.close()


def deleteMatches():
    """Remove all the match records from the database."""
    query_pattern("delete from matches")

   
def deletePlayers():
    """Remove all the player records from the database."""
    query_pattern("delete from players")


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("select count(id) from players")
    no_of_players = c.fetchone()[0]
    DB.close()
    print no_of_players
    return no_of_players


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("insert into players(name) values(%s);", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("select id, name, matches_won, matches_played from standings")
    player_standings = c.fetchall()
    DB.close()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("insert into matches(winner, loser) values(%s, %s)", (winner, loser))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    c.execute("select id, name from standings")
    players = c.fetchall()
    DB.close()
    pairings = []
    for player in range(0, len(players) - 1, 2):
        pairings.append((players[player][0], players[player][1], players[player + 1][0], players[player + 1][1]))
    return pairings


