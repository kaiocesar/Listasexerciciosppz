CREATE DATABASE blog;

CREATE TABLE posts(
    id integer,
    title varchar(256),
    body text,
    create_at date,
    status character(1)
);

INSERT INTO posts VALUES(1,'Primeiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(2,'segundo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
INSERT INTO posts VALUES(3,'terceiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(4,'quarto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(5,'quinto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
INSERT INTO posts VALUES(6,'sexto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(7,'setimo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
INSERT INTO posts VALUES(8,'oitavo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(9,'nono titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(10,'decimo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
INSERT INTO posts VALUES(11,'decimo primeiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(12,'decimo segundo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
INSERT INTO posts VALUES(13,'decimo terceiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);

