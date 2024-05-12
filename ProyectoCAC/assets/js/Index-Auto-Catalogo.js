/*Ingreso automatico de libros*/
/*ver en Index ====> section id="catalogo2" */

document.addEventListener('DOMContentLoaded', function () {
    const catalogoContainer = document.querySelector('#catalogo2');
    const libros = 
    [
        { titulo: "La última tentación de Cristo", autor: "Nikos Kazantzakis", año: 1953, imagenurl: "./assets/img/catalogo/lib-cat-1.png" },
        { titulo: "Metro 2023", autor: "Dmitri Glujovski ", año: 2007, calificacion: 9, imagenurl: "./assets/img/catalogo/lib-cat-2.png" },
        { titulo: "El Psicoanalista", autor: "John Katzenbach", año: 2002, calificacion: 8, imagenurl: "./assets/img/catalogo/lib-cat-3.png" },
        { titulo: "The Coming", autor: "Vark Vikernes", año: 2018, calificacion: 8, imagenurl: "./assets/img/catalogo/lib-cat-4.png" },
        { titulo: "Yo Matias", autor: "Sendra", año: 2006, calificacion: 10, imagenurl: "./assets/img/catalogo/lib-cat-5.png" },
        { titulo: "La alegria de cocinar", autor: "El Arguiñano", año: 1954, calificacion: 10, imagenurl: "./assets/img/catalogo/lib-cat-6.png" },
    ];

    libros.forEach(libro => 
    {
        const card = document.createElement('div'); /*Importante, el contenedor de la tarjeta es div class="card-container*/
        card.className = 'card-container';  /*dicha clase vinculada con el css que las estiliza*/
        card.innerHTML = `
            <div class="card-title">
                <p>${libro.titulo}</p>
            </div>
            
            <div class="card-body">
                <img src="${libro.imagenurl}">
                <p class="card-text">Descripción breve del libro</p>
            </div>
            
            <div class="card-foot"> 
                <p>${libro.autor} - ${libro.año}</p>
            </div>
        `;
        catalogoContainer.appendChild(card);
    });
});


/*El html ingresado - correspondiente a las card de libros*/
/*

<div class="card-container">
    <div class="card-title">
        <p>${libro.titulo}</p>
    </div>

    <div class="card-body">
        <img src="${libro.imagenurl}">
            <p class="card-text">Descripción breve del libro</p>
    </div>

    <div class="card-foot">
        <p>${libro.autor} - ${libro.año}</p>
    </div>
</div>

*/