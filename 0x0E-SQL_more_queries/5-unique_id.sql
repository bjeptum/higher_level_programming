--  Creates table with unique default ID --
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256));
