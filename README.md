# University Admission System

## Overview

In Poland, there is currently a lack of an integrated recruitment system that facilitates nationwide university applications. Each university uses different tools, making the recruitment process more challenging to manage. This project aims to create a platform that streamlines the admission process, benefiting both applicants and universities.

The system will allow applicants to submit applications, browse available programs, and track their application status. Universities will have tools to manage applications and evaluate candidates efficiently.

The system is built using the Django framework.

## Getting Started

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd system-rekrutacji
   ```

2. **Create a Virtual Environment:**

   It is recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   Use the following command to install all required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**

   Run the following command to apply database migrations:

   ```bash
   python manage.py migrate
   ```

To access the admin functionality, create a superuser account.

Since the database is initially empty, you need to populate it with data necessary for testing and using the application fully.

### Running the Server

Once everything is set up, start the development server with:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

