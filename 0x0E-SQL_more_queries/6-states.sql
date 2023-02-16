-- Creates database adn table with id as PK --
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    `id`  INTEGER NOT NULL UNIQUE,
    `name`  VARCHAR(256)  NOT NULL
    PRIMARY KEY (id));
