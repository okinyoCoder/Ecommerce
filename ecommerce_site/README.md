# E-Commerce API

This is a Django REST Framework-based API for managing products and reviews in an e-commerce platform. It supports CRUD operations for products and reviews with authentication and filtering.

## Features
- **User Authentication:** Token-based authentication for secure access.
- **Product Management:** Create, view, delete, and filter products.
- **Review Management:** Users can add, view, and delete product reviews.
- **Filtering & Searching:** Filter products by category and availability, and search by name or price.

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (or SQLite for development)
- **Authentication:** Token Authentication

---

## Installation & Setup

### 1. Clone the repository
```sh
git clone https://github.com/okinyoCoder/ecommerce-api.git
cd ecommerce-api
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
pip install -r requirements.txt

Authentication
Method	Endpoint	    Description
POST	/register/	    Register a new user
POST	/login/  	    Authenticate and get token

Products
Method	Endpoint	            Description	Permission
GET	    /products/	            List all products	Public
POST    /products/create/	    Create a new product	Admin
GET	    /products/<id>/	        Retrieve a product	Public
DELETE	/products/<id>/delete/	Delete a product	Admin


Reviews
Method	        Endpoint	            Description	Permission
GET	            /reviews/	            List all reviews Public
POST	        /reviews/create/	    Create a new review	Authenticated
GET	            /reviews/<id>/	        Retrieve a review Public
DELETE	        /reviews/<id>/delete/	Delete a review	Admin


Filtering & Searching
Products
?category=<category_name> → Filter by category
?stock_available=True → Show only available products
?search=<name_or_price> → Search products by name or price

Reviews
?user=<user_id> → Filter reviews by user
?ordering=created_date → Order reviews by date
