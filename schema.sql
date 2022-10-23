CREATE TABLE users1 (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE themes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    hidden INTEGER DEFAULT 0
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    thread_name TEXT,
    theme_id INTEGER REFERENCES themes,
    creator_id INTEGER REFERENCES users1,
    hidden INTEGER DEFAULT 0
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads,
    user_id INTEGER REFERENCES users1,
    message TEXT,
    hidden INTEGER DEFAULT 0
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    thread_id INTEGER REFERENCES threads,
    user_id INTEGER REFERENCES users1
);