SELECT * FROM artist;

SELECT * FROM favorite_song;


-- FROM CLAUSE (left table)
-- JOIN CLAUSE (right table)
SELECT *
FROM artist
INNER JOIN favorite_song
ON favorite_song.artist_id = artist.artist_id;

SELECT *
FROM favorite_song
INNER JOIN artist
ON favorite_song.artist_id = artist.artist_id;

-- LEFT JOIN
SELECT *
FROM artist
LEFT JOIN favorite_song
ON favorite_song.artist_id = artist.artist_id;

-- RIGHT JOIN
SELECT *
FROM artist
RIGHT JOIN favorite_song
ON favorite_song.artist_id = artist.artist_id;

-- FULL JOIN
SELECT *
FROM artist
FULL JOIN favorite_song
ON favorite_song.artist_id = artist.artist_id;

-- Extra stuff
SELECT artist_name, song_name, album
FROM artist
INNER JOIN favorite_song
ON favorite_song.artist_id = artist.artist_id;