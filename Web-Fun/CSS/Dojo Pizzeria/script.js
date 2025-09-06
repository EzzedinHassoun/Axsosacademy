function bakePizza() {
  const crust = document.getElementById("crust").value;
  const sauce = document.getElementById("sauce").value;

  const cheeses = Array.from(document.querySelectorAll("#cheeses input:checked"))
    .map(input => input.value);

  const toppings = Array.from(document.querySelectorAll("#toppings input:checked"))
    .map(input => input.value);

  const pizza = {
    crust,
    sauce,
    cheeses,
    toppings
  };

  document.getElementById("output").textContent = JSON.stringify(pizza, null, 2);
}
