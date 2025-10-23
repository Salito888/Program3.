
## My_api_ABB
FastAPI app built usign FastAPI Initializr

### Requirements
* Python 3.12

### Run

Create and enable virtual enviroment
```bash
python3.13 -m venv .venv
source .venv/bin/activate    # Activate on Linux
.\.venv\Scripts\activate     # Activate on Windows
```

Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Run FastAPI application
```bash
uvicorn app.main:app --port 8000 --reload
```


