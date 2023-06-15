import flask, time
from werkzeug.datastructures import ImmutableMultiDict
from db_handler import PickleDBHandler


def convert_multi_dict_to_dict(multi_dict):
    data = multi_dict
    result = {}
    for key in data.keys():
        result[key] = data.getlist(key)
    return result


db_handler = PickleDBHandler("db.db")

# do db "Capital of France" : {"Paris" : 1, "Lyon" : 2, "Marseille" : 3}

# print(sum_values_of_2_dicts({"Paris" : 1, "Lyon" : 2, "Marseille" : 3}, {"Paris" : 1, "Lyon" : 2, "Marseille" : 3}))

questions_and_choices_dictionary = [
    {
        "question": "Capital of France",
        "list_of_choices": [
            "Paris",
            "Lyon",
            "Marseille",
        ],
        "button_type": "radio",
    },
    {
        "question": "Capital of Germany",
        "list_of_choices": [
            "Berlin",
            "Hamburg",
            "Stuttgart",
        ],
        "button_type": "checkbox",
    },
]


def make_empty_db(questions_and_choices_dictionary):
    for question_dict in questions_and_choices_dictionary:
        dict_of_choices = {choice: 0 for choice in question_dict["list_of_choices"]}
        db_handler.set(question_dict["question"], dict_of_choices)


def get_template_array(questions_and_choices_dictionary):
    return [
        {
            question_dict["question"]: {
                choice: 0 for choice in question_dict["list_of_choices"]
            }
        }
        for question_dict in questions_and_choices_dictionary
    ]


# print(make_empty_db(questions_and_choices_dictionary))

app = flask.Flask(__name__, template_folder="templates")


@app.route("/")
@app.route("/home")
@app.route("/form")
def home():
    return flask.render_template(
        "form.html", questions_and_choices_dictionary=questions_and_choices_dictionary
    )


@app.route("/process_form", methods=["POST"])
def process_form():
    form_data = flask.request.form  # Získání dat z formuláře

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

    return "Data byla úspěšně zpracována!"


@app.route("/results")
def results():
    results_list = db_handler.get_all()
    print(results_list)
    output_list = []
    for result in results_list:
        output_list.append(
            {"question": result, "list_of_choices": db_handler.get(result)}
        )
        print()
        print(result)
        print(db_handler.get(result))

    print(output_list)

    return flask.render_template("result.html", output_list=output_list)


if __name__ == "__main__":
    app.run(debug=True)
