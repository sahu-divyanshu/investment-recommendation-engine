## ✅ Steps to run it on Windows locally

### ✅ 1. **Activate Virtual Environment**

Make sure you're inside your project and have your virtual environment activated:

```powershell
venv\Scripts\activate
```

If not created yet:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### ✅ 2. **Upgrade pip, setuptools, wheel**

These solve many weird install issues:

```bash
python -m pip install --upgrade pip setuptools wheel
```

---

### ✅ 3. **Clean the broken install**

Try this:

```bash
pip uninstall mako -y
```

If that fails:

1. Go to: `C:\Python312\Lib\site-packages`
2. Delete any folder named `mako` or similar (`Mako-*`), and also delete any `.dist-info` folder related to `mako`
3. Also go to: `C:\Python312\Scripts` and delete `mako-render.exe` if it exists

---

### ✅ 4. **Reinstall Mako manually**

Now retry installation:

```bash
pip install mako
```

If this succeeds, go back to your package install commands:

```bash
pip install flask flask-sqlalchemy flask-migrate flask-jwt-extended
pip install flask-cors python-dotenv requests pandas numpy
pip install gunicorn pytest flask-testing
```

---

### ✅ 5. **Temporarily Disable Antivirus (if issue persists)**

Your antivirus might be blocking file renames during install. Temporarily disable it, then repeat the installs.

---

### ✅ 6. **Alternative: Use a virtual environment inside your project**

Sometimes Python installed system-wide can cause permission issues. You can make a virtual env directly:

```bash
cd your-project-dir
python -m venv venv
venv\Scripts\activate
```

Then retry the installs.

---

## 🛠 Final Step: Regenerate `requirements.txt`

Once everything is installed correctly:

```bash
pip freeze > requirements.txt
```

