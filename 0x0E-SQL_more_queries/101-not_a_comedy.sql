-- Retrieves all shows without the genre Comedy --
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_genres.tv_show_id
    FROM tv_shows.tv_genres
    JOIN tvshows.genres ON genres.id = tv_genres.genre_id
    WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title ASC;
