create database blog;
use blog;

create table posts (
    id int primary key auto_increment not null,
    title varchar(256),
    body text,
    created_at datetime,
    status char(1)
);

insert into posts values(1,'Primeiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(2,'segundo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
insert into posts values(3,'terceiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(4,'quarto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(5,'quinto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
insert into posts values(6,'sexto titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(7,'setimo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
insert into posts values(8,'oitavo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(9,'nono titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(10,'decimo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',0);
insert into posts values(11,'decimo primeiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(12,'decimo segundo titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);
insert into posts values(13,'decimo terceiro titulo blog','decorator binds a piece of code to an URL path.','2013-01-15 10:12:33',1);


