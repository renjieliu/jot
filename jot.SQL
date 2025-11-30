select STUFF('hello world', 2, 0, '__insert___') ; 


 

/*
-- create or alter function heappop(@heapString varchar(max))
-- -- stk: score.node|
-- -- 120.A|200.B|300.C
-- -- pop -- > and push back 
-- -- adding 400.D to the stack 
*/

-- ---- heappop 
-- -- parameter: heapString
-- -- return string: lowest nodeX.cost
-- returns table as return 
-- with base as 
-- (
--     select input = @heapString
-- )
-- , to_pop as (
-- select top 1 
-- score = PARSENAME(cra.grp,2)
-- , node = PARSENAME(cra.grp, 1)
--  from base
--     cross apply (select grp = [value] from string_split([input], '|')) cra
-- order by score, node 
-- ) 
-- select top_stk =  score + '.' + node from to_pop 

-- go 



-- create or alter function heappush (@heapString varchar(max), @newNodeCost varchar(max))
-- --- heappush -- 500.D 
-- -- parameter: heapString, new nodeX.Cost
-- -- return: heapString after concatenation
-- returns table as return 
-- with base as 
-- (
--     select input =@heapString 
-- )
-- select res = CONCAT_WS('|', input, @newNodeCost) from base

-- go


-- -- Costs - this is a hashmap, to store the lowest cost for current node 

-- -- the heap is used to get the lowest cost for all the nodes, and iterate for all the nodes connecting to it


-- -- for each node, initiate like 'node1.cost|node2.cost'

-- -- get from costs, check if current node cost is < nodex.cost


-- -- getFromSet 
-- -- parameter: setString, nodeX
-- -- return nodeX.cost

-- go 


-- create or alter  FUNCTION initialize_hashmap(@nodeString varchar(max), @val bigint)
-- -- 'A,B,C,D,E'
-- -- initialize the hashmap
-- -- param: nodes (A,B,C,D,E), val
-- -- return hashmap |A.val|B.val... 

-- returns table as return 

-- with base as 
-- (select nodes = @nodeString ) -- union all select 'B' union all select 'C' )
-- select hashmap = '|' + STRING_AGG( concat_ws('.', node, @val), '|') 
-- from base 
--     cross apply (select node = [value] from string_split(nodes, ',' ) ) cra
 

-- go 



-- go 

-- create or alter function getNodeVal(@hashmap varchar(max), @node varchar(max))
-- -- Get cost from the string
-- -- get the cost of B
-- -- parameter: nodeX (|node.) , hashmap
-- -- return: cost
-- returns table as return 
-- with cte as 
-- (select rem = right(@hashmap, len(@hashmap) - CHARINDEX(@node, @hashmap)))
-- select cost = SUBSTRING(@hashmap
--                 , CHARINDEX('@node.', @hashmap) + datalength(@node)  -- from this location
--                 , CHARINDEX('|', rem) - datalength(@node)
--                 )   
-- from cte


-- go


 

-- create or alter function updateCost (@hashmap varchar(max), @node varchar(max), @cost bigint)
-- -- update the cost for NodeX in the hashmap string 
-- -- parameater: hashmap, NodeX, cost
-- -- return hashmap string after update
-- -- Eg. update B to 65121
-- returns table as return
-- with cte as (
-- select 
-- node = PARSENAME([value], 2)
-- , val = PARSENAME([value], 1)
-- from string_split(@hashmap, '|') _
-- where [value] != ''
-- ), updates as (
-- select 
-- node
-- , val
-- from cte 
-- where node != @node
-- union 
-- select 
-- @node
-- , @cost
-- ) 
-- select 
-- hashmap = '|' + string_agg(CONCAT_WS('.', node, val), '|') within group (order by node)
-- from updates

-- go 


-- drop table if exists #input

