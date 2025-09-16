# Tugas 2

### Tautan menuju aplikasi PWS yang sudah di-deploy : https://elliot-randy-chukgoods.pbp.cs.ui.ac.id/

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Jawab:
Pertama, saya membuat direktori baru khusus untuk tugas individu dan juga membuat sebuah virtual environment untuk mengisolasi dependency proyek. Kemudian, saya menginstal Django dan membuat proyek baru serta mengonfigurasi environment variables sesuai instruksi. Sebelum lanjut ke tahap pengembangan berikutnya, saya menjalankan migrasi database terlebih dahulu dan menjalankan server Django untuk melihat animasi roket sebagai tanda bahwa aplikasi Django saya berhasil dibuat. Lalu, saya membuat repository github baru, menjalankan perintah git init, menambahkan berkas .gitignore, menghubungkan repositori lokal dengan repositori github yang telah dibuat khusus untuk tugas individu, membuat branch utama bernama master, dan melakukan add, commit, dan push dari direktori repositori lokal. Kemudian, dilanjuti dengan proses pembuatan akun dan deployment melalui PWS (Pacil Web Service)

Setelah proyek Django berhasil dibuat, saya membuat aplikasi utama bernama main sesuai instruksi. Lalu, saya mendaftarkan aplikasi main ke dalam proyek dengan menambahkannya di INSTALLED_APPS pada file chukgoods/settings.py. Selanjutnya, saya mendefinisikan struktur data untuk shop di main/models.py dimana model ini memiliki enam atribut wajib. Setelah mendefinisikan model, saya menjalankan proses migrasi untuk membuat tabel yang sesuai di database. Kemudian, saya membuat sebuah fungsi view di main/views.py yang bertugas untuk mengambil semua data produk dari database dan menyiapkannya dalam sebuah context untuk dikirim ke template. Selanjutnya, saya membuat direktori templates di dalam aplikasi main dan membuat file main.html yang berfungsi untuk menampilkan data yang dikirim dari view dalam format HTML. Selanjutnya, saya mengonfigurasi URL agar permintaan dari user bisa diarahkan ke view yang tepat. Saya membuat file main/urls.py terlebih dahulu untuk mengatur rute di level aplikasi. Kemudian, saya menyambungkan main/urls.py ke football_shop/urls.py (level proyek). Terakhir, saya melakukan proses git add commit push proyek ke repositori github serta melakukan deployment ke Pacil Web Service (PWS).

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

### Jawab:
Link gambar bagan -> https://drive.google.com/file/d/1cO06XyhFfcZe6UbFz501mwyssFB4HOMj/view?usp=sharing

Saat seorang pengguna mengakses aplikasi web Django, proses dimulai ketika browser mengirimkan sebuah HTTP Request ke server. Django pertama kali menerima permintaan ini melalui file urls.py. File ini akan mencocokkan URL yang diminta dengan pola-pola yang telah didefinisikan untuk menemukan fungsi View yang tepat untuk menangani permintaan tersebut. Setelah ditemukan, fungsi di dalam views.py akan dieksekusi. Di sinilah seluruh logika aplikasi berjalan. Jika View memerlukan data, View akan berkomunikasi dengan models.py, yang berfungsi sebagai jembatan ke database melalui Django ORM. Setelah mendapatkan data yang diperlukan, View akan memanggil file template.html dan menyisipkan data tersebut ke dalamnya. Template engine Django kemudian merender file ini menjadi sebuah halaman HTML utuh, yang akhirnya dikemas oleh View ke dalam sebuah HTTP Response dan dikirim kembali ke browser untuk ditampilkan.


## 3. Jelaskan peran settings.py dalam proyek Django!

### Jawab:
File settings.py adalah pusat kendali dari sebuah proyek Django. File ini berfungsi sebagai file konfigurasi utama yang mendefinisikan hampir semua aspek perilaku proyek. Di dalamnya, kita mendaftarkan semua aplikasi yang akan digunakan melalui INSTALLED_APPS, sehingga Django mengenali model, view, dan URL dari setiap aplikasi. Selain itu, settings.py berisi konfigurasi koneksi ke database (DATABASES), menentukan jenis dan detail aksesnya. File ini juga mengatur lapisan MIDDLEWARE yang memproses setiap request dan response, menambahkan fungsionalitas seperti keamanan sesi dan autentikasi. Pengaturan untuk aset statis (CSS, JavaScript) melalui STATIC_URL, konfigurasi template engine, dan SECRET_KEY untuk keamanan kriptografi juga semuanya diatur di sini. Jadi, settings.py menyatukan semua bagian terpisah dari proyek Django dan memastikan semuanya bekerja secara harmonis sesuai dengan aturan yang telah kita tetapkan.


