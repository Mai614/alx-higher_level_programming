-- using a LEFT JOIN on the 'show_id' and 'id' columns respectively.
-- The results are ordered by 'title' from the 'tv_shows' table and 'genre_id' in ascending order.
SELECT b.title, a.genre_id
FROM tv_show_genres a
LEFT JOIN tv_shows b
ON a.show_id = b.id
ORDER BY b.title, a.genre_id ASC;
