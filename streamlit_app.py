import streamlit as st

st.title("Kalkulator Sederhana")

angka1 = st.number_input("Masukkan angka pertama")
angka2 = st.number_input("Masukkan angka kedua

operasi = st.selectbox("Pilih operasi",["Penjumlahan","Pengurangan","Perkalian","Pembagian"])
if st.button("Hitung"):
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            hasil = "Tidak bisa dibagi 0"
st.success(f"Hasil: {hasil}")
