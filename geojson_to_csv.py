import json
import csv


# LOADING GEOJSON DATA
def load_geojson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# FORMAT LINESTRING
def process_linestrings(geojson_data):
    linestrings = []

    for feature in geojson_data['features']:
        if feature['geometry']['type'] == 'LineString':
            formatted_feature = {
                "type": "Feature",
                "properties": feature['properties'],
                "geometry": feature['geometry'],
                "id": feature['id']
            }
            linestrings.append(formatted_feature)

    return linestrings


# WRITE THE DATA TO CSV
def write_to_csv(linestrings, output_csv_path):
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(["LineString Data"])  # header (optional)
        for linestring in linestrings:
            writer.writerow([json.dumps(linestring)])



if __name__ == '__main__':
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print('config.json not found')
        exit(1)

    input_geojson_path = config["input_path"]
    output_csv_path = config["output_path"]


    geojson_data = load_geojson(input_geojson_path)  # Load the GeoJSON file
    linestrings = process_linestrings(geojson_data)  # Process and filter the LineStrings
    write_to_csv(linestrings, output_csv_path)  # Write to CSV
