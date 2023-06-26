# Write your MySQL query statement below
SELECT weather.id as ID from Weather JOIN Weather as w
ON DATEDIFF(weather.recordDate, w.recordDate) = 1
WHERE weather.Temperature > w.Temperature 