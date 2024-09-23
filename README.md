# Django Mail Sender Project

This is a simple Django project that allows users to send emails through a web form using their Gmail account. It features a basic interface for composing and sending emails, along with success or failure feedback messages.

## Features

- Email form with fields for recipient address, subject, and message.
- Sends email via Gmail's SMTP server.
- Displays success or failure messages based on email delivery.
- Responsive, simple CSS styling.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Django 5.x
- Gmail account with App Password enabled (for security reasons, regular account passwords are not supported)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mailsender.git
   cd mailsender
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the project root and add the following lines, replacing `your_email@gmail.com` and `your_app_password` with your own credentials:
   ```bash
   DJANGO_SECRET_KEY=your-secret-key
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

6. Run database migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

8. Visit the app in your browser:
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) and start sending emails.

## Project Structure

- **mailsender/**: Main project directory.
- **mailsender/settings.py**: Contains Django settings, including email configuration.
- **mailsender/views.py**: Handles the email-sending logic.
- **templates/index.html**: HTML form for composing and sending emails.
- **static/style.css**: Custom CSS for the project.
- **urls.py**: Maps the homepage URL to the mail sending view.

## How it Works

1. The user fills out the email form (recipient, subject, and message).
2. Upon submission, the form data is processed by the `send_mail_page` view.
3. The `send_mail()` function from Django's `core.mail` module sends the email.
4. Success or failure messages are displayed based on the outcome.

## Environment Variables

- `DJANGO_SECRET_KEY`: Your Django secret key.
- `EMAIL_HOST_USER`: Your Gmail address.
- `EMAIL_HOST_PASSWORD`: The App Password generated for your Gmail account.

## Screenshots

![Screenshot of the Mail App](images/Screenshot%20(99).png)

## License

This project is licensed under the MIT License. Feel free to modify and distribute.

## Contributions

Feel free to submit issues, fork the repo, or create pull requests!

## Troubleshooting

- Ensure you have enabled "App Passwords" in your Google Account settings to use Gmail with this project.
- If the email fails to send, check your environment variables and ensure that all required fields are filled out in the form.
