
Write-Host "Ejemplo de funcionamiento basico"
$ruta = Read-Host "Coloque la ruta de el archivo menú"
$imagenes = Read-Host "Ruta de imagenes para metadatos"
Write-Host "Script de Metadatos"
python $ruta -script metadatos -dato $imagenes
Write-Host "Script de encriptado de textos"
python $ruta -script cifrado -dato encriptar -text "hola como estas"

Write-Host "Script de desencriptado de textos"
python $ruta -script cifrado -dato des -text "DKHW YKIK AOPWO"

Write-Host "Script de Scraping"
python $ruta -script scraping -dato "https://www.uanl.mx/"







