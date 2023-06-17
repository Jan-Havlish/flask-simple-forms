import flask
import time
import json
from werkzeug.datastructures import ImmutableMultiDict
from db_handler import PickleDBHandler
from functions import convert_multi_dict_to_dict, make_empty_db, get_template_array
from __init__ import db_handler, app, questions_and_choices_dictionary

#make_empty_db(questions_and_choices_dictionary) # nessery for each first run or change of questions (questions_and_choices.json)

@app.route("/")
@app.route("/home")
@app.route("/form")
def home():
    return flask.render_template(
        "form.html", questions_and_choices_dictionary=questions_and_choices_dictionary
    )


@app.route("/process_form", methods=["POST"])
def process_form():
    form_data = flask.request.form  # get form

    to_store = convert_multi_dict_to_dict(form_data)
    template_array = get_template_array(questions_and_choices_dictionary)

    list_of_dicts_with_1 = []
    for item in template_array:
        for question, choices in item.items():
            for choice in choices.keys():
                if question in to_store and choice in to_store[question]:
                    choices[choice] = 1
            list_of_dicts_with_1.append(item)

    for item in list_of_dicts_with_1:
        for key, value in item.items():
            db_handler.add_2_dicts_in_db(key, value)

    return "Thank you for filling this form."


@app.route("/results")
def results():
    results_list = db_handler.get_all()
    output_list = []
    for result in results_list:
        output_list.append(
            {"question": result, "list_of_choices": db_handler.get(result)}
        )

    return flask.render_template("result.html", output_list=output_list)


if __name__ == "__main__":
    app.run(debug=True)
