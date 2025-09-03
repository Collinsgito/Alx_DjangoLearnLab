# Permissions & Groups - bookshelf app

This guide explains the custom permissions on the `Book` model and how to create groups and assign those permissions.

## Custom permissions
The `Book` model (in `LibraryProject/bookshelf/models.py`) defines these custom permission codenames:
- `can_view`  — allow viewing book list/detail
- `can_create` — allow creating books
- `can_edit` — allow editing books
- `can_delete` — allow deleting books

These codenames are available as `bookshelf.can_view`, `bookshelf.can_create`, `bookshelf.can_edit`, `bookshelf.can_delete`.

## Setup & migrations
1. Install dependencies (if not already):
   ```bash
   pip install -r requirements.txt
   pip install Pillow
