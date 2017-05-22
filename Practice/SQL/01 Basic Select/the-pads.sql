SELECT CONCAT(name, '(', SUBSTRING(occupation, 1, 1), ')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are total ', COUNT(*), ' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(*), occupation;
