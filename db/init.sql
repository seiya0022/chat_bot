CREATE TABLE chat_room(
    id SERIAL PRIMARY KEY,
    room_name TEXT NOT NULL
);

CREATE TABLE chat_history(
    id SERIAL PRIMARY KEY,
    chat_history JSONB NOT NULL,
    chat_room_id INTEGER REFERENCES chat_room(id),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);