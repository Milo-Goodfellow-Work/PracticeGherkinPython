def input_gherkin(input):
    #Divide the input into Individual features in a list.
    feature_list = input.split("Feature:")

    #Clean the feature list of unnecessary spaces and excess.
    for i in range(0,len(feature_list)):
        if feature_list[i].startswith(" "):
            print(feature_list[i])
            feature_list[i] = feature_list[i][1:len(feature_list[i])]

        if feature_list[i].endswith(" "):
            print(feature_list[i])
            feature_list[i] = feature_list[i][0:-1]

    del feature_list[0]

    #Create a dictionary. The key is the position in the feature list, the item is a list of scenarios.
    #Iterate over the scenario dictionary. Divide each scenario into its component parts.
    #Given:
    #And:
    #When:
    #And:
    #And:
    #And:
    #Then:
    #Add all of these strings to a new dictionary. The key being which scenario it is in, the item being a list of all of the above in string form.
    #Once every single scenario has a respective list return the dictionary.


input_gherkin("Feature: Item1 Feature: Item2 Feature: Item3")
