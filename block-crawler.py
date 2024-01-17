import web3
import sqlite3
import argparse

ENDPOINT_DEFAULT = "https://alien-hardworking-hexagon.quiknode.pro/"
DB_DEFAULT = "/Users/samzorpette/Desktop/Ethereum Indexing for Py/db.sqlite3"
RANGE_DEFAULT = "18908800-18909050"

parser = argparse.ArgumentParser()
parser.add_argument("rpc_endpoint", help="JSON-RPC endpoint URL", default=ENDPOINT_DEFAULT)
parser.add_argument("db_path", help="Path to SQLite database file", default=DB_DEFAULT)
parser.add_argument("block_range", help="Block range in format start-end", default=RANGE_DEFAULT)
args = parser.parse_args()

w3 = web3.Web3(web3.HTTPProvider(args.rpc_endpoint))

conn = sqlite3.connect(args.db_path)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (block_hash text, block_number text, timestamp text, transaction_hash text, from_address text, to_address text, value text)''')

# get all blocks within the given range and save the relevant fields to the database
start_block, end_block = map(int, args.block_range.split("-"))
for block_number in range(start_block, end_block + 1):
    try:
        block = w3.eth.get_block(block_number, True)  # Include transactions
        print(w3.to_hex(block.hash), block.number, block.timestamp)
        for transaction in block.transactions:
            # Extract relevant fields and insert into database
            c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (str(block.hash), str(block.number), block.timestamp,
                    str(transaction.hash), str(transaction['from']),
                    str(transaction.to), str(transaction.value)))
    except Exception as e:
        print(e)
conn.commit()