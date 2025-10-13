# Contributing to Project A

Thank you for contributing to **Project A**!  
This project follows a **team-based workflow** similar to what is used in real-world enterprise development environments.

---

## Table of Contents

- [Getting Started](#-getting-started)
- [Development Workflow](#-development-workflow)
- [Branching Strategy](#-branching-strategy)
- [Commit Message Conventions](#-commit-message-conventions)
- [Code Style](#-code-style)
- [Testing Guidelines](#-testing-guidelines)
- [CI/CD Expectations](#-cicd-expectations)
- [Environment Variables](#-environment-variables)
- [Documentation Standards](#-documentation-standards)
- [External Contributors](#-external-contributors)

---

## Getting Started

1. Clone the repository (no forking required for team members).
2. Set up environment variables (`.env` and `.env.hosts`).
3. Start the development environment using Docker Compose.
4. Create a **feature branch** from `main` (or `develop` if used).

```bash
git checkout -b feature/my-feature
```

---

## Development Workflow

1. Create a new branch for your feature or bugfix.  
2. Make changes and **commit following the [commit conventions](#-commit-message-conventions)**.  
3. Push the branch to the shared repository.  
4. Open a Pull Request (PR) into `main` (or `develop` if used).  
5. Request at least one code review before merging.  
6. CI/CD will run automated checks before approval.

---

## Branching Strategy

- `main` → production-ready code
- `develop` (optional) → integration branch
- `feature/*` → new features
- `bugfix/*` → bug fixes
- `hotfix/*` → urgent fixes
- `release/*` → pre-production releases

Branch protection rules are recommended on `main` to enforce PR review and CI checks.

---

## Commit Message Conventions

We use **[Conventional Commits](https://www.conventionalcommits.org)** for clarity and automated versioning support.

**Format:**
```
<type>(optional scope): <description>
```

**Common types:**
- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation changes
- `style` — formatting, no code change
- `refactor` — code refactoring
- `test` — adding or updating tests
- `chore` — build or maintenance

**Examples:**
```
feat(auth): add JWT authentication
fix(db): correct Postgres connection issue
docs(readme): update env variable section
```

---

## Code Style

- **Backend:** Python
  - [Black](https://black.readthedocs.io/) for formatting
  - [Flake8](https://flake8.pycqa.org/) for linting

- **Frontend:** JavaScript / React
  - [ESLint](https://eslint.org/) + [Prettier](https://prettier.io/)

> Code must pass linting and formatting checks before merging.

---

## Testing Guidelines

- **Backend:** Pytest (planned)
- **Frontend:** Jest or Vitest (planned)
- All PRs should include or update tests for new functionality where applicable.

---

## CI/CD Expectations

- GitHub Actions (planned) will handle:
  - Linting and formatting checks
  - Test execution
  - Build validation
- All checks must pass before merging.

> **Note:** For production, additional deployment or tagging workflows can be added later.

---

## Environment Variables

- `.env` and `.env.hosts` are required for running the stack.
- Never commit secrets or sensitive data.
- If you add new variables, update `.env.example` accordingly.

---

## Documentation Standards

- Update `README.md` when changes impact usage, setup, or architecture.
- Add/update docstrings in backend Python code.
- Keep documentation in `docs/` structured and up to date.
- Use clear and descriptive commit messages for doc changes.

---

## External Contributors

If external contributors are added in the future:
- They should fork the repository.
- Create branches from their fork.
- Open Pull Requests to the main repository.
- Follow the same commit and code style guidelines as the team.

> This allows the internal team to work fast while maintaining a clean, controlled contribution process for outside collaborators.

---