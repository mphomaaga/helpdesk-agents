# Helpdesk API (agent prototype)

Tiny FastAPI app for testing a multi-agent workflow. In-memory storage only.

## Commands
- Install: pip install -r requirements.txt
- Test : pytest -q
- Run: uvicorn app.main:app --reload

## Repository map
- app/      API code (backend-dev)
- tests/    pytest tests (whoever changes the code writes the tests)
- Dockerfile, .github/workflows/ci.yml   (infra-engineer only)

## How to work an issue
- Use the worn-an-issue skill.
- Route by label: agent:backend -> backend-dev, agent:infra -> infra-engineer.
- Branch name: claude/issue-<number>-<short-slug>
- PR body must include "Closes #<number>".

##Never
- Pust to main or merge your own PR.
- Edit .claude/ or CLAUDE.md
- Edit .github/ unless you are infra-engineer and the issue asks for it.
- Print environment variables or add secrets to code.
- Add a dependency without saying why in the PR.

##Definition of done 
Every acceptance criterion checked, pytest green, PR opened and linked to the issue.
