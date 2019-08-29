def input_gherkin(input):
    #Divide the input into Individual features in a list.
    feature_list = input.split("Feature:")
    feature_scenario_dict = {}

    #Clean the feature list of unnecessary spaces and excess list positions.
    for i in range(0,len(feature_list)):
        if feature_list[i].startswith(" "):
            feature_list[i] = feature_list[i][1:len(feature_list[i])]

        if feature_list[i].endswith(" "):
            feature_list[i] = feature_list[i][0:-1]

    del feature_list[0]

    #Create a dictionary. The key is the position in the feature list, the item is a list of scenarios.
    for i in range(0, len(feature_list)):
        temp_scenario_list = feature_list[i].split('Scenario:')
        del temp_scenario_list[0]
        #Clean the temporary scenario list of unnecessary spaces and excess list positions.
        for x in range(0, len(temp_scenario_list)):
            if temp_scenario_list[x].startswith(" "):
                temp_scenario_list[x] = temp_scenario_list[x][1:len(temp_scenario_list[x])]
            if temp_scenario_list[x].endswith(" "):
                temp_scenario_list[x] = temp_scenario_list[x][0:-1]
        feature_scenario_dict[i] = temp_scenario_list
    #Iterate over the scenario dictionary. Divide each scenario into its component parts.
    #Given:
    #And:
    #When:
    #And:
    #And:
    #Then:
    #Add all of these strings to a new dictionary. The key being which scenario it is in, the item being a list of all of the above in string form.
    for key, item in feature_scenario_dict.items():
        component_parts = []
        scenario_li = []
        for i in item:
            component_parts = i.splitlines()
            index = 0
            while index < len(component_parts):
                for z, y in enumerate(component_parts[index]):
                    if y.isalpha():
                        component_parts[index] = component_parts[index][z:]
                        break

                if component_parts[index].isspace() or component_parts[index] == None:
                    del component_parts[index]

                index += 1



            scenario_li.append(component_parts)
        feature_scenario_dict[key] = scenario_li


    #Once every single scenario has a respective list return the dictionary.
    return feature_scenario_dict
