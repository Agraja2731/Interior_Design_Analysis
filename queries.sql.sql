DELETE FROM interior_design_trends WHERE Popularity_Score IS NULL;

UPDATE interior_design_trends
SET Style = LOWER(TRIM(Style)),
    Color = LOWER(TRIM(Color));

SELECT Style, AVG(Popularity_Score) AS Avg_Popularity
FROM interior_design_trends
GROUP BY Style
ORDER BY Avg_Popularity DESC;
