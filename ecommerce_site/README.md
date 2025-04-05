🛒 E-Commerce API
A Django REST Framework-powered API for managing products and reviews in an e-commerce platform. It supports full CRUD operations, user authentication, and advanced filtering/searching features.

🚀 Features
User Authentication: Token-based authentication for secure access.

Product Management: Create, retrieve, delete, and filter products.

Review System: Users can add, view, and delete product reviews.

Filtering & Searching:

Filter products by category or stock status.

Search products by name or price.

🛠 Tech Stack
Backend: Django, Django REST Framework

Database: PostgreSQL (or SQLite for development)

Authentication: Token Authentication

📦 Installation & Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/okinyoCoder/ecommerce-api.git
cd ecommerce-api
Create & activate a virtual environment

bash
Copy
Edit
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
🔐 Authentication Endpoints
Method	Endpoint	Description
POST	/register/	Register a new user
POST	/login/	Authenticate and retrieve token
📦 Product Endpoints
Method	Endpoint	Description	Permission
GET	/products/	List all products	Public
POST	/products/create/	Create a new product	Admin
GET	/products/<id>/	Retrieve a product	Public
DELETE	/products/<id>/delete/	Delete a product	Admin
📝 Review Endpoints
Method	Endpoint	Description	Permission
GET	/reviews/	List all reviews	Public
POST	/reviews/create/	Add a new review	Authenticated
GET	/reviews/<id>/	Retrieve a review	Public
DELETE	/reviews/<id>/delete/	Delete a review	Admin
🔍 Filtering & Searching
Products
?category=<category_name> – Filter by category

?stock_available=True – Show only available products

?search=<name_or_price> – Search by product name or price

Reviews
?user=<user_id> – Filter reviews by user

?ordering=created_date – Order reviews by date

📫 Contributing
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

Let me know if you’d like to add screenshots, an API schema (e.g., Swagger), or deployment instructions!
