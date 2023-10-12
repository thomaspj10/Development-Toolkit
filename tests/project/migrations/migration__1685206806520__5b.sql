create table Address (
    id integer primary key auto_increment, 
    name varchar(255)
);

create table User (
    id integer primary key auto_increment, 
    name varchar(255) not null, 
    address_id int, 
    verified boolean, 
    foreign key (address_id) references Address(id)
);
