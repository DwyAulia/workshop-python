# More Control Flow Tools

## Pernyataan if
pernyataan yang paling terkenal adalah pernyataan if. Kata kunci 'elif' adalah singkatan dari 'else if', dan berguna untuk menghindari lekukan yang berlebihan. 
if elif ... elif ... urutan adalah pengganti switch atau pernyataan case yang ditemukan dalam bahasa lain.
## Pernyataan for 
Pernyataan for Python sedikit berbeda dari apa yang mungkin biasa Anda gunakan di C atau Pascal. 
Daripada selalu mengulangi perkembangan aritmatika angka (seperti dalam Pascal), atau memberikan pengguna kemampuan untuk menentukan kedua langkah iterasi dan menghentikan kondisi (sebagai C),
Python for pernyataan iterasi atas item dari urutan apapun (daftar atau string), dalam urutan bahwa mereka muncul dalam urutan.
## Fungsi range()
saat melakukan iterasi atas urutan angka, rentang fungsi bawaanrange() sangat berguna. 
Dalam banyak hal objek yang dikembalikan oleh range() berperilaku seolah-olah itu adalah daftar, tetapi sebenarnya tidak. 
Ini adalah objek yang mengembalikan item berturut-turut dari urutan yang diinginkan ketika Anda berulang di atasnya, tetapi tidak benar-benar membuat daftar, sehingga menghemat ruang.
## break dan continue Pernyataan, dan Klausul else tentang Loop
Pernyataan break, seperti di C, keluar dari penutup terdalam for atau while loop.
Pernyataan loop mungkin memiliki klausa else; itu dieksekusi ketika loop berakhir melalui kelelahan iterable (dengan for) atau ketika kondisi menjadi salah (dengan while),
tetapi tidak ketika loop diakhiri oleh pernyataan break. 
Ketika digunakan dengan loop, klausa else memiliki lebih banyak kesamaan dengan klausa else dari pernyataan try daripada dengan if: klausa else berjalan ketika tidak try ada pengecualian terjadi, 
dan klausa else loop berjalan ketika tidak ada break terjadi.
## Pernyataan pass
Pernyataan pass tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan.
## Pernyataan match
Pernyataan match mengambil ekspresi dan membandingkan nilainya dengan pola berturut-turut yang diberikan sebagai satu atau lebih blok kasus. 
Ini secara dangkal mirip dengan pernyataan switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai ke dalam variabel.
## Mendefinisikan Fungsi
Kata kunci def memperkenalkan definisi fungsi. Itu harus diikuti oleh nama fungsi dan daftar parameter formal yang dimutasikan.
Pernyataan pertama dari tubuh fungsi secara opsional dapat berupa string literal; string literal ini adalah string dokumentasi fungsi, atau docstring.(Lebih lanjut tentang docstrings dapat ditemukan di bagian String Dokumentasi.) Eksekusi fungsi memperkenalkan tabel simbol baru yang digunakan untuk variabel lokal fungsi.
Lebih tepatnya, semua tugas variabel dalam fungsi menyimpan nilai dalam tabel simbol lokal; sedangkan referensi variabel pertama kali terlihat di tabel simbol lokal, kemudian di tabel simbol lokal fungsi melampirkan, kemudian di tabel simbol global, dan akhirnya dalam tabel nama built-in.
Parameter aktual (argumen) untuk panggilan fungsi diperkenalkan dalam tabel simbol lokal dari fungsi yang disebut ketika dipanggil; dengan demikian, 
argumen dilewatkan menggunakan call by value (di mana nilai selalu merupakan referensi objek, bukan nilai objek). 
Ketika fungsi memanggil fungsi lain, atau menyebut dirinya rekursif, tabel simbol lokal baru dibuat untuk panggilan itu.
Definisi fungsi mengaitkan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Interpreter mengenali objek yang ditunjukkan oleh nama itu sebagai fungsi yang ditentukan pengguna.
## Lebih lanjut tentang Mendefinisikan Fungsi
untuk mendefinisikan fungsi dengan sejumlah argumen variabel. Ada tiga bentuk, yang dapat dikombinasikan :
### Nilai Argumen Default
Bentuk yang paling berguna adalah menentukan nilai default untuk satu atau beberapa argumen. Ini menciptakan fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang didefinisikan untuk memungkinkan.
### Argumen Kata Kunci
Fungsi juga dapat disebut menggunakan argumen kata kunci dari bentuk kwarg=value. Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisi. Semua argumen kata kunci yang dilewatkan harus cocok dengan salah satu argumen yang diterima oleh fungsi (misalnya actor bukanlah argumen yang valid untuk fungsi parrot), dan urutannya tidak penting. Ini juga mencakup argumen non-opsional (misalnya parrot(voltage=1000) juga berlaku).
### Parameter khusus
Secara default, argumen dapat diteruskan ke fungsi Python baik berdasarkan posisi atau secara eksplisit dengan kata kunci. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat diteruskan sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewatkan oleh posisi, berdasarkan posisi atau kata kunci, atau dengan kata kunci.
di mana / dan * adalah opsional. Jika digunakan, simbol-simbol ini menunjukkan jenis parameter dengan bagaimana argumen dapat diteruskan ke fungsi: hanya posisional, posisional-atau-kata kunci, dan kata kunci saja. Parameter kata kunci juga disebut sebagai parameter bernama.
#### Argumen Posisi atau Kata Kunci
Jika / dan * tidak hadir dalam definisi fungsi, argumen dapat diteruskan ke fungsi berdasarkan posisi atau dengan kata kunci.
#### Parameter Khusus Posisi
Parameter posisi hanya ditempatkan sebelum / (garis miring ke depan). / digunakan untuk secara logis memisahkan parameter posisi hanya dari parameter lainnya. Jika tidak ada / dalam definisi fungsi, tidak ada parameter posisi saja. Parameter setelah / mungkin posisional-atau-kata kunci atau kata kunci saja.
#### Argumen Khusus Kata Kunci
Untuk menandai parameter sebagai kata kunci saja, menunjukkan parameter harus dilewatkan dengan argumen kata kunci, tempatkan * dalam daftar argumen tepat sebelum parameter kata kunci pertama saja.
### Daftar Argumen Arbitrer
rgumen ini akan dibungkus dalam tuple (lihat Tuples and Sequences). Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi.
argumen variadic ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka meraup semua argumen input yang tersisa yang diteruskan ke fungsi.
### Membongkar Daftar Argumen
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tuple tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah.
#### Ekspresi Lambda
Fungsi anonim kecil dapat dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a+b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanya gula sintaksis untuk definisi fungsi normal. 
#### String Dokumentas
Berikut adalah beberapa konvensi tentang konten dan pemformatan string dokumentasi.
Baris pertama harus selalu menjadi ringkasan singkat dan ringkas dari tujuan objek. Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, secara visual memisahkan ringkasan dari sisa deskripsi. Baris berikut harus satu atau lebih paragraf yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.
arser Python tidak menghapus lekukan dari literal string multi-line di Python, sehingga alat yang memproses dokumentasi harus melucuti lekukan jika diinginkan. Hal ini dilakukan dengan menggunakan konvensi berikut. Baris non-kosong pertama setelah baris pertama string menentukan jumlah lekukan untuk seluruh string dokumentasi.
