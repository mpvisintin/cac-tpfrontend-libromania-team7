/*Ingreso automatico de libros*/
/*ver en Index ====> section id="catalogo2" */

document.addEventListener('DOMContentLoaded', function () {
    const catalogoContainer = document.querySelector('#catalogo2');
    const libros = 
    [
        { titulo: "La última tentación de Cristo", autor: "Nikos Kazantzakis", año: 1953, 
        imagenurl: "./assets/img/catalogo/lib-cat-1.png", 
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim" 
        },

        { titulo: "Metro 2023", autor: "Dmitri Glujovski ", año: 2007, 
        imagenurl: "./assets/img/catalogo/lib-cat-2.png", 
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim" 
        },

        { titulo: "El Psicoanalista", autor: "John Katzenbach", año: 2002,  
        imagenurl: "./assets/img/catalogo/lib-cat-3.png",
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim" 
        },

        { titulo: "The Coming", autor: "Vark Vikernes", año: 2018, 
        imagenurl:"./assets/img/catalogo/lib-cat-4.png",
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim"
        },

        { titulo: "Yo Matias", autor: "Sendra", año: 2006, 
        imagenurl: "./assets/img/catalogo/lib-cat-5.png", 
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim" 
        },

        { titulo: "La alegria de cocinar", autor: "El Arguiñano", año: 1954, 
        imagenurl: "./assets/img/catalogo/lib-cat-6.png",
        descripcion: "lacus laoreet non curabitur gravida arcu ac tortor dignissim"
        },
        ,
    ];
   
    libros.forEach(libro => {
        const card = document.createElement('div');
        card.className = 'card-container';
        card.innerHTML = `
            <div class="card-title">
                <p>${libro.titulo}</p>
            </div>
            
            <div class="card-body">
                <img src="${libro.imagenurl}">
                <p class="card-text">"${libro.descripcion}"</p>
            </div>
            
            <div class="card-foot"> 
                <p>${libro.autor} - ${libro.año}</p>
            </div>
        `;
        document.querySelector('.cards-catalogo').appendChild(card); // Aquí se modifica
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