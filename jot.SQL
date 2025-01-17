create or alter function fn_AOC_2024_Day11_WorkStones(@Stones varchar(max)) returns table
as
return 

with i as
(select isnull(Val1, Val2) Val, count(*)*cnt cnt
from string_split(@Stones, ',') r
    cross apply (select parsename(r.[value], 2) sVal, cast(parsename(r.[value], 1) as bigint) Cnt) c
    cross apply (select cast(sVal as bigint) Val) s
    cross apply (select len(sVal) lVal) l
    cross apply (select lVal%2 NoSplit) s1
    cross apply (select case when Val = 0 then 1
                            when NoSplit = 1 then Val*2024
                        end Val1
                ) i
    outer apply (select cast(iif([value] = 1, left(sVal, lVal/2), right(sVal, lVal/2)) as bigint) Val2
                    from (select value = 1 union all select 2 ) _
                    where NoSplit = 0
                ) i1
group by isnull(Val1, Val2), cnt
)
, i1 as
(select concat(Val, '.', sum(cnt)) v
from i
group by Val
)
select string_agg(cast(v as varchar(max)), ',') Stones
from i1
GO



declare @Input varchar(max) =
'4022724 951333 0 21633 5857 97 702 6'

drop table if exists #Input
drop table if exists #Final1
drop table if exists #Final2


;with i as
	(select concat(Val, '.', count(*)) v
		from string_split(@Input, ' ' ) r
			cross apply (select cast([value] as bigint) Val) v
		group by Val
	)
	, i1 as
	(select string_agg(cast(v as varchar(max)), ',') Stones
		from i
	) -- select * from i1
	, rec as
	(select Stones, 0 Blinks
	from i1
	union all
	select w.Stones, Blinks + 1 -- putting the aggregation into a function.
	from rec r
		cross apply fn_AOC_2024_Day11_WorkStones(Stones) w
	where r.Blinks < 75
	)
	, f as
	(select top 1 *
		from rec
		order by Blinks desc
	)
select sum(cnt) Answer2
from f
	cross apply string_split(Stones, ',') r
    cross apply string_split(r.value, '.') d
	cross apply (select cast(d.[value] as bigint) Cnt) c





select * from Employees

; with cte as 
(
select 
j= (select * from Employees for json path, WITHOUT_ARRAY_WRAPPER) 
)
select JSON_query(j , '$.employee_name') AS employee_name from cte 
 




;WITH cte AS (
    SELECT 
        j = (SELECT * FROM Employees FOR JSON PATH) 
)
SELECT 
    JSON_VALUE(value, '$.employee_name') AS employee_name
FROM 
    cte
CROSS APPLY 
    OPENJSON(j);



; with cte as 
(select 1 id 
union ALL
select c2.id +1 from cte, cte c2
)
select * from cte 