---postgres table for aiminpetperson---
drop table if exists pet;
create table pet(
    name text not null,
    species text not null,
    age int not null,
    breed text not null,
    owners text[]
);

drop table if exists person;
create table person(
    name text not null,
    contact text not null,
    age int not null,
    address text not null,
    year_of_joining int not null
)