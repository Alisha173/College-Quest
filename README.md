
# College Quest

**College Quest** is a web-based platform designed to assist students in their search for the best colleges. The application is powered by **Flask** and utilizes data stored in **CSV files** to provide college information. It enables students to search and filter colleges based on criteria like location, available courses, and budget.

## Key Features

- **College Search**: Quickly search colleges by their location, available courses, and your budget.
- **Data-Driven**: The platform relies on CSV files that are updated periodically with new college data.
- **User-Friendly Interface**: Designed with user experience in mind, the app uses Flask to dynamically generate pages.
- **Comprehensive Information**: Each college entry includes detailed information to help users make informed decisions.

## Prerequisites

To run the project, you need to have the following:

- Python 3.x
- Pip (Python package manager)
- Git (for version control)

## Getting Started

Follow these steps to get started with the **College Quest** project:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Alisha173/College-Quest.git
```

### 2. Set Up a Virtual Environment

It is recommended to set up a virtual environment to avoid dependency conflicts. Run these commands:

```bash
cd College-Quest
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

After activating the virtual environment, install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Once all dependencies are installed, you can run the app with:

```bash
python app.py
```

The app will be available at `localhost:5000`. Open your browser and go to `http://127.0.0.1:5000` to access the application.

## Folder Structure

The project contains the following folder structure:

```
College-Quest/
│
├── Instance/                  # Instance-specific files
├── CSV files/                 # CSV data for colleges
├── Program Codes/             # Python files for the backend logic
├── Static/                    # Static files such as CSS and JS
├── Templates/                 # HTML templates for Flask
├── app.py                     # Main Flask application script
├── .gitignore                 # Git ignore file to exclude unnecessary files
└── requirements.txt           # Python libraries required for the project
```

## Contribution

Feel free to fork the repository and submit pull requests if you would like to contribute to the project. All contributions are welcome!


## Acknowledgments

- Special thanks to the Flask framework for enabling easy web development.
- Thanks to the open-source community for providing useful libraries and resources.
