# Tests - Python - Selenium

## Description

This repository contains automated testing for browser.

## Configuration

The configuration for browser follows this generic schema:

1. Pydantic default values
2. config file
3. Environment variables

### Browser

The order of loading variables/secrets is as follows:

1. Pydantic default values: These are the default values specified in the code.
2. Config file: configuration file can be used to override default values.
3. Environment variables: Environment variables can further override settings.
4. `.env` file: For local development, the `.env` file is automatically loaded to set environment variables.

- The environment variables have the highest priority.

## Setup

Pre-requisites:

- Python 3.10 or higher
- pip
- Chrome/Chromium/Edge browser/Firefox browser (dependin on required driver)

### On Windows

Environment setup:

```powershell
pip install -r requirements-windows.txt # run with privileged user
copy .env.example .env
```

Browser setup:

1. Extract the certificate by running `python -m seleniumwire extractcert`. That will produce a file called ca.crt in the current working directory.
2. Open Chrome/Other's settings and search for "Manage certificates".
3. On the Manage certificates screen, click the "Authorities" tab and then "Import".
4. Select the ca.crt file and ensure that you check all boxes relating to trust settings before clicking "OK".
5. Restart your browser.

### On Linux

Environment setup:

```bash
pip install -r requirements-linux.txt
cp .env.example .env
sudo apt-get install openssl
```

Browser setup:

1. Extract the certificate by running `python3 -m seleniumwire extractcert` in the current directory. That will produce a file called ca.crt in the current working directory.
2. Open Chrome/Other's settings and search for "Manage certificates".
3. On the Manage certificates screen, click the "Authorities" tab and then "Import".
4. Select the ca.crt file and ensure that you check all boxes relating to trust settings before clicking "OK".
5. Restart your browser.

## Run Tests

On Windows:

```powershell
source .env && export $(cut -d= -f1 < .env)
```

```powershell
pytest tests/ -k browser
```

On Linux:

```powershell
source .env && export $(cut -d= -f1 < .env)
```

```bash
pytest tests/ -k browser
```

## TODOs

Nice to have things:

- [ ] Remove unused libraries from requirements.txt.
- [ ] Optimize imports.
- [ ] Add configuration mechanism for better flexibility and add tests for it.
- [ ] Implement a nice logger instead of prints.
- [ ] Add more verbosity for logging.
- [ ] Add a mechanism to run tests in parallel.
- [ ] Update functions and methods docs with docstrings.
- [ ] Standardize selectors.
- [ ] Add a setup.py for dynamic requirements based on OS.
- [ ] Add a mechanism to run tests in headless mode.
- [ ] Add a mechanism for better config profiles for the variables.
- [ ] Add a mechanism for various resolution testing.
- [ ] Add a API configuration.