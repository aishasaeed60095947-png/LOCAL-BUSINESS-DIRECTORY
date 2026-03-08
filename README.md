# Local Business & Startup Directory

A web-based platform to showcase startups and businesses within the university community. This application transitions from terminal-based logic to an interactive web presence using the Flask framework.

## Key Features
- **Business Viewing**: A comprehensive homepage listing all registered businesses with their OOP-generated summaries.
- **Business Registration**: An interactive HTML form that allows the community to add new businesses to the directory seamlessly.
- **Recently Added (Stack)**: Highlights the last 3-5 registered businesses using a custom-built Stack data structure, demonstrating LIFO (Last-In-First-Out) methodology.
- **Timestamping**: All entries are precisely timestamped using the Python `datetime` module upon registration.

## Technical Requirements Fulfilled
- **OOP Integration**: Core logic is encapsulated within the `Business` class in `models.py`. Includes attribute management and behavior methods like `get_summary()`.
- **Data Structures**: Created a `BusinessStack` class that intelligently uses Python lists and slicing to strictly operate as a LIFO stack.
- **Web UI (Flask)**: Secure, template-driven routing (`/` and `/add`) connected to a visually premium frosted-glass UI.

## Local Setup & Installation

To run this project on your local machine, follow these steps:

1. **Setup a Virtual Environment (Recommended but optional)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install Dependencies**
   Install Flask via pip:
   ```powershell
   pip install flask
   ```

3. **Run the Application**
   Start the development server:
   ```powershell
   python app.py
   ```

4. **View the Dashboard**
   Open your browser and navigate to `http://127.0.0.1:5000/`. You can immediately start registering test businesses!
