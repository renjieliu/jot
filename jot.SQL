; with cte as 
(select col = '#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####')
, cte2 as (
select col = replace(replace(col, char(10), ''), char(13), '|') from cte
), cte3 as (
select id = ROW_NUMBER() over(order by split.ordinal),  split.lines from cte2 cross apply 
    (select ordinal, lines = [value] from string_split_RL(col, '|', 1)) split  
 where split.lines != ''
) 
select 
grp = (id-1) / 7 
, ln = (id-1) % 7 + 1 
, lines
 from cte3



-- does 201, 200, E exist? 
-- (score, nxt_r, nxt_c, nd)

-- score,nxt_r,nxt_c,nd|
-- 1000,(1,2),100|2000,(3,4),500
-- if exists --r = 1, c = 2 
-- update it to 1001
-- and return

-- go



-- create or alter function testing_exists(@score varchar(max)
-- 								, @r int
-- 								, @c int
-- 								, @dir int 
-- 								-- , @concat varchar(max)
-- 								)
-- returns table as return

--  with base as 
-- (select input = replace(
-- 						TRANSLATE(@score, '()', '``' )
-- 						, '`'
-- 						, ''
-- 						)
-- ), cte as (
-- select 
-- group_number = main_group.ordinal
-- , content =  main_group.VALUE
-- , score = case when sub.ordinal = 1 then sub.[value] else null end
-- , r = case when sub.ordinal = 2 then sub.[value] else null end
-- , c = case when sub.ordinal = 3 then sub.[value] else null end
-- , dir = case when sub.ordinal = 4 then sub.[value] else null end
-- from base 
-- cross APPLY (select * from string_split_rl(input, '|', 1)) main_group
-- cross apply (select * from string_split_rl(main_group.value, ',', 1)) sub
-- ) , brk as (
-- select
--  group_number, content 
-- , score = max(score)
-- , r = max(r)
-- , c= max(c)
-- , dir = max(dir)
--  from cte 
-- group by group_number, content 
-- )
-- select * from brk 
-- where r = @r and c = @c and dir = @dir 

-- go


-- select * from testing_exists( '1000,(201,200),100' +  REPLICATE( cast( '|2000,(300,400),500' as varchar(max)) , 100 ) 
-- 							, 201
-- 							, 200
-- 							, 100
-- 							)
-- option (maxrecursion 0)


-- go


-- select
-- group_ID = main.ordinal
-- , subgroup_Id = case when sub.ordinal = 1 then 'score'
-- 				     when sub.ordinal = 2 then 'r'
-- 					 when sub.ordinal = 3 then 'c'
-- 				end
-- , sub.[value]
--  from string_split_RL('(100,100,300)|(100,200,300)|(101,201,301)', '|', 1) main
-- cross APPLY
--  (select * from string_split_RL(SUBSTRING( [value], 2 , len([value])-2 ), ',', 1)) sub

--score/(nxt_r, nxt_c)/face/curr_r/curr_c|
--1000/(201, 200)/E/(201, 400)|1000/(201, 200)/E/(2001, 4000)

-- does 201, 200, E exist? 
-- (score, nxt_r, nxt_c, nd)

-- score,nxt_r,nxt_c,nd|
-- 1000,(1,2),100|2000,(3,4),500
-- if exists --r = 1, c = 2 
-- update it to 1001
-- and return








-- declare @totalscore bigint, @r int, @c int, @stk varchar(max)


-- ; with cte as (
-- select
-- group_ID = main.ordinal
-- , score = case when sub.ordinal = 1 then sub.[value] else null end 
-- , r =  case when sub.ordinal = 2 then sub.[value] else null end 
-- , c =  case when sub.ordinal = 3 then sub.[value] else null end 
--  from string_split_RL('(100,200,300)|(101,201,301)', '|', 1) main
-- cross APPLY 
--  (select * from string_split_RL(SUBSTRING( [value], 2 , len([value])-2 ), ',', 1)) sub
-- )
-- select 
-- rnk = DENSE_RANK() over (partition by group_ID order by max(score) desc)
-- , group_ID
-- , score = max(score)
-- , r = max(r)
-- , c= max(c)
--  from cte 
-- group by group_ID 







-- go 

