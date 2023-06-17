import json

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

with open("questions_and_choices.json", "w", encoding="utf-8") as f:
    json.dump(questions_and_choices_dictionary, f, ensure_ascii=False)
    print("Data saved.")