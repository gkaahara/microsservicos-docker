<?php
header('Content-Type: application/json');
echo json_encode([
    'service' => 'PHP Apache Microservice 3',
    'message' => 'API PHP funcionando!',
    'timestamp' => date('c')
]);
?>