-- create or alter function fn_AOC_2024_Day11_WorkStones(@Stones varchar(max)) returns table
-- as
-- return 

-- with i as
-- (select isnull(Val1, Val2) Val, count(*)*cnt cnt
-- from string_split(@Stones, ',') r
--     cross apply (select parsename(r.[value], 2) sVal, cast(parsename(r.[value], 1) as bigint) Cnt) c
--     cross apply (select cast(sVal as bigint) Val) s
--     cross apply (select len(sVal) lVal) l
--     cross apply (select lVal%2 NoSplit) s1
--     cross apply (select case when Val = 0 then 1
--                             when NoSplit = 1 then Val*2024
--                         end Val1
--                 ) i
--     outer apply (select cast(iif([value] = 1, left(sVal, lVal/2), right(sVal, lVal/2)) as bigint) Val2
--                     from (select value = 1 union all select 2 ) _
--                     where NoSplit = 0
--                 ) i1
-- group by isnull(Val1, Val2), cnt
-- )
-- , i1 as
-- (select concat(Val, '.', sum(cnt)) v
-- from i
-- group by Val
-- )
-- select string_agg(cast(v as varchar(max)), ',') Stones
-- from i1
-- GO




-- declare @Input varchar(max) =
-- '4022724 951333 0 21633 5857 97 702 6'

-- drop table if exists #Input
-- drop table if exists #Final1
-- drop table if exists #Final2


-- ;with i as
-- 	(select concat(Val, '.', count(*)) v
-- 		from string_split(@Input, ' ' ) r
-- 			cross apply (select cast([value] as bigint) Val) v
-- 		group by Val
-- 	)
-- 	, i1 as
-- 	(select string_agg(cast(v as varchar(max)), ',') Stones
-- 		from i
-- 	) -- select * from i1
-- 	, rec as
-- 	(select Stones, 0 Blinks
-- 	from i1
-- 	union all
-- 	select w.Stones, Blinks + 1 -- putting the aggregation into a function.
-- 	from rec r
-- 		cross apply fn_AOC_2024_Day11_WorkStones(Stones) w
-- 	where r.Blinks < 75
-- 	)
-- 	, f as
-- 	(select top 1 *
-- 		from rec
-- 		order by Blinks desc
-- 	)
-- select sum(cnt) Answer2
-- from f
-- 	cross apply string_split(Stones, ',') r
--     cross apply string_split(r.value, '.') d
-- 	cross apply (select cast(d.[value] as bigint) Cnt) c





-- select * from Employees

-- ; with cte as 
-- (
-- select 
-- j= (select * from Employees for json path, WITHOUT_ARRAY_WRAPPER) 
-- )
-- select JSON_query(j , '$.employee_name') AS employee_name from cte 
 




-- ;WITH cte AS (
--     SELECT 
--         j = (SELECT * FROM Employees FOR JSON PATH) 
-- )
-- SELECT 
--     JSON_VALUE(value, '$.employee_name') AS employee_name
-- FROM 
--     cte
-- CROSS APPLY 
--     OPENJSON(j);



-- ; with cte as 
-- (select 1 id 
-- union ALL
-- select c2.id +1 from cte, cte c2
-- )
-- select * from cte 



-- go 



-- drop table if exists #t

-- ;
-- with base as 
-- (select 
-- id= 1
-- ,col = REPLICATE(cast('a' as varchar(max)), 100000)  
-- )
-- , cte as 
-- (select 
-- id = 1
-- , curr = left (col, 1)
-- , rem = right(col, len(col) - 1)
-- from base 
-- union all 
-- select 
-- id + 1 
-- , curr = left(rem, 1)
-- , rem = right(rem, len(rem) - 1) 
-- from cte
-- where len(rem) > 0
-- )
-- , swap as 
-- (select id = cast(id as varchar(max))
-- 	, curr = cast(curr as varchar(max))
-- from cte where id not in (999, 1000)
--  union all 
--  select 1000 id, curr from cte where id = 999 
--  union all 
--  select 999 id, curr from cte where id = 1000
-- )  -- select len(col)  from base
--  select x = string_agg(concat(id, ',', curr), '|') 
--  within group (order by id)  into #t from swap
--  option (maxrecursion  0)



-- select len(x) from #t





