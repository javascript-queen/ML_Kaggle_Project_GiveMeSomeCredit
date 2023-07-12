import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prediction_page import show_prediction_page
from PIL import Image

page = st.sidebar.selectbox("Dataset Or Prediction", ("Prediction", "Dataset"))

if page == "Prediction":
  show_prediction_page()
else:
  st.title("Stack Overflow Annual Developer Survey")

  
  
  image = Image.open('lang.png')
  
  st.image(image, caption='Programming, scripting, and markup languages')
  
  st.write("""
          #### The dataset used URLs:
          """)
  
  def create_link(url:str) -> str:
    return f'''<a href="{url}">🔗</a>'''

  df = pd.DataFrame(
      {"Year": "2023 Others".split(),
      "URL": "https://survey.stackoverflow.co/2023 https://insights.stackoverflow.com/survey".split()}
      )

  df['Link'] = [create_link(url) for url in df["URL"]]

  fig = go.Figure(
    data=[
      go.Table(
        columnwidth = [0.5,2,0.5],
        header=dict(
          values=[f"<b>{i}</b>" for i in df.columns.to_list()],
          fill_color='#F1B45A'
          ),
        cells=dict(
          values=df.transpose()
          )
        )
      ]
    )

  st.plotly_chart(fig, use_container_width=True)
  
  