import streamlit as st

st.title("Vücut Kitle Endeksi (BMI) Uygulaması")
st.write("Lütfen aşağıdaki bilgileri doldurarak vücut kitle endeksinizi hesaplayın.")

boy = st.number_input("Boyunuzu giriniz (cm):", min_value=50.0, max_value=250.0, step=0.1)
kilo = st.number_input("Kilonuzu giriniz (kg):", min_value=10.0, max_value=300.0, step=0.1)


if st.button("Hesapla"):
    if boy > 0 and kilo > 0:
        endeks = round((kilo) / (boy / 100) ** 2, 2)

        boy_int = int(boy)
        kilo_int = int(kilo)


        if endeks < 18.5:
            st.write(f"Boyunuz: {boy_int} cm, Kilonuz: {kilo_int} kg")
            st.write(f"Vücut Kitle Endeksiniz: {endeks} ve zayıfsınız.")
            st.image("zayıf.png", width=200)
        elif endeks < 25:
            st.write(f"Boyunuz: {boy_int} cm, Kilonuz: {kilo_int} kg")
            st.write(f"Vücut Kitle Endeksiniz: {endeks} ve normalsiniz.")
            st.image("normal.png" , width=150)
        elif endeks < 30:
            st.write(f"Boyunuz: {boy_int} cm, Kilonuz: {kilo_int} kg")
            st.write(f"Vücut Kitle Endeksiniz: {endeks} ve kilolusunuz.")
            st.image("kilolu.png" , width=150)
        else:
            st.write(f"Boyunuz: {boy_int} cm, Kilonuz: {kilo_int} kg")
            st.write(f"Vücut Kitle Endeksiniz: {endeks} ve obezsiniz.")
            st.image("obez.png" , width=150)
    else:
        st.write("Lütfen geçerli bir boy ve kilo giriniz.")
