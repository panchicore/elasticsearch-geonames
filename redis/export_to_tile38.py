import requests
import redis
import json

ES_URL = "http://localhost:9200/"
INDEX_URL = ES_URL + "geonames"

payload = {
  "size": 1,
  "_source": {
    "includes": ["ASCIIName", "geom_*", "tags", "CountryName", "GeonamesId"]
  },
  "query": {
    "bool": {
      "filter": {
        "term": {
          "tags": "country"
        }
      }
    }
  }
}

print "Scrolling..."

res = requests.post(INDEX_URL + "/_search?scroll=1m", json=payload).json()

scroll_id = res["_scroll_id"]

hits = res["hits"]["hits"]

geojson_types = {
    "point": "Point",
    "linestring": "LineString",
    "polygon": "Polygon",
    "multipoint": "MultiPoint",
    "multilinestring": "MultiLineString",
    "multipolygon": "MultiPolygon",
    "geometrycollection": "GeometryCollection"
}

tile38 = redis.StrictRedis(host='localhost', port=9851)

while True:

    payload = {
      "scroll" : "1m",
      "scroll_id": scroll_id
    }

    res = requests.post(ES_URL + "_search/scroll", json=payload).json()

    if len(res["hits"]["hits"]) == 0:
        break

    o = res["hits"]["hits"][0]["_source"]

    key = "gn_{0}_{1}".format(o["GeonamesId"], o["CountryName"].replace(" ", ""))

    print key, "..."

    geojson = {
        "type": geojson_types[o["geom_polygon"]["type"]],
        "coordinates": o["geom_polygon"]["coordinates"]
    }
    command = "DEL {0} {1}".format(o["tags"][0], key)
    tile_res = tile38.execute_command(command)
    command = "SET {0} {1} OBJECT {2}".format(o["tags"][0], key, json.dumps(geojson, separators=(',', ':')))
    tile_res = tile38.execute_command(command)
    command = "PERSIST {0} {1}".format(o["tags"][0], key)
    tile_res = tile38.execute_command(command)

requests.delete(ES_URL + "_search/scroll/" + scroll_id)
print "Deleted."

if __name__ == "__main__":
    pass
