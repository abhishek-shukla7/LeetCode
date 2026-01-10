# Write your MySQL query statement below
select id as Id from 
(
    select id,temperature,recordDate,
    lag(temperature)over(order by recordDate)as pre_temp,
    lag(recordDate)over(order by recordDate)as pre_date
    from Weather
)t
where temperature>pre_temp
and recordDate=Date_ADD(pre_date,interval 1 Day)