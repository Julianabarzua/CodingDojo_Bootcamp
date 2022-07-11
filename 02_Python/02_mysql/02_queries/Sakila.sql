SELECT c.first_name, c.last_name, c.email, a.address
FROM customer as c
LEFT JOIN address as a ON a.address_id = c.address_id
WHERE a.city_id = 312;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, cat.name
FROM film as f
JOIN film_category as fc ON f.film_id = fc.film_id
JOIN category as cat ON cat.category_id = fc.category_id
WHERE cat.name = "Comedy";

SELECT a.actor_id, concat(a.first_name,' ',a.last_name) as Name, f.title, f.description, f.release_year
FROM actor as a
JOIN film_actor as fa ON a.actor_id = fa.actor_id
JOIN film as f ON f.film_id = fa.film_id
WHERE a.actor_id = 5;

SELECT c.first_name, c.last_name, c.email, a.address
FROM customer as c
JOIN address as a ON c.address_id = a.address_id
WHERE c.store_id = 1 AND a.city_id IN (1,42,312,459);

SELECT f.title, f.description, f.release_year, f.rating, f.special_features
FROM actor as a
JOIN film_actor as fa ON a.actor_id = fa.actor_id
JOIN film as f ON f.film_id = fa.film_id
WHERE a.actor_id = 15 AND f.rating="G" AND f.special_features LIKE '%behind the scenes%';

SELECT f.film_id, f.title, a.actor_id, concat(a.first_name,' ',a.last_name) as name
FROM actor as a
JOIN film_actor as fa ON a.actor_id = fa.actor_id
JOIN film as f ON f.film_id = fa.film_id
WHERE fa.film_id = 369;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, cat.name
FROM film as f
JOIN film_category as fc ON f.film_id = fc.film_id
JOIN category as cat ON cat.category_id = fc.category_id
WHERE cat.name = "Drama" AND f.rental_rate = 2.99;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, cat.name, a.first_name, a.last_name
FROM film as f
JOIN film_category as fc ON f.film_id = fc.film_id
JOIN category as cat ON cat.category_id = fc.category_id
JOIN film_actor as fa ON f.film_id = fa.film_id
JOIN actor as a ON a.actor_id = fa.actor_id
WHERE cat.name = "Action" AND a.first_name="Sandra" AND a.last_name="Kilmer";
