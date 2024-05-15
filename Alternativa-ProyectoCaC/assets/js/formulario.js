document.addEventListener("DOMContentLoaded", function() {
    const actualizarVisibilidadCampos = () => {
        const tipoDomicilio = document.querySelector('input[name="tipo"]:checked').value;
        const esDepartamento = tipoDomicilio === 'departamento';
        document.getElementById('pisoContainer').style.display = esDepartamento ? 'block' : 'none';
        document.getElementById('timbreContainer').style.display = esDepartamento ? 'block' : 'none';
    };

    document.querySelectorAll('input[name="tipo"]').forEach(radio => {
        radio.addEventListener('change', actualizarVisibilidadCampos);
    });
});