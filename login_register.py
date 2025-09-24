import firebase_admin
from firebase_admin import credentials, auth
import streamlit as st
import requests

cred_data = {
  "type": "service_account",
  "project_id": "cardiovasculardisease-ibs",
  "private_key_id": "16da6c5038958485db99fa25e1db6e9568ec1a84",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQD3q7j2B16W4V/+\nrxd7Vavo55vN8OBpKZwsrUpm93v3mIbGYtAlifDE7lhri2nuajOJCspKTqqwNFEZ\neIbk26hmRcVdbDKmpDAnKqwqqF/yKaCZ200DQ8RZq2Iv3BpdqLLW52cF0/i4j5bS\npA3TD0ywTxC/Bc+/Gw2S42DJ4+z1HNz6q+KEZXWB3jnC/4v3fnTY9+GLFFTCzOXK\njGEBVxU1Y/eA5J9OcUq25eIf3ad0lJ//QZePdBXJUxYwiCVCsgGiC5ZqzX64YTMN\n3BDDEMejVWZUatKgRFo+DxvoLpub4OpdO32VgBHkXon4b0ORFLxSYCoOHiFpI8A1\nK0g366tXAgMBAAECggEAEwiO59VsJwM9+dgh4VgVpIn8FskOrfZFKsfMgno9fCss\nHF3mqiPeLXw1rloh83EU8dCy+B/wjScQHnl9QGRDHkz5XHMet2DB1Ji6b3LOINGj\nJn/MfNY95jg+DPiIzC7VQ5+38qI2KJTcXea+qzwvRBNncY60RvcAxYuU2h8ajEGb\nY7LpT2O0LcHF5I5/pXgQ2sNgGhvR1ggs4EWYCI3btSIZ3HdK3HLtJBdX9clrWQ84\nac/dnJ5tL5jBnuvw0R329LsuZP9rSM1h8k8vwSx1WLv2OxiS43J6biDVbXkBgxET\nIWJeLtTUhtduUv1/zYVURL2KbT+sUsu6Brh/3LAcIQKBgQD+I4hDcMTrPvqtdG/n\nCV5B1bN/hHs1PZr+ZpSWZLmDHGWAj8t4gSSaXehsQo8A3SvWvUQBRAg6YV009exr\nfEMuYdBtdL/cXU44jZOWLtMc/1a5XGi+iLg/F+5Bm8Zy48gNaf0gTY0A8AoCPCkC\nUMiw2zGaTfi+3qC2lrLZZVWTtwKBgQD5fBBU02Dsl4WBxL5yiPCh4R+w9sTWvaPQ\n88O6Iruy7v5c/X4hzvZZ8ADwiJTdNU5UwZUcr+h/4yw69VnJ1YpLZoyU4yeEaABp\nzocLx3Cyouln0CSKkrzu+SGcwSOQ8LDU5VeL9RJ8WOW9dzT1SUl9FxLz8fQNQG0W\nqMmTvYTlYQKBgQCrpYQbSMc3vEnDbalG+mTXQmcB8ZDl3L4apV4mVdGWZE+KDZT3\nxwHZ4SNiO3Iquzcoypxr3m9QPwKdCpyr3Dnj0dzckMYlKD/0omrUPLwKEcuZVnjI\nd785nggl9/iJEJ/Fr5hvgPGDeJzJ9agdEEL8cI+IELG4+NTDffU+L9sk8QKBgQDF\n+Kno9fdypuYdTKcnsfzpKACC577Y/JFSzSyits8lNTsJRWpin52jTq0gMfGW+6bV\n4OtXYUtouDcv7eO7IsVkAdNKjlqcWf8B9w34zeFjD52RcHyercRZCb6fai+z4xsf\nRYJMIEP0AoMD7uVKQ0aaicXTaEsWfOpT0cprfzdG4QKBgGEaBkc3mdyBAVqi76gX\n4e2bvDYLm19Wa9+hTGr8+TiU53Jth8Fm+dYpILoAviyto9xv5jVr3FOsBWrzMc+c\nsUTe+lLsTaOo0hUI0zCzWz9fIR2ADSS/f8Sb6AK7fqXojYdNloMd6JpromM9+ou1\nDl3er3boPJI4VOKIRzHp2CQF\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@cardiovasculardisease-ibs.iam.gserviceaccount.com",
  "client_id": "111823302926588970769",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40cardiovasculardisease-ibs.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


# Fungsi untuk menginisialisasi Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_data)
        firebase_admin.initialize_app(cred)

# Fungsi login
def login():
    st.sidebar.title("Login")

    # Kolom masukan untuk email dan kata sandi
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if not email or not password:
            st.error("Harap isi semua kolom")
        else:
            try:
                # URL REST API Otentikasi Firebase
                url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
                payload = {
                    'email': email,
                    'password': password,
                    'returnSecureToken': True
                }
                # Ganti 'YOUR_FIREBASE_API_KEY' dengan kunci API proyek Firebase Anda
                params = {
                    'key': 'AIzaSyB4ct8S_4QOLfF2q9W2gdWIAS8vy9Tym2o'
                }
                response = requests.post(url, params=params, json=payload)
                response_data = response.json()

                if 'error' in response_data:
                    error_message = response_data['error']['message']
                    if error_message == 'EMAIL_NOT_FOUND':
                        st.error("Email tidak ditemukan. Silakan daftar jika belum memiliki akun.")
                    elif error_message == 'INVALID_PASSWORD':
                        st.error("Password salah. Silakan coba lagi.")
                    else:
                        st.error(f"Autentikasi gagal: {error_message}")
                else:
                    st.success("Berhasil masuk!")
                    st.session_state['logged_in'] = True
                    st.rerun()
            except requests.exceptions.RequestException as e:
                st.error(f"Terjadi kesalahan jaringan: {e}")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    return (email)

# Fungsi pendaftaran
def signup():
    st.sidebar.title("Daftar")
    initialize_firebase()
    # Kolom masukan untuk email dan kata sandi
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Kata Sandi", type="password")

    # Tombol Daftar
    if st.sidebar.button("Daftar"):
        if not email or not password:
            st.error("Harap isi semua kolom")
        else:
            try:
                # Membuat pengguna dengan email dan kata sandi menggunakan SDK Admin Firebase
                user = auth.create_user(email=email, password=password)
                st.success("Pengguna berhasil dibuat!")
                
                # Otomatis masuk pengguna setelah mendaftar
                st.session_state['page'] = login
                st.rerun()
            except auth.EmailAlreadyExistsError:
                st.error("Email sudah digunakan. Gunakan email lain.")
            except Exception as e:
                st.error(f"Error saat membuat pengguna: {e}")
