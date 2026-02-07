<?php
	class Perro{
		function __construct($nombre,$color,$edad){
			$this->nombre = $nombre;
			$this->color = $color;
			$this->edad = $edad;
		}
	}
	
	$perro1 = new Perro("Toto","Marron",7);
  	$perro2 = new Perro("Coco","Negro",9);
	
	var_dump($perro1);
	var_dump($perro2);
	
?>

