CREATE TABLE dog (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    gender VARCHAR(100),
    color VARCHAR(100),
    favoritefood VARCHAR(100),
    favoritytoy VARCHAR(100)

);

CREATE TABLE breed (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    size VARCHAR(100),
    friendliness INTEGER,
    trainability INTEGER,
    sheddingmanagement INTEGER,
    exerviseneeds INTEGER
);


INSERT INTO dog (name) VALUES ('Lune');
INSERT INTO breed (name) VALUES ('mutt');