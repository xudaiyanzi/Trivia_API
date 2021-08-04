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
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "How many players in a basketball team?",
            "answer": "5",
            "category": "6"
        }

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
    # def test_get_categories(self):
    #     """Test for get_categories"""
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_categories'], 6)

    # def test_get_questions(self):
    #     """Test for get_questions"""
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'], 19)
    #     self.assertIsNotNone(data['current_categories'])

    # def test_delete_question(self):
    #     """Test for delete_question"""
    #     res = self.client().delete('/questions/4')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted_question']['id'], 4)

    # def test_create_question(self):
    #     """Test for create_question"""
    #     res = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_questions'],19)

    # def test_search_question(self):
    #     """Test for search_question"""
    #     new_search = {
    #         "searchTerm": "What"
    #         }
    #     res = self.client().post('/questions/search', json = new_search)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertIsNotNone(data['current_questions'])


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





    # def test_get_random_question_by_category(self):
    #     """Test for get_random_question_by_category"""
    #     res = self.client().post('/quizzes', json={'previous_quesitons': [16], 'quiz_category':{'id': 2, 'type': 'Art'}})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertIsNotNone(data['current_question'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()