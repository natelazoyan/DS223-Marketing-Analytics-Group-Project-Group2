from CLV_Analysis.DB.sql_interactions import SqlHandler

Inst = SqlHandler('temp', ['sales_fact','transactions','customer','property','agent','date'])

# Retrieve properties with square footage greater than 1500.
query1 = "SELECT * FROM property WHERE square_footage > 1500;"

# Retrieve customers from New York born after January 1, 1990.
query2 = "SELECT * FROM customer WHERE birthday > '1990-01-01' AND city = 'New York';"

# Retrieve agents with more than 5 years of experience.
query3 = "SELECT * FROM agent WHERE experience_years > 5;"

# Retrieve transactions made using credit cards.
query4 = "SELECT * FROM transactions WHERE payment_method = 'Credit Card';"

# Retrieve sales transactions where the transaction amount is over 100000.
query5 = "SELECT * FROM sales_fact WHERE transaction_id IN (SELECT transaction_id FROM transactions WHERE transaction_amount > 100000);"

# Retrieve property sales made in the year 2022.
query6 = "SELECT * FROM property p JOIN sales_fact s ON p.property_id = s.property_id JOIN date d ON s.date_id = d.date_id WHERE d.year = 2022;"

# Retrieve sales transactions handled by agent with ID 5.
query7 = "SELECT * FROM sales_fact WHERE agent_id = 5;"

# Calculate total transaction amounts grouped by month and year for the year 2023.
query8 = "SELECT d.month, d.year, SUM(t.transaction_amount) AS total_amount FROM transactions t JOIN date d ON strftime('%Y', t.transaction_date) = d.year WHERE d.year = 2023 GROUP BY d.month, d.year;"

# Count the number of properties in each city.
query9 = "SELECT city, COUNT(*) AS property_count FROM property GROUP BY city;"

# Calculate the average number of bathrooms for properties built after 2010.
query10 = "SELECT AVG(number_of_bathrooms) AS avg_bathrooms FROM property WHERE year_built > 2010;"

# Calculate total transaction amounts grouped by property type in a specific city.
query11 = "SELECT p.property_type, SUM(t.transaction_amount) AS total_transaction_amount FROM property p LEFT JOIN sales_fact s ON p.property_id = s.property_id LEFT JOIN transactions t ON s.transaction_id = t.transaction_id WHERE p.city = 'East Samuel' GROUP BY p.property_type;"

# Calculate the average square footage of properties sold by agents with more than 5 years of experience.
query12 = "SELECT AVG(p.square_footage) AS average_square_footage FROM property p JOIN sales_fact s ON p.property_id = s.property_id JOIN agent a ON s.agent_id = a.agent_id WHERE a.experience_years > 5;"

# Retrieve top 5 customers with the highest total transaction amounts.
query13 = "SELECT c.customer_name, c.customer_surname, SUM(t.transaction_amount) AS total_transactions FROM customer c JOIN sales_fact s ON c.customer_id = s.customer_id JOIN transactions t ON s.transaction_id = t.transaction_id GROUP BY c.customer_id ORDER BY total_transactions DESC LIMIT 5;"

# Retrieve properties that were not involved in any sales transactions.
query14 = "SELECT p.* FROM property p LEFT JOIN sales_fact s ON p.property_id = s.property_id WHERE s.property_id IS NULL;"

# Retrieve the agent with the highest number of transactions in Spain.
query15 = "SELECT a.agent_name, a.agent_surname, COUNT(s.transaction_id) AS transaction_count FROM agent a JOIN sales_fact s ON a.agent_id = s.agent_id JOIN customer c ON s.customer_id = c.customer_id WHERE c.country = 'Spain' GROUP BY a.agent_id ORDER BY transaction_count DESC LIMIT 1;"

# Calculate total transaction amounts grouped by quarter for the year 2010.
query16 = "SELECT d.quarter, SUM(t.transaction_amount) AS total_sales_amount FROM transactions t JOIN date d ON strftime('%Y', t.transaction_date) = d.year WHERE d.year = 2010 GROUP BY d.quarter;"

# Retrieve customer details for customers who bought properties in the same city they were born in and in the year their birth year matches the property's year built.
query17 = "SELECT c.* FROM customer c JOIN sales_fact s ON c.customer_id = s.customer_id JOIN property p ON s.property_id = p.property_id WHERE c.city = p.city AND strftime('%Y', c.birthday) = strftime('%Y', p.year_built);"

# Retrieve properties where the number of bedrooms equals the number of bathrooms.
query18 = "SELECT * FROM property WHERE number_of_bedrooms = number_of_bathrooms;"

# Calculate the average customer age at the time of their transactions.
query19 = "SELECT AVG(strftime('%Y', 'now') - strftime('%Y', c.birthday)) AS average_customer_age FROM customer c JOIN sales_fact s ON c.customer_id = s.customer_id;"

# Calculate the total number of transactions grouped by day of the week, and retrieve the busiest day.
query20 = "SELECT d.day_of_week_name, COUNT(s.transaction_id) AS transaction_count FROM sales_fact s JOIN date d ON s.date_id = d.date_id GROUP BY d.day_of_week_name ORDER BY transaction_count DESC LIMIT 1;"


queries = [query1,
query2,
query3,
query4,
query5 ,
query6,
query7,
query8,
query9,
query10,
query11,
query12,
query13,
query14,
query15,
query16,
query17,
query18,
query19,
query20]

for i in queries:
       Inst.execute_custom_query(i)