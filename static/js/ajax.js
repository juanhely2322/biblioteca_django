const listarLibros=async()=>{
    try{

        const response =await fetch("./libros");
        const data =await response.jsom();

    }catch(error){

    }

};


const cargaInicial=async()=>{


};




window.addEventListener("load",async()=>{

    await cargaInicial();
});