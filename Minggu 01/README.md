RINGKASAN

BAB 1 Whetting Your Appetite


Python adalah bahasa yang ditafsirkan, yang dapat menghemat banyak waktu selama pengembangan program karena tidak ada kompilasi dan penautan yang diperlukan. Interpreter dapat digunakan secara interaktif, yang membuatnya mudah untuk bereksperimen dengan fitur bahasa, untuk menulis program membuang-buang, atau untuk menguji fungsi selama pengembangan program bottom-up. Ini juga merupakan kalkulator meja yang berguna.
Python memungkinkan program ditulis secara ringkas dan mudah dibaca. Program yang ditulis dalam Python biasanya jauh lebih pendek daripada program C, C ++, atau Java yang setara, karena beberapa alasan:

•	tipe data tingkat tinggi memungkinkan Anda untuk mengekspresikan operasi yang kompleks dalam satu pernyataan;
•	pengelompokan pernyataan dilakukan dengan lekukan alih-alih memulai dan mengakhiri tanda kurung;
•	tidak ada deklarasi variabel atau argumen yang diperlukan.

Python dapat diperluas: jika Anda tahu cara memprogram di C, mudah untuk menambahkan fungsi atau modul bawaan baru ke penerjemah, baik untuk melakukan operasi penting dengan kecepatan maksimum, atau untuk menautkan program Python ke pustaka yang mungkin hanya tersedia dalam bentuk biner (seperti perpustakaan grafis khusus vendor). Setelah Anda benar-benar terpikat, Anda dapat menghubungkan interpreter Python ke dalam aplikasi yang ditulis dalam C dan menggunakannya sebagai bahasa ekstensi atau perintah untuk aplikasi itu.
bahasa ini dinamai menurut acara BBC "Monty Python's Flying Circus" dan tidak ada hubungannya dengan reptil. Membuat referensi ke sandiwara Monty Python dalam dokumentasi tidak hanya diperbolehkan, tetapi juga didorong.


BAB 2 Menggunakan Python Interpreter

2.1. Memanggil Penerjemah
Interpreter Python biasanya diinstal sebagai /usr/local/bin/python3.10 pada mesin-mesin yang tersedia; menempatkan /usr/local/bin di jalur pencarian shell Unix Anda memungkinkan untuk memulainya dengan mengetikkan perintah "python3.10" (tanpa tanda petik) ke shell.  Karena pilihan direktori tempat penerjemah tinggal adalah opsi instalasi, tempat lain dimungkinkan; periksa dengan guru Python lokal atau administrator sistem Anda. (Misalnya, /usr/local/python adalah lokasi alternatif yang populer.)

Pada mesin Windows tempat Anda menginstal Python dari Microsoft Store, perintah python3.10 akan tersedia. Jika Anda memiliki peluncur py.exe diinstal, Anda dapat menggunakan perintah py. Lihat Excursus: Mengatur variabel lingkungan untuk cara lain meluncurkan Python. Mengetik karakter end-of-file (Control-D di Unix, Control-Z pada Windows) pada prompt utama menyebabkan interpreter keluar dengan status keluar nol. Jika itu tidak berhasil, Anda dapat keluar dari penerjemah dengan mengetikkan perintah berikut: quit().

