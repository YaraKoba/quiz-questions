# Quiz question
### By Kobyakov Yaroslav



## Getting Started
### Environment Setup
1. Clone the repository:
    ```commandline
    git clone https://github.com/YaraKoba/quiz-questions.git
    cd quiz-questions
    ```
2. Create a `.env` file in the project root directory and add the necessary environment variables. You can use the `.env.sample` file as a template.
3. Install Python dependencies:
    ```commandline
    pip install -r requirements.txt
    ```
### Running the Application
1. Start the application and PostgreSQL database with Docker Compose:

    ```commandline
    docker-compose up -d
    ```
2. Run Alembic database migrations to set up the database schema:
    ```commandline
    alembic upgrade head
    ```
3. Start the FastAPI application:
    ```commandline
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

