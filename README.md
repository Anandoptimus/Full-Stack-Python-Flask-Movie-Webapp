# Flask Movie Ratings

This Flask Movie Ratings project is a web application that allows users to manage and track their top 10 favorite movies. Users can add, edit, and delete movies, as well as provide ratings and reviews for each film.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Usage](#setup-and-usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **View Movies:** Display a list of top 10 favorite movies with rankings.
- **Edit Movies:** Modify movie ratings and reviews.
- **Delete Movies:** Remove movies from the list.
- **Add Movies:** Add new movies using The Movie Database (TMDb) API.
- **Responsive Design:** The application is designed to be responsive for a seamless experience on various devices.

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Python with Flask
- **Database:** SQLite for storage
- **API:** The Movie Database (TMDb) for movie information
- **Version Control:** Git and GitHub

## Setup and Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Anandoptimus/flask-movie-ratings.git
    cd flask-movie-ratings
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Key:**

    Obtain an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api) and replace `API_KEY` in `main.py` with your key.

4. **Initialize the Database:**

    ```bash
    python main.py
    ```

5. **Run the Application:**

    ```bash
    python main.py
    ```

6. **Access the Application:**

    Open your web browser and go to http://localhost:5000/ to access the application.

## Project Structure

- **main.py:** The main application file containing the Flask web server setup.
- **templates/:** Contains HTML templates for rendering pages.
- **static/:** Static files (CSS, images, etc.).
  - **css/styles.css:** Stylesheet for the application.
- **movies.db:** SQLite database file.

## Screenshots

![image](https://github.com/Anandoptimus/Flask-Movie-Webapp/assets/101982906/702d0d84-c3d7-4489-ac4d-d51bf189b093)
![image](https://github.com/Anandoptimus/Flask-Movie-Webapp/assets/101982906/13b2bc7d-fd76-4b5d-847e-86e7c8ebf381)
![image](https://github.com/Anandoptimus/Flask-Movie-Webapp/assets/101982906/9d8fc140-22bb-45f4-acca-aa11031685c4)
![image](https://github.com/Anandoptimus/Flask-Movie-Webapp/assets/101982906/17651238-fcaf-435c-ac18-a85b2c7ef1db)


## Contributing

Contributions are welcome! Please follow the Contributing Guidelines for detailed instructions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **Flask:** A lightweight web application framework in Python that made building the backend seamless.
- **SQLite:** A simple and efficient database engine used for storing movie information.
- **Bootstrap:** A front-end framework that provided a clean and responsive design for the user interface.
- **The Movie Database (TMDb):** An API used for fetching movie details.
- **Font Awesome:** For icons used in the project, enhancing the overall visual appeal.
- **Git and GitHub:** Essential tools for version control and collaborative development.
