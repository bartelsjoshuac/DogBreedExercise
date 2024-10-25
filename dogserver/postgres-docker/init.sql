-- This is not needed and also unsafe.  Django takes care of this as part of the model.py and the migrations.  It doesn't even get run
-- NOTE: We can not do data bounds checking here like we can in the Django model because its SQL

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

-- Insert one partial dog to start
INSERT INTO dog (name) VALUES ('Lune');
INSERT INTO breed (name) VALUES ('mutt');