-- SELECT 'A' AS Node1, 'B' AS Node2, 2 AS Cost
-- into #input
-- UNION
-- SELECT 'A' AS Node1, 'C' AS Node2, 6 AS Cost
-- UNION
-- SELECT 'B' AS Node1, 'D' AS Node2, 5 AS Cost
-- UNION
-- SELECT 'C' AS Node1, 'D' AS Node2, 8 AS Cost
-- UNION
-- SELECT 'C' AS Node1, 'E' AS Node2, 2 AS Cost
-- UNION
-- SELECT 'D' AS Node1, 'F' AS Node2, 10 AS Cost
-- UNION
-- SELECT 'D' AS Node1, 'G' AS Node2, 15 AS Cost
-- UNION
-- SELECT 'G' AS Node1, 'F' AS Node2, 6 AS Cost
-- UNION
-- SELECT 'G' AS Node1, 'H' AS Node2, 6 AS Cost
-- UNION
-- SELECT 'F' AS Node1, 'H' AS Node2, 2 AS Cost
-- UNION
-- SELECT 'E' AS Node1, 'F' AS Node2, 20 AS Cost


-- select 
-- id = 1 
-- , currNode = 'A'
-- , hashmap  = (select start_node.hashmap
--                 from
--                 (
--                     select nodes = STRING_AGG(node, ',') within group(order by node) from 
--                     (
--                         select node =  Node1 from #input
--                         union  
--                         select node2 
--                         from #input
--                     )  _ 
--                 ) n 
--                 cross apply (select hashmap from initialize_hashmap(nodes, 99999)) ini
--                 cross apply (select hashmap from updateCost(hashmap, 'A', 0)) start_node
--             )






-- -- updateCost
-- -- getNodeVal
-- -- initialize_hashmap
-- -- heappush
-- -- heappop






-- -- insert into #input 
-- -- select node2, node1, cost from #input


-- -- select * from #input order by 1 

-- -- ; with cte as 
-- -- (
-- --     select
-- --      red = cast('A' as varchar(max) ) 
-- --     , to_reach = cast('A' as varchar(max) ) 
-- --     , cost = 0
-- --     , seen =  cast('A' as varchar(max)) 

-- --     union all 
    
-- --    select 
-- --     red_candidate = cast(nxt.Node1 as varchar(max)) -- this node can reach the previous red 
-- --     , to_reach = cast(nxt.Node2 as varchar(max) ) -- what marked as red, will be the next one to reach
-- --     , cost = c.cost + nxt.Cost
-- --     , seen = cast(seen + nxt.Node2 as varchar(max) ) 
 
-- --     from cte c inner join #input nxt 
-- --     on  nxt.Node1 = c.to_reach
-- --     where CHARINDEX(nxt.Node2, seen) = 0

-- -- )
-- -- select * from cte
-- -- order by to_reach

-- -- select * from #input


--  -- from prev node N to curre C , it's cost C 


-- -- rollback 
-- -- DECLARE @Graph NVARCHAR(MAX)= '
-- -- SELECT ''A'' AS Node1, ''B'' AS Node2, 2 AS Cost
-- -- UNION
-- -- SELECT ''A'' AS Node1, ''C'' AS Node2, 6 AS Cost
-- -- UNION
-- -- SELECT ''B'' AS Node1, ''D'' AS Node2, 5 AS Cost
-- -- UNION
-- -- SELECT ''C'' AS Node1, ''D'' AS Node2, 8 AS Cost
-- -- UNION
-- -- SELECT ''C'' AS Node1, ''E'' AS Node2, 2 AS Cost
-- -- UNION
-- -- SELECT ''D'' AS Node1, ''F'' AS Node2, 10 AS Cost
-- -- UNION
-- -- SELECT ''D'' AS Node1, ''G'' AS Node2, 15 AS Cost
-- -- UNION
-- -- SELECT ''G'' AS Node1, ''F'' AS Node2, 6 AS Cost
-- -- UNION
-- -- SELECT ''G'' AS Node1, ''H'' AS Node2, 6 AS Cost
-- -- UNION
-- -- SELECT ''F'' AS Node1, ''H'' AS Node2, 2 AS Cost
-- -- UNION
-- -- SELECT ''E'' AS Node1, ''F'' AS Node2, 20 AS Cost
-- -- '
-- -- DECLARE @Source VARCHAR(128) = 'A'-- You may put any node here for @Source
-- -- DECLARE @Target VARCHAR(128) = 'H'-- You may put any node here for @Target
-- -- -- Declarations
-- -- DECLARE @ROW_COUNT INT
-- -- DECLARE @Cost VARCHAR(16)
-- -- DECLARE @Path VARCHAR(MAX)
-- -- DECLARE @Node VARCHAR(128)
-- -- --  Drop table #Graph
-- -- IF OBJECT_ID(N'tempdb..#Graph') IS NOT NULL DROP TABLE #Graph
-- -- --  Create table #Graph
-- -- CREATE TABLE #Graph (
-- -- Node1 VARCHAR(128)
-- -- ,Node2 VARCHAR(128)
-- -- ,Cost INT 
-- -- );
-- -- -- Populate table #Graph
-- -- INSERT INTO #Graph EXEC dbo.sp_executeSQL @Graph
-- -- -- Drop table #RED
-- -- IF OBJECT_ID(N'tempdb..#RED') IS NOT NULL DROP TABLE #RED
-- -- --  Create table #RED
-- -- CREATE TABLE #RED (
-- -- step int 
-- -- , [prev] VARCHAR(128)
-- -- ,[Next] VARCHAR(128)
-- -- ,Cost INT 
-- -- );



