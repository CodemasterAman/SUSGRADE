# /susgrade

**See what's actually worth testing.**

susgrade is a test-effectiveness analysis tool for Python. It fuses two
established software-quality signals into one report:

1. **Cyclomatic complexity** — how many independent paths each function has
   (how much there is to test).
2. **Mutation score** — how good the existing tests are at catching injected
   bugs (coming in Sprint 2).

The goal is usability: make test-quality analysis simple enough for a
low-experience developer to run single-handedly, while keeping the metrics
valid and standard.

## Project structure

```
susgrade/
├── backend/                FastAPI service (Sprint 1)
│   ├── app/
│   │   ├── main.py         API endpoints
│   │   ├── models.py       request/response schemas
│   │   └── analysis/
│   │       ├── complexity.py   cyclomatic complexity engine (ast-based)
│   │       └── mutation.py     mutation-testing engine        (Sprint 2)
│   ├── tests/              pytest suite (13 tests)
│   └── requirements.txt
├── frontend/
│   └── index.html          interactive analyzer UI (open in a browser)
└── docs/
    └── susgrade_SRS.docx   Software Requirements Specification
```

## Run the backend

```bash
cd backend
python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload      # docs at http://127.0.0.1:8000/docs
pytest                             # run the 13-test suite
```

## Run the frontend

Just open `frontend/index.html` in any browser — no build step. The sample
tabs show real scores from the engine; the "your code" tab runs an in-browser
estimate (verified to match the engine on the samples). In production it calls
the API for exact AST scores.

## Sprint plan

| Sprint | Goal | Status |
|-------|------|--------|
| 1 | Backend scaffold + cyclomatic complexity engine + API + frontend | ✅ done |
| 2 | Mutation-testing engine with sandboxed mutant execution | ⬜ next |
| 3 | Combined complexity × mutation-score risk report | ⬜ |
| 4 | Wire frontend to API + deployment | ⬜ |

## Story cards — Sprint 1

- **SG-1** — *Submit Python and get each function's cyclomatic complexity.* ✅
  McCabe decision-point rules; dotted names for methods/nested functions;
  module summary (total, avg, max). Covered by `tests/test_complexity.py`.
- **SG-2** — *Get a clear error instead of a crash on a syntax error.* ✅
  API returns HTTP 422 with the offending line number.
- **SG-3** — *Each function is labelled with a readable risk band.* ✅
  simple / moderate / complex / very complex, from standard thresholds.

## Team

- **Aman Behera** — 23FE10CSE00607
- **Bhomik Jain** — 23FE10CSE00707

Manipal University Jaipur · CSE4149 Software Verification and Testing
