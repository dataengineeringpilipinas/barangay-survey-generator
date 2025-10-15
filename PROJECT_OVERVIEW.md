# Barangay Survey Generator - Project Overview

## 🎯 Project Summary

A lightweight FastAPI application designed specifically for Philippine barangays to create, manage, and analyze community surveys. This tool helps local government units gather feedback, conduct polls, and make data-driven decisions for better community governance.

## 🏗️ Architecture

**Framework**: FastAPI with MVC (Model-View-Controller) architecture
**Database**: SQLite (lightweight, file-based)
**Frontend**: Jinja2 templates with Tailwind CSS
**Backend**: Python 3.8+ with SQLAlchemy ORM

## 📁 Project Structure

```
barangay-survey-generator/
├── app.py                 # Main FastAPI application
├── run.py                 # Startup script with auto-reload
├── demo_data.py           # Sample data generator
├── requirements.txt       # Python dependencies
├── README.md             # Comprehensive documentation
├── .gitignore            # Git ignore rules
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Homepage with survey listings
│   ├── create_survey.html # Survey creation form
│   ├── edit_survey.html  # Question editor interface
│   ├── survey.html       # Survey taking interface
│   ├── results.html      # Results and analytics view
│   └── thanks.html       # Thank you page
└── static/               # Static files directory
```

## 🚀 Key Features

### Survey Management
- ✅ Create surveys with custom titles and descriptions
- ✅ Add multiple question types (text, single choice, multiple choice)
- ✅ Mark questions as required or optional
- ✅ Edit and delete questions dynamically
- ✅ Preview surveys before publishing

### Response Collection
- ✅ Anonymous and named responses
- ✅ Real-time form validation
- ✅ Mobile-responsive design
- ✅ Thank you confirmation page

### Analytics & Results
- ✅ Real-time response tracking
- ✅ Summary statistics (total questions, responses)
- ✅ Individual response viewing
- ✅ Percentage breakdowns for choice questions
- ✅ Detailed analytics dashboard

### User Experience
- ✅ Modern, clean UI with Tailwind CSS
- ✅ Responsive design for all devices
- ✅ Intuitive navigation and workflows
- ✅ Community-focused branding
- ✅ Fast loading and smooth interactions

## 🎨 Design System

**Color Palette**:
- Primary Blue: `#1e40af` (Barangay Blue)
- Success Green: `#059669` (Barangay Green)  
- Warning Orange: `#ea580c` (Barangay Orange)
- Neutral Grays: Various shades for text and backgrounds

**Typography**: Clean, readable fonts with proper hierarchy
**Components**: Consistent button styles, form elements, and cards
**Layout**: Mobile-first responsive design

## 🗄️ Database Schema

### Tables
1. **surveys** - Survey metadata and settings
2. **questions** - Survey questions with types and options
3. **responses** - Individual survey submissions
4. **answers** - Answers to specific questions

### Relationships
- One-to-Many: Survey → Questions
- One-to-Many: Survey → Responses  
- One-to-Many: Question → Answers
- One-to-Many: Response → Answers

## 🔧 Technical Implementation

### Backend (FastAPI)
- RESTful API endpoints
- SQLAlchemy ORM for database operations
- Form handling with validation
- Dependency injection for database sessions
- Error handling and HTTP status codes

### Frontend (Jinja2 + Tailwind)
- Server-side rendering with Jinja2
- Tailwind CSS for styling (CDN-based)
- JavaScript for dynamic interactions
- Form validation and AJAX requests
- Responsive grid layouts

### Database (SQLite)
- File-based database for easy deployment
- Automatic table creation on startup
- Foreign key relationships
- Indexed columns for performance

## 🚀 Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py

# Create demo data (optional)
python demo_data.py

# Access the application
# http://localhost:8000
```

## 📊 Sample Use Cases

1. **Community Needs Assessment**
   - Gather feedback on local issues
   - Prioritize barangay projects
   - Understand resident concerns

2. **Event Planning**
   - Plan barangay fiestas and celebrations
   - Collect preferences for activities
   - Organize volunteer participation

3. **Health & Safety Surveys**
   - Assess health service needs
   - Evaluate safety concerns
   - Plan community health programs

4. **Budget Planning**
   - Gather input on budget priorities
   - Understand spending preferences
   - Plan infrastructure projects

## 🔮 Future Enhancements

- User authentication and role management
- Survey templates and themes
- Data export (CSV, PDF)
- Advanced analytics and reporting
- Multi-language support (Filipino/English)
- Email notifications and reminders
- Integration with other barangay tools
- Mobile app companion

## 🌟 Why This Project Matters

This tool addresses a real need in Philippine barangays for:
- **Digital Transformation**: Moving from paper-based to digital surveys
- **Community Engagement**: Making it easier for residents to participate
- **Data-Driven Decisions**: Providing insights for better governance
- **Accessibility**: Free, open-source solution for all barangays
- **Scalability**: Can be deployed locally or in the cloud

## 🤝 Contributing to The Puso Project

This project is part of [The Puso Project](https://www.thepusoproject.ph/solutions) - an initiative to build digital solutions for Philippine barangays. By contributing to this project, you're helping improve local governance and community engagement across the Philippines.

---

**Built with ❤️ for Philippine barangays**