## 4. Bagaimana cara kerja migrasi database di Django?

### Jawab:
Migrasi pada Django adalah sebuah sistem untuk mengelola dan menyinkronkan perubahan pada skema database secara terstruktur, sejalan dengan perubahan yang dibuat pada file models.py. Proses ini bekerja dalam dua langkah utama yang saling melengkapi. Langkah pertama adalah menjalankan perintah makemigrations, yang akan membandingkan kondisi model saat ini dengan catatan migrasi terakhir. Jika terdeteksi adanya perubahan (seperti penambahan kolom atau pembuatan tabel baru), Django akan secara otomatis menghasilkan sebuah file migrasi baru. File ini pada dasarnya adalah yang mendeskripsikan perubahan yang perlu dilakukan pada database, namun belum mengeksekusinya. Langkah kedua adalah menjalankan perintah migrate, yang membaca file-file migrasi yang belum diterapkan tersebut, menerjemahkannya menjadi perintah SQL, dan mengeksekusinya pada database. Dengan cara ini, struktur database akan diperbarui agar sesuai dengan definisi model terbaru di kode kita.


## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### Jawab:
Django dijadikan framework yang ideal untuk pemula karena mengikuti istilah "batteries-included". Artinya, Django sudah menyediakan berbagai komponen penting seperti panel admin, sistem autentikasi, dan ORM (Object-Relational Mapper) secara bawaan. Hal ini memungkinkan pengembang pemula untuk langsung fokus pada logika aplikasi tanpa perlu menghabiskan waktu merakit komponen dasar dari nol. Struktur Model-View-Template (MVT) yang jelas juga mengajarkan prinsip desain perangkat lunak yang baik, yaitu pemisahan antara data, logika, dan tampilan. Adanya ORM sangat mempermudah interaksi dengan database tanpa harus menulis SQL secara manual, sementara fitur keamanan bawaan melindungi aplikasi dari ancaman umum sejak awal. Selain itu, Django didukung oleh dokumentasi yang sangat lengkap dan komunitas yang besar, sehingga pemula dapat dengan mudah menemukan jawaban atas permasalahan yang dihadapi dan membangun aplikasi yang kokoh serta dapat diskalakan untuk kebutuhan di masa depan.


## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

### Jawab: 
Tidak ada, asisten dosen telah melaksanakan tugasnya dengan baik pada tutorial 1 kemarin.

#### Referensi :
https://docs.djangoproject.com/en/5.2/intro/overview/#the-request-response-cycle
https://docs.djangoproject.com/en/5.2/topics/settings/
https://docs.djangoproject.com/en/5.2/topics/migrations/
https://www.djangoproject.com/start/overview/

# Tugas 3

### Link screenshot dari hasil akses URL pada Postman : https://drive.google.com/drive/folders/1P61PGA9AhCROQnlpG4KaddaGVWRlz2nE?usp=sharing

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

### Jawab: 
Karena data delivery memungkinkan kita untuk memisahkan backend dari frontend. Dengan data delivery, backend yang sama bisa mengirimkan data ke berbagai platform, misalnya ke situs web dan aplikasi mobile sekaligus, tanpa perlu membuat ulang semua logika dari awal sehingga membuat development jadi lebih efisien karena tim backend bisa fokus mengurus data dan logika, sementara tim frontend bisa fokus mengurus tampilan. Jadi, data delivery lewat format seperti API (JSON/XML) membuat platform lebih fleksibel, skalabel, dan lebih mudah dikelola ke depannya.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

