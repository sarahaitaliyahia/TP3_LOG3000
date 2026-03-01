# TP3 LOG3000 - Web Calculator

## Project Purpose and Scope
This project is a web calculator application developed with Flask.
It lets users evaluate simple arithmetic expressions through a browser-based interface.
The backend validates and computes expressions, while the frontend provides a minimal calculator UI.
This README is written so a new developer can clone the repository and become
productive without prior project context.

Its goals are:
- to provide a web interface to evaluate an arithmetic expression with 1 operator
- to implement a clear architecture between:
  - the Flask server (`backend/app.py`);
  - the operations logic (`backend/operators.py`);
  - the interface (`templates/` and `static/`).
    
## Installation Guide
### Prerequisites
- Python installed
- Git installed locally
- pip installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sarahaitaliyahia/TP3_LOG3000.git
   cd TP3_LOG3000
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install flask
   ```

## Usage
### Run the application
1. Verify that the virtual environment is active.
2. Start the server:
   ```bash
   python backend/app.py
   ```
3. Open the browser at `http://127.0.0.1:5000`

### Use the features
- Enter an expression with the buttons (e.g., `7+2`).
- Click `=` to send the calculation to the server and get the result (or an error message).
- Click `C` to reset the input.

## Tests
The test module is located in the `tests/` folder and currently contains
automated tests for core arithmetic behavior.

Current scope:
- subtraction behavior (`subtract`)
- multiplication behavior (`multiply`)
- division behavior (`divide`)

Run all tests from the project root:
```bash
source .venv/bin/activate
python -m unittest discover -s tests -v
```

Run the operators test module only:
```bash
python -m unittest tests.test_operators -v
```

Run one specific test:
```bash
python -m unittest tests.test_operators.TestOperatorLogicBugs.test_subtract_operand_order -v
```

As new tests are added later, keep using `unittest discover` so new files are
picked up automatically without changing the command.

## Contribution Workflow
### 1. Create an issue
- Create an issue for any improvement or bug.
- Describe the situation and expected impact and results.

### 2. Create a branch
Name branches according to the type of work:
- `feature-<short-descriptive-name>` to work on a feature
- `fix-<short-descriptive-name>` to fix a problem or error
- `docs-<short-descriptive-name>` to work on documentation

Example:
```bash
git checkout -b docs/main-readme
```

### 3. Develop and validate locally
- Make atomic commits with a clear message.
- Verify that the application starts.
- Run the relevant tests before opening a PR.
- If you are fixing an issue, re-run the failing test first, then confirm it passes after your change.

### 4. Open a Pull Request
- Push the branch to the remote repository.
- Create a PR targeting `main`.
- Clearly describe:
  - the problem;
  - the proposed solution;
  - the validations performed.
- Reference the issue in the PR (e.g., `Closes #12`).

### 5. Merge and close the issue
- Merge only after review is approved and checks pass.
- Ensure the linked issue is closed by the PR reference.
