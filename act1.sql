SELECT 
    grade,
    COUNT(*) AS total_students,
    AVG(score) AS average_score
FROM students
WHERE score > 60          -- filter rows
GROUP BY grade            -- group data
HAVING AVG(score) > 70    -- filter groups
ORDER BY average_score DESC;  -- sort results