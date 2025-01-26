# Assert No Trailing Whitespace

A GitHub action that asserts that there is not trailing whitespace in the
specified files.

## Usage

Create a workflow file in `.github/workflows/assert-no-trailing-whitespace.yml`.

A basic use case could look like the following:
```yaml
name: Assert No Trailing Whitespace

on:
  push:
    branches:
      - master

jobs:
  check-whitespace:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Assert No Trailing Whitespace
      uses: AlexanderKosnac/assert-no-tws@v1.0.0
      with:
        path: '.'
        extensions: ''
```

## Development

The primary script executed in this project is `check-files-for-whitespace.py`.
It can be run using the following command:

```bash
python3 check-files-for-whitespace.py "<root>" "<extensions>"
```

Parameters:
- `root`: The root directory from which the script will recursively scan files.
- `extensions`: A comma-separated list of file extensions to include in the scan (e.g., `"py,md"`).
