dict1 = {'fruit': 'apple','vegetable':'cauliflower','nuts':'almond'}
dict2 = {'fruit1':'orange','vegetable1':'cabbage','nuts1':'cashew'}
dict3 = {'fruit2':'banana','vegetable2':'spinach','nuts2':'walnut'}
dict4 = {**dict1, **dict2}

print(dict4)

dict5 = dict1.copy()
dict5.update(dict3)

print(dict5)
