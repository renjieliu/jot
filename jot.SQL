
; with fib AS(
 select n = 2, A= cast( 1 as decimal(38, 0) ), B = cast( 1 as decimal(38, 0) )
 union all 
 select n + 1, A = B, B = A + B from fib 
 where n < 100
)
select B from fib  
where n = 10



-- STRING_SPLIT -- the result row order is Not guaranteed to match the substring in the input string.

select * from STRING_SPLIT('a|c|d',  '|' )

