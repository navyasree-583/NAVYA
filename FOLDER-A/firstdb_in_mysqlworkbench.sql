

# use firstdb;
# select abs(-22);
select sqrt(144);
select power(10,3);
select least(1,2,3,45,0);
select greatest(2,34,22,67);
select round(999.99);
select truncate(123.456,2);

create table students1(
std_id int, 
std_name varchar(20),age int);
insert into students1 values(1,"abhi",22),(2,"akash",24);
select * from students1;
delete from  students1 where age =24;

select upper("Jaipur") as upper_case;

select lower("Jaipur") as lower_case;
select std_name, char_length(std_name) as length
from students1;
select concat("India", " is"," beautiful");
select replace("Tomato is a vegetable" , "vegetable","fruit");
select reverse(std_name) from students1;
select length("     India   ");
# ltrim rtrim trim
select length(rtrim("     India   "));
select position("fruit" in "orange is a fruit") as position;

select ascii('Z');

use firstdb;
select s1.name , s2.location from studentss as s1 inner join student_info as s2 on s1.id = s2.id where( s2.location = "Delhi" or s2.location = "banglore");
