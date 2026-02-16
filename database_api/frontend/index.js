const inputBoxes = Array.from(document.getElementsByClassName("input"));
const submitBtn = document.getElementsByClassName("data-submit")[0];

inputBoxes.forEach(input => { // Checks each input value every time a user keystroke is detected
    input.addEventListener("input", function() {
        const values = inputBoxes.map(input => input.value);

        const allFilled = values.every(value => value !== ""); // Checks if all fields have a value

        submitBtn.disabled = !allFilled; // Disables submit button if allFilled = false
        
        submitBtn.value = allFilled ? "Submit" : "Please fill all fields first";
    });
});


console.log(inputBoxes);

const Table = fetch('http://127.0.0.1:5000/api/cars');


