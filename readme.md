# 🎓 Student Organization Management System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Revision Date: 2025-August rev 01 8

## Project Overview
A web-based Django application for managing student organizations, colleges, programs, students, and memberships.  
Admins can efficiently manage all records with a clean and intuitive interface.

## Features

| Feature | Description |
|---------|-------------|
| Admin Dashboard | Central hub for managing all records efficiently |
| College Management | Add, edit, search, and filter colleges |
| Program Management | Manage programs linked to colleges; searchable and filterable |
| Organization Management | Add student organizations, associate with colleges, include descriptions |
| Student Management | Maintain detailed student records with program associations |
| OrgMemberships | Track student memberships in organizations, including join dates |
| Enhanced Admin UI | Searchable lists, filters, and custom columns for better usability |

## Installation

Clone the repository:
git clone https://github.com/yourusername/student-org-system.git
cd student-org-system

Activate virtual environment:
C:\Users\username\psusenv\Scripts\activate

Windows:
source psusenv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Run server:
python manage.py runserver

Open the Admin Interface in your browser: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Authors

| Name | Role |
|------|------|
| John Erwin Anquillano | Backend & Admin Interface |

## License
MIT License