-- -- -- Initialize table #RED with @Source
-- -- INSERT INTO #RED SELECT step = 0, @Source AS [prev], @Source AS [Next], 0 AS Cost 
-- -- -- Populate table #RED according to induction argument
-- -- SET @ROW_COUNT = -1
-- -- WHILE @ROW_COUNT <> 0
-- -- BEGIN
-- -- INSERT INTO #RED
-- -- SELECT TOP 1
-- -- step
-- -- , d.[prev]
-- --  , d.nxt
-- --  , d.Cost FROM-- Select top row from query
-- -- (
-- -- SELECT 
-- -- step = red.step + 1
-- -- , prev = Graph.Node2  
-- -- , nxt = RED.[prev]  
-- -- , cost = Graph.Cost + RED.Cost 
-- -- FROM #Graph Graph 
-- --      INNER JOIN #RED RED ON Graph.Node1 = RED.[prev]
-- --  WHERE Graph.Node2 NOT IN (SELECT [prev] FROM #RED)
-- -- ) d
-- -- ORDER BY d.Cost ASC-- Pick closest neighbor to @Source
-- -- SET @ROW_COUNT = @@ROWCOUNT
-- -- END

-- -- select * from #red
-- -- --
-- -- -- Display answer 
-- -- --
-- -- -- Get cost of minimal path from @Target to @Source
-- -- SELECT @Cost = Cost FROM #RED WHERE [prev] = @Target  -- @Target may not belong to #RED 
-- -- IF @Cost IS NOT NULL  -- @Target belongs to #RED  
-- -- BEGIN
-- -- -- Build minimal path from @Source to @Target 
-- -- SET @Path = @Target
-- -- SET @Node = @Target
-- -- WHILE @Node <> @Source -- Loop through nodes from @Target to @Source using Next column in #RED
-- -- BEGIN
-- -- SELECT @Node = [Next] FROM #RED WHERE [Node] = @Node-- Get Next node for current node
-- -- SET @Path = @Node + ' --> ' + @Path-- Append to path
-- -- END
-- -- -- Display minimal path from @Source to @Target
-- -- SELECT @Cost AS Cost, @Path AS Path
-- -- -- Display all minimal paths
-- -- SELECT * FROM #RED
-- -- END
-- -- ELSE
-- -- SELECT -1 AS Cost, '@Source and @Path are not connected' AS Path


-- -- does 201, 200, E exist? 
-- -- (score, nxt_r, nxt_c, nd)

-- -- score,nxt_r,nxt_c,nd|
-- -- 1000,(1,2),100|2000,(3,4),500
-- -- if exists --r = 1, c = 2 
-- -- update it to 1001
-- -- and return

-- -- go



-- -- create or alter function testing_exists(@score varchar(max)
-- -- 								, @r int
-- -- 								, @c int
-- -- 								, @dir int 
-- -- 								-- , @concat varchar(max)
-- -- 								)
-- -- returns table as return

-- --  with base as 
-- -- (select input = replace(
-- -- 						TRANSLATE(@score, '()', '``' )
-- -- 						, '`'
-- -- 						, ''
-- -- 						)
-- -- ), cte as (
-- -- select 
-- -- group_number = main_group.ordinal
-- -- , content =  main_group.VALUE
-- -- , score = case when sub.ordinal = 1 then sub.[value] else null end
-- -- , r = case when sub.ordinal = 2 then sub.[value] else null end
-- -- , c = case when sub.ordinal = 3 then sub.[value] else null end
-- -- , dir = case when sub.ordinal = 4 then sub.[value] else null end
-- -- from base 
-- -- cross APPLY (select * from string_split_rl(input, '|', 1)) main_group
-- -- cross apply (select * from string_split_rl(main_group.value, ',', 1)) sub
-- -- ) , brk as (
-- -- select
-- --  group_number, content 
-- -- , score = max(score)
-- -- , r = max(r)
-- -- , c= max(c)
-- -- , dir = max(dir)
-- --  from cte 
-- -- group by group_number, content 
-- -- )
-- -- select * from brk 
-- -- where r = @r and c = @c and dir = @dir 

-- -- go


-- -- select * from testing_exists( '1000,(201,200),100' +  REPLICATE( cast( '|2000,(300,400),500' as varchar(max)) , 100 ) 
-- -- 							, 201
-- -- 							, 200
-- -- 							, 100
-- -- 							)
-- -- option (maxrecursion 0)


-- -- go


-- -- select
-- -- group_ID = main.ordinal
-- -- , subgroup_Id = case when sub.ordinal = 1 then 'score'
-- -- 				     when sub.ordinal = 2 then 'r'
-- -- 					 when sub.ordinal = 3 then 'c'
-- -- 				end
-- -- , sub.[value]
-- --  from string_split_RL('(100,100,300)|(100,200,300)|(101,201,301)', '|', 1) main
-- -- cross APPLY
-- --  (select * from string_split_RL(SUBSTRING( [value], 2 , len([value])-2 ), ',', 1)) sub

-- --score/(nxt_r, nxt_c)/face/curr_r/curr_c|
-- --1000/(201, 200)/E/(201, 400)|1000/(201, 200)/E/(2001, 4000)

-- -- does 201, 200, E exist? 
-- -- (score, nxt_r, nxt_c, nd)

-- -- score,nxt_r,nxt_c,nd|
-- -- 1000,(1,2),100|2000,(3,4),500
-- -- if exists --r = 1, c = 2 
-- -- update it to 1001
-- -- and return








-- -- declare @totalscore bigint, @r int, @c int, @stk varchar(max)


-- -- ; with cte as (
-- -- select
-- -- group_ID = main.ordinal
-- -- , score = case when sub.ordinal = 1 then sub.[value] else null end 
-- -- , r =  case when sub.ordinal = 2 then sub.[value] else null end 
-- -- , c =  case when sub.ordinal = 3 then sub.[value] else null end 
-- --  from string_split_RL('(100,200,300)|(101,201,301)', '|', 1) main
-- -- cross APPLY 
-- --  (select * from string_split_RL(SUBSTRING( [value], 2 , len([value])-2 ), ',', 1)) sub
-- -- )
-- -- select 
-- -- rnk = DENSE_RANK() over (partition by group_ID order by max(score) desc)
-- -- , group_ID
-- -- , score = max(score)
-- -- , r = max(r)
-- -- , c= max(c)
-- --  from cte 
-- -- group by group_ID 







-- -- go 

-- -- create or alter function fn_AOC_2024_Day11_WorkStones(@Stones varchar(max)) returns table
-- -- as
-- -- return 

-- -- with i as
-- -- (select isnull(Val1, Val2) Val, count(*)*cnt cnt
-- -- from string_split(@Stones, ',') r
-- --     cross apply (select parsename(r.[value], 2) sVal, cast(parsename(r.[value], 1) as bigint) Cnt) c
-- --     cross apply (select cast(sVal as bigint) Val) s
-- --     cross apply (select len(sVal) lVal) l
-- --     cross apply (select lVal%2 NoSplit) s1
-- --     cross apply (select case when Val = 0 then 1
-- --                             when NoSplit = 1 then Val*2024
-- --                         end Val1
-- --                 ) i
-- --     outer apply (select cast(iif([value] = 1, left(sVal, lVal/2), right(sVal, lVal/2)) as bigint) Val2
-- --                     from (select value = 1 union all select 2 ) _
-- --                     where NoSplit = 0
-- --                 ) i1
-- -- group by isnull(Val1, Val2), cnt
-- -- )
-- -- , i1 as
-- -- (select concat(Val, '.', sum(cnt)) v
-- -- from i
-- -- group by Val
-- -- )
-- -- select string_agg(cast(v as varchar(max)), ',') Stones
-- -- from i1
-- -- GO




-- -- declare @Input varchar(max) =
-- -- '4022724 951333 0 21633 5857 97 702 6'

-- -- drop table if exists #Input
-- -- drop table if exists #Final1
-- -- drop table if exists #Final2


-- -- ;with i as
-- -- 	(select concat(Val, '.', count(*)) v
-- -- 		from string_split(@Input, ' ' ) r
-- -- 			cross apply (select cast([value] as bigint) Val) v
-- -- 		group by Val
-- -- 	)
-- -- 	, i1 as
-- -- 	(select string_agg(cast(v as varchar(max)), ',') Stones
-- -- 		from i
-- -- 	) -- select * from i1
-- -- 	, rec as
-- -- 	(select Stones, 0 Blinks
-- -- 	from i1
-- -- 	union all
-- -- 	select w.Stones, Blinks + 1 -- putting the aggregation into a function.
-- -- 	from rec r
-- -- 		cross apply fn_AOC_2024_Day11_WorkStones(Stones) w
-- -- 	where r.Blinks < 75
-- -- 	)
-- -- 	, f as
-- -- 	(select top 1 *
-- -- 		from rec
-- -- 		order by Blinks desc
-- -- 	)
-- -- select sum(cnt) Answer2
-- -- from f
-- -- 	cross apply string_split(Stones, ',') r
-- --     cross apply string_split(r.value, '.') d
-- -- 	cross apply (select cast(d.[value] as bigint) Cnt) c





-- -- select * from Employees

-- -- ; with cte as 
-- -- (
-- -- select 
-- -- j= (select * from Employees for json path, WITHOUT_ARRAY_WRAPPER) 
-- -- )
-- -- select JSON_query(j , '$.employee_name') AS employee_name from cte 
 




-- -- ;WITH cte AS (
-- --     SELECT 
-- --         j = (SELECT * FROM Employees FOR JSON PATH) 
-- -- )
-- -- SELECT 
-- --     JSON_VALUE(value, '$.employee_name') AS employee_name
-- -- FROM 
-- --     cte
-- -- CROSS APPLY 
-- --     OPENJSON(j);



-- -- ; with cte as 
-- -- (select 1 id 
-- -- union ALL
-- -- select c2.id +1 from cte, cte c2
-- -- )
-- -- select * from cte 



-- -- go 



-- -- drop table if exists #t

-- -- ;
-- -- with base as 
-- -- (select 
-- -- id= 1
-- -- ,col = REPLICATE(cast('a' as varchar(max)), 100000)  
-- -- )
-- -- , cte as 
-- -- (select 
-- -- id = 1
-- -- , curr = left (col, 1)
-- -- , rem = right(col, len(col) - 1)
-- -- from base 
-- -- union all 
-- -- select 
-- -- id + 1 
-- -- , curr = left(rem, 1)
-- -- , rem = right(rem, len(rem) - 1) 
-- -- from cte
-- -- where len(rem) > 0
-- -- )
-- -- , swap as 
-- -- (select id = cast(id as varchar(max))
-- -- 	, curr = cast(curr as varchar(max))
-- -- from cte where id not in (999, 1000)
-- --  union all 
-- --  select 1000 id, curr from cte where id = 999 
-- --  union all 
-- --  select 999 id, curr from cte where id = 1000
-- -- )  -- select len(col)  from base
-- --  select x = string_agg(concat(id, ',', curr), '|') 
-- --  within group (order by id)  into #t from swap
-- --  option (maxrecursion  0)



-- -- select len(x) from #t





-- select * from information_schema.tables 
-- order by 3 


-- select * from webTracker
-- order by record_insert_date desc 


-- update webTracker set visit_from = 'UN_Laptop'
-- where record_insert_date = '2025-09-30 15:26:23.0000000'
 

 

-- select domain, sum(visit_length) / 86400.0
-- from webTracker
-- where visit_from = 'UN_Laptop'
-- group by domain 
-- order by 2 desc 


