import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

# start paginate the questions, which make the display more appealing
def paginate_questions(request, selection):

  # if no 'page' is provided, return the first page
  # if 'page' is provided, return the requested page
  page = request.args.get('page', 1, type=int) 
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  # try to format the questions
  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  ### Done!!!
  CORS(app)

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  ## Done!!! set the CORS headers
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization') 
    response.headers.add('Access-Control-Allow-Method', 'GET,PUT,POST,DELETE,PATCH')

    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  ### Done!!!
  @app.route('/categories', methods=['GET'])
  def retrieve_categories():
    
    selection = Category.query.order_by(Category.id).all()
    categories = []
    for item in selection:
      categories.append(item.format())

    if len(categories) == 0:
      abort(404)
    
    return jsonify({
      'success': True,
      'categories': categories,
      'total_categories': len(categories)
      })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  ### Done!!!

  @app.route('/questions', methods=['GET'])
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    categories = Category.query.order_by(Category.id).all()

    current_questions = paginate_questions(request, selection)
    
    # get the unique category ids
    current_categories_id = set()
    for item in current_questions:
      current_categories_id.add(item['category']) 

    current_categories = []
    for item in current_categories_id:
      current_categories.append(Category.query.filter_by(id=item).first().format())

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'current_categories': current_categories,
      'categories': [category.format() for category in categories],
      'total_categories': len(categories)
    })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  ### Done!!!
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.filter_by(id=question_id).first()

    if question is None:
      abort(404)

    question.delete()
    return jsonify({
      'success': True,
      'deleted_question': question.format()
    })


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  ### Done!!!
  @app.route('/questions', methods=['POST'])
  def add_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)

    question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
    question.insert()

    return jsonify({
      'success': True,
      'new_question': question.format(),
      'total_questions': len(Question.query.all())
    })


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  ### Done!!!
  @app.route('/questions/search', methods=['POST'])
  def search_questions():

    body = request.get_json()
    
    ## it is import to use try/except here to avoid the loading error
    try:
      search_term = body.get('searchTerm', None)

      if search_term:

        # selection = Question.query.filter(Question.question.ilike('%{}%',format(search_term))).all()
        # the above line is not working, so I use the following line. I do not know why.
        selection = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
        if len(selection) == 0:
            abort(422)
        current_questions = paginate_questions(request, selection)

        return jsonify({
            'success': True,
            'current_questions': current_questions,
            'total_questions': len(selection)
        })

      else:
        abort(422)

    except:
      abort(422)

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  # Done!!!
  @app.route('/categories/<int:categories_id>/questions', methods=['GET'])
  def retrieve_questions_by_category (categories_id):
    selection = Question.query.filter_by(category = str(categories_id)).order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    current_categories = Category.query.filter_by(id=categories_id).first().format()

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'current_questions': current_questions,
      'total_questions': len(selection),
      'current_categories': current_categories,
    })


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quiz', methods=['POST'])
  def retrieve_random_question_by_category ():

    try:
      body = request.get_json()    
      categories_id = body.get('quizCategory', None)['id']
      previous_questions = body.get('previousQuestions', [])

      current_category = Category.query.filter_by(id=categories_id).first()

      if current_category is None:
        abort(404)
      
      questions = Question.query.filter_by(category=categories_id).order_by(Question.id).all()
      if len(questions) == 0:
        abort(422)
      
      collected_question = []
      for item in questions:
        if item['id'] not in previous_questions:
          collected_question.append(item.format())

      if len(collected_question) == 0:
        abort(422)

      current_question = random.choice(collected_question)
    
      return jsonify({
        'success': True,
        'current_category': current_category.format(),
        'current_question': current_question
      })
    except:
      abort(422)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    