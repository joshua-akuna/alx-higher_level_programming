-- list all shows without genre Comedy in database hbtn_0d_tvshows
-- tv_genres contain knly one record where name = Comedy
-- each record should display tv_shows.title
-- results must be sorted in ascending order by the show title
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
