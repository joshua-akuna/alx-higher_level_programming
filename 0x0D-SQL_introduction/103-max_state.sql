-- the script displays the maximum temperature of each state
-- ordered by state (descending)
SELECT state, MAX(value) AS max_temp 
FROM temperatures 
GROUP BY state
ORDER BY state 
