with recursive aoc16_input(i) as (select '
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'),
lines(y,line) as (
   select 0, substr(i,1,position(E'\n' in i)-1), substr(i,position(E'\n' in i)+1)
   from aoc16_input
   union all
   select y+1,substr(r,1,position(E'\n' in r)-1), substr(r,position(E'\n' in r)+1)
   from lines l(y,l,r) where position(E'\n' in r)>0
),
field(x,y,v) as (
   select x::smallint,y::smallint,substr(line,x::integer,1)
   from (select * from lines l where line<>'') s, lateral generate_series(1,length(line)) g(x)
),
walls(x,y) as (select x,y from field where v='#'),
startpos(x,y) as (select x,y from field where v='S' limit 1),
endpos(x,y) as (select x,y from field where v='E' limit 1),
directions(d,dx,dy) as (values(0,1::smallint,0::smallint),(1,0::smallint,1::smallint),(2,-1::smallint,0::smallint),(3,0,-1::smallint)),
turns(td,tc) as (values(0,0),(1,1000),(2,2000),(3,1000)),
part1steps(r,x,y,d,c) as (
   select 0,x,y,0,0 from startpos
   union all (
   with tmp(r,x,y,d,c) as (select * from part1steps),
      agg(r,x,y,d,c) as (select r,x,y,d,min(c) from (
         select r,x,y,(d+td)%4 as d,c+tc as c from tmp cross join turns
         ) s group by r,x,y,d)
      select r+1,(x+dx)::smallint,(y+dy)::smallint,d,c+1
      from agg a natural join directions where not exists(select * from walls w where a.x+dx=w.x and a.y+dy=w.y)
      and r<(select count(*) from field)
   )),
part1(x,y,d,c) as (select x,y,d,min(c) from (select x,y,(d+td)%4 as d, (c+tc) as c from part1steps cross join turns) group by x,y,d),
best1(c) as (select min(c) from part1 natural join endpos)


