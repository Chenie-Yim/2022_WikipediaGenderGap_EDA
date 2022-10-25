import streamlit as st
import pandas as pd
import seaborn as sns

df = pd.read_csv('C:/Users/user/Desktop/Data_Assignment/Wisconsin Breast Cancer Diagnostic dataset.csv')
st.dataframe(data = df)

st.header("WI Cancer Dataset") 
st.sidebar.subheader("Choose X-AXIS among Area-realted columns")
select_box1_1 = st.sidebar.selectbox(label = 'X axis', options = ('area_mean', 'radius_mean', 'perimeter_mean'))
print(select_box1_1)


# Create Joint Plot
st.sidebar.subheader("Joint Plot Option: Area vs. Density")
select_box1_2 = st.sidebar.selectbox(label = 'Y axis', options = ('smoothness_mean', 'concavity_mean', 'texture_mean'))


fig1 = sns.jointplot(x = df[select_box1_1], y = df[select_box1_2], hue = "diagnosis", kind = "kde", data = df, rug = True, fill =True)
st.pyplot(fig1)


# Create Relational Plot
st.sidebar.subheader("Relational Plot Option: Area vs. Shape")
select_box2_1 = select_box1_1
print(select_box2_1)
select_box2_2 = st.sidebar.selectbox(label = 'Y axis', options = ('symmetry_mean', 'fractal_dimension_mean'))

fig2 = sns.relplot(x = select_box2_1, y = select_box2_2, hue = "diagnosis", data = df, kind = "line", style = "diagnosis")
st.pyplot(fig2)

# streamlit run TEST.py