# Python Virtual Environment Setup & Dependency Installation

This guide explains how to create a Python virtual environment (venv) and install the required dependencies for this project.

## Prerequisites

* Python **3.8 or newer** installed
* `pip` available (usually bundled with Python)

You can verify your Python installation with:

```bash
python --version
pip --version
```

---

## Step 1: Create a Virtual Environment (venv)

It is strongly recommended to use a virtual environment to isolate project dependencies.

### On Linux / macOS

```bash
python3 -m venv venv
```

### On Windows

```bash
python -m venv venv
```

This will create a folder named `venv` in your project directory.

---

## Step 2: Activate the Virtual Environment

### On Linux / macOS

```bash
source venv/bin/activate
```

### On Windows (Command Prompt)

```bat
venv\Scripts\activate
```

### On Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

Once activated, your terminal prompt should change to indicate that the virtual environment is active.

---

## Step 3: Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

## Step 4: Install Required Python Packages

Install the external dependencies using `pip`:

```bash
pip install pynput cryptography
```

### Notes on Standard Libraries

The following modules **do not need to be installed** because they are part of Python’s standard library:

* `socket`

You can import them directly in your code:

```python
import socket
```

---

## Step 5: Verify Installation

You can verify that the packages are installed correctly by running:

```bash
pip list
```

Or by testing imports in Python:

```bash
python
```

```python
import pynput
from cryptography.fernet import Fernet
import socket
```

If no errors appear, the setup was successful.

---

## Deactivating the Virtual Environment

When you are done working on the project, deactivate the virtual environment with:

```bash
deactivate
```

---

## Summary

* `venv` is used to isolate project dependencies
* `pynput` and `cryptography` must be installed via `pip`
* `socket` are built-in Python libraries

Your environment is now ready for development.
