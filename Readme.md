# PC Automation Framework

## Overview

This project is a Python and Robot Framework based automation framework developed for automating software update workflows in a Network Management application.

The framework uses:

* Python
* Robot Framework
* SeleniumLibrary
* Selenium WebDriver
* ChromeDriver Manager

---

## Project Structure

```text
pc_automation/
│
├── lib/
│   └── automation.py
│
├── resources/
│   └── CommonKeywords.robot
│
├── testbed/
│   ├── pc_elements.py
│   └── pc_variables.py
│
├── testsuites/
│   └── Login_Test.robot
│
├── logs/
│
├── report.html
├── log.html
├── output.xml
└── README.md
```

---

## Framework Components

### 1. lib/

Contains Python automation scripts.

**automation.py**

* Launches Chrome browser
* Opens application URL
* Performs Login
* Navigates to Software Update page
* Selects devices
* Creates software update job
* Starts deployment

---

### 2. resources/

Contains reusable Robot Framework keywords.

**CommonKeywords.robot**

Keywords available:

```robot
Login pc Application
Install IOSXR Image
Close pc Application
```

These keywords can be reused across multiple test suites.

---

### 3. testbed/

Contains test data and object repository.

**pc_elements.py**

* Stores locators

**pc_variables.py**

* Stores environment variables
* Test data
* Configuration values

---

### 4. testsuites/

Contains Robot Framework test cases.

**Login_Test.robot**

Sample Test:

```robot
Install Software ON IOSXR
    Login pc Application
    Install IOSXR Image
    Close pc Application
```

---

## Prerequisites

Install Python 3.11+

Install required packages:

```bash
pip install robotframework
pip install robotframework-seleniumlibrary
pip install selenium
pip install webdriver-manager
```

---

## Execute Python Script

```bash
python lib/automation.py
```

---

## Execute Robot Test Suite

Run all test cases:

```bash
robot testsuites/
```

Run specific test suite:

```bash
robot testsuites/Login_Test.robot
```

---

## Reports Generated

After execution Robot Framework generates:

| Report      | Description            |
| ----------- | ---------------------- |
| report.html | Execution Summary      |
| log.html    | Detailed Execution Log |
| output.xml  | Raw Execution Results  |

---

## Automation Workflow

1. Launch Browser
2. Open Network Management Application
3. Login with credentials
4. Navigate to Software Update section
5. Select devices
6. Configure deployment job
7. Start software update
8. Generate execution reports

---

## Technologies Used

* Python
* Selenium WebDriver
* Robot Framework
* SeleniumLibrary
* ChromeDriver Manager

---

## Author

Venkata Sai Mandapati

Automation Engineer

Experience: 3.3 Years

Skills:

* Python
* Selenium
* Robot Framework
* Playwright
* Pytest
* API Testing
* Jenkins
* Git
* Linux
