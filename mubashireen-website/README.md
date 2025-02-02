# Mubashireen Website

## Overview
The Mubashireen website is a modern web application built using Streamlit, designed to present the corporation "Mubashireen." The mission of Mubashireen is to provide "good news" through innovative AI solutions tailored for various clients.

## Project Structure
```
mubashireen-website
├── src
│   ├── home
│   │   └── home.py          # Main content for the home page
│   ├── team
│   │   └── team.py          # Presentation of team members
│   ├── product_requests
│   │   └── product_requests.py # Interface for product requests
│   ├── login_signup
│   │   └── login_signup.py   # User authentication handling
│   └── utils
│       └── styles.py         # Styling functions and constants
├── .streamlit
│   └── config.toml           # Configuration settings for Streamlit
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation
```

## Features
- **Home Page**: Introduces Mubashireen and its mission.
- **Team Presentation**: Showcases team members with pictures and descriptions.
- **Product Requests**: Allows users to submit requests for products.
- **Login/Sign-Up**: User authentication for accessing additional features.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd mubashireen-website
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```
   streamlit run src/home/home.py
   ```

## Usage Guidelines
- Access the home page to learn about Mubashireen.
- Navigate to the team section to view team members.
- Use the product requests section to submit inquiries.
- Log in or sign up to access personalized features.

## License
This project is licensed under the MIT License.