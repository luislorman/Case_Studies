use olist;

# N° orders by category
select product_category_name, count(order_id) as Total_Orders from products 
inner join order_items using(product_id)
group by product_category_name;

# N° orders by category and profit
select products.product_category_name, count(order_id) as Total_Orders, floor(sum(total_price)) as Total_Price from products 
inner join order_items using(product_id)
inner join order_status_year_price using (order_id)
group by product_category_name order  by Total_Price desc ;

# que categoria da mas dinero por item, sin transporte
select product_category_name, floor(avg(price)) as price from order_items
inner join products using (product_id)
group by product_category_name order by price desc ;

select cat, floor(avg(price)) as price from prod_cat_price 
group by cat 
order by price desc;

# freight cost per item type
select product_category_name, order_customer_items_paid.freight_value as freight_cost
from order_customer_items_paid 
inner join order_items using (order_id)
inner join products using(product_id)
group by product_category_name order by freight_cost desc;


# categoria que da mas dinero en total

select cat, final_price from prod_cat_price 
inner join order_items using (product_id)
inner join order_customer_items_paid using (order_id)
group by cat order by final_price desc;


select business_segment, business_type, product_category_name, order_customer_items_paid.freight_value as freight_cost, final_price
from order_customer_items_paid 
inner join closed_deals using (seller_id)
inner join order_items using (order_id)
inner join products using(product_id)
inner join prod_cat_price using (product_id)
group by product_category_name order by final_price desc;


# union area de negocio, resselervs manufacter, item price, ferigt cost, final price
select business_segment, business_type, sum(order_customer_items_paid.price) as item_price, avg(order_customer_items_paid.freight_value) as freight_cost, sum(final_price)  from closed_deals
inner join order_items using (seller_id)
inner join products using (product_id)
inner join order_customer_items_paid using (order_id)
group by business_segment;



select business_segment, business_type, product_category_name  from closed_deals
inner join order_items using(seller_id)
inner join products using (product_id);

# juntar esta dos tables por medio de la columna productcategroy name en pyhton, usandola de puente

select business_segment, business_type, product_category_name  from closed_deals
inner join order_items using(seller_id)
inner join products using (product_id);

select product_category_name, floor(sum(order_customer_items_paid.price)), 
floor(avg(order_customer_items_paid.freight_value)), 
floor(sum(order_customer_items_paid.final_price)) as total_price from products 
inner join order_items using (product_id) # puente para order_customer_paid
inner join order_customer_items_paid using (order_id)
group by product_category_name order by total_price desc;




select * from products;
select * from order_items;
select * from order_customer_items_paid;

create table nueva as (select * from products
inner join order_items using (product_id)
inner join order_customer_items_paid using (order_id));

#creaccion de esas tables y juntarlas en una nueva

create table nueva as (select product_category_name, floor(sum(order_customer_items_paid.price)) as sum_price_no_transport, 
floor(avg(order_customer_items_paid.freight_value))  as avg_freight_value,
floor(sum(order_customer_items_paid.final_price)) as total_price from products
inner join order_items using (product_id)
inner join order_customer_items_paid using (order_id) group by product_category_name order by total_price desc);


create table nueva_2 as (select business_segment, business_type, product_category_name  from closed_deals
inner join order_items using(seller_id)
inner join products using (product_id));


create table final_table as ( select *  from nueva
inner join nueva_2 using (product_category_name));

show tables;
select * from final_table;



select payment_type from order_payments

# order customers vs selles  by states

select seller_state, count(seller_state) from sellers
 group by seller_state
 order by count(seller_state) desc;
 
 
select customer_state, count(customer_state) from customers
 group by customer_state
 order by count(customer_state) desc;
 
 select seller_state, count(seller_state), count(customer_unique_id), count(order_id) from sellers  
 inner join order_items using(seller_id)
 inner join orders using (order_id)
 inner join customers using (customer_id)
 group by seller_state;
 
select count(order_id) from orders;

# buscar si hay relacion entre industrai y tipo de lead, se miraod corr en python, y no hay
 select distinct lead_type, lead_behaviour_profile,business_type from closed_deals;
 

 select distinct lead_type ,business_type from closed_deals;
 
 
 
 

