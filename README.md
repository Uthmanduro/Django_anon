# Anonymous Website

## Overview

This is an anonymous messaging website inspired by features similar to Kubool. Users can send and receive anonymous messages without revealing their identities. The platform provides a space for open communication while maintaining user privacy.

## Features

- **Anonymous Messaging:** Send and receive messages without revealing your identity.
- **Inbox:** View and manage received messages securely.
- **Message Tracking:** Keep track of the status of sent messages (read/unread).
- **User Privacy:** Prioritize user privacy and anonymity.

## Getting Started

### Prerequisites

- Ensure you have [Python](https://www.python.org/) installed.
- Set up a virtual environment:

  ```bash
  python -m venv venv
  source venv/bin/activate  # For Linux/Mac
  # or
  .\venv\Scripts\activate  # For Windows
  
### Installation
Clone the repository:

```
git clone https://github.com/uthmanduro/Django_anon.git
```
Install dependencies:

```
pip install -r requirements.txt
```
Configure the settings:

Set up your database in config/settings.py.
Customize other settings such as secret key, etc.
Run migrations:
```
python manage.py migrate
```
Start the development server:

```
python manage.py runserver
```
Access the website at http://localhost:8000/.

#### Usage
Navigate to the website.
Create an account or log in if you already have one.
Explore the features, send and receive anonymous messages.
Contributing
Contributions are welcome! Please follow our contribution guidelines.

### License
This project is licensed under the MIT License.


