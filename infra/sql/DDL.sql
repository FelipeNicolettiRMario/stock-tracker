CREATE DATABASE stock_tracker;

\c stock_tracker;

CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(70) UNIQUE,
    phone VARCHAR(20) UNIQUE
);

CREATE TABLE rule (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(7) NOT NULL,
    period INT NOT NULL,
    operator BOOLEAN NOT NULL,
    target NUMERIC(5,2),
    comparison_target VARCHAR(7),
    UNIQUE (period, operator, target, comparison_target)
);

CREATE TABLE rule_to_client (
    client_id INT,
    rule_id INT,
    FOREIGN KEY (client_id) REFERENCES client(id),
    FOREIGN KEY (rule_id) REFERENCES rule(id)
);
