use crime_sort;
select * from crime_sort;

select  Primary_Type, count(Primary_Type) as cases from crime_sort  
group by Primary_Type order by cases desc;

select  IF(Arrest = 1, 'TRUE', 'FALSE') as status, count(Arrest)  
from crime_sort group by status;


select  Primary_Type, IF(Arrest = 1, 'TRUE', 'FALSE') as status, count(Arrest)  
from crime_sort group by status having Primary_Type ="THEFT" ;


#------- bien
select Primary_Type, count(Arrest) as not_resolved
from crime_sort WHERE  Arrest = " FALSE" group by Primary_Type order by not_resolved desc;

select Primary_Type, count(Arrest) as resolved
from crime_sort WHERE  Arrest = " TRUE" group by Primary_Type order by resolved desc;

#####---

select Primary_Type, (select count(Arrest) 
from crime_sort where Arrest= "False" group by Primary_Type), (select count(Arrest)
from crime_sort where Arrest= "True" group by Primary_Type) from crime_sort;



create table not_resolved as (select Primary_Type, count(Arrest) as not_resolved
from crime_sort WHERE  Arrest = FALSE group by Primary_Type order by not_resolved desc);

create table resolved as (select Primary_Type, count(Arrest) as resolved
from crime_sort WHERE  Arrest = True group by Primary_Type order by resolved desc);

select *, not_resolved + resolved as total, 
(not_resolved/ (not_resolved + resolved))*100 as Por_not_resolved 
 from not_resolved inner join resolved using (Primary_Type);
