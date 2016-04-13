lappend sourceDatasets {C:/Users/ndrissi/Desktop/test_fme/1_tests_fme_donnees_entree/communes-20150101-50m.shp}
set sourceDatasets [lsort [eval FME_RecursiveGlob $sourceDatasets]]
foreach dataset $sourceDatasets {
C:/Program Files/FME/fme.exe C:/ndrissi/Desktop/test_fme/postgis2shape_testLambert93.fmw --source "$dataset"
}