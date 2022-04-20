-- dev_playground.employee definition

-- Drop table

-- DROP TABLE dev_playground.employee;

CREATE TABLE dev_playground.employee (
	employee_id int4 NOT NULL,
	"name" varchar(100) NOT NULL,
	age int4 NOT NULL,
	address varchar(100) NULL,
	salary float4 NULL,
	company varchar(100) NULL,
	CONSTRAINT employee_pkey PRIMARY KEY (employee_id)
);