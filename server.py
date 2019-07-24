from flask import Flask, render_template, request, redirect, url_for

import data_manager, connection

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def show_list():
    return render_template('list.html',
                           question_list = data_manager.question_list,
                           QUESTION_HEADERS = connection.QUESTION_HEADERS)

@app.route('/question/<question_id>')
def show_question_and_answers(question_id: int):
    single_question=data_manager.get_single_question(question_id, connection.get_all_data(connection.QUESTION_PATH))
    return render_template('question.html',
                           question_id=question_id,
                           single_question=single_question,
                           QUESTION_HEADERS=connection.QUESTION_HEADERS)


if __name__ == '__main__':
    app.run(
        debug = True,
        port = 5000
    )