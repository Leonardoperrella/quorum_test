# Quorum

### Python

    - 3.9.5

### Libraries

    fastapi
    pandas
    Jinja2

## How to developer?

    1. Clone the repository
    2. Create a virtualenv
    3. Active o virtualenv
    4. Install the dependencies.
    5. Execute tests
    6. Execute server

```console
git clone https://github.com/Leonardoperrella/quorum_test quorum
cd quorum
python3 -m venv env
source .env/bin/activate
pip install -r requirements.txt
pytest -vv
uvicorn quorum.main:app --reload
```
