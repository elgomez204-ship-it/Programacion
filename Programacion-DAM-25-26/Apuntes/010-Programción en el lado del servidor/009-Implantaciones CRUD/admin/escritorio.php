<!doctype html>
<html lang="es">
	<head>
		<title>LocalHost - Panel de control</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/estilo.css">
	</head>
	<body>
		<nav>
			<button>Noticias</button>
			<button>Autores</button>
		</nav>
		<main>
			<?php
			// ESTO SE CONOCE COMO ROUTER (ENRUTADOR) ////////////////////////
				if(isset($_GET['accion'])){
					if($_GET['accion'] == "nuevo"){									// DEFINO LA ACCION NUEVO
						include "inc/create/formulario.php";						// INCLUYO FORMULARIO.PHP
						
					}else if($_GET['accion'] == "eliminar"){						// DEFINO LA ACCION ELIMINAR
						include "inc/delete/eliminar.php";							// INCLUYO ELIMINAR.PHP
						
					}else if($_GET['accion'] == "editar"){							// DEFINO LA ACCION EDITAR
						include "inc/update/formulario_actualizar.php";				// INCLUYO FORMULARIO_ACTUALIZAR.PHP
					}
					
				}else{
					include "inc/read/Leer.php";
				}
			?>
			<a href="?accion=nuevo" id="nuevo">+</a>
		</main>
	</body>
</html>


