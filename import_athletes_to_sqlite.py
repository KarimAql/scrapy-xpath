import sqlite3
import csv
connection = sqlite3.connect("athletes.db") 
# table = 'Create table athletes(rank integer, name varchar(255), result decimal)'
cursor = connection.cursor()
# cursor.execute(table)
# connection.commit()
# with open('/workspaces/scrapy-xpath/wiki_athletes/wiki_athletes/spiders/athletes.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
    
#     # Insert each row into the database, ignoring 'Nationality'
#     for row in reader:
#         # Prepare SQL query to insert data, only inserting rank, name, and result
#         cursor.execute("""
#             INSERT INTO athletes (rank, name, result)
#             VALUES (?, ?, ?)
#         """, (row['Rank'], row['Name'], row['Result']))

#     # Commit the transaction
#     connection.commit()

#Try querying the data:
cursor.execute("SELECT * FROM athletes")

# Fetch all results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)


# Close the connection
connection.close()
