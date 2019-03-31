## 1. Introducing Joins ##

SELECT * FROM facts
INNER JOIN cities on  cities.facts_id=facts.id
LIMIT 10;