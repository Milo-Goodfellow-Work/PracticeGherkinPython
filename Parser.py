import Lexer
successful_list = []

#All_parser finds a dictionary item in which the value is equal to the case given to it.
#If this isn't found, it throws an error.
def all_parser(expected_given, parse_dictionary):
    dictionary_key = 'not found'
    key_position = 'not found'
    for key, x in parse_dictionary.items():
        for k in x:
            for i in range(0, len(k)):
                if k[i] == expected_given:
                    dictionary_key = key
                    key_position = i

    if dictionary_key != 'not found' and key_position != 'not found':
        successful_list.append('PASSED GIVEN: {}'.format(expected_given))
        return [dictionary_key, key_position]
    else:
        raise Exception('Check failed with input:"{}"'.format(expected_given))

def all_tests_completed():
    print(successful_list)
