use world;
-- part 1
SELECT countries.name FROM world.countries;

select
countries.name ,languages.language , languages.percentage
from
countries,
languages
where
countries.id=languages.country_id
and languages.language="Slovene" 
order by languages.percentage desc;
-- part 2
select
countries.name,count(cities.name)
from
countries,
cities
where
countries.id= cities.country_id
group by countries.name
order by count(countries.name) desc;
-- part 3
select
cities.name,cities.population,cities.country_id
from
cities
where cities.country_id=136 and cities.population > 500000;

--- part4
select
countries.name,languages.language,languages.percentage
from
countries,languages
where
countries.id=languages.country_id and languages.percentage>89 order by languages.percentage desc;

-- part5
select countries.name,surface_area, countries.population
from
countries
where
countries.surface_area<501 and countries.population>100000;

-- part6
select
countries.name, countries.government_form,countries.capital, countries.life_expectancy
from
countries
where
countries.life_expectancy>75 and countries.capital>200 and countries.government_form="Constitutional Monarchy";

-- part7
	select
    countries.name, cities.name,cities.district,cities.population
    from
    countries,
    cities
    where
    countries.id=cities.country_id and cities.district="Buenos Aires" and cities.population>500000;
    
    -- part 8
    
select 
countries.region, COUNT(countries.name)
from
countries
group by countries.region
order by COUNT(countries.name) desc
