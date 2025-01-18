# Installation Guide for Database_ORM

## 1. Setting Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.
It is recommended to skip points one to seven

### 1.1 Creating the Virtual Environment
Open a terminal or command prompt and navigate to the project folder:
```sh
cd /path/to/your/project
```
Then, create a virtual environment named `venv`:
```sh
python -m venv venv
```

### 1.2 Activating the Virtual Environment
#### Windows:   (skip on VSC)
```sh
venv\Scripts\activate
```
#### macOS/Linux:
```sh
source venv/bin/activate
```
After activation, you should see `(venv)` at the beginning of the terminal prompt.

---

## 2. Installing Required Packages

### 2.1 Updating `pip`
Ensure `pip` is up to date before installing dependencies:
```sh
pip install --upgrade pip
```

### 2.2 Installing `mysql-connector-python`
This package is required to connect Python with MySQL:
```sh
pip install mysql-connector-python
```

### 2.3 Installing Other Dependencies (if any)
If your project has additional dependencies, install them using:
```sh
pip install -r requirements.txt
```
Ensure that a `requirements.txt` file exists in the project folder listing all dependencies.

---

## 3. Configuring the Database Connection
Modify the `config.json` file in your project to include the correct database credentials:
```json
{
    "database":{
        "host":"your-database-host",
        "port":3306,
        "user":"your-username",
        "password":"your-password",
        "database":"your-database-name"
    },
    "logging":{
        "level":"ERROR",
        "log_file":"app.log"
    }
}
```

---

## 4. Running the Application
Once everything is installed and configured, start the application using:
```sh
python main.py
```

If you encounter issues, ensure that:
- The virtual environment is activated.
- The database connection details are correct.
- The required packages are installed properly.

---

## 5. Deactivating the Virtual Environment
When you are done working, deactivate the virtual environment using:
```sh
deactivate
```

This will return you to the system-wide Python environment.

---

## 6. Additional Commands

### 6.1 Checking Installed Packages
To verify installed dependencies:
```sh
pip freeze
```

### 6.2 Creating a `requirements.txt` File
To generate a list of installed packages:
```sh
pip freeze > requirements.txt
```
This file can be used to install the same dependencies in another environment using:
```sh
pip install -r requirements.txt
```

---

## 7. Troubleshooting
### Issue: `mysql-connector-python` Installation Fails
Try using:
```sh
pip install mysql-connector-python --no-cache-dir
```
If the issue persists, check that you have a compatible Python version installed (recommended: Python 3.8+).

### Issue: Database Connection Error
- Verify the database credentials in `config.json`.
- Ensure MySQL server is running.
- Check if the MySQL port (3306) is open and accessible.

---

Now you're ready to use Database_ORM! 🚀


## 1 try easy way

### 1.1
```sh
python -m venv venv
```
### 1.2
```sh
.\venv\Scripts\pip.exe install -r requirements.txt
```
