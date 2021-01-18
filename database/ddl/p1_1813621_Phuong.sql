create database SHIP_TRACKING
go

use SHIP_TRACKING
go

create table Country
(
	Code int not null,
	Name nvarchar(20) not null,
	Continent nvarchar(20),

	primary key (Name)
)
go

create table Ocean 
(
	Name nvarchar(30) primary key,
	GeographicFeature nvarchar(20),
	MeteorologicalFeature nvarchar(20)
)
go

create table Ship_Type
(
	ShipType nvarchar(10) primary key,
	Tonnage int,
	Hull nvarchar(10)
)
go

create table Ship
(
	Sname nvarchar(20) primary key,
	ShipType nvarchar(10) not null,
	OwnerID int not null,
	RegDate date,
	CaptainSSN int not null,
	CountryName nvarchar(20),
	Pname nvarchar(20),
)
go

create table Worker
(
	SSN int primary key,
	DOB date,
	Nationality nvarchar(20),
	Salary int,
	Sname nvarchar(20),
	WorkDate date,
)
go

create table Sailor
(
	SSN int primary key,
	Experience nvarchar(20),
	Height int,
	Weight int,
)
go

create table SupportingWorker
(
	SSN int primary key,
	Expertise nvarchar(20),
)
go

create table Owner
(
	OwnerID int primary key
)
go

create table Person
(
	SSN int primary key,
	LastName nvarchar(10),
	FirstName nvarchar(10),
	PersonAddress nvarchar(30),
	Phone int,
	OwnerID int,
)
go

create table Orgnization
(
	ID int primary key,
	Name nvarchar(20),
	OrgAddress nvarchar(30),
	Phone int,
	OwnerID int,
)
go

create table Port 
(
	CountryName nvarchar(20) not null,
	Pname nvarchar(20) not null,
	OceanName nvarchar(30) not null,

	primary key (CountryName, Pname),
)
go

create table Port_Visit
(
	Sname nvarchar(20),
	CountryName nvarchar(20),
	Pname nvarchar(20),
	StartDate date,
	EndDate date,
)
go

create table Ship_Movement
(
	Sname nvarchar(20) not null,
	DateVisit date not null,
	TimeVisit date not null,
	Latitude int,
	Longitude int,

	primary key (Sname, DateVisit, TimeVisit),
)
go

-- foreign keys
-- alter table dbo. add foreign key () references dbo.()

alter table dbo.Sailor add foreign key (SSN) references dbo.Worker(SSN)
alter table dbo.SupportingWorker add foreign key (SSN) references dbo.Worker(SSN)
alter table dbo.Person add foreign key (OwnerID) references dbo.Owner(OwnerID)
alter table dbo.Orgnization add foreign key (OwnerID) references dbo.Owner(OwnerID)
alter table dbo.Port add foreign key (CountryName) references dbo.Country(Name)
alter table dbo.Port_Visit add foreign key (Sname) references dbo.Ship(Sname)
alter table dbo.Port_Visit add foreign key (CountryName, Pname) references dbo.Port(CountryName, Pname)
alter table dbo.Ship_Movement add foreign key (Sname) references dbo.Ship(Sname)

alter table dbo.Ship add foreign key (ShipType) references dbo.Ship_Type(ShipType)
alter table dbo.Ship add foreign key (OwnerID) references dbo.Owner(OwnerID)
alter table dbo.Ship add foreign key (CaptainSSN) references dbo.Sailor(SSN)
alter table dbo.Ship add foreign key (CountryName, Pname) references dbo.Port(CountryName, Pname)
alter table dbo.Worker add foreign key (Sname) references dbo.Ship(Sname)
alter table dbo.Port add foreign key (OceanName) references dbo.Ocean(Name)