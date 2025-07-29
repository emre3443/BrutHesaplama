import streamlit as  st

brut=st.number_input("Yıllık Brüt Giriniz")

v158=158000*0.15
v330=(330000-158000)*0.20
v800=(800000-330000)*0.27
v4300=(4300000-800000)*0.35

if brut<158000:
    vergi=brut*0.15

elif brut<330000:
    vergi=v158+((brut-158000)*0.20)

elif brut<800000:
    vergi=v158+v330+((brut-330000)*0.27)

elif brut<4300000:
    vergi=v158+v330+v800+((brut-800000)*0.35)

else:
    vergi=v158+v330+v800+v4300+((brut-4300000)*0.40)
    st.ballons()

st.write("Toplam Vergi:",vergi,"Net Gelir",brut-vergi,"Aylık Net",(brut-vergi)/12)

