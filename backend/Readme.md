## Command to generate Secret TOKEN
This command generates 32 bit secret token for safe url.

```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
## Command to execute this code:
```
uvicorn app.main:app --reload
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```