
; with fib AS(
 select n = 2, A= cast( 1 as decimal(38, 0) ), B = cast( 1 as decimal(38, 0) )
 union all 
 select n + 1, A = B, B = A + B from fib 
 where n < 100
)
select B from fib  
where n = 10





select ROW_NUMBER() over(order by (select NULL)),  * from STRING_SPLIT('a c d',  ' ') 


