def input_gherkin(input):
    #Divide the input into Individual features in a list.
    feature_list = input.split("Feature:")
    feature_scenario_dict = {}

    #Clean the feature list of unnecessary spaces and excess list positions.
    for i in range(0,len(feature_list)):
        if feature_list[i].startswith(" "):
            print(feature_list[i])
            feature_list[i] = feature_list[i][1:len(feature_list[i])]

        if feature_list[i].endswith(" "):
            print(feature_list[i])
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
    print(feature_scenario_dict)
    #Iterate over the scenario dictionary. Divide each scenario into its component parts.
    #Given:
    #And:
    #When:
    #And:
    #And:
    #Then:
    #Add all of these strings to a new dictionary. The key being which scenario it is in, the item being a list of all of the above in string form.
    for key, item in feature_scenario_dict:
        for i in item:
            component_parts = item.split("\n")
            for x in range(0, len(component_parts)):
                if component_parts[x].startswith(" "):
                    component_parts[x] = component_parts[x][1:len(component_parts[x])]
                if component_parts[x].endswith(" "):
                    component_parts[x] = component_parts[x][0:-1]

        feature_scenario_dict[key] = component_parts

    #Once every single scenario has a respective list return the dictionary.
    return feature_scenario_dict

user_in = '''
Feature: Some terse yet descriptive text of what is desired
  In order to realize a named business value
  As an explicit system actor
  I want to gain some beneficial outcome which furthers the goal

  Scenario: Some determinable business situation
    Given some precondition
      And some other precondition
     When some action by the actor
      And some other action
      And yet another action
     Then some testable outcome is achieved
      And something else we can check happens too

  Scenario: A different situation
'''
print(input_gherkin(user_in))
