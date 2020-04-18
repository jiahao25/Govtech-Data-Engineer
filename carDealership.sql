CREATE TABLE public.customers (
	customerID INTEGER NOT NULL PRIMARY KEY,
	customerName VARCHAR (255) NOT NULL,
	customerPhone INTEGER
);

CREATE TABLE public.salespersons (
	salespersonID INTEGER NOT NULL PRIMARY KEY,
	salespersonName VARCHAR (255) NOT NULL,
	salespersonPhone INTEGER
);

CREATE TABLE public.manufacturers (
	manufacturerID INTEGER NOT NULL PRIMARY KEY,
	manufacturerName VARCHAR (255) NOT NULL
);

CREATE TABLE public.carModel (
	modelNameVariant VARCHAR (255) NOT NULL PRIMARY KEY,
	weight float(3),
	engineCapacity float(3),
	price float(2) NOT NULL,
	manufacturerID INTEGER REFERENCES manufacturers(manufacturerID) NOT NULL
);

CREATE TABLE public.cars (
	serialNum VARCHAR (255) NOT NULL PRIMARY KEY,
	modelNameVariant VARCHAR (255) REFERENCES carModel(modelNameVariant) NOT NULL,
	newCar BOOLEAN NOT NULL
);

CREATE TABLE public.transactions (
	transactionID INTEGER NOT NULL PRIMARY KEY,
	transactionDate DATE NOT NULL,
	transactionTime TIME NOT NULL,
	customerID INTEGER REFERENCES customers(customerID) NOT NULL,
	serialNum VARCHAR (255) REFERENCES cars(serialNum) NOT NULL,
	salespersonID INTEGER REFERENCES salespersons(salespersonID) NOT NULL
)
