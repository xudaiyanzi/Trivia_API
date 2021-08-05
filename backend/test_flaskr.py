import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
                             'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # # Done!
    # def test_get_categories(self):
    #     """Test for get_categories"""
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_categories'], 6)
# Done!

# ## NOT DONE YET ###
#     def test_error_get_categories(self):
#         """Test for get_categories"""
#         res = self.client().get('/categories')
#         data = json.loads(res.data)

#         self.assertEqual(res.status_code, 404)
#         self.assertEqual(data['success'], False)
#         self.assertEqual(data['message'], 'not found')
# NOT DONE YET

# Done!
    def test_get_questions(self):
        """Test for get_questions"""
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertEqual(data['total_questions'], 31)
        self.assertIsNotNone(data['categories'])

    def test_error_get_questions(self):
        """Test for get_questions"""
        res = self.client().get('/questions?page=10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "not found")

    def test_delete_question(self):
        """Test for delete_question"""
        res = self.client().delete('/questions/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_question']['id'], 4)

    def test_error_delete_question(self):
        """Test for delete_question"""
        res = self.client().delete('/questions/300')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "not found")

    def test_create_question(self):
        """Test for create_question"""
        new_question = {
            "question": "How many players in a basketball team?",
            "answer": "5",
            "category": "6"
        }

        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_error_create_question(self):
        """Test for create_question"""
        new_question_error = {
            "question": "",
            "answer": "",
            "category": ""
        }
        res = self.client().post('/questions', json=new_question_error)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_search_question(self):
        """Test for search_question"""
        new_search = {
            "searchTerm": "What"
            }
        res = self.client().post('/questions/search', json=new_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['questions'])

    def test_error_search_question(self):
        """Test for search_question"""
        new_search = {
            "searchTerm": "XXXXXXXXXX"
            }
        res = self.client().post('/questions/search', json=new_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'not found')

    def test_get_questions_by_category(self):
        """Test for get_questions"""
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['totalQuestions'], 3)

    def test_error_get_questions_by_category(self):
        """Test ERROR for get_questions"""
        res = self.client().get('/categories/10/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_get_random_question_by_category(self):
        """Test for get_random_question_by_category"""
        res = self.client().post('/quizzes', json={
            'previous_quesitons': [16],
            'quiz_category': {'id': 2, 'type': 'Art'}
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['question'])

    def test_error_get_random_question_by_category(self):
        """Test for get_random_question_by_category"""
        res = self.client().post('/quizzes', json={
            'previous_quesitons': [16],
            'quiz_category': {'id': 7}
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

# Done!

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
