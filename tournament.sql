-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;

CREATE TABLE players(id serial primary key not null, name text not null);

CREATE TABLE matches(winner integer references players(id) , loser integer references players(id));

CREATE VIEW standings as 
SELECT players.id, players.name,
(SELECT COUNT(*) FROM matches WHERE matches.winner = players.id) AS matches_won,
(SELECT COUNT(*) FROM matches WHERE players.id in (winner, loser)) AS matches_played 
FROM players
GROUP BY players.id
ORDER BY matches_won DESC;