import streamlit as st
from streamlit_option_menu import option_menu
from login_register import login, signup
from firebase_init import initialize_firebase

# Init Firebase sekali di awal
initialize_firebase()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        choice = st.selectbox("Login / Sign Up", ("Login", "Sign Up"))
        if choice == "Login":
            login()
        else:
            signup()
    else:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Deteksi Penyakit", "Chatbot"],
                icons=["house", "file-medical", "chat"],
                menu_icon="cast",
                default_index=0
            )

        if selected == "Home":
            st.write("Home")
        elif selected == "Deteksi Penyakit":
            st.write("Deteksi Penyakit")
        elif selected == "Chatbot":
            st.write("Chatbot")

if __name__ == "__main__":
    main()
