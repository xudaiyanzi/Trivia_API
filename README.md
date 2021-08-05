# Trivia API - a way to learn API 

I used this project to improve my API skill. It seperates the full stack work into backend and frontend. Here, my main focus is on the backend, where I finished the API request and error handlers in the flaskr, and write the test_flaskr.py to test each API, and use curl to request the API response. In the well-built frontend, I update the urls, which allows API response being read successfully.

All the API responses are presented in json files.

## 1. Getting started

Install the backend prerequirement dependencies by using this command:

    pip3 install -r requirements.txt

We need then create database and insert all the data in tables
- for database, , cd to '\backend' directory and excute this command:

        psql 
        \i setup.sql

        \q  \\to exit the database before insert data to tables
    
- for tables, cd to '\backend' directory and excute:

        psql trivia < trivia.psql

After install the database and tables, we start the backend and frontend server to play.
- for backend, cd to '\backend' directory:

        export FLASK_APP=flaskr
        export FLASK_ENV=development
        flask run
    
- for frontend, cd to '\frontend' directory:

        npm install
        npm start

So far, we have done the server part, the following section will be focused on the detailed API reference

## 2. API reference

In this project, the API is a REST API. The requests include "GET", "POST", and "DELETE", and the error codes are 400, 404, 422, and 405. Using the API, we can request all the categories and the questions (in pagination, with the specific category for each question on a particular page), we can search questions in a selected category, create questions, delete questions, and find a random question in any chosen category.

#### (1) Base url - get all the categories

This command is expected to fetch json file, including all the categories in a json file, the status of fetch ("success", true or false), and the total number of categories. The category json is a dictionary with a key named as "id", and a description.

    curl http://127.0.0.1:5000/categories

The response is 

    {
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "success": true, 
    "total_categories": 6
    }

#### (2) All questions
This request can render all the questions but in pagination form. The default page = 1 with 8 questions showingup. The categories the response are the categories of the shown 8 questions, other than all the categories in the database:

    curl http://127.0.0.1:5000/questions

the reponse:

    {
    "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "current_categories": {
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
    }, 
    "questions": [
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
        "answer": "Maya Angelou", 
        "category": 4, 
        "difficulty": 2, 
        "id": 5, 
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
        "answer": "Brazil", 
        "category": 6, 
        "difficulty": 3, 
        "id": 10, 
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
        "answer": "Uruguay", 
        "category": 6, 
        "difficulty": 4, 
        "id": 11, 
        "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
        "answer": "George Washington Carver", 
        "category": 4, 
        "difficulty": 2, 
        "id": 12, 
        "question": "Who invented Peanut Butter?"
        }, 
        {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
        }, 
        {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ], 
    "success": true, 
    "total_questions": 19
    }

For questions in other pages, we can use the command: curl http://127.0.0.1:5000/questions?page=${integer}. For example:

    curl http://127.0.0.1:5000/questions?page=2

#### (3) Creating a question
This method will create a new entry of question. A successful create requires all of three: "question", "answer", "category". 

    curl -X POST -H "Content-Type: application/json" -d '{"question": "test question", "answer": "test answer", "category": "1", "difficulty":"1"}' http://127.0.0.1:5000/questions

response:

    {
    "new_question": {
        "answer": "test answer", 
        "category": 1, 
        "difficulty": 1, 
        "id": 28, 
        "question": "test question"
    }, 
    "success": true, 
    "total_questions": 20
    }


#### (4) Deleting a question
We can also delete a question, by using

    curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:5000/questions/20

Response:
    {  "deleted_question": {
        "answer": "The Liver", 
        "category": 1, 
        "difficulty": 4, 
        "id": 20, 
        "question": "What is the heaviest organ in the human body?"
    }, 
    "success": true
    }

#### (5) Searching a question
Here, we search any words/letters in a question description, and the reponses will list all the questions that fit the requirement, along with their corresponding categories.

        curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"what"}' -H "Content-Type: application/json" 


-response:
    
    {
    "current_category": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment"
    }, 
    "questions": [
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

#### (6) listing all question in a category
The command will pull all the questions in the chosen category. `curl http://127.0.0.1:5000/categories/${integer}/questions` It will automatically validate the integer number, and check whether it is in the categories id range. I give an example to fetch questions in category 1:

        curl http://127.0.0.1:5000/categories/1/questions

response:
     
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

#### (7) Rendering a random question in a category


        curl -d '{"previous_questions":[17], "quiz_category":{"type": "Art", "id": "2"}}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/quizzes

--response
    
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
    

#### (8) error handlers
The error code in our project are 400, 404, 405, and 422. We also render a json file to explain the error. For example, we use:

    curl http://127.0.0.1:5000/categories/100/questions

error 422
response:
``` 
    {
    "error": 422, 
    "message": "can not process the resource", 
    "success": false
    }
```

## 3. Authors
Yan Xu, Udacity Full-stack team

## 4. Acknowledgement
Yan thanks the mentors in Full-stack team. They are patient and resourceful. In particular, Mr. Nitish K offered a huge help on the /quizzs handler.
