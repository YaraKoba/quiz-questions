# Quiz question
### By Kobyakov Yaroslav

## Prerequisites:
- Docker
- Docker Compose
- Python 3.8+
- FastAPi
- postgresSQL
- alembic
- pip
- Git

## Getting Started
### Environment Setup
1. Clone the repository:
    ```commandline
    git clone https://github.com/YaraKoba/quiz-questions.git
    cd quiz-questions
    ```
2. Create a `.env` file in the project root directory and add the necessary environment variables. You can use the `.env.sample` file as a template.

### Running the Application
1. Start the application and PostgreSQL database with Docker Compose:

    ```commandline
    docker-compose up -d
    ```
2. Run Alembic database migrations to set up the database schema:
    ```commandline
    docker-compose exec web alembic upgrade head
    ```
3. Check it. Now you can go to http://127.0.0.1/docs. You will see the automatic interactive API documentation

