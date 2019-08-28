successful_list = []

#Given_parser finds a dictionary item in which the "Given" value is equal to the case given to it.
#If this isn't found, it throws an error.
def given_parser(expected_given, parse_dictionary):
    dictionary_key = 'not found'
    for key, i in parse_dictionary.items():
        if i[0] == expected_given:
            dictionary_key = key

    if dictionary_key != 'not found':
        successful_list.append('PASSED GIVEN: {}'.format(expected_given))
        return dictionary_key
    else:
        raise Exception('Given check failed with input:"{}"'.format(expected_given))

#When finds an item in a dictionary item in which the "When" value is equal to the case given to it.
#It is provided with the dictionary to search.
#If this is not found, it throws an error.
def when_parser(expected_given, dict_key, dict):
    dict_pos = dict[dict_key]
    item_found = 0
    for i in dict_pos:
        if i[1] == expected_given:
            item_found = 1
    if item_found != 0:
        successful_list.append('PASSED WHEN: {}'.format(expected_given))
        return True
    else:
        raise Exception('When check failed with given input:"{}"'.format(expected_given))

#Then finds an item in a dictionary item in which the "Then" value is equal to the case given to it.
#It is provided with the dictionary to search
#If this is not found, it throws an error.
def then_parser(expected_given, dict_key, dict):
    dict_pos = dict[dict_key]
    item_found = 0
    for i in dict_pos:
        if i[2] == expected_given:
            item_found = 1
    if item_found != 0:
        successful_list.append('PASSED THEN: {}'.format(expected_given))
        return True
    else:
        raise Exception('Then check failed with given input:"{}"'.format(expected_given))
