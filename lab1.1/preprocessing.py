from datetime import datetime

def timeconvert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:6]


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def easyconvert(list_to_change, x):
    list_to_insert = []
    for i in range(len(list_to_change)):
        list_to_insert.append(int(str(list_to_change[i])[:x]))
    return list_to_insert


def dateconvert(list_to_change):
    list_to_insert = []
    for i in range(len(list_to_change)):
        if str(list_to_change[i])[-3:] == "Jul":
            list_to_insert.append(str(str(list_to_change[i])[:-3] + '07.2019'))
        elif str(list_to_change[i])[-3:] == "Aug":
            list_to_insert.append(str(str(list_to_change[i])[:-3] + '08.2019'))
    # for i in range(len(list_to_insert)):
    #     list_to_insert[i] = datetime.strptime(list_to_insert[i], '%d.%m.%Y')
    return list_to_insert



def parse(database_df):
    list_to_change = unique(list(database_df['Time']))
    list_to_insert = []
    for i in range(len(list_to_change)):
        if len(list_to_change[i]) == 7:
            list_to_insert.append('0' + list_to_change[i])
        else:
            list_to_insert.append(list_to_change[i])
    for i in range(len(list_to_insert)):
        list_to_insert[i] = timeconvert(list_to_insert[i])
    database_df['Time'] = database_df['Time'].replace(to_replace=list_to_change,
                                                      value=list_to_insert)
    database_df['Humidity'] = database_df['Humidity'].replace(to_replace=list(database_df['Humidity']),
                                                              value=easyconvert(list(database_df['Humidity']), -1))

    database_df['Wind Speed'] = database_df['Wind Speed'].replace(to_replace=list(database_df['Wind Speed']),
                                                                  value=easyconvert(list(database_df['Wind Speed']),
                                                                                    -4))
    database_df['Wind Gust'] = database_df['Wind Gust'].replace(to_replace=list(database_df['Wind Gust']),
                                                                  value=easyconvert(list(database_df['Wind Gust']),
                                                                                    -4))
    database_df['day/month'] = database_df['day/month'].replace(to_replace=list(database_df['day/month']),
                                                                value=dateconvert(list(database_df['day/month'])))
    return database_df