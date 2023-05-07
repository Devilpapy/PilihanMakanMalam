import random

def pilih_menu_makanan():
    menu_makanan = [
        "Nasi Goreng",
        "Sate Ayam",
        "Gado-gado",
        "Rendang",
        "Soto Ayam",
        "Ayam Bakar",
        "Nasi Padang",
        "Sop Buntut",
        "Nasi Uduk",
        "Bakso",
        "Mie Goreng",
        "Ayam Betutu",
        "Pempek",
        "Rawon",
        "Sambal Udang",
        "Soto Betawi",
        "Ayam Geprek",
        "Nasi Kuning",
        "Bakmi Jawa",
        "Lontong Sayur",
        "Pepes Ikan",
        "Martabak",
        "Bebek Goreng",
        "Ketoprak"
    ]

    makanan_hari_ini = random.choice(menu_makanan)
    return makanan_hari_ini

menu_hari_ini = pilih_menu_makanan()
print("Menu makan malam hari ini adalah:", menu_hari_ini)
