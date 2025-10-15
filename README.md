# Barangay Survey Generator

A lightweight FastAPI application for creating and managing surveys for barangay communities in the Philippines. This tool helps local government units (LGUs) gather community feedback, conduct polls, and make data-driven decisions.

## Features

- **Easy Survey Creation**: Create surveys with multiple question types (text, single choice, multiple choice)
- **Real-time Results**: View responses and analytics as they come in
- **Community Focused**: Designed specifically for barangay management in the Philippines
- **Responsive Design**: Modern UI with Tailwind CSS that works on all devices
- **SQLite Database**: Lightweight, file-based database for easy deployment
- **MVC Architecture**: Clean, maintainable code structure

## Question Types

- **Text Answer**: Open-ended text responses
- **Single Choice**: Radio button selection (one answer only)
- **Multiple Choice**: Checkbox selection (multiple answers allowed)

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd barangay-survey-generator
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and go to: `http://localhost:8000`

## Usage

### Creating a Survey

1. Click "Create Survey" on the home page
2. Enter a title and description for your survey
3. Click "Create Survey" to proceed to the question editor
4. Add questions using the form:
   - Enter your question text
   - Select question type (text, single choice, multiple choice)
   - For choice questions, enter options separated by commas
   - Mark questions as required or optional
5. Click "Add Question" to add each question

### Taking a Survey

1. Share the survey link with community members
2. Respondents can access the survey and fill out their responses
3. Responses are automatically saved to the database

### Viewing Results

1. Click "View Results" on any survey
2. See summary statistics and individual responses
3. For choice questions, view percentage breakdowns
4. Export or analyze the data as needed

## API Endpoints

- `GET /` - Home page with list of active surveys
- `GET /create` - Survey creation form
- `POST /create` - Create a new survey
- `GET /survey/{id}` - View and take a survey
- `POST /survey/{id}/submit` - Submit survey responses
- `GET /survey/{id}/edit` - Edit survey questions
- `POST /survey/{id}/add-question` - Add a new question
- `DELETE /survey/{id}/question/{qid}/delete` - Delete a question
- `GET /survey/{id}/results` - View survey results
- `GET /survey/{id}/thanks` - Thank you page after submission

## Database Schema

The application uses SQLite with the following tables:

- **surveys**: Survey metadata (title, description, creation date)
- **questions**: Survey questions with type and options
- **responses**: Individual survey responses
- **answers**: Answers to specific questions

## Customization

### Styling

The application uses Tailwind CSS for styling. You can customize the appearance by:

1. Modifying the color scheme in `templates/base.html`
2. Updating the Tailwind configuration
3. Adding custom CSS classes

### Branding

Update the following files to match your barangay's branding:

- `templates/base.html` - Navigation and footer
- `templates/home.html` - Hero section and features
- Logo and colors can be customized in the base template

## Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

For production deployment, consider:

1. **Using a production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **Environment variables** for configuration
3. **Reverse proxy** (nginx) for static files and SSL
4. **Database backup** strategies for SQLite
5. **Security considerations** for public deployment

## Contributing

This project is part of [The Puso Project](https://www.thepusoproject.ph/solutions) - an initiative to build digital solutions for Philippine barangays.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or support:

- Visit [The Puso Project](https://www.thepusoproject.ph/solutions)
- Join the community discussions
- Report issues through the project repository

## Roadmap

Future enhancements may include:

- User authentication and role management
- Survey templates and themes
- Data export functionality (CSV, PDF)
- Advanced analytics and reporting
- Multi-language support (Filipino, English)
- Integration with other barangay management tools
- Mobile app companion
- Email notifications and reminders

---

**Built with ❤️ for Philippine barangays by [The Puso Project](https://www.thepusoproject.ph/solutions)**