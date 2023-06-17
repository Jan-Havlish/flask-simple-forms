from __init__ import db_handler


def convert_multi_dict_to_dict(multi_dict):
    data = multi_dict
    result = {}
    for key in data.keys():
        result[key] = data.getlist(key)
    return result


def make_empty_db(questions_and_choices_dictionary):
    for question_dict in questions_and_choices_dictionary:
        dict_of_choices = {
            choice: 0 for choice in question_dict["list_of_choices"]}
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
