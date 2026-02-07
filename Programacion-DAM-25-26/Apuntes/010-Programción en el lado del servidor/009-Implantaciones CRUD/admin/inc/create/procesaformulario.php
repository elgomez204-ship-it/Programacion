<?php
	// Primero cogemos la info que viene del formulario

	$titulo = $_POST['titulo'];								// ATRAPO EL TITULO
	$contenido = $_POST['contenido'];						// ATRAPO EL CONTENIDO
	$fecha_publicacion = $_POST['fecha_publicacion'];		// ATRAPO LA FECHA
	$autor_id = $_POST['autor_id'];							// ATRAPO EL ID DEL AUTOR

	 // Y luego metemos esa información en la base de datos
	$host = "localhost";									// ME CONECTO A LA BBDD	
	$user = "periodico";
	$pass = "Periodico123$";
	$db   = "periodico";

	$conexion = new mysqli($host, $user, $pass, $db);		// EJECUTO LA CONEXION

	// Metemos los datos en la base de datos
	$sql = "
	INSERT INTO noticias VALUES(
		NULL,
		'".$titulo."',
		'".$contenido."',
		'".$fecha_publicacion."',
		".$autor_id."
		);
	";														// LANZO LA CONEXION													 
	$conexion->query($sql);

	$conexion->close();										// CIERRO LA CONEXION
	header("Location: ../../escritorio.php");				// VUELVO AL ESCRITORIO

?>

