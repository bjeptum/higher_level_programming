-- Creates the table unique_id --
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256));
    INSERT IGNORE INTO unique_id (id, name)
    VALUES (1, 'Bob');
