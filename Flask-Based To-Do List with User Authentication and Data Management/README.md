# SkillUp Projects: Task Manager Web Application

Welcome to the SkillUp Projects Task Manager Web Application! This Flask-based web application allows users to register, login, manage tasks, and logout seamlessly. It provides a user-friendly interface for managing tasks efficiently.

## Features

- **User Registration**: Users can sign up for a new account by providing a unique username and password.
- **User Authentication**: Secure user authentication ensures that only registered users can access the system.
- **Task Management**: Users can manage their tasks, including adding, updating, and deleting tasks.
- **Session Management**: The application maintains user sessions for seamless navigation and user experience.
- **Data Persistence**: User task data is stored persistently in JSON format on the server.
- **Responsive Design**: The web application is designed to be responsive and works well across various devices and screen sizes.

## Project Structure

- **`app.py`**: This file contains the main Flask application code, including route definitions for various endpoints such as registration, login, task management, and logout.
- **`authentication.py`**: Manages user authentication functionalities such as user registration, login authentication, and password hashing.
- **`filemanagement.py`**: Handles file operations such as creating and updating user-specific JSON files to store task data.
- **`templates`**: This directory contains HTML templates for rendering different pages of the web application.
- **`static`**: Contains static assets such as CSS files, images, and client-side JavaScript files.

## Setup Instructions

To run the project locally, follow these steps:

1. Clone the repository from [GitHub - arycodes/skillup-projects](https://github.com/arycodes/skillup-projects.git).
2. Ensure you have Python and Flask installed on your system.
3. Navigate to the project directory.
4. Run `pip install -r requirements.txt` to install the required dependencies.
5. Set the Flask app secret key in `app.py` to a secure value.
6. Run `python app.py` to start the Flask development server.
7. Access the application in your web browser at `http://localhost:5000`.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About

This project is part of the SkillUp Projects initiative, aimed at providing hands-on coding experience and building practical skills in web development.

For more projects and resources, visit [SkillUp Projects](https://github.com/arycodes/skillup-projects).

Thank you for using the SkillUp Task Manager Web Application! Happy task managing! 🚀