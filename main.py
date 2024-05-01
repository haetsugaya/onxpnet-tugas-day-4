import colorama
import service.keuangan as bca

from colorama import Fore, Style

def tampilkan_menu(options):
    colorama.init(autoreset=True)
    print(Fore.CYAN + Style.BRIGHT + "Silahkan pilih salah satu menu:" + Style.RESET_ALL)
    for index, option in enumerate(options, 1):
        print(Fore.YELLOW + f"{index}. {option}")

def get_pilihanUser(options):
    while True:
        try:
            choice = int(input(Fore.GREEN + "Masukan pilihan (nomor 1-6): "))
            if 1 <= choice <= len(options):
                if choice == len(options):
                    print(Fore.GREEN + "Sedang mengakhiri aplikasi...")
                    exit()
                elif choice == 1:
                    bca.uang_masuk(float(input(Fore.GREEN + "Masukan nominal uang masuk: ")))
                elif choice == 2:
                    bca.uang_keluar(float(input(Fore.GREEN + "Masukan nominal uang keluar: ")))
                elif choice == 3:
                    print(Fore.WHITE + "Total Uang Masuk: " + str(bca.sum_total_uang_masuk()))
                    print(bca.total_uang_masuk())
                elif choice == 4:
                    print(Fore.WHITE + "Total Uang Keluar: " + str(bca.sum_total_uang_keluar()))
                    print(bca.total_uang_keluar())
                elif choice == 5:
                    if bca.total_balance() <= 0:
                        color = Fore.RED
                    else: 
                        color = Fore.GREEN
                    print( color + "Total balance: " + str(bca.total_balance()))
            else:
                print(Fore.RED + "Pilihan tidak ada!")
        except ValueError:
            print(Fore.RED + "Pilihan salah, tolong masukan angka!")

def main():
    menu = [
        'Tambah Uang Masuk', 
        'Tambah Uang Keluar', 
        'Lihat Uang Masuk', 
        'Lihat Uang Keluar', 
        'Total Balance',
        'Keluar']
    tampilkan_menu(menu)
    get_pilihanUser(menu)


# Tampilkan menu hanya jika main.py di execute secara langsung
if __name__ == "__main__":
    main()