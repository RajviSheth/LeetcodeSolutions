# Write your MySQL query statement below
# SELECT user_id, followers AS followers_count
# FROM
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
