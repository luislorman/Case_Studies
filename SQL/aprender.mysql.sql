
# primer dia enlaces del ironhack lab en web

use bank;

select client_id from client where district_id = 1;

select district_id from client;

### Query 2
#In the `client` table, get an `id` value of the last client where the `district_id` equals to 72.

show columns from client;
select client_id from client where district_id = 72;


### Query 3
#Get the 3 lowest amounts in the `loan` table.

select amount from loan order by amount asc limit  3;

### Query 4
#What are the possible values for `status`, ordered alphabetically in ascending order in the `loan` table?

select distinct status  from loan order by status asc;

### Query 5
#What is the `loan_id` of the highest payment received in the `loan` table?
select loan_id, payments from loan order by payments desc;

### Query 6
#What is the loan `amount` of the lowest 5 `account_id`s in the `loan` table? Show the `account_id` and the corresponding `amount`
select loan_id, amount from loan order by amount asc;

### Query 7
#What are the top 5 `account_id`s with the lowest loan `amount` that have a loan `duration` of 60 in the `loan` table?

select account_id, amount from loan where duration = 60 order by amount asc limit 5;


### Query 10
#In the `order` table, which `account_id`s were responsible for orders 
#between `order_id` 29540 and `order_id` 29560 (inclusive)?

select order_id from bank.order where order_id < 29559 and order_id >29539  order by order_id asc;


### Query 12
#In the `trans` table, show the `trans_id`, `date`, `type` and `amount` of the 10 first transactions 
#from `account_id` 793 in chronological order, from newest to oldest.

select trans_id,date,type, amount from trans where account_id = 793 order by date asc limit 10;


# Optional
### Query 13
#In the `client` table, of all districts with a `district_id` lower than 10, how many clients are from each `district_id`? 
#Show the results sorted by the `district_id` in ascending order.
select client_id,district_id from client where district_id < 10 group by district_id;

### Query 14
#In the `card` table, how many cards exist for each `type`? 
#Rank the result starting with the most frequent `type`.

select type,count(type) from card group by type order by count(type) desc;

### Query 15
#Using the `loan` table, print the top 10 `account_id`s 
#based on the sum of all of their loan amounts.

select account_id, amount from loan group by amount order by amount desc limit 10;

### Query 16
#In the `loan` table, retrieve the number of loans issued for each day, before (excl) 930907, 
#ordered by date in descending order.

select count(loan_id) as LoanID_total ,date from loan where date < 930907 group by date order by date desc;

### Query 17
#In the `loan` table, for each day in December 1997, count the number of 
#loans issued for each unique loan duration, ordered by date and duration, 
#both in ascending order. 
#You can ignore days without any loans in your output.

select date, count(loan_id) as LoanID_total , duration from loan 
where date >=  971200 and date <=971231 group by date order by date and duration asc;

### Query 18
#In the `trans` table, for `account_id` 396, sum the amount 
#of transactions for each type (`VYDAJ` = Outgoing, `PRIJEM` = Incoming). 
#Your output should have the `account_id`, the `type` and 
#the sum of amount, named as `total_amount`. Sort alphabetically by type.

select  account_id,type, floor (sum(amount)) from trans where account_id = 396 group by type order by type desc;

### Query 19
#From the previous output, translate the values for `type` to English, rename the column 
#to `transaction_type`, round `total_amount` down to an integer

select  account_id,case type 
when "PRIJEM" THEN 'Incoming' when "VYDAJ" THEN 'Outcoming' else type end as transaction_type, floor(sum(amount)) from trans where account_id = 396 group by type order by type desc;

#####################################################################################################
# Lab_SQL_Join_Two_Tables.sql
use sakila;

#Which actor has appeared in the most films? 

select count(actor.actor_id) as number, actor.actor_id,actor.first_name, actor.last_name from actor 
inner join film_actor on actor.actor_id = film_actor.actor_id group by actor.actor_id order by count(actor.actor_id) desc;
#el groupy by con actor, xq una peli tienen varios actores pero un acotr solo una y hay q agrupar alreddor del ator



#2. Most active customer (the customer that has rented the most number of films)
#ambas son buenas   lo tengo q agrupar por el custoemr

#n veces se reptie el customer 
select  customer_id, count(customer_id) from rental group by customer_id order by count(customer_id) desc;

# n veces q hay films rentadas
select  customer_id, count(rental_id) from rental group by customer_id order by count(customer_id) desc;

#3. List number of films per `category`.

#amabas buenas
select name, category.category_id, count(category.category_id) from category inner join film_category on category.category_id = film_category.category_id group by category.category_id order by count(category.category_id) desc;

select name, category.category_id, count(film_category.film_id) from category inner join film_category on category.category_id = film_category.category_id group by category.category_id order by count(category.category_id) desc;

