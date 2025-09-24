import streamlit as st
import requests
from firebase_admin import auth
from firebase_init import initialize_firebase

# Pastikan hanya memanggil init di awal modul
initialize_firebase()

def login():
    st.sidebar.title("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if not email or not password:
            st.error("Harap isi semua kolom")
        else:
            try:
                url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
                payload = {'email': email, 'password': password, 'returnSecureToken': True}
                params = {'key': 'YOUR_FIREBASE_API_KEY'}
                response = requests.post(url, params=params, json=payload)
                data = response.json()

                if 'error' in data:
                    st.error(f"Autentikasi gagal: {data['error']['message']}")
                else:
                    st.success("Berhasil masuk!")
                    st.session_state['logged_in'] = True
                    st.rerun()
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    return email

def signup():
    st.sidebar.title("Daftar")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Kata Sandi", type="password")

    if st.sidebar.button("Daftar"):
        if not email or not password:
            st.error("Harap isi semua kolom")
        else:
            try:
                user = auth.create_user(email=email, password=password)
                st.success("Pengguna berhasil dibuat!")
                st.session_state['logged_in'] = True
                st.rerun()
            except auth.EmailAlreadyExistsError:
                st.error("Email sudah digunakan.")
            except Exception as e:
                st.error(f"Error saat membuat pengguna: {e}")
