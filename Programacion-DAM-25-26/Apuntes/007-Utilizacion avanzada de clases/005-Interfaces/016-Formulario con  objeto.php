<?php

	$cliente = [
		"nombre" => "Valentín",
		"apellidos" => "De Gennaro",
		"email" => "info@valentindg.com"
	];

	foreach($cliente as $clave=>$valor){
		echo "<label>".$clave."<label>";    					## LEGEND(escalonado) LABEL(horizontal)
		echo "<input type='text' value='".$valor."'>";
	}


?>
