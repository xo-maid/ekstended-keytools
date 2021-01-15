###  Import system untuk menggunakan fungsi system()
###  Import time sebenarnya optional
###    program akan lebih cepat tanpa time.sleep()
###    time.sleep() Xito gunakan untuk hiasan saja
from os import system
import time

###  Xito membuat beberapa fungsi di sini untuk
###    mempermudah proses update (jika ada)
###  Rencananya kedepannya, user bisa menentukan sendiri
###    tombol apa saja yang akan dia gunakan

###  Fungsi _head() di sini untuk membersihkan
###    log terminal agar terlihat rapi

def _head():
    system('clear')
    print('•'*5, 'Ekstended Keyboard Tools')
    print('•'*3, 'Author  : Xitoid')
    print('•'*3, 'GitHub  : https://github.com/Xo-maid')
    print('•'*10)

###  _cdir() adalah fungsi pendukung _mover()
###    _cdir() membuat direktori yang akan
###    menjadi target direktori fungsi _mover()

def _cdir():
    print('Menyiapkan direktori .termux . . .')
    system('mkdir $HOME/.termux')
    time.sleep(1)
    print('Direktori berhasil dibuat.')

def _mover():
    print('Mengganti file asli . . .')
    system('mv termux.properties $HOME/.termux/')
    time.sleep(1)
    print('File asal sukses diganti.')

###     ***MEMBAHAS _cdir() &  _mover()***

###  Bisa saja seseorang clone repo ini di sebuah
###    direktori yg tidak diketahui.

###    >> [ FYI ] file termux.properties harus
###       ada di dalam direktori $HOME/.termux/

###  Memakai '../' di open() ketika berada di folder
###    yang tidak tepat, akan menyebabkan Error
###    atau kode gagal.
###     (Tidak bisa menampilkan tombol tambahan yang
###       diinginkan)
###
###    >> [ NOTE ] Kalian tidak bisa menggunakan
###       $HOME di dalam fungsi open().
###       Alasannya, karena $HOME berada di luar
###       bahasa python (Hanya berfungsi di Shell/System)

###  Seperti yang sudah disinggung di atas,
###    _write() digunakan untuk membuat file.
###     (file: termux.properties)
###  Sebelum bisa menulis di filenya, kita perlu
###    membuka koneksi ke file dengan membuat
###    objek (_file) memakai fungsi open().
###  Setelah itu kita bisa memperlakukan var _file
###    selayaknya objek (seperti dalam bahasa java)
###    _file.write() untuk mengisi file dengan konten

def _write(_prop_):
    print('Menyiapkan termux.properties . . .')
    time.sleep(1)
    __file = open('termux.properties', 'w')
    print('File termux.properties siap diisi.')
    print('Memasukkan tombol ke list ekstended keyboard . . .')
    time.sleep(1)
    __file.write(_prop_)
    print('Pembuatan termux.properties selesai.')

###  prop_ adalah string yang Xito tulis menggunakan
###    triple quotes agar valuenya bisa ditulis
###    di line yang berbeda.
###  Ini adalah pengaturan termux yang sebenarnya.
###  Kamu bisa dapet info lebih lanjut mengenai
###    setting ini di situs wiki termux:
###     https://wiki.termux.com/wiki/Touch_Keyboard

prop_ = """extra-keys = [ \
['ESC','-','/','HOME','UP','END','PGUP','DEL'], \
['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP'] \
]
"""
###  Di bawah ini adalah alur bagaimana tools ini
###    bekerja membuat file untukmu

###  1. Membuat file termux.properties
###  2. Menyiapkan direktori tersembunyi .termux
###  3. Memindahkan termux.properties di direktori
###     saat ini ke direktori $HOME/.termux yang
###     dibuat di tahap 2.

###  Perlu kalian ketahui. Saat membuat objek file
###    di fungsi _write(), Xito menggunakan
###    option 'w' di fungsi open(). Sehingga ketika
###    program ini diulang, maka isi dari
###    file termux.properties yang lama akan ditimpa,
###    bukan ditambahi string baru.

###  Xito sangat berharap,
###    kalian yang sedang mendalami Termux akan
###    lebih antusias untuk mempelajari
###    bahasa pemrogrammannya, bukan mencari
###    tools2 cracking yang sebagian besar hanya
###    menampilkan string semata.

###  TERIMAKASIH sudah berkunjung ke repositori Xitoid
###  Semoga repo ini bermanfaat.

_head()
print('[NOTE] Program ini hanya akan bekerja pada termux dengan konfigurasi $HOME bawaan.') 
time.sleep(2)
_write(prop_)
time.sleep(2)
_head()
_cdir()
_mover()
time.sleep(2)
_head()

print('[ S U K S E S ]')
system('termux-reload-settings')
print('Jika keyboard belum berubah, kamu bisa reboot (matikan dan hidupkan kembali) Termux-mu.')
