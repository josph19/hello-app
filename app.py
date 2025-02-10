import streamlit as st

def main():
    # Streamlit App Title
    st.title("VSM Generator from Text")

    # User Input
    user_input = st.text_area("Describe your process or workflow:", "Enter your process description here...")
        

if __name__ == "__main__":
    main()
