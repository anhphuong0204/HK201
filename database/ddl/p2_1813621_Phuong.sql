create database BANKING
go

use BANKING
go

create table Person
(
	SSN int primary key,
	FirstName nvarchar(10),
	LastName nvarchar(10),
)
go

create table Customer
(
	Number int primary key,
	CusSSN int not null,
	EmployeeID int not null,
	CusType nvarchar(10),
)
go

create table Employee 
(
	ID int primary key,
	Salary int,
	StartDate date,
	EmSSN int not null,
	BranchName nvarchar(30) not null,
	SupervisorID int,
)
go

create table Branch
(
	Name nvarchar(30) primary key,
	BranchAddress nvarchar(40),
	ID int not null,
	Assets int,
)
go

create table Account
(
	Number int primary key,
	Balance int,
	BranchName nvarchar(30),
	OpenDate date,
	ContractID int,
)
go

create table Saving 
(
	Number int primary key,
	InterestRate int,
)
go

create table Checking
(
	Number int primary key,
	Overdraft int,
)
go

create table Loan
(
	Number int primary key,
	Amount int,
	DueDate date,
	Program nvarchar(20),
	BranchName nvarchar(30) not null,
	OpenDate date,
	ContractID int,
)
go

create table Payment
(
	Number int not null,
	LoanNumber int not null,
	Amount int,
	PayDate date,

	primary key (Number, LoanNumber)
)
go

create table ContractOfCus
(
	ContractID int unique,
	StartDate date,
	CustomerNumber int,
	BranchName nvarchar(30),
	Value int,
	ContractText nvarchar(40),

	primary key (StartDate, CustomerNumber, BranchName),
)
go

-- relationships
create table Borrow
(
	CustomerNumber int,
	LoanNumber int,
	BorrowDate date,

	primary key (CustomerNumber, LoanNumber),
	Foreign key (CustomerNumber)
	References Customer(Number),
	Foreign key (LoanNumber)
	References Loan(Number)
)
go

create table Deposit
(
	CustomerNumber int,
	AccountNumber int, 
	AccessDate date,

	primary key (CustomerNumber, AccountNumber),
	Foreign key (CustomerNumber)
	References Customer(Number),
	Foreign key (AccountNumber)
	References Account(Number)
)
go

-- multiple value
create table PersonPhone
(
	SSN int,
	Phone int,

	primary key (SSN, Phone),
	Foreign key (SSN)
	References Person(SSN)
)
go

create table CustomerContactAddress
(
	Number int,
	CusAddress nvarchar(40),

	primary key (Number, CusAddress),
	Foreign key (Number)
	References Customer(Number)
)
go



-- create foreign key, avoid unexpected errors

-- for natural foreign keys
alter table dbo.Customer add Foreign key (CusSSN) References dbo.Person(SSN)
alter table dbo.Employee add Foreign key (EmSSN) References dbo.Person(SSN)
alter table dbo.Saving add Foreign key (Number) References dbo.Account(Number)
alter table dbo.Checking add Foreign key (Number) References dbo.Account(Number)
alter table dbo.ContractOfCus add Foreign key (CustomerNumber) References dbo.Customer(Number)
alter table dbo.ContractOfCus add Foreign key (BranchName) References dbo.Branch(Name)
go

-- for relationships

alter table dbo.Branch add Foreign key (ID) References dbo.Employee(ID)
alter table dbo.Employee add Foreign key (BranchName) References dbo.Branch(Name)
alter table dbo.Employee add Foreign key (SupervisorID) References dbo.Employee(ID)
alter table dbo.Customer add Foreign key (EmployeeID) References dbo.Employee(ID)
alter table dbo.Payment add Foreign key (LoanNumber) References dbo.Loan(Number)
alter table dbo.Loan add Foreign key (BranchName) References dbo.Branch(Name)
alter table dbo.Account add Foreign key (BranchName) References dbo.Branch(Name)
alter table dbo.Account add Foreign key (ContractID) References dbo.ContractOfCus(ContractID)
go
