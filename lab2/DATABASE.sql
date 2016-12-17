use lab2db;

drop table if exists credit;
drop table if exists client_tab;
drop table if exists time_tab;
drop table if exists bank_tab;

create table client_tab (client_id int primary key auto_increment,
					     client_name varchar(30), age int, is_working boolean);
                     
create table time_tab (time_id int primary key auto_increment,
				       start_date date, end_date date);
                       
create table bank_tab (bank_id int primary key auto_increment,
					   bank_name varchar(30), is_solvent boolean);
          
create table credit (credit_id int primary key auto_increment,
					 client_id int, time_id int, bank_id int,
					 summa decimal(6, 2), percentage decimal(3,1),
					 currency varchar(3), 
					 foreign key (client_id) references client_tab(client_id), 
                     foreign key (time_id) references time_tab(time_id),
                     foreign key (bank_id) references bank_tab(bank_id));
                     
select * from client_tab;
