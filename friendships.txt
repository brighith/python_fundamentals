INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES 
("Jarrod", "Vickers", now(), now()),
("Jessica", "Vickers", now(), now()),
("Jean", "Knowles", now(), now()),
("Gaia", "Sargent", now(), now()),
("Ryan", "Horger", now(), now()),
("Xandra", "Cullen", now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(1, 2, now(), now()),
(1, 4, now(), now()),
(1, 6, now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(2, 1, now(), now()),
(2, 3, now(), now()),
(2, 5, now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(3, 2, now(), now()),
(3, 5, now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(4, 3, now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(5, 1, now(), now()),
(5, 6, now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES
(6, 2, now(), now()),
(6, 3, now(), now());

SELECT * FROM friendships;

SELECT CONCAT(users.first_name, ' ', users.last_name) AS user, CONCAT (user2.first_name, ' ', user2.last_name) AS friend FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;