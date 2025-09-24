import firebase_admin
from firebase_admin import credentials
import streamlit as st
from streamlit_option_menu import option_menu
from login_register import login, signup
# import homepage
# import chatbot
# import deteksi_penyakit
cred_obj = {
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
# Function to initialize Firebase
def initialize_firebase():
    if not firebase_admin._apps:
        cred_ = credentials.Certificate(cred_obj)
        firebase_admin.initialize_app(cred_)

# Main function
def main():
    initialize_firebase()

    # Check if user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # If not logged in, show login or signup page
    if not st.session_state['logged_in']:
        login_or_signup = st.selectbox(
            "Login/Sign Up",
            ("Login", "Sign Up")
        )

        if login_or_signup == "Login":
            login()
        else:
            signup()
    else:
        # Show content page with sidebar after login
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Deteksi Penyakit", "Chatbot"],
                icons=["house", "file-medical", "chat"],
                menu_icon="cast",
                default_index=0,
            )

        # Display the selected page
        if selected == "Home":
            # homepage.app()
            st.write("Home")
        elif selected == "Deteksi Penyakit":
            st.write("Deteksi penyakit")
        elif selected == "Chatbot":
            st.write("Chatbot")

if __name__ == "__main__":
    main()
