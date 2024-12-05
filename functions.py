from collections import Counter
import pandas as pd
from wordcloud import WordCloud
from urlextract import URLExtract
extract = URLExtract()

def total_message(selected_user,df):

    if selected_user == 'overall':
        num_msg = df.shape[0]
        return num_msg
    else:
        new_df = df[df['user'] == selected_user]
        num_message = new_df.shape[0]
        return num_message

def total_words(selected_user,df):
    if selected_user == 'overall':
        words = []
        for mes in df['message']:
            words.extend(mes.split())
        return len(words)
    else:
        words = []
        new_df = df[df['user'] == selected_user]
        for mes in new_df['message']:
            words.extend(mes.split())
        return len(words)

def total_media_msg(selected_user,df):
    if selected_user == 'overall':
       num_media_mes = df[df['message'] == '<Media omitted>\n'].shape[0]
       return num_media_mes
    else:
        new_df = df[df['user'] == selected_user]
        num_media_mes = df[df['message'] == '<Media omitted>\n'].shape[0]
        return num_media_mes

def total_links(selected_user,df):
    if selected_user == 'overall':
        links = []
        for message in df['message']:
            links.extend(extract.find_urls(message))
        return len(links)
    else:
        new_df = df[df['user'] == selected_user]
        links = []
        for msg in new_df['message']:
            links.extend(extract.find_urls(msg))
        return len(links)

def most_active_user(df):
    x = df['user'].value_counts().head()
    return x

def percent_peruser(df):
    new_df=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={ 'user': 'name' , 'count':'percent'})
    return new_df

def create_wordcloud(selected_user,df):
    f = open("stop_hinglish.txt", 'r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        sent = []
        for word in message.lower().split():
            if word not in stop_words:
                sent.append(word)
        return " ".join(sent)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')

    temp["message"] = temp['message'].apply(remove_stop_words)

    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user , df):
    f = open("stop_hinglish.txt",'r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for mes in temp['message']:
        for word in mes.lower().split():
            if word not in stop_words:
                words.append(word)

    new_df = pd.DataFrame(Counter(words).most_common(20))
    return new_df