Fitur pengeditan baris penerjemah termasuk pengeditan interaktif, substitusi riwayat, dan penyelesaian kode pada sistem yang mendukung pustaka GNU Readline. Mungkin pemeriksaan tercepat untuk melihat apakah pengeditan baris perintah didukung adalah mengetik Control-P ke prompt Python pertama yang Anda dapatkan. Jika berbunyi bip, Anda memiliki pengeditan baris perintah; lihat Lampiran Pengeditan Input Interaktif dan Substitusi Sejarah untuk pengenalan tombol. Jika tidak ada yang muncul, atau jika ^P digaungkan, pengeditan baris perintah tidak tersedia; Anda hanya dapat menggunakan backspace untuk menghapus karakter dari baris saat ini.
Interpreter beroperasi agak seperti shell Unix: ketika dipanggil dengan input standar yang terhubung ke perangkat tty, ia membaca dan menjalankan perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi skrip dari file tersebut.
Cara kedua untuk memulai interpreter adalah python -c command [arg] ..., yang mengeksekusi statement (s) dalam perintah, analog dengan opsi -c shell. Karena pernyataan Python sering berisi spasi atau karakter lain yang khusus untuk shell, biasanya disarankan untuk mengutip perintah secara keseluruhan dengan satu kutipan.
Beberapa modul Python juga berguna sebagai skrip. Ini dapat dipanggil menggunakan python -m module [arg] ..., yang mengeksekusi file sumber untuk modul seolah-olah Anda telah mengeja nama lengkapnya pada baris perintah.
Ketika file skrip digunakan, terkadang berguna untuk dapat menjalankan skrip dan memasuki mode interaktif sesudahnya. Ini dapat dilakukan dengan melewati -i sebelum skrip.

2.1.1. Argument Passing

Ketika diketahui oleh penerjemah, nama skrip dan argumen tambahan setelahnya diubah menjadi daftar string dan ditugaskan ke variabel argv dalam modul sys. Anda dapat mengakses daftar ini dengan mengeksekusi import sys. Panjang daftar setidaknya satu; ketika tidak ada skrip dan tidak ada argumen yang diberikan, sys.argv[0] adalah string kosong. Ketika nama skrip diberikan sebagai '-' (yang berarti input standar), sys.argv[0] diatur ke '-'. Ketika perintah -c digunakan, sys.argv[0] diatur ke '-c'. Ketika modul -m digunakan, sys.argv[0] ke nama lengkap modul yang terletak. Opsi yang ditemukan setelah perintah -c atau modul -m tidak dikonsumsi oleh pemrosesan opsi interpreter Python tetapi dibiarkan di sys.argv untuk ditangani oleh perintah atau modul.

2.1.2. interactive mode
Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif. Dalam mode ini meminta perintah berikutnya dengan prompt utama, biasanya tiga tanda yang lebih besar dari (>>>); untuk garis kelanjutan yang dimintanya dengan prompt sekunder, secara default tiga titik (...). Penerjemah mencetak pesan selamat datang yang menyatakan nomor versi dan pemberitahuan hak cipta sebelum mencetak prompt pertama
2.2. The Interpreter and Its Environment

2.2.1. Source code encoding
Secara default, file sumber Python diperlakukan sebagai dikodekan dalam UTF-8. Dalam pengkodean itu, karakter dari sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam literal string, pengidentifikasi dan komentar - meskipun pustaka standar hanya menggunakan karakter ASCII untuk pengidentifikasi, sebuah konvensi yang harus diikuti oleh kode portabel apa pun. Untuk menampilkan semua karakter ini dengan benar, editor Anda harus mengenali bahwa file tersebut adalah UTF-8, dan harus menggunakan font yang mendukung semua karakter dalam file.

Untuk mendeklarasikan pengkodean selain yang default, baris komentar khusus harus ditambahkan sebagai baris pertama file. Sintaksnya adalah sebagai berikut:
# -*- coding: encoding -*-
di mana pengkodean adalah salah satu codecs valid yang didukung oleh Python.
Misalnya, untuk menyatakan bahwa pengkodean Windows-1252 akan digunakan, baris pertama file kode sumber Anda harus:
# -*- coding: cp1252 -*-
Satu pengecualian untuk aturan baris pertama adalah ketika kode sumber dimulai dengan garis "shebang" UNIX. Dalam hal ini, deklarasi pengkodean harus ditambahkan sebagai baris kedua file.


BAB 3 An Informal Introduction to Python.

