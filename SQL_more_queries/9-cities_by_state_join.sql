-- 9 list all cities again but it's different

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;