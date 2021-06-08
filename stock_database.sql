STOCK_MARKET DATABASE:

DDL:

1) create table stock(id int primary key, symbol varchar2(20), company varchar2(20));

2) create table stock_price( id int primary key, stock_id int, s_date varchar2(20), open float, high float, close float, current_price float, volume int, foreign key(stock_id) references stock(id));

3) create table stock_purchase( id int primary key, stock_id int, current_price float, buy varchar2(20), foreign key(stock_id) references stock(id));

4) create table stock_purchased(id int primary key, name varchar2(20), stock_id int, purchased_date varchar2(20), number_of_stocks_purchased int, sell varchar2(4), foreign key(stock_id) references stock(id));



DML:

Stock table:

1) Insert into stock values(1, 'AAPL', 'Apple');
2) Insert into stock values(2, 'MSFT', 'Microsoft');
3) Insert into stock values(3, 'RELIANCE', 'Reliance Ind. Ltd');
4) Insert into stock values(4, 'ADANI', 'Adani Power');
5) Insert into stock values(5, 'AMD', 'Advanced Mircro Device');

Stock_price:

1) Insert into stock_price values( 100, 1, '07-06-2021', 9036.01, 9188.23, 9025.54, 9168.25, 75169743);
2) Insert into stock_price values( 101, 2, '07-06-2021', 17036.01, 18828.23, 17025.54, 18265.25, 6644131);
3) Insert into stock_price values( 103, 3, '07-06-2021', 2202.01, 2242, 2185, 227.15, 75169743);
4) Insert into stock_price values( 104, 4, '07-06-2021', 112.01, 126.23, 111.54, 126.25, 70000);



Stock_purchase:

1) Insert into stock_purchase values( 88, 1, 9168.25, 'Yes');
2) Insert into stock_purchase values( 52, 2, 18265.25, 'Yes');
3) Insert into stock_purchase values( 26, 3, 227.15, 'Yes');
4) Insert into stock_purchase values( 18, 4, 126.25, 'Yes');
5) Insert into stock_purchase values( 51, 5, 9168.25, 'Yes');

Stock_purchased:

1) Insert into stock_purchased values(51, 'Ruturaj', 5, '20-05-2021', 5, 'Yes');
2) Insert into stock_purchased values(18, 'Melvin', 4, '10-05-2021', 10, 'Yes'); 
3) Insert into stock_purchased values(26, 'Vinay', 3, '50-05-2021', 8, 'Yes'); 
4) Insert into stock_purchased values(52, 'Pavan', 2, '11-05-2021', 4, 'Yes'); 
5) Insert into stock_purchased values(88, 'Shubham', 1, '17-05-2021', 5, 'Yes'); 


Queries:

1) select symbol, count(*) as c from stock group by symbol order by c desc; (selects symbol and counts it from stock table)

2) select name, purchased_date, stock.id from stock_purchased inner join stock on stock.id = stock_purchased.stock_id; (selects name, purchased date and stock id using inner join)

3) select stock_id, max(current_price) var from stock_price group by stock_id order by var desc; (selects stock id and highest stock price in descending order from stock_price table)

4) select symbol, s_date, open, high, close from stock_price join stock on stock.id = stock_price.stock_id where symbol = 'AAPL'; (selects symbol, s_date, open , high, close from stock_price table using join operation)

5) select symbol, company, number_of_stocks_purchased from stock_purchased join stock on stock.id = stock_purchased.stock_id where name = 'Melvin'; (displays number of stocks purchased by Melvin with symbol and company name)

6) select purchased_date, number_of_stocks_purchased, number_of_stocks_purchased * current_price as Total_price from stock_purchased join stock_price on stock_price.stock_id = stock_purchased.stock_id where name = 'Melvin'; (selects purchased_date, number of stocks purchased and total price of the stock purchased by name = Melvin using join operatin)

7) select symbol, company from stock join stock_price on stock.id = stock_price.stock_id  where current_price < 5000; (selects symbol, company name whose current_price is less than 5000)

8) select symbol, company from stock join stock_price on stock.id = stock_price.stock_id  where current_price > 10000; (selects symbol, company name whose current_price is greater than 10000)

9) select * from stock where id in (select stock_id from stock_price where current_price > 5000); (selects all data from stock where current_price of stock is greater than 5000 using nested query)

10) update stock_purchased set number_of_stocks_purchased = number_of_stocks_purchased - 1 where id =51 and sell = 'Yes'; (updates number_of_stocks_purchased if the customer wants to sell it)

11) update stock_purchased set number_of_stocks_purchased = number_of_stocks_purchased + 1  where stock_id in  (select stock_id from stock_purchase where buy ='Yes' and id =88 ); (updates number_of_stocks_purchased if the customer wants to buys it using nested query)
