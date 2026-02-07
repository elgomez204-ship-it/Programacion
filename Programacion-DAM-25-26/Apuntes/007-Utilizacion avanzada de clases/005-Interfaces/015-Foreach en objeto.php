<?php

	$cliente = [
		"nombre" => "Valentín",
		"apellidos" => "De Gennaro",
		"email" => "info@valentindg.com"
	];

	foreach($cliente as $clave=>$valor){
		echo $clave. ": ".$valor."<br>";
	}


?>
