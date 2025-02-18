# **Django Forum Application**

A simple Django-based forum application where users can create threads, comment on threads, and interact with each other. This project includes full **CRUD** functionality for threads and comments, along with **user authentication** to ensure that only logged-in users can create, edit, or delete their posts.

---

## **Features**
- **User Authentication**: Sign up, login, and logout functionality.
- **Thread Management**: Users can create, read, update, and delete threads.
- **Commenting**: Authenticated users can comment on threads, with full CRUD functionality for comments.
- **User Permissions**: Only authenticated users can create, edit, or delete threads and comments.

---

## **Tech Stack**
- **Backend**: Django (Python web framework)
- **Database**: SQLite (default for development, can be changed to PostgreSQL, MySQL, etc.)
- **Authentication**: Django's built-in authentication system
- **Frontend**: Minimal HTML templates (no external CSS or JS frameworks used; however, Bootstrap can be added for styling)
- **Version Control**: Git & GitHub for collaboration

---

## **Installation**

### 1. **Clone the Repository**
```bash
git clone https://github.com/LisaMatzner/Django-Forum.git
cd django-forum
```

### 2. **Create a Virtual Environment**  
Create and activate a virtual environment to install dependencies locally.
```bash
python3 -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. **Install Dependencies**
Install all necessary dependencies with pip.
```bash
pip install -r requirements.txt
```

### 4. **Setup Database**
Run migrations to set up the database:
```bash
python manage.py migrate
```

### 5. **Create a Superuser**
To manage the app through the admin interface, create a superuser account:
```bash
python manage.py createsuperuser
```

### 6. **Run the Development Server**
Start the Django development server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## **Usage**
- **Login**: Navigate to `/login/` to sign in with the credentials you created during registration.
- **Register**: Navigate to `/register/` to create a new account.
- **Threads**: Navigate to `/threads/` to view a list of all threads. Users can click on a thread to view it, post comments, or edit their own threads.
- **Comments**: Users can add, edit, or delete comments on threads, but only on threads they have access to.

---

## **GitHub Workflow**

### **Branching Strategy**
- `main`: Stable, production-ready code.
- `dev`: Active development branch where all feature branches are merged.
- `feature/{feature-name}`: Branches created for specific features or tasks, e.g., `feature/authentication`, `feature/thread-crud`, `feature/comment-crud`.

### **Development Workflow**
1. Create a **feature branch** for each task or feature.
2. Develop the feature, commit frequently, and push to GitHub.
3. Open a **pull request** to merge your feature branch into `develop`.
4. After review and approval, the pull request is merged.
5. After all features are complete, merge `develop` into `main` for deployment.

---

## **Contributing**
We welcome contributions to the project! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write your code and commit it with clear messages.
4. Open a pull request with a description of your changes.

---

## **Testing**
To run the tests, use the following command:
```bash
python manage.py test
```
This will run all the unit tests for the app, ensuring that all features work as expected.

---

## **License**
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## **Project Team**
- **Member 1**: [Lisa Matzner](https://github.com/LisaMatzner)
- **Member 2**: [ChrisPMint](https://github.com/ChrisPMint)
- **Member 3**: [navid-dot](https://github.com/navid-dot)
- **Member 4**: [blueanthocyanin](https://github.com/blueanthocyanin)

---

## **Known Issues**
- User interface is minimal; the focus is on functionality.
- No email verification or password reset functionality (can be added in future versions).

---

## **Future Improvements**
- Add **email verification** for user registration.
- Implement **password reset** functionality.
- Add more detailed **styling** using CSS frameworks (like Bootstrap).
- Allow **thread categorization** (e.g., General, Feedback, Support).
- Add **search functionality** to find threads by title or content.

---

## **Acknowledgments**
- Thanks to the Django community for their excellent documentation and support.
- Special thanks to our team members for their hard work and collaboration.

