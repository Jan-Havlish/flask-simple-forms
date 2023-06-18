from __init__ import db_handler


def convert_multi_dict_to_dict(multi_dict):
    """
    Converts a multi-value dictionary to a standard dictionary by creating new key-value pairs
    for each unique key with a list of all its values as the value.

    :param multi_dict: A dictionary with multiple values for some keys.
    :type multi_dict: dict

    :return: A dictionary with unique keys and a list of all their values.
    :rtype: dict
    """
    data = multi_dict
    result = {}
    for key in data.keys():
        result[key] = data.getlist(key)
    return result


def make_empty_db(questions_and_choices_dictionary):
    """
    Takes a dictionary of questions and choices and creates an empty database for each question
    with a dictionary of choices initialized to 0. 

    :param questions_and_choices_dictionary: A dictionary containing questions and their choices.
    :type questions_and_choices_dictionary: dict

    :return: None
    :rtype: None
    """
    for question_dict in questions_and_choices_dictionary:
        dict_of_choices = {
            choice: 0 for choice in question_dict["list_of_choices"]}
        db_handler.set(question_dict["question"], dict_of_choices)


def get_template_array(questions_and_choices_dictionary):
    """
    Returns a list of dictionaries where each dictionary contains a question as the key 
    and a dictionary containing the choices as the key and 0 as the value. 

    :param questions_and_choices_dictionary: A list of dictionaries where each dictionary contains a 
        question as the key and a list of choices for that question as the value.
    :type questions_and_choices_dictionary: List[Dict[str, Union[str, List[str]]]]

    :return: A list of dictionaries where each dictionary contains a question as the key 
        and a dictionary containing the choices as the key and 0 as the value.
    :rtype: List[Dict[str, Dict[str, int]]]
    """
    return [
        {
            question_dict["question"]: {
                choice: 0 for choice in question_dict["list_of_choices"]
            }
        }
        for question_dict in questions_and_choices_dictionary
    ]
