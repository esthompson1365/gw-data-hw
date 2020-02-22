CREATE VIEW title_count AS
SELECT
	film.title,
	COUNT(film.title)
FROM film
RIGHT JOIN inventory
ON film.film_id = inventory.film_id
WHERE film.title IN (SELECT film.title 
               		FROM film
					RIGHT JOIN inventory
					ON film.film_id = inventory.film_id
               		GROUP BY film.title HAVING COUNT(*) = 7)
GROUP BY film.title
ORDER BY film.title	