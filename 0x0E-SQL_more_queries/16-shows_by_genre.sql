-- list all shows and all genres linked to that show from the db hbtn_0d_tvshows
-- if a show doesn't have a genre, NULL is display in the genre column
-- results are sorted in ascending order by the show title and the genre name
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
