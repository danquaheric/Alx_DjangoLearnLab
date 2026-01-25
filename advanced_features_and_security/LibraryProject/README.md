# LibraryProject

This is a basic Django project created as part of the Introduction to Django Development Environment Setup task.

## Setup Instructions
1. Install Django using `pip install django`
2. Navigate to the project directory
3. Run the development server using `python manage.py runserver`
4. Open http://127.0.0.1:8000/ in your browser

# Permissions and Groups Setup

1. Custom permissions are defined in Book model: can_view, can_create, can_edit, can_delete.
2. Groups:
   - Admins: All permissions
   - Editors: can_create, can_edit
   - Viewers: can_view
3. Views use @permission_required decorator to enforce permissions.
4. Groups and permissions are created with the management command:
   python manage.py setup_groups

