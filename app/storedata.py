import csv
import copy
import os

def write_to_csv(filepath, columns, data):
    columns.sort()
    is_empty = os.path.getsize(filepath) < 20

    if is_empty:
        with open(filepath, "w", newline="") as out_file:
            csv_writer = csv.writer(out_file)
            csv_writer.writerow(columns)

    with open(filepath, "a", newline="") as out_file:
        csv_writer = csv.writer(out_file)           

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
    flattened_data = list(map( lambda x: flatten_json(x, "__"), data_array))
    return flattened_data

def column_finder(flatted_json):
    columns = [ x for row in flatted_json for x in row.keys() ]
    # columns = []
    # for row in copied_flat:
    #     for x in row.keys():
    #         columns.append(x)

    # columns = list( set( columns ) )
    return columns 

def format_data_and_write_to_csv(filepath, data):
    flattened_data = flatten_all_objects(data)
    columns = column_finder(flattened_data)
    write_to_csv(filepath, columns, flattened_data)
    
