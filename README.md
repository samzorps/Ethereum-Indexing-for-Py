# Desctiption
Python app to retreive etherium mainnet transactions within a given block range and add them to a SQLite database. Then query that database to find the block with the most volume between 2024-01-01 00:00:00 and 2024-01-01 00:30:00.

# Quickstart 
1. Create and activate a virtual envoirnment and download dependencies. Run the following in a terminal at the project:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

2. Populate the database using block-crawler.py
```
python block-crawler [YOUR API ENDPOINT] [PATH/TO/DATABASE] [RANGE OF BLOCKS TO DOWNLOAD]
```
Example
```
python block-crawler https://rpc.quicknode.pro/key/[key] db.sqlite3 18908800-18909050
```
You will see a list of blocks with their hashes being downloaded to the DB.

3. Search database using get-highest-volume-block.py
```
python3 get-highest-volume-block.py
```
You will see the block with the highest volume printed:

Block with highest volume (block number, timestamp, volume): 18909040, 1704069011, 1.5397723118880007e+21
