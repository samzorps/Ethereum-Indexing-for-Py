import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

# Query for block with highest volume within specified time range
c.execute("""
SELECT block_number, SUM(value) AS total_volume
FROM blocks
WHERE timestamp BETWEEN 1685468800 AND 1685472400
GROUP BY block_number
ORDER BY total_volume DESC
LIMIT 1
""")
result = c.fetchone()
print("Block with highest volume:", result)
