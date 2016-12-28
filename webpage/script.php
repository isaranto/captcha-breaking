<?php
$images = glob('images/*');
return $images[rand(0, count($images) - 1)];
?>

