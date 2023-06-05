import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
from PIL import Image
import numpy as np
import joblib
import json

st.set_page_config(
    page_title ='Student Alcohol Consumption',
    layout='wide',
    initial_sidebar_state='expanded'
)
def run():
    st.title ('Student Alcohol Consumption')
    st.subheader('EDA untuk Analisis Dataset Student')

    st.write('''Hai I'm **Muhammad Afif Alvan** from ftds-016-rmt''')

    image = Image.open('haha.jpg')
    st.image(image, caption = 'Stress Being Study')

    st.markdown('---')

    # Magic Syntax
    '''
    At this time I will discuss how the impact of alcohol
    on student scores in Portugal in mathematics
    '''
    st.markdown('---')
    #Show the Dataset

    st.write('**DATASET**')
    df = pd.read_csv('student-mat.csv')
    st.dataframe(df)

    st.write('**Describe**')
    describe = df.describe()
    st.dataframe(describe)
    # Rename Columns
    df.rename(columns={'G3': 'Final Grade'}, inplace= True)

    st.write('''
            **Analisis**
    1. Students surveyed have an age range of `15-22 years`
    2. Most alcohol consumption every day is at the `high` level
    3. The longest study time is more than 10 hours
    4. There are students who have perfect scores in the final grade
    5. There are students who have '75 days' absences
    ''')

    st.write('## Visualization')
    # Membuat barplot
    st.write('#### Barplot Grade vs Walc')
    fig = plt.figure(figsize=(15,5))
    plt.title('Barplot Final Grade vs Walc')
    sns.barplot(x=df['Final Grade'], y=df['Walc'], data = df)
    st.pyplot(fig)
    st.write('''At a glance, it can be seen that weekly
            alcohol consumption has no effect on student grades.''')
    st.write('------------')

    # Display Sex
    st.write('#### Distribution sex')
    sex = sns.catplot(x='sex', kind='count', palette ='Set1', data = df)
    plt.title('Distribution Sex')
    st.pyplot(sex)
    st.write('''Judging from this dataset, most of the students surveyed
            were girls, although the comparison was not too significant''')
    st.write('------------')


    # Membuat histogram untuk price
    st.write('### Final Grade')
    fg = plt.figure(figsize=(10,5))
    plt.title('Histogram of Price')
    sns.histplot(df['Final Grade'], kde= True, bins = 40, color='Red')
    st.pyplot(fg)
    st.write('''
            In this visualization, it can be seen that most students
            get a final grade with a score of 10. And not a few students
            get a score of 0 in this dataset.
            ''')
    st.write('------------')

    # barplot
    st.write('### Age vs Walc')
    umur = pd.cut(df['age'], bins = 2)

    umr = plt.figure(figsize=(10,5))
    sns.barplot(x = umur, y = df['Walc'], hue= df['sex'], data = df )
    st.pyplot(umr)
    st.write('''
            It is known that male students with the age range of 15-19 
            consume the most alcohol each week. However, as they get older,
            namely in the age range of 18-22, the consumption of alcohol for men 
            decreases, unlike women who consume the same every week in any age range.
            ''')
    st.write('------------')

if __name__ == '__main__':
    run()