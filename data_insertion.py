
from CLV_Analysis.DB.sql_interactions import SqlHandler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from CLV_Analysis.DB.schema import Sale 

Inst=SqlHandler('temp', 'customer')


import pandas as pd
data=pd.read_csv('data_csv/customer.csv')

#Inst.truncate_table()
Inst.insert_many(data)


Inst.close_cnxn()

# #transaction
# Inst1=SqlHandler('temp', 'transactions')

# import pandas as pd
# data1=pd.read_csv('data_csv/transactions.csv')

# #Inst1.truncate_table()
# Inst1.insert_many(data1)


# Inst1.close_cnxn()

# #property
# Inst2=SqlHandler('temp', 'property')

# import pandas as pd
# data2=pd.read_csv('data_csv/property.csv')

# #Inst2.truncate_table()
# Inst2.insert_many(data2)


# Inst2.close_cnxn()

# #agent
# Inst3=SqlHandler('temp', 'agent')

# import pandas as pd
# data3=pd.read_csv('data_csv/agent.csv')

# #Inst3.truncate_table()
# Inst3.insert_many(data3)


# Inst3.close_cnxn()

# #date
# Inst4=SqlHandler('temp', 'date')

# import pandas as pd
# data4=pd.read_csv('data_csv/date.csv')

# #Inst4.truncate_table()
# Inst4.insert_many(data4)


# Inst4.close_cnxn()


# # Create a SQLAlchemy engine and session
# engine = create_engine('sqlite:///temp.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# import pandas as pd
# # Read CSV file into a list of dictionaries
# data5 = pd.read_csv('data_csv/sales.csv').to_dict(orient='records')

# # Insert the sample data into the 'sales_fact' table
# for data in data5:
#     sale = Sale(**data)
#     session.add(sale)

# # Commit the changes to the database
# session.commit()

# # Close the session
# session.close()