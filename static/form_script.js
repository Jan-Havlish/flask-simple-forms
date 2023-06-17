
function validateForm() {
    // get all forms
    var form = document.getElementById("myForm");
    var inputs = form.getElementsByTagName("input");

    // is filled al least one field in each form?
    for (var i = 0; i < inputs.length; i++) {
        var input = inputs[i];
        if (input.type === "radio" || input.type === "checkbox") {
            var question = input.name;
            var questionInputs = form.querySelectorAll('input[name="' + question + '"]');
            var checkedInputs = Array.prototype.slice.call(questionInputs).filter(function (input) {
                return input.checked;
            });

            if (checkedInputs.length === 0) {
                alert("Vyberte prosím odpověď na všechny otázky.");
                return false;
            }
        }
    }

    return true;
}
