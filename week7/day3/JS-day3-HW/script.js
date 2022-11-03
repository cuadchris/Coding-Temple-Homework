const getPokemon = async () => {
  const input = document.getElementById("searchname").value.toLowerCase();
  let response = await fetch(`https://pokeapi.co/api/v2/pokemon/${input}`);
  let data = await response.json();

  const name = data.name;
  const img = data.sprites.front_shiny;
  abilities = [];
  for (let i = 0; i < data.abilities.length; i++) {
    abilities.push(data.abilities[i].ability.name);
  }
  document.getElementById("pic").src = img;
  document.getElementById("name").innerText = (() => {
    // converting first letter to uppercase
    return name.charAt(0).toUpperCase() + name.slice(1);
  })();
  document.getElementById("abilities").innerHTML = abilities
    .map(function (ability) {
      return "<li class='list-group-item'>" + ability + "</li>";
    })
    .join("");
};
