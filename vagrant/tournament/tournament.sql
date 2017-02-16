-- Here I delete previous table if they exists.
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;
DROP VIEW IF EXISTS standings CASCADE;
DROP VIEW IF EXISTS wins CASCADE;
DROP VIEW IF EXISTS count CASCADE;


-- Here the players table, with ID and name
CREATE TABLE players ( id serial PRIMARY KEY, name VARCHAR(20) NOT NULL);


-- Here the matches table, with ID and winner and loser references-ID
-- that will be deleted when the ID on the players table will be deleted
CREATE TABLE matches( id serial PRIMARY KEY,
  winner int REFERENCES players(id) on DELETE CASCADE,
  loser int REFERENCES players(id) on DELETE CASCADE );


-- Creates a view of wins to sort out how many wins a player has
CREATE VIEW wins AS
    SELECT players.id, count(matches.winner) AS num FROM players
      LEFT JOIN matches ON players.id = matches.winner
      GROUP BY players.id;

-- Creates a view of matches count per player
CREATE VIEW count AS
    SELECT players.id, count(matches.winner) AS num FROM players
      LEFT JOIN matches ON players.id = matches.winner
      OR players.id = matches.loser
      GROUP BY players.id;

-- Creates standings view
CREATE VIEW standings AS
    SELECT players.id, players.name, wins.num AS wins, count.num AS matches_played
        FROM players, wins, count
          WHERE players.id = wins.id and players.id = count.id
          ORDER BY wins DESC;
