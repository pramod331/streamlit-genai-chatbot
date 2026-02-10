import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title for the application
st.title("My First Streamlit App")

# Create a text input field
name = st.text_input("What is your name?")

# Create a button
if st.button("Submit"):
    st.write("Hello, " + name + "!")

# Create a dataframe
data = pd.DataFrame({
    "Name": ["John", "Mary", "David"],
    "Age": [25, 31, 42]
})

# Create a table
st.write(data)

# Create a plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 6])
st.pyplot(fig)