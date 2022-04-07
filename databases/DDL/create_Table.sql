-- dev_playground.students definition

-- Drop table

-- DROP TABLE dev_playground.students;

-- TRUNCATE TABLE dev_playground.students;

CREATE TABLE dev_playground.students (
	student_id int4 NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	age int4 NOT NULL,
	adress varchar(100) NOT NULL,
	semester int4 NOT NULL,
	CONSTRAINT students_pkey PRIMARY KEY (student_id)
);