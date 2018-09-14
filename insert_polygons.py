"""
Use this to insert the polygons from allshapes.txt into existing ES GN index.
"""
import time
import requests
import json

x = 0
shapes_txt_path = "tmp/allshapes.txt"
# shapes_txt_path = "tmp/test.txt"
_from = int(raw_input("Index number?") or 0)
s = []
size_acum = 0

with open(shapes_txt_path) as infile:
    for line in infile:
        x += 1
        if x < _from:
            continue

        colums = line.split("\t")
        geoname_id = colums[0]

        size = len(colums[1].encode('utf-8')) / 1000
        size_acum += size

        # if size <= 5000:
        #     pass
        # else:
        #     continue

        try:
            o = json.loads(colums[1])
        except Exception as e:
            print e
            continue

        coordinates = o["coordinates"]

        new_coords = []

        if o["type"] == "Polygon":
            for root in coordinates:
                temp = None
                root_coords = []
                for c in root:
                    if c == temp: continue
                    temp = c
                    root_coords.append(c)

                if root_coords[0] != root_coords[-1]:
                    root_coords.append(root_coords[0])

                new_coords.append(root_coords)

        else:
            for base in coordinates:
                base_coords = []
                for root in base:
                    temp = None
                    root_coords = []
                    for c in root:
                        if c == temp: continue
                        temp = c
                        root_coords.append(c)

                    if root_coords[0] != root_coords[-1]:
                        root_coords.append(root_coords[0])
                    base_coords.append(root_coords)
                new_coords.append(base_coords)

        polygon = {
            "type": o["type"].lower(),
            "coordinates": new_coords
        }

        payload = {
            "doc": {"geom_polygon": polygon, "geom_polygon_type": "polygon"},
        }

        print x, geoname_id, "size:", size

        bulk = True
        try:
            # d = json.dumps(payload)
            # res = requests.post("http://localhost:9200/geonames_new/doc/{}/_update".format(geoname_id),
            #                     data=d,
            #                     headers={'Content-Type': 'application/json'})
            #print x, "\t", geoname_id, "\t", res.elapsed, "\t", res.content

            s.append('{"update": {"_id": %s, "_type": "doc", "_index": "geonames_new"}}' % (geoname_id))
            s.append(json.dumps(payload))

            if size_acum > 1000:
                s = "\n".join(s) + "\n"
                res = requests.post("http://localhost:9200/_bulk", data=s, headers={"Content-Type": "application/x-ndjson"})
                print x, "\t", res.elapsed
                s = []
                size_acum = 0
        except Exception as e:
            print e
            f = open("x/{}.txt".format(geoname_id), "w")
            f.write(colums[1])
            f.close()


print "END"