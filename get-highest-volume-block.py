import sqlite3

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

# Query for block with highest volume within specified time range
c.execute("""
SELECT block_number, timestamp, TOTAL(value) AS total_volume
FROM transactions
WHERE timestamp BETWEEN 1704067200 AND 1704069000
GROUP BY block_number
ORDER BY total_volume DESC
LIMIT 1
""")
result = c.fetchone()
print("Block with highest volume (block number, timestamp, volume):", result)
