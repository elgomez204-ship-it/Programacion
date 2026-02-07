<?php
	// Primero cogemos la info que viene del formulario

	$titulo = $_POST['titulo'];								// ATRAPO EL TITULO
	$contenido = $_POST['contenido'];						// ATRAPO EL CONTENIDO
	$fecha_publicacion = $_POST['fecha_publicacion'];		// ATRAPO LA FECHA
	$autor_id = $_POST['autor_id'];							// ATRAPO EL ID DEL AUTOR
	$id = $_POST['id'];										// ATRAPO EL ID				

	// Y luego metemos esa información en la base de datos
	$host = "localhost";														// Me conecto a la base de datos
	$user = "periodico";
	$pass = "Periodico123$";
	$db   = "periodico";

	$conexion = new mysqli($host, $user, $pass, $db);		// EJECUTO LA CONEXION

	// Metemos los datos en la base de datos
	$sql = "
		UPDATE noticias
		SET 
		titulo = '".$titulo."',
		contenido = '".$contenido."',
		fecha_publicacion = '".$fecha_publicacion."',
		autor_id = ".$autor_id."
		WHERE id = ".$id.";
	";	
		
	echo $sql;												// LANZO LA CONEXION													 
	$conexion->query($sql);

	$conexion->close();										// CIERRO LA CONEXION
	header("Location: ../../escritorio.php");				// VUELVO AL ESCRITORIO

?>

