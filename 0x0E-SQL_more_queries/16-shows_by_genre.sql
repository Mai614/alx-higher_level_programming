-- Retrieve titles of TV shows along with their corresponding genres
SELECT A.title, C.name
FROM tv_shows A
LEFT JOIN tv_show_genres B
ON A.id = B.show_id
LEFT JOIN tv_genres C
ON B.genre_id = C.id
ORDER BY 1, 2 ASC;
