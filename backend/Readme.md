## Command to generate Secret TOKEN
This command generates 32 bit secret token for safe url.

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"

## Command to execute this code:
```bash
uvicorn app.main:app --reload
