import streamlit as st
import preprocessor,functions
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")

    df=preprocessor.preprocess(data)
    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")

    selected_user = st.sidebar.selectbox("show user list", user_list)

    if st.sidebar.button("show analysis"):

       total_messages=functions.total_message(selected_user,df)
       total_words = functions.total_words(selected_user,df)
       total_media_msg = functions.total_media_msg(selected_user,df)
       total_links = functions.total_links(selected_user,df)
       col1,col2,col3,col4 = st.columns(4)

       with col1:
            st.header("Total Messages")
            st.title(total_messages)

       with col2:
           st.header("Total Words")
           st.title(total_words)

       with col3:
           st.header("Total Media shared")
           st.title(total_media_msg)

       with col4:
           st.header("Total links shared")
           st.title(total_links)

       # most active user
       if selected_user == 'overall':
           st.title("most active users")
           x = functions.most_active_user(df)
           fig, ax = plt.subplots()

           col1,col2 = st.columns(2)

           with col1:
               ax.bar(x.index, x.values)
               plt.xticks(rotation=90)
               st.pyplot(fig)

           with col2:
               new_df=functions.percent_peruser(df)
               st.dataframe(new_df)

       st.title("wordCloud")
       df_wc = functions.create_wordcloud(selected_user, df)
       fig , ax = plt.subplots()
       ax.imshow(df_wc)

       st.pyplot(fig)

       #most common word
       most_common_word_df = functions.most_common_words(selected_user,df)

       fig , ax = plt.subplots()

       ax.bar(most_common_word_df[0],most_common_word_df[1])
       plt.xticks(rotation='vertical')
       st.title("most common words")
       st.pyplot(fig)

       st.dataframe(most_common_word_df)
