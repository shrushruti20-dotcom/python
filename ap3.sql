CREATE TABLE IF NOT EXISTS community_activity (
    activity_id     INTEGER PRIMARY KEY,
    activity_name   TEXT    NOT NULL,
    activity_type   TEXT    NOT NULL,
    day             TEXT    NOT NULL,
    participants    INTEGER NOT NULL,
    duration_mins   INTEGER NOT NULL
);

INSERT INTO community_activity VALUES
(1, 'Yoga Class',        'Wellness', 'Monday',    18, 60), 
(2, 'Art Workshop',      'Creative', 'Tuesday',   12, 90),
(3, 'Chess Club',        'Games',    'Wednesday', 16, 75),
(4, 'Dance Practice',    'Wellness', 'Thursday',  20, 60),
(5, 'Coding Club',       'Learning', 'Friday',    14, 90);


SELECT * FROM community_activity;

SELECT activity_name, participants
FROM community_activity
ORDER BY participants ASC;
SELECT activity_name, participants
FROM community_activity
ORDER BY participants DESC;
SELECT activity_name, activity_type, participants
FROM community_activity
ORDER BY activity_type ASC, participants DESC;
SELECT activity_name, participants
FROM community_activity
ORDER BY participants DESC
LIMIT 3;
SELECT activity_type, COUNT(*) AS activity_count
FROM community_activity
GROUP BY activity_type;
SELECT activity_type,
       SUM(participants) AS total_participants,
       AVG(duration_mins) AS average_duration_mins
FROM community_activity
GROUP BY activity_type;
SELECT activity_type, COUNT(*) AS activity_count
FROM community_activity
GROUP BY activity_type
HAVING COUNT(*) > 2;
SELECT activity_type, AVG(participants) AS average_participants
FROM community_activity
GROUP BY activity_type
HAVING AVG(participants) >= 15;