#4. Display the first and last names, as well as the address, of each staff member.

select staff.first_name, staff.last_name, address.address from staff inner join address on staff.address_id = address.address_id;

#5. get films titles where the film language is either English or italian, 
#and whose titles starts with letter "M" , sorted by title descending.

select title, language.name from film inner join language on language.language_id = film.language_id where title like "M%" order by title desc;

#6. Display the total amount rung up(recaudar) by each staff member in August of 2005.

select staff.staff_id, payment_date, sum(amount)  from staff inner join payment on payment.staff_id = staff.staff_id where payment_date >=20050801 and payment_date <=20050831 group by staff_id;


#7. List each film and the number of actors who are listed for that film.
select title, film.film_id, count(actor_id) from film inner join film_actor on film_actor.film_id = film.film_id group by film.film_id order by count(actor_id) desc;

#8. Using the tables `payment` and `customer` and the JOIN command, 
#list the total paid by each customer. List the customers alphabetically by last name.
select last_name, sum(amount) from payment 
inner join customer on customer.customer_id = payment.customer_id 
group by payment.customer_id order by customer.last_name asc;

#inner join payment using (customer_id)  !!!!!!!! 


#9. Write sql statement to check if you can find any actor who never particiapted in any film. 

select first_name, last_name,title from actor
left join film_actor using (actor_id)
right join film using (film_id)
where title is null;

#------------------------------------------------------------
# subqueries

use sakila;
#1.List all films whose length is longer than the average of all the films.
select title, length from film where length > (select avg(length) from film );

#2.How many copies of the film Hunchback Impossible exist in the inventory system?
select title, count(film_id) from film inner join inventory using (film_id) where title = "Hunchback Impossible";

select count(inventory_id) from inventory where film_id = (select film_id from film where title like "%Hunchback Impossible%");

#3.Use subqueries to display all actors who appear in the film Alone Trip.
select film.title, first_name, last_name from actor 
inner join film_actor using (actor_id) 
inner join film using (film_id) where title = "Alone Trip"; # pasando de una tabla a otra por medio de una tercera, ya q no tienen 'puente' directo


select film_id, actor_id, first_name, last_name from actor
join film_actor using (actor_id) 
where film_id = (select film_id from film_text where title like "%Alone Trip%"); # estoy diciendo e q el filmd_id es ese titlo de otra columna

#4.Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
#Identify all movies categorized as family films.

select title, film_id from film 
inner join film_category  using (film_id) 
inner join category using ( category_id)
where name like "%Family%" ;

select title, film_id from film inner join film_category using (film_id) where film_id in
(select film_id from film_category inner join category using ( category_id) where category_id in 
(select category_id from category where name = "Family"));

select title, film_id from film join film_category using(film_id)
 where film_id in  (select film_id from film_category join category using (category_id)
where category_id = (select category_id from category where name like "%Family%"));

#5.Get name and email from customers from Canada using subqueries. Do the same with joins. 
#Note that to create a join, you will have to identify the correct tables with their primary keys and foreign keys, 
#that will help you get the relevant information.


select first_name, last_name, email from customer inner join address using (address_id) where address_id in
(select address_id from address where city_id in (
select city_id from city inner join country using (country_id) where country_id in 
(select country_id from country where country like "%Canada%")));


select first_name, last_name, email from customer where address_id in 
(select address_id from address where city_id IN  
(select city_id from city where country_id like 
(select country_id from country where country = "Canada")));

#Optional
#6Which are films starred by the most prolific actor? Most prolific actor is defined as the actor that has acted in the most number of films.
#First you will have to find the most prolific actor and then use that actor_id to find the different films that he/she starred.
use sakila;

select title from film where film_id in 
(select film_id from film_actor where actor_id like 
(select actor_id from film_actor group by actor_id order by count(actor_id) desc limit 1));



#7 Films rented by most profitable customer. 
#You can use the customer table and payment table to find the most profitable customer ie the customer that has made the largest sum of payments


select title from film  where film_id in  (
select film_id from inventory where inventory_id in  (
select inventory_id from rental  where customer_id like (
select customer_id from payment group by customer_id order by sum(amount) desc limit 1))) order by title asc;


#8Customers who spent more than the average payments(this refers to the average of all amount spent per each customer).


select customer_id, sum(amount) from payment inner join customer using (customer_id) 
group by customer_id having avg(amount) > (select floor(avg(amount)) from payment ) order by sum(amount) desc;


select customer_id, avg(amount) from payment group by customer_id having avg(amount) > (select avg(amount) from payment) ;





select sum(amount) / count(amount) from payment group by customer_id;

select avg(amount) from payment group by customer_id;