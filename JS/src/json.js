fetch("https://LucianoPueyo.github.io/Codo-a-codo-Fullstack-24172/datos.json")
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.log("Ocurrió un error!"));
