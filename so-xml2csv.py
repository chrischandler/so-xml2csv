import csv
import xml.etree.ElementTree as ET


def xml2csv(xml_file, csv_name) -> None:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[0])
        writer.writenow(headers)
        num_records = len(root)

        for record in range(num_records):
            row = (child.text for child in root[record])
            writer.writerow(row)


if __name__ == '__main__':
    import sys
    import pathlib

    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]

    except IndexError:
        print('Usage: {} <file_path> <csv_name>'.format(
            pathlib.Path(__file__).name))
        sys.exit(1)

    with pathlib.Path(file_path) as xml_file:
        if xml_file.is_file():
            xml2csv(xml_file, csv_name)
        else:
            print('{} is not a file'.format(xml_file))
            sys.exit(1)
