# blog-api
A basic API with operations to create, update and delete blog posts.

Requires Python 3.7+. 
Database connection URL is hardcoded. If postgres is not configured similarly, please change the connection URL as well in `app/database.py`.

To run:
1. Open the Terminal.
2. Create a virtual environment `python3 -m venv venv`.
3. Activate the virtual environment.
4. Clone the repository `git clone https://github.com/k-hari-93/blog-api.git`.
5. Change to the application directory `cd blog-api`.
6. Install dependencies `pip install -r requirements.txt`.
7. Run the application `uvicorn app.main:app`.
