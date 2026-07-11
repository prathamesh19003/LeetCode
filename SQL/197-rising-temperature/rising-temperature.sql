/* Write your PL/SQL query statement below */
select today.id from weather today
cross join weather prev_day
where today.recordDate-prev_day.recordDate=1
and today.temperature>prev_day.temperature;