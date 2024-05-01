from decimal import Decimal
from tabulate import tabulate


class Celengan:
    def __init__(self):
        self._daftarTransaksiMasuk = []
        self._daftarTransaksiKeluar = []

    def set_uangMasuk(self, uang: Decimal):
        if not isinstance(uang, Decimal):
            raise TypeError("Hanya menerima jumlah angka decimal")
        self._daftarTransaksiMasuk.append([uang])

    def set_uangKeluar(self, uang: Decimal):
        if not isinstance(uang, Decimal):
            raise TypeError("Hanya menerima jumlah angka decimal")
        self._daftarTransaksiKeluar.append([uang])

    def get_daftarTransaksiMasuk(self):
            if not self._daftarTransaksiMasuk:
                return "Tidak ada transaksi"
            headers = ["Transaksi Masuk"]
            return tabulate(self._daftarTransaksiMasuk, headers=headers, tablefmt="grid")
        
    def get_daftarTransaksiKeluar(self):
        if not self._daftarTransaksiKeluar:
            return "Tidak ada transaksi"
        headers = ["Transaksi Keluar"]
        return tabulate(self._daftarTransaksiKeluar, headers=headers, tablefmt="grid")

    def get_totalTransaksiMasuk(self):
        return sum(trans[0] for trans in self._daftarTransaksiMasuk) if self._daftarTransaksiMasuk else Decimal('0')

    def get_totalTransaksiKeluar(self):
        return sum(trans[0] for trans in self._daftarTransaksiKeluar) if self._daftarTransaksiKeluar else Decimal('0')
    
    def get_totalBalance(self):
        totalMasuk = self.get_totalTransaksiMasuk()
        totalKeluar = self.get_totalTransaksiKeluar()
        return totalMasuk - totalKeluar if (totalMasuk or totalKeluar) else Decimal('0')