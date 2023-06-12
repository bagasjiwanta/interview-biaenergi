create table customers (
    ID varchar(16) primary key,
    first_name varchar(200),
    last_name varchar(200),
    origin varchar(5),
    phone unique varchar(20),
)