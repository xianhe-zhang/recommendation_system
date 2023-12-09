# Recall Service for Concrec

## Setup
- `docker run --name recall-redis -d -p 6379:6379 redis`
- `pip install -r requirements.txt`

## Run
- `source venv/bin/activate`
- `./start.sh`

## API
- `GET` `/?user_id=<uid>`
  - Get recall for a user
  - Returns list of anime ids


- `GET` `/sim?anime_id=<aid>`
  - Get similar items for an anime
  - Returns list of anime ids
