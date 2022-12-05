(function(){
    
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro que quieres eliminar el cliente?')
            if(!confirmacion){
                e.preventDefault();
            }
        })
    });
})();
