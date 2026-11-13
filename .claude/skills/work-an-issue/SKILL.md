---
name: work-an-issue
description: Standard routine for turning a GitHub issue into a pull request. Use whenever asked to work, implement or fix an issue by number.
---

# Work an issue

1. Read it: `gh issue view <n>`. Restate the acceptance criteria as a checklist.
2. If anything is ambiguous, stop and comment on the issue with your question instead of guessing.
3. Branch: `git checkout -b claude/issue-<n>-<slug>`.
4. Implement only what the criteria ask. Stay inside the "Files likely touched" list.
5. Write or update tests for every criterion, then run `pytest -q` until green.
6. Commit with a Conventional Commit message (feat:, fix:, chore:).
7. Push and open the PR:
   `gh pr create --fill --body "Closes #<n>" --label <the issue's agent label>`
8. Reply with: the PR link, each criterion marked done or not, and any open questions.
