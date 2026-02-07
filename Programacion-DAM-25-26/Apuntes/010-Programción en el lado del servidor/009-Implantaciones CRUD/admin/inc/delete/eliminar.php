<?php

  $id = $_GET['id'];									// ATRAPO EL ID A ELIMINAR

  $host = "localhost";									// EM CONECTO A LA BASE DE DATOS
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);		// EJECUTO LA CONEXION

  $sql = "DELETE FROM noticias WHERE id = ".$id.";";	// PREPARO LA PETICION
  
  $conexion->query($sql);								// EJECUTO LA PETICION
	
  $conexion->close();									// CIERRO LA CONEXION
  header("Location: escritorio.php");					// Y ME VUELVO AL ESCRITORIO
  
?>
