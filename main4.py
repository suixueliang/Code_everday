cities_dict={'Beijing': {'Capital': 'China'},'Moscow': {'Capital': 'Russia'},'Paris': {'Capital': 'France'}}
for key in sorted(cities_dict.keys()):
    for key_1 in cities_dict[key]:
        print(f"{key} is the {key_1} of {cities_dict[key][key_1]}!")