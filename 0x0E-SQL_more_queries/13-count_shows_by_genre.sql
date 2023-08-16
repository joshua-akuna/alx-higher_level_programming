-- lists all genres from hbtn_0d_tvshows and displays the number of
--	shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY genre HAVING number_shows > 0 ORDER BY number_shows DESC
