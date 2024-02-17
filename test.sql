
-- Eliminar post user

DELETE FROM post_user
WHERE user_id = 4;


-- obtener post

SELECT title, user_id FROM post_user;

-- Insertar nuevo usuario

INSERT INTO user (name, email, password, username) 
VALUES ('John', 'mail@sample40.com', '1234', 'john40');

-- Actualizar usuario

UPDATE user
SET image_file = 'default.jpg'
WHERE id = 4;