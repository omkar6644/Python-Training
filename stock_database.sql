STOCK_MARKET DATABASE:

DDL:

1) Create table stock(id int primary key, symbol varchar2(20), company varchar2(20));

2) create table stock_price( id int primary key, stock_id int, s_date varchar2(20), open float, high float, close float, current_price float, volume int, foreign key(stock_id) references stock(id));

3) create table stock_purchased(id int primary key, name varchar2(20), stock_id int, purchased_date varchar2(20), number_of_stocks_purchased int, foreign key(stock_id) references stock(id));


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

Stock_purchased:

1) Insert into stock_purchased values(51, 'Ruturaj', 5, '20-05-2021', 5);
2) Insert into stock_purchased values(18, 'Melvin', 4, '10-05-2021', 10); 
3) Insert into stock_purchased values(26, 'Vinay', 3, '50-05-2021', 8); 
4) Insert into stock_purchased values(52, 'Pavan', 2, '11-05-2021', 4); 
5) Insert into stock_purchased values(88, 'Shubham', 1, '17-05-2021', 5); 


Queries:

1) select symbol, count(*) as c from stock group by symbol order by c desc; (selects symbol and counts it from stock table)
2) select stock_id, max(current_price) var from stock_price group by stock_id order by var desc; (selects stock id and highest stock price in descending order from stock_price table)
3) select symbol, s_date, open, high, close from stock_price join stock on stock.id = stock_price.stock_id where symbol = 'AAPL'; (selects symbol, s_date, open , high, close from stock_price table using join operation)
4) select number_of_stocks_purchased from stock_purchased where name = 'Melvin'; (displays number of stocks purchased by Melvin)
5) select purchased_date, number_of_stocks_purchased, number_of_stocks_purchased * current_price as Total_price from stock_purchased join stock_price on stock_price.stock_id = stock_purchased.stock_id where name = 'Melvin'; (selects purchased_date, number of stocks purchased and total price of the stock purchased by name = Melvin using join operatin)