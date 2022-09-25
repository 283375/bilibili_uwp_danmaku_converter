from time import sleep
from xml.dom.minidom import parse
from os.path import split as path_split, join as path_join
from sys import argv

def convert(file):
    dom = parse(file)
    collection = dom.documentElement

    danmakus = collection.getElementsByTagName("d")

    for d in danmakus:
        properties = d.getAttribute("p").split(",")

        row_id = properties[0]
        time_int = properties[2]
        type = properties[3]
        size = properties[4]
        color = properties[5]
        timestamp = properties[6]
        uid_crc32 = properties[8]

        time_decimal = list(time_int)
        time_decimal.insert(-3, ".")
        time_decimal = "".join(time_decimal)
        replace_properties = [
            time_decimal,
            type,
            size,
            color,
            timestamp,
            "0",
            uid_crc32,
            row_id,
        ]
        replace_properties = ",".join(replace_properties)

        d.setAttribute("p", replace_properties)

    fp_fn = path_split(file)
    new_fn = fp_fn[1].split('.')
    new_fn[-2] = f'{new_fn[-2]}_converted'
    new_file = path_join(fp_fn[0], ".".join(new_fn))
    with open(new_file, "w+", encoding='utf-8') as f:
        dom.writexml(f, encoding="utf-8")


if __name__ == "__main__":
    filelist = argv[1:]

    for file in filelist:
        print(f'Processing {file}...')
        try:
            convert(file)
        except Exception as e:
            print(f'Error while processing {file}:')
            print(e)

    print('All done.')
    sleep(1)