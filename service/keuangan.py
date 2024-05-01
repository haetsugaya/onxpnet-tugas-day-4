import model.celengan as cl
from decimal import Decimal, InvalidOperation

tabungan = cl.Celengan()

def convert_uang(uang):
    try:
        decimal_uang = Decimal(uang)
    except InvalidOperation:
        raise ValueError("Hanya menerima jumlah angka dalam format yang valid")
    return decimal_uang

def uang_masuk(uang):
    tabungan.set_uangMasuk(convert_uang(uang))

def uang_keluar(uang):
    tabungan.set_uangKeluar(convert_uang(uang))

def total_uang_masuk():
    return tabungan.get_daftarTransaksiMasuk()

def total_uang_keluar():
    return tabungan.get_daftarTransaksiKeluar()

def sum_total_uang_masuk():
    return tabungan.get_totalTransaksiMasuk()

def sum_total_uang_keluar():
    return tabungan.get_totalTransaksiKeluar()

def total_balance():
    return tabungan.get_totalBalance()