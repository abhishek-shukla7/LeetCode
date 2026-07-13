# Write your MySQL query statement below
select firstName,lastName,city,state from Person p1
left join Address A
on p1.personId=A.personId
