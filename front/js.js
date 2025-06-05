document.addEventListener("DOMContentLoaded",()=>{
    fetchprodutos()
});
function fetchprodutos() {
    fetch("http://127.0.0.1:8000/api/comidas/")
    .then (res => res.json())
    .then (data => rendercomidas(data))
    .catch (err => console.error("erro ao buscar", err))
}
function rendercomidas(comidas){
    const container = document.getElementById("ultragrid");
    container.innerHTML = "";
    comidas.forEach(comida => {
        const card = document.createElement("div");
        card.className = "jacinto_grid";
        card.innerHTML = `
            <img src="${comida.imagem}" alt="${comida.nome}" class="img-comida">
            <div>
                <h2 class="nome-comida">${comida.nome}</h2>
                <p>${comida.descricao}</p>
            </div>
        `;
        container.appendChild(card)
    });
}