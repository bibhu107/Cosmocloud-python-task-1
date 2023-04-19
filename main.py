list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # Create a dictionary to store the merged data
    merged_dict = {}
    
    # Merge the data from list_1 into the merged dictionary
    for item in list_1:
        merged_dict[item["id"]] = item
    
    # Merge the data from list_2 into the merged dictionary
    for item in list_2:
        if item["id"] in merged_dict:
            merged_dict[item["id"]].update(item)
        else:
            merged_dict[item["id"]] = item
    
    # Convert the merged dictionary back to a list
    list_3 = list(merged_dict.values())
    
    return list_3


list_3 = merge_lists(list_1, list_2)

for element in list_3:
    print(element)