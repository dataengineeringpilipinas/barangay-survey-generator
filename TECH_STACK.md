# Barangay Survey Generator - Tech Stack

## 🏗️ Architecture Overview

This project follows a **Model-View-Controller (MVC)** architecture pattern, providing a clean separation of concerns and maintainable code structure.

## 🐍 Backend Technologies

### Core Framework
- **FastAPI** `0.104.1`
  - Modern, fast web framework for building APIs with Python 3.8+
  - Automatic API documentation with Swagger UI
  - Built-in data validation and serialization
  - High performance with async/await support
  - Type hints throughout the codebase

### Web Server
- **Uvicorn** `0.24.0`
  - ASGI server implementation
  - High-performance async server
  - Auto-reload capability for development
  - Production-ready with worker support

### Database & ORM
- **SQLAlchemy** `2.0.23`
  - Python SQL toolkit and Object-Relational Mapping (ORM)
  - Database-agnostic design
  - Declarative base for model definitions
  - Session management and connection pooling

- **SQLite**
  - Lightweight, file-based database
  - Zero-configuration database engine
  - Perfect for small to medium applications
  - ACID compliant with full SQL support

### Template Engine
- **Jinja2** `3.1.2`
  - Modern templating engine for Python
  - Template inheritance and composition
  - Automatic HTML escaping for security
  - Rich template language with filters and macros

### Form Handling
- **python-multipart** `0.0.6`
  - FastAPI dependency for form data parsing
  - Handles file uploads and form submissions
  - Efficient multipart/form-data processing

## 🎨 Frontend Technologies

### CSS Framework
- **Tailwind CSS** (CDN)
  - Utility-first CSS framework
  - Responsive design system
  - Custom color palette for barangay branding
  - Mobile-first approach
  - Rapid UI development

### JavaScript
- **Vanilla JavaScript**
  - No external dependencies
  - Modern ES6+ features
  - AJAX requests for dynamic interactions
  - Form validation and user interactions

### Icons & Graphics
- **Heroicons** (via Tailwind)
  - Beautiful SVG icons
  - Consistent icon system
  - Scalable vector graphics

## 📊 Database Schema

### Tables Structure
```sql
-- Surveys table
surveys (id, title, description, created_at, is_active)

-- Questions table  
questions (id, survey_id, question_text, question_type, options, is_required, order)

-- Responses table
responses (id, survey_id, respondent_name, submitted_at)

-- Answers table
answers (id, response_id, question_id, answer_text)
```

### Relationships
- **One-to-Many**: Survey → Questions
- **One-to-Many**: Survey → Responses
- **One-to-Many**: Question → Answers
- **One-to-Many**: Response → Answers

## 🛠️ Development Tools

### Package Management
- **pip** - Python package installer
- **requirements.txt** - Dependency specification
- **Virtual Environment** - Isolated Python environment

### Code Quality
- **Type Hints** - Python type annotations throughout
- **PEP 8** - Python code style guidelines
- **Clean Architecture** - Separation of concerns

### Development Features
- **Auto-reload** - Automatic server restart on code changes
- **Hot Module Replacement** - Instant template updates
- **Debug Mode** - Detailed error messages and logging

## 🚀 Deployment & Production

### Production Considerations
- **Gunicorn** - WSGI HTTP Server for production
- **Nginx** - Reverse proxy and static file serving
- **SSL/TLS** - HTTPS encryption
- **Environment Variables** - Configuration management
- **Database Backups** - SQLite backup strategies

### Performance Features
- **Async/Await** - Non-blocking I/O operations
- **Connection Pooling** - Efficient database connections
- **Static File Serving** - Optimized asset delivery
- **Caching Headers** - Browser caching optimization

## 📱 Responsive Design

### Breakpoints
- **Mobile**: < 640px
- **Tablet**: 640px - 1024px  
- **Desktop**: > 1024px

### Design System
- **Color Palette**: Barangay-themed colors (blue, green, orange)
- **Typography**: Clean, readable font hierarchy
- **Spacing**: Consistent margin and padding system
- **Components**: Reusable UI components

## 🔒 Security Features

### Built-in Security
- **CSRF Protection** - Cross-site request forgery prevention
- **SQL Injection Prevention** - Parameterized queries via SQLAlchemy
- **XSS Protection** - Automatic HTML escaping in Jinja2
- **Input Validation** - FastAPI automatic validation

### Best Practices
- **Environment Variables** - Sensitive data management
- **HTTPS Ready** - SSL/TLS support
- **Secure Headers** - Security headers configuration

## 📦 Project Structure

```
barangay-survey-generator/
├── app.py                 # Main FastAPI application
├── run.py                 # Development server script
├── demo_data.py           # Sample data generator
├── requirements.txt       # Python dependencies
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Homepage
│   ├── create_survey.html # Survey creation
│   ├── edit_survey.html  # Question editor
│   ├── survey.html       # Survey taking interface
│   ├── results.html      # Analytics dashboard
│   └── thanks.html       # Thank you page
├── static/               # Static assets
│   └── img/             # Images and logos
└── *.db                 # SQLite database files
```

## 🔄 API Endpoints

### RESTful API Design
- **GET** `/` - Homepage
- **GET** `/create` - Survey creation form
- **POST** `/create` - Create new survey
- **GET** `/survey/{id}` - View/take survey
- **POST** `/survey/{id}/submit` - Submit responses
- **GET** `/survey/{id}/edit` - Edit survey
- **POST** `/survey/{id}/add-question` - Add question
- **DELETE** `/survey/{id}/question/{qid}/delete` - Delete question
- **GET** `/survey/{id}/results` - View results
- **GET** `/survey/{id}/thanks` - Thank you page

## 🌐 Browser Compatibility

### Supported Browsers
- **Chrome** 90+
- **Firefox** 88+
- **Safari** 14+
- **Edge** 90+

### Features Used
- **CSS Grid & Flexbox** - Modern layout systems
- **CSS Custom Properties** - Dynamic theming
- **ES6+ JavaScript** - Modern JavaScript features
- **Fetch API** - HTTP requests

## 📈 Performance Metrics

### Optimization Features
- **Lazy Loading** - On-demand resource loading
- **Minification** - Compressed assets
- **Caching** - Browser and server-side caching
- **CDN Ready** - Content delivery network support

### Expected Performance
- **First Load**: < 2 seconds
- **Page Transitions**: < 500ms
- **Database Queries**: < 100ms
- **Form Submissions**: < 1 second

## 🔧 Configuration

### Environment Variables
```bash
# Database
DATABASE_URL=sqlite:///./barangay_surveys.db

# Server
HOST=0.0.0.0
PORT=8000
DEBUG=True

# Security
SECRET_KEY=your-secret-key-here
```

### Customization Points
- **Color Scheme** - Tailwind CSS configuration
- **Logo/Branding** - Static assets in `/static/img/`
- **Database** - SQLAlchemy models and migrations
- **Templates** - Jinja2 template customization

---

**Built with modern web technologies for Philippine barangay communities** 🇵🇭
