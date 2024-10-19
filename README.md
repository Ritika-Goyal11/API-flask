# Geolocation Flask App

## Overview

This project is a simple web application built with Flask that allows users to retrieve geolocation information based on an IP address. Utilizing the [IP Geolocation API](https://ipgeolocation.io/), users can input an IP address to get details about its location.

## Features

- Fetch geolocation data for a provided IP address.
- Automatically retrieves the geolocation of the server's IP if none is provided.
- User-friendly interface for easy IP input and results display.
- Error handling for invalid IP addresses.

### Prerequisites

- Python 3.x
- Flask
- Requests
- An API key from [IP Geolocation API](https://ipgeolocation.io/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ritika-Goyal11/API-flask
   cd geolocation-flask-app
   ```

2. **Set up your environment variables:**

   Creating a `.env` file in the root directory and adding the API key:

   ```
   API_KEY=api_key_here
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the application:**

   ```bash
   python geoloc.py
   ```

   The application will be available at `http://localhost:5000`.
2. **Access the application:**
   - Going to the home page and giving an IP address as input to fetch geolocation data.
   ![Input Page](https://github.com/user-attachments/assets/151a5696-2a9a-4620-9f8e-b1f6dd544e1a)


### Using Docker

To run the application using Docker, following these steps:

1. **Build the Docker image:**

   ```bash
   docker build -t geolocation-flask-app .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 --env-file .env geolocation-flask-app
   ```
**Link to Docker image:**
   ```bash
  docker pull ritikagoyal11/geo-location:latest
   ```

### Pushing to GitHub

To push the changes to GitHub, following the steps mentioned below:

1. **Stage the changes:**

   ```bash
   git add .
   ```

2. **Commit the changes:**

   ```bash
   git commit -m "First commit"
   ```

3. **Push to the main branch:**

   ```bash
   git push origin main
   ```

## File Structure

```
geolocation-flask-app/
├── geoloc.py               # Main application file
├── Dockerfile              # Dockerfile for containerization
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── home.html          # Display location information
│   ├── input.html         # Input form for IP address
│   └── error.html         # Error display page in case of wrong IP address
└── static/                 # Static files
    └── style.css          # Custom styles for the app
```
## Final Page
![IP Information Page](https://github.com/user-attachments/assets/e90e09e8-1211-4451-915a-4b8eca879a1d)
