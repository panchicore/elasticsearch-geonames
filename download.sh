#!/usr/bin/env bash
echo "Setting env vars..."
source environment_variables.sample.sh

echo "Downloading Geonames gazetteer..."
mkdir tmp
cd tmp
#wget http://download.geonames.org/export/dump/countryInfo.txt
#wget http://www.geonames.org/premiumdata/latest/allCountries.zip
echo "Unpacking..."
#unzip allCountries.zip

echo "Downloading Geonames bounding boxes..."
#wget http://www.geonames.org/premiumdata/latest/boundingbox.zip
echo "Unpacking..."
#unzip boundingbox.zip

cd ..

echo "Creating mappings for the fields in the Geonames index:"
echo ${ES_GEONAMES_HOST}${ES_GEONAMES_INDEX}
curl -XPUT ${ES_GEONAMES_HOST}${ES_GEONAMES_INDEX} -H 'Content-Type: application/json' -d @./mappings/geonames_mapping.json

echo "Creating mappings for the countries info:"
echo ${ES_GEONAMES_HOST}geonames_country_info
curl -XPUT ${ES_GEONAMES_HOST}geonames_country_info -H 'Content-Type: application/json' -d @./mappings/geonames_mapping.countryInfo.json


echo "Done"


