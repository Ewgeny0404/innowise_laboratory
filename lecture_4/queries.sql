
-- 1. CREATE tables

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY(student_id) REFERENCES students(id)
);

-- 2. INSERT initial data

-- students
INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- grades
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),

    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),

    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),

    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),

    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),

    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),

    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),

    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),

    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- 3. SELECT queries

-- all subjects and grades for a specific student (Alice Johnson)
SELECT g.subject, g.grade
FROM grades AS g
JOIN students AS s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- average grade per student
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

-- all students born after 2004
SELECT s.full_name, s.birth_year
FROM students AS s
WHERE s.birth_year > 2004;

-- all subjects with their average grades
SELECT g.subject, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades AS g 
GROUP BY g.subject;

-- top 3 students by average grade
SELECT s.full_name, ROUND(AVG(g.grade), 2) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- students who have at least one grade below 80
SELECT DISTINCT s.full_name
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
WHERE g.grade < 80;
