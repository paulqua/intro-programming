-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS tournament CASCADE;
DROP TABLE IF EXISTS matches CASCADE;


CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
    player_id serial PRIMARY KEY,
    player_name text
);

CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    winner_id integer REFERENCES players,
    loser_id integer REFERENCES players
);

CREATE VIEW winners AS
    SELECT player_id, player_name, count(winner_id) wins
    FROM players
    LEFT JOIN matches
    ON player_id = winner_id
    GROUP BY player_id
    ORDER BY wins DESC;

CREATE VIEW games AS
    SELECT player_id, COUNT(matches.*) matches
    FROM players 
    LEFT JOIN matches
    ON player_id = winner_id
    OR player_id = loser_id
    GROUP BY player_id;

CREATE VIEW standings AS
    SELECT winners.player_id, winners.player_name, winners.wins,
    games.matches
    FROM winners, games, players
    LEFT JOIN matches
    ON players.player_id = matches.winner_id
    OR players.player_id = matches.loser_id
    GROUP BY winners.player_id, winners.player_name, winners.wins,
    games.matches
    ORDER BY winners.wins DESC;


