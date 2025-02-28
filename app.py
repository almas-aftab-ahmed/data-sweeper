import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("📊 Data Sweeper App")
st.write("Upload a CSV file to clean and analyze it.")

# Upload File
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show raw data
    st.subheader("📌 Raw Data")
    st.write(df.head())

    # Cleaning Options
    st.subheader("🛠️ Data Cleaning Options")

    if st.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()
        st.success("✅ Duplicates Removed")

    if st.checkbox("Fill Missing Values (with mean)"):
        df = df.fillna(df.mean(numeric_only=True))
        st.success("✅ Missing Values Filled")

    # Show cleaned data
    st.subheader("✅ Cleaned Data")
    st.write(df.head())

    # Basic Statistics
    st.subheader("📈 Basic Data Statistics")
    st.write(df.describe())

    # Data Visualization
    st.subheader("📊 Data Visualization")
    numeric_columns = df.select_dtypes(["number"]).columns

    if len(numeric_columns) > 0:
        column = st.selectbox("Select a column to visualize", numeric_columns)
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=20, edgecolor="black")
        ax.set_title(f"Distribution of {column}")
        st.pyplot(fig)
    else:
        st.write("No numeric columns found for visualization.")

    # Download cleaned data
    st.subheader("📥 Download Cleaned Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "cleaned_data.csv", "text/csv")

st.markdown("**Made with ❤️ using Streamlit**")
