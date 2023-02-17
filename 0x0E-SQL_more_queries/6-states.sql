-- Creates database andi table with id as PK --
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id  INTEGER NOT NULL AUTO_INCREMENT,
    name  VARCHAR(256)  NOT NULL,
    PRIMARY KEY (id));
