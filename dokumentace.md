# Database\_ORM Documentation

## 1. Project Information

- **Project Name:** Database\_ORM
- **Author:** Martin Hornych
- **Contact:** [hornych@spsejecna.cz](mailto\:hornych@spsejecna.cz)
- **Date:** 2025-01-17
- **School:** Střední průmyslová škola elektrotechnická Ječná
- **Project Type:** School project

---

## 2. User Requirements

This project is part of the **IOTA (ι - ióta) group** and must implement **Object-Relational Mapping (ORM)** using the **Mapper pattern**.

---

## 3. Application Architecture

### Design Patterns Used

- **Singleton**: Used to ensure a single instance of key objects (e.g., database connection manager).
- **ORM (Object-Relational Mapping)**: Enables seamless interaction between Python objects and a MySQL database.

### UML Diagrams

DOPLNIT
---

## 4. Application Behavior

### UML Behavioral Diagrams

DOPLNIT

---

## 5. Database Model

### Entity-Relationship (E-R) Diagram

DOPLNIT

---

## 6. File Import/Export

### Supported Formats

- **CSV**: The application supports importing and exporting customer data from CSV files.

### Example CSV Format

```csv
id,name,email,phone,is_vip,loyalty_points
1,John Doe,johndoe@example.com,+123456789,true,100.5
2,Jane Smith,janesmith@example.com,+987654321,false,50.0
```

### Data Validation Rules

- **ID:** Must be an integer.
- **Email:** Must be a valid email format.
- **Phone:** Must contain only numbers and optional `+`.
- **Loyalty Points:** Must be a positive floating-point number.

---

## 7. Configuration Settings

Configuration is stored in `config.json`:

```json
{
    "database":{
        "host":"18.199.158.215",
        "port":3306,
        "user":"hornych1app",
        "password":"moje heslo*",
        "database":"Hotel"
    },
    "logging":{
        "level":"ERROR",
        "log_file":"app.log"
    }
}
```

### Configuration Options

- **Database Settings**: Host, port, user, password, and database name.
- **Logging Settings**: Log level and log file location.

---

## 8. Installation & Execution

### Installation

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```sh
   pip install mysql-connector-python
   ```

### Running the Application

```sh
python main.py
```

---

## 9. Error Handling

### Common Errors and Solutions

| Error                         | Cause                                  | Solution                             |
| ----------------------------- | -------------------------------------- | ------------------------------------ |
| `Invalid phone number format` | Non-numeric characters entered         | Ensure only numbers and `+` are used |
| `Database connection failed`  | Incorrect credentials in `config.json` | Verify database settings             |
| `Invalid email format`        | Email does not contain `@` and `.`     | Provide a valid email                |

---

## 10. Third-Party Libraries

- `mysql-connector-python`: MySQL database connection
- `json`: Configuration management
- `csv`: Import/export functionality

---

## 11. Project Summary

### Project Goals

The main goal was to design and implement a **fully universal ORM** for database interaction.

### Technologies Used

- **Programming Language:** Python
- **Database:** MySQL (via MySQL Workbench)
- **Design Patterns:** Singleton, ORM

### Challenges Faced

- Understanding and designing a functional ORM system.
- Ensuring modularity for future expansions.

### Future Enhancements

- **Admin Interface** for managing database records.
- **Customer Interface** to allow individual users to access their data.

---

