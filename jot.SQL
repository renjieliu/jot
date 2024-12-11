
; with fib AS(
 select n = 2, A= cast( 1 as decimal(38, 0) ), B = cast( 1 as decimal(38, 0) )
 union all 
 select n + 1, A = B, B = A + B from fib 
 where n < 100
)
select B from fib  
where n = 10





select ROW_NUMBER() over(order by (select NULL)),  * from STRING_SPLIT('a c d',  ' ') 





go 


; 

create function u_split_string(
    @input varchar(max)
    , @delimiter char(1)
)
returns table as return 

with cte as (
    select 
    id = 1 
    , curr = left(@input, CHARINDEX(@delimiter, @input)-1)  
    , rem = right(@input, len(@input)-CHARINDEX(@delimiter, @input)) 
    where CHARINDEX (@delimiter, @input) != 0	
    union all 
    select 
    id + 1
    , curr = left(rem, CHARINDEX(@delimiter, rem)-1)
    , right(rem, len(rem)-CHARINDEX(@delimiter, rem)) 
    from cte
    where CHARINDEX(@delimiter, rem) != 0 
)
select id, curr, rem from cte 
where curr != ''
union all 
select id+1, rem, '' from cte
where id = (select max(id) from cte)
and rem != ''
union all 
select id = -1
, @input
, ''
where CHARINDEX (@delimiter, @input) = 0 	



select * from dbo.u_split_string('1.2.3.4.5', '.')
option (maxrecursion 100 )

go 


