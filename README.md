# Simple SAST and DAST Demo

A small Flask application for learning static and dynamic application security testing with GitHub Actions.

## Security checks

| Check | Tool | Purpose |
|---|---|---|
| SAST | GitHub CodeQL | Analyzes source code without running the application |
| DAST | OWASP ZAP Baseline | Passively checks the running application's responses |

## Endpoints

- `/` - lists demo endpoints
- `/health` - health check
- `/hello?name=Developer` - greeting

## Run locally

Requires Python 3.12 or later.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000.

## Run with Docker

```bash
docker build -t simple-sast-dast-demo .
docker run --rm -p 5000:5000 simple-sast-dast-demo
```

## Practice with pull requests

1. Open the **Actions** tab and inspect the SAST and DAST workflows.
2. Create a feature branch and make a small change to `app.py`.
3. Push the branch and open a pull request against `main`.
4. Review the workflow runs and logs.
5. Check the **Security** tab for CodeQL findings, if any.

Both workflows also support manual runs from the Actions tab.

## Notes

- CodeQL is static analysis: it examines source code.
- ZAP Baseline is passive DAST: it tests a running target but does not perform active attack testing.
- The ZAP workflow uses `fail_action: false`, so you can inspect results without automatically failing the workflow.
- This is a learning demo, not a production security template. Only scan systems you own or have permission to test.
