## __Links__

* [Monorepo](https://github.com/pandalearnstocode/sample_components)
* [Sub component 1](https://github.com/pandalearnstocode/sample_subcomponents_1)
* [Sub component 2](https://github.com/pandalearnstocode/sample_subcomponents_2)

## __Setup__
```bash
git init
git add README.md
git commit -m "first commit"
git branch -M init
git remote add origin https://github.com/pandalearnstocode/sample_components.git
git push -u origin init
```
## __GitHub actions:__

### __High level overview:__


```yml
name: CI
on:
  push:
    branches:
      - init
  workflow_dispatch:
jobs:
  pr_validator:
    runs-on: ubuntu-latest
    steps:
    - name: PR validator
      run: echo "step 1"
  test_suite:
    runs-on: ubuntu-latest
    needs: pr_validator
    steps:
    - name: Test suite
      run: echo "step 1"    
  linting_checks:
    runs-on: ubuntu-latest
    needs: pr_validator
    steps:
    - name: Linting check
      run: echo "step 1"
  formatting_checks:
    runs-on: ubuntu-latest
    needs: pr_validator
    steps:
    - name: Formatting check
      run: echo "step 1"
  security_checks:
    runs-on: ubuntu-latest
    needs: pr_validator
    steps:
    - name: Security checks
      run: echo "step 1"
  notify:
    runs-on: ubuntu-latest
    needs: [test_suite, linting_checks, formatting_checks, security_checks]
    steps:
    - name: Notification
      run: echo "step 1"
```


```yml
name: Release
on:
  pull_request:
    branches:
      - init
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
    - name: Create release
      run: echo "step 1"
  notify:
    runs-on: ubuntu-latest
    needs: release
    steps:
    - name: Notify users
      run: echo "step 1"
```

### __Components:__

#### __Git checkout__

```yml
- uses: actions/checkout@v3
  with:
    fetch-depth: 0
```

* [Reference](https://github.com/actions/checkout)

#### __Setup python__

```yml
- uses: actions/setup-python@v4
  with:
    python-version: '3.10'
```

* [Reference](https://github.com/actions/setup-python)

#### __Install Poetry Action__

```yml
- name: Install Poetry
  uses: snok/install-poetry@v1
  with:
    virtualenvs-create: true
    virtualenvs-in-project: true
    installer-parallel: true
```

* [Reference](https://github.com/marketplace/actions/install-poetry-action)

#### __Cache:__

```yml
- name: Load cached venv
  id: cached-poetry-dependencies
  uses: actions/cache@v3
  with:
    path: .venv
    key: venv-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('**/poetry.lock') }}
```

#### __Install dependencies:__

```yml
- name: Install dependencies
  if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
  run: poetry install --no-interaction --no-root
```

#### __Install project__

```yml
- name: Install project
  run: poetry install --no-interaction
```

#### __Common setup block:__

```yml
- uses: actions/checkout@v3
  with:
    fetch-depth: 0
- uses: actions/setup-python@v4
  with:
    python-version: '3.8'
- name: Install Poetry
  uses: snok/install-poetry@v1
  with:
    virtualenvs-create: true
    virtualenvs-in-project: true
    installer-parallel: true
- name: Load cached venv
  id: cached-poetry-dependencies
  uses: actions/cache@v3
  with:
    path: .venv
    key: venv-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('**/poetry.lock') }}
- name: Install dependencies
  if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
  run: poetry install --no-interaction --no-root
```


## __Install poetry__

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
poetry new sample_components
poetry env use python3.8
poetry shell
python --version
```

### __Directory structure__

```bash
.
├── pyproject.toml
├── README.md
├── sample_components
│   └── __init__.py
└── tests
    └── __init__.py

2 directories, 4 files
```

```bash
poetry install
poetry add pytest
poetry run pytest
poetry build
poetry remove pytest
```

* [Poetry cheat sheet](https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb)

This is a dummy commit.

