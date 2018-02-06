import csv

def write_to_csv(filepath, columns, data):
    with open(filepath, "w") as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(columns)

        for row in data:
            csv_writer.writerow( map( lambda x: row.get(x, ""), columns))

def flatten_json(json, delimiter):
    result = {}
    for key in json.keys():
        if isinstance( json[key], dict ):
            get = flatten_json( json[key], delimiter )
            for next_key in get.keys():
                result[ key + delimiter + next_key ] = get[next_key]
        else:
            result[key] = json[key]

    return result

def flatten_all_objects(data_array):
    flattened_data = map( lambda x: flatten_json(x, "__"), data_array)
    return flattened_data

def column_finder(flatted_json):
    # columns = [x for x in flatted_json.keys()]
    columns = [ x for row in flatted_json for x in row.keys() ]
    columns = list( set( columns ) )
    return columns 

def format_data_and_write_to_csv(filepath, data):
    flattened_data = flatten_all_objects(data)
    columns = column_finder(flattened_data)
    write_to_csv(filepath, columns, flattened_data)