input dan output dibedakan oleh ada atau tidak adanya prompt (>>> dan ...): untuk mengulangi contoh, Anda harus mengetik semuanya setelah prompt, ketika prompt muncul; baris yang tidak dimulai dengan prompt adalah output dari interpreter. Perhatikan bahwa prompt sekunder pada baris dengan sendirinya dalam contoh berarti Anda harus mengetik baris kosong; ini digunakan untuk mengakhiri perintah multi-baris.
Komentar di Python dimulai dengan karakter hash, #, dan meluas ke akhir baris fisik. Komentar dapat muncul di awal baris atau mengikuti spasi atau kode, tetapi tidak dalam string literal. Karakter hash dalam string literal hanyalah karakter hash. Karena komentar adalah untuk mengklarifikasi kode dan tidak ditafsirkan oleh Python, mereka dapat dihilangkan saat mengetik

3.1. Menggunakan Python sebagai Kalkulator

3.1.1 Angka
Interpreter bertindak sebagai kalkulator sederhana, dengan mengetik ekspresi di dalamnya dan itu akan menulis nilainya. Sintaks ekspresi sangat mudah: operator +, -, * dan / bekerja seperti di kebanyakan bahasa lain (misalnya, Pascal atau C); tanda kurung (()) dapat digunakan untuk pengelompokan. 

3.1.2. String 
Selain angka, Python juga dapat memanipulasi string, yang dapat diekspresikan dalam beberapa cara. Mereka dapat dilampirkan dalam tanda kutip tunggal ('...') atau kutipan ganda ("...") dengan hasil yang sama 2. \ dapat digunakan untuk menghindari kutipan. 
Dalam interpreter interaktif, string output tertutup dalam tanda kutip dan karakter khusus lolos dengan backslashes. Meskipun ini kadang-kadang mungkin terlihat berbeda dari input (kutipan melampirkan bisa berubah), dua string yang setara. String diapit dalam tanda kutip ganda jika string berisi satu kutipan dan tidak ada kutipan ganda, jika tidak, itu tertutup dalam tanda kutip tunggal. Fungsi print() menghasilkan output yang lebih mudah dibaca, dengan menghilangkan kutipan penutup dan dengan mencetak karakter yang lolos dan khusus.

3.1.3 Daftar
Python tahu sejumlah tipe data majemuk, yang digunakan untuk mengelompokkan nilai lainnya. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Daftar mungkin berisi item dari berbagai jenis, tetapi biasanya semua item memiliki jenis yang sama.

3.2 Firs Steps Towards Programming
Python dapat juga digunakan untuk tugas yang lebih rumit daripada menambahkan dua dan dua Bersama – sama, misalnya dapat menulis sub-urutan awal dari seri Fibonaci. sebagai berikut:

>>>
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8

Contoh ini memperkenalkan beberapa fitur baru.
•	Baris pertama berisi beberapa tugas: variabel a dan b secara bersamaan mendapatkan nilai baru 0 dan 1. Pada baris terakhir ini digunakan lagi, menunjukkan bahwa ekspresi di sisi kanan semua dievaluasi terlebih dahulu sebelum salah satu tugas terjadi. Ekspresi sisi kanan dievaluasi dari kiri ke kanan.
•	Loop while dijalankan selama kondisi (di sini: a < 10) tetap benar. Di Python, seperti di C, nilai integer non-nol adalah benar; Nol adalah palsu. Kondisi ini mungkin juga merupakan nilai string atau daftar, sebenarnya urutan apa pun; apa pun dengan panjang non-nol adalah benar, urutan kosong salah. Tes yang digunakan dalam contoh adalah perbandingan sederhana. Operator perbandingan standar ditulis sama seperti dalam C: < (kurang dari), > (lebih besar dari), == (sama dengan), <= (kurang dari atau sama dengan), >= (lebih besar dari atau sama dengan) dan != (tidak sama dengan).
•	Tubuh loop menjorok: lekukan adalah cara Python mengelompokkan pernyataan. Pada prompt interaktif, Anda harus mengetik tab atau spasi untuk setiap baris indentasi. Dalam praktiknya Anda akan menyiapkan input yang lebih rumit untuk Python dengan editor teks; semua editor teks yang layak memiliki fasilitas auto-indentasi. Ketika pernyataan majemuk dimasukkan secara interaktif, itu harus diikuti oleh garis kosong untuk menunjukkan penyelesaian (karena parser tidak dapat menebak ketika Anda telah 







