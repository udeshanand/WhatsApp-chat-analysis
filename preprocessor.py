import pandas as pd
import re

def preprocess(data):
    pattern = '[0-9]{2}\/[0-9]{2}\/[0-9]{2},\s[0-9]{1,2}:[0-9]{1,2}'
    mes = re.split(pattern, data)
    str = ""
    message = []
    for i in mes:
        str = i.replace("\u202f", "")
        str = str.replace("pm - ", "")
        str = str.replace("am - ", "")
        # str1=(i.encode("ascii", "ignore"))
        # str1 = str1.decode()
        message.append(str)

    dates = re.findall(pattern, data)

    valid_data = []
    # Iterate through both lists using zip
    for msg, date in zip(message, dates):
        # Only add data if both message and date exist
        if msg and date:
            valid_data.append({'user_message': msg, 'message_date': date})

    df = pd.DataFrame(valid_data)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)


    return df
'''
  df['message_date'] = pd.to_datetime(df['message_date'], format= 'mixed')
    df['only_date'] = df['message_date'].dt.date
    df['year'] = df['message_date'].dt.year
    df['month_num'] = df['message_date'].dt.month
    df['month'] = df['message_date'].dt.month_name()
    df['day'] = df['message_date'].dt.day
    df['day_name'] = df['message_date'].dt.day_name()
    df['hour'] = df['message_date'].dt.hour
    df['minute'] = df['message_date'].dt.minute
'''
