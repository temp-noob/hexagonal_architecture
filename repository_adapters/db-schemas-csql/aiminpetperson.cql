CREATE KEYSPACE aiminpetperson WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE aiminpetperson.pet (
    name text,
    species text,
    age int,
    breed text,
    owners list[text]
) ;

CREATE TABLE aiminpetperson.person (
    name text,
    contact text,
    age int,
    address text,
    year_of_joining int
) ;
