/*Ingreso automatico del carousel*/
/*ver en Index ====> section id="carousel" */

document.addEventListener('DOMContentLoaded', function () {

/*Variable contenedora de todo el html*/
var carousel_boots = 
`
<div class="carousel-container">
<div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="5000">
            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-1.png"
                alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="5000">
            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-2.png"
                alt="...">
        </div>
        <div class="carousel-item">
            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-3.png"
                alt="...">
        </div>
    </div>
    <!--Botones-->
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
</div>
`

document.getElementById("carousel").innerHTML = carousel_boots;
});

/*El html ingresado - correspondiente al carousel de Bootstrap*/
/*

            <div class="carousel-container">
                <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item active" data-bs-interval="5000">
                            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-1.png"
                                alt="...">
                        </div>
                        <div class="carousel-item" data-bs-interval="5000">
                            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-2.png"
                                alt="...">
                        </div>
                        <div class="carousel-item">
                            <img class="d-block w-100 carousel-img" src="./assets/img/carousel/lib-carou-3.png"
                                alt="...">
                        </div>
                    </div>
                    <!--Botones-->
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval"
                        data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval"
                        data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
                <!--Clase "data-bs-interval="valor" " controla el tiempo, esta en miliseg (multiplicar tiempo deseado x1000)-->
                <!--Control de contenedor de imagenes "d-block" y "w-100" // Buscar en documentacion para ajuste en maquetacion final-->
            </div>

*/