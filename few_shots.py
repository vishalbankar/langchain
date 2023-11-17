few_shots = [
    {'Question' : "How many Van Huesen t-shirts are left in stock of white color?",
     'SQLQuery' : "SELECT SUM(stock_quantity) as total_tshirt FROM t_shirts WHERE brand='Van Huesen' and color='white' ",
     'SQLResult': "Result of the SQL query",
     'Answer' : "248"},
    {'Question': "How many t-shirts do we have left for nike in extra small size and white color?",
     'SQLQuery': "SELECT COALESCE (SUM(stock_quantity),0) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND "
                 "size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer': "0"},
    {'Question': "How much is the price of the inventory for all small size t-shirts?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "21618"},
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our "
                 "store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "22364.25"},
     {'Question' : "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate "
                   "without discount?",
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
      'SQLResult': "Result of the SQL query",
      'Answer' : "23385"},
    {'Question': "How many white color Levi's shirt I have?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "201"}
]