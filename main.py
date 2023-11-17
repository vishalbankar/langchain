from langchainhelper import get_few_shot_db_chain
import streamlit as st


st.title(" T-shirt:DB Q&A for atliq")
que = st.text_input("qusetions: ")

if que:
    chain=get_few_shot_db_chain()
    ans = chain.run(que)
    st.header("Answer")
    st.write(ans)