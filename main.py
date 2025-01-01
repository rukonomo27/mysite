import streamlit as st 
import time
# import numpy as np
# import pandas as pd
# from PIL import Image 

st.title('Streamlit 超入門')

st.write('Dispaly Image')

st.write('Interactive widgets')


text = st.text_input('あなたの趣味は？')
'あなたの趣味:', text

condition = st.slider('今の調整は？', 0, 100, 50)
'あなたの調子:', condition

option = st.selectbox(
        '好きな数字を教えてください',
        list(range(1,11))
)

'好きな数字は ', option ,' です'

# if st.checkbox('Show Image'):
#     img = Image.open('cat_image.jpg')
#     st.image(img, caption = 'cat', use_container_width = True)

# st.write('DataFrame')
# df = pd.DataFrame(
#         np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], 
#         columns=['lat', 'lon']
# )
# st.map(df)

# st.dataframe(df, width=100, height=100)
