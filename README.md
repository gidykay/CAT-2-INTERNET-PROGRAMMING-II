# Obituary Management Platform

A web application for submitting, managing, and displaying obituaries. The platform supports SEO and social media optimization features.

## Features
- Submit obituaries with name, date of birth, date of death, content, and author.
- View a list of submitted obituaries.
- Includes SEO optimization (meta tags, Open Graph tags).
- Social media sharing integration.

## Technologies Used
- **Flask**: A lightweight Python web framework.
- **MySQL**: Database for storing obituary data.
- **HTML, CSS, JavaScript**: For frontend development.
- **Flask-MySQLdb**: MySQL database connector for Flask.
- **Jinja2**: Templating engine for dynamic HTML rendering.

## Installation

### Step 1: Clone the repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/yourusername/Internet-programming-2.git

Step 2: Install Dependencies

Navigate to the project directory and install the required Python dependencies:

pip install -r requirements.txt

Step 3: Setup the Database

Ensure you have MySQL installed and running locally.

1. Create a new database obituary_platform.


2. Create a table called obituaries with the following columns:

id (INT, Primary Key, Auto Increment)

name (VARCHAR(100))

date_of_birth (DATE)

date_of_death (DATE)

content (TEXT)

author (VARCHAR(100))

submission_date (DATETIME, default to current timestamp)

slug (VARCHAR(255), Unique)




Step 4: Run the Application

Start the Flask application by running:

python app.py

The app will be available at http://127.0.0.1:5000.

Usage

Submit an Obituary:

Go to the homepage (/) and fill in the form to submit an obituary.

After submission, the obituary will be saved to the database.


View Submitted Obituaries:

Go to /obituaries_list to view a list of all submitted obituaries.


SEO and Social Media Optimization

The platform includes meta tags for SEO and Open Graph tags for better social media sharing previews.


License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Thanks to Flask and MySQL for powering this platform.

Special thanks to open-source contributors.


### Instructions for customizing:
1. **Replace the GitHub URL**: Replace the `https://github.com/yourusername/Internet-programming-2.git` with your actual GitHub repository link.
2. **Add License (if applicable)**: If you use any license, you can add the respective license text in the **License** section.
3. **Add additional info if needed**: You can update sections like **Acknowledgments** or any other specific details about your project.
