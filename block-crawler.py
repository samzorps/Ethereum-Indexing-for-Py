import web3
import sqlite3
import argparse

ENDPOINT_DEFAULT = "https://alien-hardworking-hexagon.quiknode.pro/3be6fd1ea6eb39233fbdc7a167ca8ff85c082c78/"
DB_DEFAULT = "/Users/samzorpette/Desktop/Ethereum Indexing for Py/db.sqlite3"
RANGE_DEFAULT = "200-300"

parser = argparse.ArgumentParser()
parser.add_argument("--rpc_endpoint", help="JSON-RPC endpoint URL", default=ENDPOINT_DEFAULT, required=False)
parser.add_argument("--db_path", help="Path to SQLite database file", default=DB_DEFAULT, required=False)
parser.add_argument("--block_range", help="Block range in format start-end", default=RANGE_DEFAULT, required=False)
args = parser.parse_args()

w3 = web3.Web3(web3.HTTPProvider(args.rpc_endpoint))

conn = sqlite3.connect(args.db_path)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS blocks
             (block_hash text, block_number text, timestamp integer, transaction_hash text, from_address text, to_address text, value text)''')

start_block, end_block = map(int, args.block_range.split("-"))
for block_number in range(start_block, end_block + 1):
    block = w3.eth.get_block(block_number, True)  # Include transactions
    print(block_number)
    for transaction in block.transactions:
        # Extract relevant fields and insert into database
        print(block.hash.hex(), block.number.hex(), block.timestamp,
                   transaction.hash.hex(), transaction.from_address.hex(),
                   transaction.to_address.hex(), transaction.value)
        c.execute("INSERT INTO blocks VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (block.hash.hex(), block.number.hex(), block.timestamp,
                   transaction.hash.hex(), transaction.from_address.hex(),
                   transaction.to_address.hex(), transaction.value))
conn.commit()