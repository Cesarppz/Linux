function cerarVentana(){
    let closeButton = document.querySelector('.close a');
    let content     = document.querySelector('.content') 

    closeButton.addEventListener('click', function(ev){
        ev.preventDefault();

        content.classList.remove('animate__animated');
        content.classList.remove('animate__bounceIn');
            
        content.classList.add('animate__backOutDown');
        content.classList.add('animate__animated');
        
        setTimeout(() => {
            location.href = '/';
        }, 600);
    })
};



cerarVentana()