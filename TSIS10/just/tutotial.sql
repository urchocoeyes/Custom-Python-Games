--each column consists of the column name,
--the kind of data that column stores,
--the length of data
--the column constraint(NOT NULL, UNIQUE, PRIMARY KEY, CHECK, KEY)

CREATE TABLE [IF NOT EXISTS] table_name(
    column1 datatype(length) column_constraint,
    column2 datatype(length) column_constraint,
    column3 datatype(length) column_constraint,
    table_constraints
);