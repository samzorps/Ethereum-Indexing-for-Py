import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

# Query for block with highest volume within specified time range
c.execute("""
SELECT block_number, TOTAL(value) AS total_volume
FROM transactions
WHERE block_number BETWEEN 18908800 AND 18909050
GROUP BY block_number
ORDER BY total_volume DESC
LIMIT 1
""")
result = c.fetchone()
print("Block with highest volume:", result)
