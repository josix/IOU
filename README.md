# IOU
IOU means "How much $ I OWE YOU?"
## Prepare enviorment
1. Install All Dependent Libraries
```bash
poetry install
```
2. Seeting Enviorment Variables
```bash
export CHANNEL_ACCESS_TOKEN=YOUR_CHANNEL_ACCESS_TOKEN
export CHANNEL_SECRET=YOUR_CHANNEL_SECRET
```
or create a `.env` file with following content
```
CHANNEL_ACCESS_TOKEN=YOUR_CHANNEL_ACCESS_TOKEN
CHANNEL_SECRET=YOUR_CHANNEL_SECRET
```
## Running the service
### Running locally
```
ngrok http 5000
```
```
poetry run uvicorn iou.main:app --host=0.0.0.0 --port=${PORT:-5000} --reload
```
### Running on heroku
