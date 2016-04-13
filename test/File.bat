C:/Program Files/FME/fme.exe C:/Users/ndrissi/Desktop/test_fme/scanFME.tcl
pause

set error_file [open "C:/Users/ndrissi/Desktop/test_fme/erreurs.log" "w"]
lappend sourceDatasets {C:/Users/ndrissi/Desktop/test_fme/1_tests_fme_donnees_entree/communes-20150101-50m.shp}
set sourceDatasets [lsort [eval FME_RecursiveGlob $sourceDatasets]]
foreach dataset $sourceDatasets {
puts "Traitement de : $dataset"
if [ catch { C:/PROGRA~1/FME/FME.EXE C:/Users/ndrissi/Desktop/test_fme/postgis2shape_testLambert93.fmw --source "$dataset" -LOG_FILENAME "C:/Users/ndrissi/Desktop/test_fme/fme.log" -LOG_APPEND "YES" } erreur ] {
puts $error_file "erreur lors du chargement de $dataset"
puts "Erreur avec le jeu de données $dataset : $erreur \n"
}
}
close $error_file