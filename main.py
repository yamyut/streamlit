import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.write('入門')

'start'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'

#left_column,right_column=st.columns(2)
#button=left_column.button('右カラムに文字表示')
#if button:
#    right_column.write('ここは右カラム')

expander=st.expander('問い合わせ1')
expander.write('問い合わせ回答')
expander=st.expander('問い合わせ2')
expander.write('問い合わせ回答')
expander=st.expander('問い合わせ3')
expander.write('問い合わせ回答')

#condition=st.sidebar.slider('あなたの今の調子は',0,100,50)
#'コンディションは',condition

#option=st.text_input('あなたの趣味は？')
#'あなたの趣味は',option,'です'

#option=st.selectbox('好きな数字を入力',list(range(1,10)))
#'あなたの好きな数字は',option,'です'

#if st.checkbox('Show Image'):
#    img=Image.open('kose.png')
#    st.image(img,caption='kose',use_column_width=True)