### Jawab: 
Menurut saya, JSON lebih baik karena sintaksis JSON itu sendiri pada dasarnya adalah objek JavaScript sehingga jadi keuntungan besar karena frontend web sangat bergantung pada JavaScript, jadi data dari server bisa langsung diolah tanpa perlu proses parsing yang rumit. Selain itu, JSON juga lebih ringkas karena tidak seperti XML yang butuh tag pembuka dan penutup, sehingga ukuran datanya lebih kecil dan proses transfernya lebih cepat. Karena lebih ringan, cepat, dan gampang diintegrasikan dengan JavaScript, JSON jadi standar industri dan jauh lebih populer untuk API saat ini.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

### Jawab: 
Method is_valid() pada form Django fungsinya sebagai penjaga untuk database kita. Sebelum data dari pengguna diizinkan masuk dan disimpan, method ini akan melakukan pemeriksaan menyeluruh. is_valid() akan memastikan semua data yang diinput sudah sesuai aturan yang kita tentukan, misalnya, apakah kolom yang wajib diisi sudah diisi, apakah tipe datanya benar (angka untuk harga, teks untuk deskripsi), dan apakah panjang karakternya tidak melebihi batas. Method ini dibutuhkan karena menjadi penjaga integritas data dan mencegah data yang salah atau tidak lengkap merusak sistem kita. Tanpa is_valid(), kita harus melakukan semua validasi itu secara manual sehingga jadi repot dan rawan terjadi kesalahan.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### Jawab :
Kita butuh csrf_token di setiap form Django untuk menjadi security layer untuk mencegah serangan Cross-Site Request Forgery (CSRF) karena csrf_token ini hanya dimiliki oleh pengguna yang sah di sesi itu. Jika kita tidak menggunakan csrf_token, aplikasi kita jadi rentan diserang. Penyerang bisa membuat situs palsu yang berisi form tersembunyi. Ketika pengguna yang sedang login di situs kita mengunjungi situs palsu itu, form tersebut bisa secara otomatis mengirim permintaan berbahaya atas nama pengguna, misalnya permintaan untuk menghapus akun atau mentransfer uang. Karena permintaan itu dikirim dari browser pengguna yang sah, server kita akan menganggapnya valid. csrf_token mencegah hal tersebut terjadi karena situs penyerang tidak akan tahu apa isi token tersebut, sehingga ketika permintaan palsu itu masuk tanpa token yang benar, Django akan langsung menolaknya.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Jawab :
Pertama-tama, saya membuat direktori template di direktori utama, kemudian membuat file base.html di dalam foldernya yang berfungsi sebagai kerangka dasar untuk semua halaman lain, isinya hanya struktur HTML kosong dengan {% block content %}. Lalu, saya mendaftarkan direktori templates ini di settings.py sehingga semua template lain seperti main.html atau create_product.html tinggal memakai {% extends 'base.html' %} di baris paling atas, jadi saya tidak perlu menulis ulang kode HTML yang sama berkali-kali.

Selanjutnya, saya membuat forms.py untuk mendefinisikan form input produk berdasarkan model Product. Kemudian di views.py, saya membuat tiga fungsi utama, yaitu show_main untuk menampilkan semua produk, create_product untuk menangani proses penambahan produk baru lewat form, dan show_product untuk menampilkan detail satu produk berdasarkan ID-nya. Ketiga fungsi ini saya daftarkan di urls.py agar bisa diakses. Untuk tampilannya, saya membuat tiga file HTML, yaitu main.html untuk daftar produk, create_product.html untuk menampilkan form, dan product_detail.html untuk halaman detail.

Terakhir, saya membuat empat fungsi lagi di views.py, yaitu show_xml dan show_json untuk mengembalikan semua data produk dalam format XML dan JSON, serta show_xml_by_id dan show_json_by_id untuk melakukan hal yang sama tapi hanya untuk satu produk spesifik. Setiap fungsi baru ini juga saya daftarkan path-nya di urls.py agar bisa diakses sebagai endpoint API.

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

### Jawab : 
Tidak ada, asisten dosen telah melaksanakan tugasnya dengan baik pada tutorial 2 kemarin.

#### Referensi :
https://www.freecodecamp.org/product/what-is-an-api-in-english-please-b880a3214a82/
https://aws.amazon.com/compare/the-difference-between-json-xml/
https://docs.djangoproject.com/en/5.2/ref/forms/validation/
https://docs.djangoproject.com/en/5.2/ref/csrf/