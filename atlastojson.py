import json

def main():
    file_dict = {
        "sprite_sheets": []
    }
    pieces = []

    file = open("Teen.atlas", "r")
    lines = file.read()

    counter = -1
    image_data = []
    for line in lines.split("\n"):
        if (line == ""):
            counter = counter + 1
            if image_data != []:
                pieces.append(image_data)
                image_data = []
        else:
            image_data.append(line)

    for piece in pieces:
        file_part_dict = extract_data(piece)
        file_dict["sprite_sheets"].append(file_part_dict)

    file.close()

    f = open("teen_atlas.json", "w")
    f.write(json.dumps(file_dict))
    f.close()

def extract_data(lines):
    image_dict = {}
    parts_dict = []
    # first line is always the file name
    image_dict["name"] = lines[0].removesuffix("\n")
    # add file details
    index = 1
    while(":" in lines[index]):
        (key, value) = lines[index].split(":")
        key = key.replace(" ", "")
        value = value.replace("\n", "").replace(" ", "")
        if ("," in value):
            value = value.split(",")
        image_dict[key] = value
        index = index + 1
    # Start with file parts array
    item = 0
    while(index < (len(lines) - 1)):
        item_details = {}
        item_details["name"] = lines[index].removesuffix("\n").removeprefix(" ")
        index = index + 1
        while(index < (len(lines) - 1) and ":" in lines[index]):
            (key, value) = lines[index].split(":")
            key = key.replace(" ", "")
            value = value.replace("\n", "").replace(" ", "")
            if ("," in value):
                value = value.split(",")
            item_details[key] = value
            index = index + 1
        item = item + 1
        parts_dict.append(item_details)
    image_dict["parts"] = parts_dict
    return image_dict

main()
