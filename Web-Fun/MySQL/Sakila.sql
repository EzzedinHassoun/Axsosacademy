use sakila;
-- part1
select 
    city.city_id,
    customer.first_name,
    customer.last_name,
    customer.email
from
    customer
        join
    address on address.address_id = customer.address_id
        join
    city on city.city_id = address.city_id
    
where
    city.city_id = 312;
    
    -- part2
    select 
    film.film_id,
    film.description,
    film.release_year,
    film.rating,
    film.special_features,
    category.name as genre
from
    film
        join
    film_category on film.film_id = film_category.film_id
        join
    category on film_category.category_id = category.category_id
where
    category.name = 'Comedy';
    
    -- part3
    select 
    a.actor_id,
    concat_ws(' ', a.first_name, a.last_name) as 'actor_name',
    f.title,
    f.description,
    f.release_year
from
    actor a
        join
    film_actor fc on a.actor_id = fc.actor_id
        join
    film f on fc.film_id = f.film_id
where
    a.actor_id = 5;
    
    -- part4
    select 
    c.first_name,
    c.last_name,
    c.email,
    a.address
from
    customer c
        join
    address a on c.address_id = a.address_id
where
    c.store_id = 1
        and a.city_id in (1 , 42, 312, 459);
        
        -- part5
	select
    f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features
from
    film f
        join
    film_actor fa on f.film_id = fa.film_id
where
    fa.actor_id = 15 and f.rating = 'G'
        and f.special_features like '%behind the scenes%';
        
        -- part6
        select 
    f.film_id,
    f.title,
    a.actor_id,
    CONCAT_WS(' ', a.first_name, a.last_name) as 'actor_name'
from
    actor a
        join
    film_actor fc on a.actor_id = fc.actor_id
        join
    film f on fc.film_id = f.film_id
where
    f.film_id = 369;
    
    -- part7
    select 
    f.title,
    f.description,
    f.release_year,
    f.rating,
    f.special_features,
    c.name as genre

from
    film f
        join
    film_category fc on f.film_id = fc.film_id
        join
    category c on fc.category_id = c.category_id
where
    c.name = 'Drama'
        and f.rental_rate = 2.99;
        
        -- part8
        select
        concat_ws(" ",a.first_name, a.last_name) as "actor_name",
        f.title, 
        f.description, 
        f.release_year,
        f.rating, 
        f.special_features,
        c.name as genre 
from 
actor a join film_actor fc 
on a.actor_id = fc.actor_id 
join 
film f 
on fc.film_id = f.film_id 
join 
film_category fca
on f.film_id = fca.film_id 
join
 category c 
on c.category_id = fca.category_id
where
 a.first_name = "SANDRA" and 
	  a.last_name = "KILMER" and 
      c.name = "Action" 
order by
 f.film_id;