-- using a LEFT JOIN on the 'genre_id' and 'id' columns respectively.
SELECT b.name AS genre, count(a.show_id) AS number_of_shows
FROM tv_show_genres a
LEFT JOIN tv_genres b
ON a.genre_id = b.id
GROUP BY a.genre_id
ORDER BY number_of_shows DESC;