---
# VS Code Debug Guide - Investment Recommendation Engine

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Debug Methods](#debug-methods)
- [Debug Features](#debug-features)
- [Breakpoint Management](#breakpoint-management)
- [Debug Controls](#debug-controls)
- [Variable Inspection](#variable-inspection)
- [Troubleshooting](#troubleshooting)
- [Advanced Debugging](#advanced-debugging)

## Prerequisites

Before debugging, ensure you have:
- ✅ VS Code installed
- ✅ Python extension for VS Code installed
- ✅ Project virtual environment activated
- ✅ All dependencies installed (`pip install -r requirements.txt`)
- ✅ `.vscode` folder created with configuration files

## Setup Instructions

### Step 1: Verify VS Code Configuration
```bash
# Check if .vscode folder exists in project root
ls -la .vscode/

# Should contain:
# - launch.json
# - settings.json  
# - tasks.json
```

### Step 2: Open Project in VS Code
```bash
# Navigate to project directory
cd investment-recommendation-engine

# Open in VS Code
code .
```

### Step 3: Select Python Interpreter
1. Press `Ctrl+Shift+P`
2. Type: `Python: Select Interpreter`
3. Choose: `./venv/Scripts/python.exe`
4. Verify in status bar (bottom-left shows interpreter path)

## Debug Methods

### Method 1: Using Debug Panel (Recommended)

#### Step-by-Step:
1. **Open Debug Panel**
   - Press `Ctrl+Shift+D` OR
   - Click the "Run and Debug" icon in sidebar

2. **Select Debug Configuration**
   - Click dropdown at top of debug panel
   - Select: `Flask: Investment Engine Debug`

3. **Start Debugging**
   - Click green play button ▶️ OR
   - Press `F5`

4. **Set Breakpoints**
   - Open any Python file (e.g., `app/routes/auth.py`)
   - Click on line number where you want to pause
   - Red dot appears = breakpoint set

5. **Test Your API**
   - Open browser: `http://localhost:5000`
   - Make API calls to trigger breakpoints

#### Visual Guide:
```
Debug Panel Layout:
┌─────────────────────────────────┐
│ [Flask: Investment Engine ▼] ▶️ │ ← Configuration & Start
├─────────────────────────────────┤
│ VARIABLES                       │ ← Variable inspection
│ WATCH                          │ ← Custom expressions
│ CALL STACK                     │ ← Execution path
│ BREAKPOINTS                    │ ← Manage breakpoints
└─────────────────────────────────┘
```

### Method 2: Using Command Palette

#### Quick Start:
```bash
# Step 1: Select interpreter
Ctrl+Shift+P → "Python: Select Interpreter" → ./venv/Scripts/python.exe

# Step 2: Start debugging
F5 (starts with default configuration)
```

#### Alternative Commands:
```bash
# Run specific configuration
Ctrl+Shift+P → "Debug: Select and Start Debugging" → Choose config

# Start without debugging
Ctrl+F5 (runs without breakpoints)
```

### Method 3: Using Tasks

#### Available Tasks:
1. **Install Dependencies**
   ```bash
   Ctrl+Shift+P → "Tasks: Run Task" → "Install Dependencies"
   ```

2. **Run Flask Development Server**
   ```bash
   Ctrl+Shift+P → "Tasks: Run Task" → "Run Flask Development Server"
   ```

3. **Run Tests**
   ```bash
   Ctrl+Shift+P → "Tasks: Run Task" → "Run Tests"
   ```

4. **Database Migration**
   ```bash
   Ctrl+Shift+P → "Tasks: Run Task" → "Database Migration"
   ```

5. **Create Migration**
   ```bash
   Ctrl+Shift+P → "Tasks: Run Task" → "Create Migration"
   # Enter migration message when prompted
   ```

## Debug Features

### 1. Flask Debug Mode

#### Automatic Features:
- 🔄 **Hot Reload**: Code changes auto-restart server
- 📝 **Detailed Errors**: Full stack traces in browser
- 🐛 **Interactive Debugger**: Debug directly in browser
- 🎨 **Template Debugging**: Jinja template error highlighting

#### Browser Debug Interface:
```
When Flask error occurs in browser:
┌─────────────────────────────────┐
│ Traceback (most recent call):   │
│ File "app/routes/auth.py", line │
│ [Interactive Console Available] │ ← Click to debug
└─────────────────────────────────┘
```

### 2. Breakpoint Debugging

#### Setting Breakpoints:
```python
# Example: Set breakpoint in auth.py
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()           # ← Click line 25 (example)
    user = User.query.filter_by(        # ← Red dot appears
        email=data['email']             # ← Execution will pause here
    ).first()
```

#### Breakpoint Types:
- 🔴 **Regular Breakpoint**: Pauses execution
- 🔶 **Conditional Breakpoint**: Pauses only if condition is true
- 📊 **Logpoint**: Logs message without stopping

#### Managing Breakpoints:
```bash
# Keyboard shortcuts
F9              # Toggle breakpoint on current line
Ctrl+Shift+F9   # Toggle conditional breakpoint
F5              # Continue execution
F10             # Step over (next line)
F11             # Step into (enter function)
Shift+F11       # Step out (exit function)
```

### 3. Environment Variables

#### Automatic Loading:
- 📄 **`.env` file**: Automatically loaded
- 🔧 **Development mode**: `FLASK_ENV=development`
- 🐛 **Debug mode**: `FLASK_DEBUG=1`
- 🗄️ **Database**: SQLite for development

#### Environment Switching:
```json
// Different configurations in launch.json
"Flask: Investment Engine Debug"     // Development mode
"Flask: Investment Engine (No Debug)" // Production mode
```

### 4. Testing Integration

#### Debug Tests:
1. **Select Test Configuration**
   - Debug panel → `Python: Run Tests`
   - Press `F5`

2. **Set Breakpoints in Tests**
   ```python
   # tests/test_auth.py
   def test_user_registration():
       response = client.post('/api/auth/register', json={
           'username': 'testuser',    # ← Set breakpoint here
           'email': 'test@example.com',
           'password': 'password123'
       })
   ```

## Breakpoint Management

### Setting Breakpoints

#### Method 1: Click Line Numbers
```
app/routes/auth.py
  20    def login():
  21        data = request.get_json()
● 22        user = User.query.filter_by(email=data['email']).first()
  23        if user and user.check_password(data['password']):
```

#### Method 2: Keyboard Shortcut
- Place cursor on desired line
- Press `F9`

#### Method 3: Right-Click Menu
- Right-click on line
- Select "Toggle Breakpoint"

### Conditional Breakpoints

#### Setup:
1. Right-click on line number
2. Select "Add Conditional Breakpoint"
3. Enter condition: `user is None` or `len(data) > 5`

#### Example:
```python
# Only pause if email contains 'admin'
user = User.query.filter_by(email=data['email']).first()  # Condition: 'admin' in data['email']
```

### Logpoints

#### Setup:
1. Right-click on line number
2. Select "Add Logpoint"
3. Enter message: `User login attempt: {data['email']}`

## Debug Controls

### Execution Control
```
F5              Continue execution
F10             Step Over (execute current line)
F11             Step Into (enter function call)
Shift+F11       Step Out (exit current function)
Ctrl+Shift+F5   Restart debugging session
Shift+F5        Stop debugging
```

### Debug Toolbar
```
┌─────────────────────────────────────────┐
│ ▶️ ⏭️ ⬇️ ⬆️ 🔄 ⏹️ │
│ │  │  │  │  │  └─ Stop
│ │  │  │  │  └─ Restart  
│ │  │  │  └─ Step Out
│ │  │  └─ Step Into
│ │  └─ Step Over
│ └─ Continue
└─────────────────────────────────────────┘
```

## Variable Inspection

### During Debug Session

#### Variables Panel:
```
VARIABLES
├── Locals
│   ├── data: {'email': 'user@example.com', 'password': '***'}
│   ├── user: <User object at 0x...>
│   └── access_token: 'eyJ0eXAiOiJKV1Q...'
├── Globals
│   ├── app: <Flask 'app'>
│   ├── db: <SQLAlchemy object>
│   └── request: <Request 'http://localhost:5000/api/auth/login'>
```

#### Hover Inspection:
- Hover over any variable in code
- Tooltip shows current value
- Works for objects, lists, dictionaries

#### Debug Console:
```python
# Type in Debug Console (bottom panel):
>>> user.to_dict()
{'id': 1, 'username': 'testuser', 'email': 'test@example.com'}

>>> db.session.query(User).count()
1

>>> request.json
{'email': 'test@example.com', 'password': 'password123'}
```

### Watch Expressions

#### Add Custom Watches:
1. Click "+" in WATCH panel
2. Enter expression: `user.email`
3. Updates automatically during debugging

#### Useful Watch Expressions:
```python
user.to_dict()                    # User object as dictionary
request.json                      # Request body
db.session.dirty                  # Unsaved changes
app.config['SECRET_KEY']          # Configuration values
```

## Troubleshooting

### Common Issues & Solutions

#### 1. Python Interpreter Not Found
```bash
# Problem: "Python interpreter not found"
# Solution:
Ctrl+Shift+P → "Python: Select Interpreter" → ./venv/Scripts/python.exe
```

#### 2. Module Import Errors
```bash
# Problem: "ModuleNotFoundError: No module named 'app'"
# Solution: Check PYTHONPATH in settings.json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.envFile": "${workspaceFolder}/.env"
}
```

#### 3. Port Already in Use
```bash
# Problem: "Address already in use"
# Solution: Kill existing Flask process
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Or change port in run.py:
app.run(debug=True, port=5001)
```

#### 4. Breakpoints Not Hit
```bash
# Problem: Breakpoints ignored
# Solutions:
1. Check "justMyCode": true in launch.json
2. Ensure breakpoint is on executable line
3. Verify correct Python interpreter selected
4. Restart debug session (Ctrl+Shift+F5)
```

#### 5. Environment Variables Not Loading
```bash
# Problem: .env file not loaded
# Solutions:
1. Check .env file exists in project root
2. Verify "python.envFile" in settings.json
3. Restart VS Code
4. Check .env file format (no spaces around =)
```

### Debug Session Logs
```bash
# Check VS Code output for debug info:
View → Output → Select "Python" from dropdown
```

## Advanced Debugging

### Multi-threaded Debugging
```json
// In launch.json for database operations
{
    "name": "Flask: Multi-thread Debug",
    "type": "python",  
    "request": "launch",
    "program": "${workspaceFolder}/run.py",
    "args": ["--threaded"],
    "justMyCode": false  // Debug into Flask internals
}
```

### Remote Debugging
```python
# For debugging deployed applications
import debugpy
debugpy.listen(5678)
debugpy.wait_for_client()  # Pauses until debugger connects
```

### Database Debugging
```python
# In debug console, inspect database:
>>> from app import db
>>> db.session.execute("SELECT COUNT(*) FROM user").scalar()
1

>>> User.query.all()
[<User 1>, <User 2>]
```

### Performance Debugging
```json
// Add profiling to launch.json
{
    "name": "Flask: Profile Debug",
    "type": "python",
    "request": "launch", 
    "program": "${workspaceFolder}/run.py",
    "args": ["--profile"],
    "console": "integratedTerminal"
}
```

## Quick Reference Card

### Essential Shortcuts
```
F5                 Start/Continue debugging
Ctrl+Shift+F5      Restart debugging  
Shift+F5           Stop debugging
F9                 Toggle breakpoint
F10                Step over
F11                Step into
Shift+F11          Step out
Ctrl+Shift+D       Open debug panel
Ctrl+Shift+P       Command palette
Ctrl+`             Toggle terminal
```

### Debug Panel Sections
```
VARIABLES          Current variable values
WATCH              Custom expressions to monitor  
CALL STACK         Function execution path
BREAKPOINTS        Manage all breakpoints
DEBUG CONSOLE      Execute code during debug
```

### Common Debug Scenarios
```python
# 1. API endpoint debugging
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # ← Breakpoint: inspect request
    # ... rest of function

# 2. Database operation debugging  
user = User.query.filter_by(email=email).first()  # ← Breakpoint: check query

# 3. Error handling debugging
try:
    # ... some operation
except Exception as e:
    print(f"Error: {e}")  # ← Breakpoint: inspect exception
```

---

**Happy Debugging! 🐛✨**

For more advanced debugging techniques, check the [VS Code Python debugging documentation](https://code.visualstudio.com/docs/python/debugging).