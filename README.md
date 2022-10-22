```bash
git init
git add README.md
git commit -m "first commit"
git branch -M init
git remote add origin https://github.com/pandalearnstocode/sample_components.git
git push -u origin init
```

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