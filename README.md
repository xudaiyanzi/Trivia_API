# Full Stack API Final Project
API
- random question:

        curl -d '{"previous_questions":[17], "quiz_category":{"type": "Art", "id": "2"}}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/quizzes

--response
    ```
    {
    "question": {
        "answer": "One", 
        "category": 2, 
        "difficulty": 4, 
        "id": 18, 
        "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    "success": true
    }
    ```


- questions in each category:

        curl http://127.0.0.1:5000/categories/1/questions

response

    ``` 
    {
        "current_questions": [
            {
            "answer": "The Liver", 
            "category": 1, 
            "difficulty": 4, 
            "id": 20, 
            "question": "What is the heaviest organ in the human body?"
            }, 
            {
            "answer": "Alexander Fleming", 
            "category": 1, 
            "difficulty": 3, 
            "id": 21, 
            "question": "Who discovered penicillin?"
            }, 
            {
            "answer": "Blood", 
            "category": 1, 
            "difficulty": 4, 
            "id": 22, 
            "question": "Hematology is a branch of medicine involving the study of what?"
            }
        ], 
        "success": true, 
        "total_questions": 3
    }
    ```
-search:

        curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"what"}' -H "Content-Type: application/json" 


-response:

    ```
    {
    "current_questions": [
        {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "Mona Lisa", 
        "category": 2, 
        "difficulty": 3, 
        "id": 17, 
        "question": "La Giaconda is better known as what?"
        }, 
        {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
        }, 
        {
        "answer": "Blood", 
        "category": 1, 
        "difficulty": 4, 
        "id": 22, 
        "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ], 
    "success": true, 
    "total_questions": 8
    }
    ```


- error
error 422
response:

    ```
    {
    "error": 422, 
    "message": "can not process the resource", 
    "success": false
    }
    ```




```

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter) and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.
>Once you're ready, you can submit your project on the last page.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend
The [./backend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads? 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. *./frontend/src/components/QuestionView.js*
2. *./frontend/src/components/FormView.js*
3. *./frontend/src/components/QuizView.js*


By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API. 



>View the [README within ./frontend for more details.](./frontend/README.md)
