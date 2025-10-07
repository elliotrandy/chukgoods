<details>
  <summary>Tugas 2</summary>
  
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
</details>

<details>
  <summary>Tugas 3</summary>
  
  ### Link screenshot dari hasil akses URL pada Postman : https://drive.google.com/drive/folders/1P61PGA9AhCROQnlpG4KaddaGVWRlz2nE?usp=sharing
  
  ## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
  
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
</details>

<details>
  <summary>Tugas 4</summary>
  
  ## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya!
  
  ### Jawab: 
  AuthenticationForm adalah form bawaan Django untuk proses login yang sudah menangani validasi username/password serta binding ke backend autentikasi. Kelebihannya adalah cepat dipakai tanpa bikin form dari nol, validasinya aman (hashing password via auth backend), integrasi mulus dengan login() dan middleware session, serta otomatis memberi pesan error yang tepat ketika kredensial salah. Sedangkan kekurangannya adalah tampilan dan field bersifat generik sehingga perlu kostumisasi jika mau UI/UX khusus (misalnya login pakai email, captcha, atau two-factor), dan logika tambahannya (rate-limit, device check, dsb.) tetap harus dibuat sendiri.
  
  ## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
  
  ### Jawab: 
  Autentikasi adalah proses memverifikasi siapa pengguna (login), sedangkan otorisasi adalah menentukan apa yang boleh dilakukan pengguna yang sudah terverifikasi (izin/permission). Di Django, autentikasi ditangani oleh Authentication Framework (authenticate(), login(), logout(), model User, password hashing, backends). Sedangkan otorisasi dikelola lewat permissions dan groups pada model User, decorator/CBV mixin seperti @login_required, permission_required, UserPassesTestMixin, serta pengecekan request.user.is_authenticated, is_staff, is_superuser, atau user.has_perm('app_label.codename'). Singkatnya: login memastikan identitas, permission memastikan akses.
  
  ## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
  
  ### Jawab: 
  Session menyimpan data di server (ID-nya saja di browser melalui cookie sessionid). Kelebihannya adalah lebih aman karena data tidak diekspos ke client, mudah dipakai (request.session[...]), dan fleksibel untuk state yang sensitif. Sedangkan kekurangannya adalah butuh storage di server (database/cache/file), serta harus dikelola masa aktifnya. 
  
  Cookies menyimpan data langsung di browser. Kelebihannya adalah ringan, tidak memerlukan storage server, cocok untuk preferensi sederhana (mis. tema, last visit). Sedangkan kekurangannya adalah ukuran kecil, mudah dimodifikasi/terbaca user, rentan jika berisi data sensitif, dan wajib dikonfigurasi atribut keamanan dengan benar.
  
  ## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
  
  ### Jawab: 
  Cookies tidak otomatis aman secara default karena bisa disadap atau dimanipulasi jika tidak dikunci. Risiko umumnya adalah seperti pencurian cookie (session hijacking), XSS yang membaca cookie, dan CSRF. Django memitigasi hal tersebut lewat pengaturan seperti SESSION_COOKIE_SECURE dan CSRF_COOKIE_SECURE (hanya dikirim via HTTPS), SESSION_COOKIE_HTTPONLY dan CSRF_COOKIE_HTTPONLY (mencegah akses JS), CSRF_COOKIE_SAMESITE/SESSION_COOKIE_SAMESITE (batasi pengiriman lintas situs), token CSRF pada form, dan framework auth/session yang tidak menyimpan data sensitif di cookie—hanya ID session. Praktiknya dengan mengaktifkan HTTPS dan set opsi keamanan cookie tersebut di settings.py.
  
  ## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  
  ### Jawab: 
  Saya memulai dengan menambahkan mekanisme autentikasi dasar, yaitu halaman registrasi berbasis UserCreationForm, login dengan AuthenticationForm, serta logout, lengkap dengan routing dan template masing-masing. Setelah itu, saya merestriksi akses halaman utama menggunakan login_required agar hanya pengguna terautentikasi yang bisa mengaksesnya. Berikutnya, saya menghubungkan model Product ke User melalui relasi ForeignKey sehingga setiap produk memiliki pemilik yang jelas, alur penambahan produk otomatis menempelkan pengguna yang sedang login, dan halaman utama saya lengkapi filter “All” vs “My” untuk menampilkan seluruh produk atau hanya milik pengguna. Untuk penyimpanan state ringan, saya menerapkan cookie last_login yang diset saat login dan dihapus saat logout, serta menampilkan nilainya di halaman utama bersama informasi username. Terakhir, saya membuat dua akun pengguna di lingkungan lokal dan mengisi masing-masing tiga data produk dummy, lalu menguji login dengan kedua akun untuk memastikan pemisahan data berjalan (produk milik akun A tidak muncul ketika login sebagai akun B), sekaligus memverifikasi alur autentikasi, session, dan cookies sudah berfungsi sesuai kebutuhan.
</details>

<details>
  <summary>Tugas 5</summary>
  
  ## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  
  ### Jawab: 
  Jika sebuah elemen HTML ditargetkan oleh beberapa selector CSS, browser akan menerapkan style berdasarkan urutan prioritas yang disebut spesifisitas. Aturan dengan spesifisitas tertinggi akan selalu menang. Urutan prioritas dari yang paling tinggi ke paling rendah adalah: inline style (atribut style di dalam tag HTML), ID selector (misalnya, #header), class, attribute, dan pseudo-class selectors (misalnya, .card, [type="submit"], :hover), dan yang terakhir adalah element dan pseudo-element selectors (misalnya, div, p). Jika spesifisitasnya sama, maka aturan yang ditulis paling akhir di dalam file CSS yang akan diterapkan. Aturan !important dapat digunakan untuk mengesampingkan semua prioritas lainnya, namun sebaiknya dihindari agar kode tetap mudah dikelola.
  
  ## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
  
  ### Jawab: 
  Responsive design adalah konsep krusial dalam pengembangan web modern karena memastikan sebuah situs web dapat tampil dan berfungsi secara optimal di berbagai ukuran layar, mulai dari desktop hingga smartphone. Di era di mana mayoritas pengguna mengakses internet melalui perangkat mobile, situs yang tidak responsif akan memberikan pengalaman buruk, seperti teks yang sulit dibaca atau tombol yang sulit ditekan, yang membuat pengguna frustrasi dan cenderung meninggalkan situs tersebut. Contoh aplikasi yang sudah menerapkan responsive design dengan baik adalah YouTube, yang tata letaknya berubah total dari tampilan multi-kolom di desktop menjadi single-kolom yang mudah di-scroll di mobile. Sebaliknya, banyak situs pemerintah atau akademik lama yang belum responsif, di mana pengguna mobile harus melakukan zoom dan geser secara manual untuk menavigasi halaman, membuktikan betapa tidak efektifnya desain yang kaku.
  
  ## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  
  ### Jawab: 
  Dalam CSS Box Model, margin, border, dan padding adalah tiga properti yang mengatur ruang di sekitar sebuah elemen. Bayangkan sebuah elemen sebagai foto dalam bingkai. Padding adalah ruang transparan di dalam bingkai, yang memisahkan foto (konten) dari bingkainya. Border adalah bingkainya itu sendiri, yang memiliki ketebalan, warna, dan gaya. Sementara itu, Margin adalah ruang transparan di luar bingkai, yang menciptakan jarak antara bingkai foto tersebut dengan bingkai foto atau elemen lain di dinding. Singkatnya, padding mengatur ruang di dalam, border adalah garis tepinya, dan margin mengatur jarak dengan elemen di luar.
  
  ## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
  
  ### Jawab: 
  Flexbox dan Grid adalah dua sistem layout CSS untuk menyusun elemen, namun dengan tujuan berbeda. Flexbox adalah sistem layout satu dimensi, yang ideal untuk mengatur elemen dalam satu baris (horizontal) atau satu kolom (vertikal). Kegunaan utamanya adalah untuk mendistribusikan ruang dan perataan item di dalam sebuah container, seperti menyusun item navigasi di dalam sebuah navbar. Di sisi lain, Grid adalah sistem layout dua dimensi yang dirancang untuk mengatur elemen dalam baris dan kolom secara bersamaan. Ini membuatnya sangat cocok untuk layout halaman yang kompleks, seperti membuat galeri gambar, atau menyusun struktur utama halaman web yang terdiri dari header, sidebar, konten, dan footer.
  
  ## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
  
  ### Jawab: 
  Untuk menyelesaikan tugas ini, saya memulai dengan mengintegrasikan framework Tailwind CSS ke dalam proyek Django melalui CDN di base.html untuk fondasi styling. Selanjutnya, saya mengimplementasikan fungsionalitas backend untuk mengedit dan menghapus produk dengan membuat fungsi di views.py dan mendaftarkan URL-nya di urls.py. Setelah itu, saya fokus ke frontend dengan mengubah tampilan. Saya membuat navbar yang responsif, mendesain halaman daftar produk menggunakan sistem grid dan kartu (card), serta mengimplementasikan logika kondisional untuk menampilkan pesan khusus jika tidak ada produk. Setiap kartu produk dilengkapi dengan tombol edit dan hapus yang terhubung ke fungsi backend. Terakhir, saya menerapkan styling yang konsisten pada semua halaman lain seperti login, register, dan detail produk, lalu melakukan pengujian menyeluruh untuk memastikan semua fitur berfungsi dan desainnya responsif di berbagai ukuran layar.

  #### Referensi :
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity
  https://css-tricks.com/specifics-on-css-specificity/
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
  https://web.dev/articles/responsive-web-design-basics
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model
  https://www.freecodecamp.org/news/css-box-model-explained-by-living-in-a-boring-suburban-neighborhood-9a9e692773c1/
  https://css-tricks.com/snippets/css/a-guide-to-flexbox/
  https://css-tricks.com/snippets/css/complete-guide-grid/
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Relationship_of_grid_layout_with_other_layout_methods
</details>

<details>
  <summary>Tugas 6</summary>
  
  ## 1. Apa perbedaan antara synchronous request dan asynchronous request?
  
  ### Jawab: 
  Perbedaan mendasar antara synchronous dan asynchronous request terletak pada cara eksekusi kode. Pada synchronous request, atau permintaan sinkron, klien (browser) mengirim permintaan ke server dan harus menunggu hingga server memberikan respons sebelum dapat melanjutkan eksekusi kode lainnya. Ini berarti seluruh halaman akan "terjebak" atau tidak responsif selama proses menunggu. Sebaliknya, pada asynchronous request, atau permintaan asinkron, klien dapat mengirim permintaan ke server dan tetap melanjutkan eksekusi kode lain tanpa harus menunggu respons. Ketika respons dari server tiba, sebuah fungsi (callback) akan dijalankan untuk memproses data tersebut. Proses ini memungkinkan halaman web tetap interaktif dan responsif bagi pengguna, karena tidak ada proses pemblokiran yang terjadi.
  
  ## 2. Bagaimana AJAX bekerja di Django (alur request–response)?
  
  ### Jawab: 
  Dalam Django, alur kerja AJAX dimulai ketika suatu peristiwa dipicu di sisi klien, misalnya pengguna mengklik tombol. Sebuah fungsi JavaScript kemudian membuat objek XMLHttpRequest atau menggunakan Fetch API untuk mengirim permintaan HTTP (seperti GET atau POST) ke URL tertentu di aplikasi Django. Permintaan ini membawa data, seringkali dalam format JSON. Django menerima permintaan ini melalui URL dispatcher-nya (urls.py) yang mengarahkannya ke fungsi view yang sesuai. Di dalam view, Django memproses data yang masuk, berinteraksi dengan model (database), dan menyiapkan respons. Selain merender template HTML lengkap, view biasanya mengembalikan data dalam format JSON menggunakan JsonResponse. Data ini kemudian diterima kembali oleh fungsi JavaScript di sisi klien, yang selanjutnya memanipulasi DOM (Document Object Model) untuk memperbarui sebagian kecil dari halaman web tanpa perlu memuat ulang seluruh halaman.
  
  ## 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
  
  ### Jawab: 
  Keuntungan utama menggunakan AJAX di Django dibandingkan dengan render biasa adalah peningkatan performa dan pengalaman pengguna (UX). Dengan AJAX, hanya data yang relevan yang dipertukarkan antara klien dan server, bukan seluruh halaman HTML. Ini secara signifikan mengurangi jumlah data yang ditransfer, membuat aplikasi terasa lebih cepat dan lebih responsif. Pengguna tidak perlu mengalami kedipan putih (white flash) akibat pemuatan ulang halaman penuh setiap kali ada interaksi kecil, seperti mengirim komentar atau memfilter data. Hal ini menciptakan pengalaman yang lebih mulus dan dinamis seperti pada aplikasi desktop, di mana pembaruan terjadi secara instan di bagian halaman yang relevan saja, sehingga meningkatkan efisiensi dan kepuasan pengguna secara keseluruhan.
  
  ## 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
  
  ### Jawab: 
  Untuk memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django, beberapa langkah krusial harus diterapkan. Pertama, Cross-Site Request Forgery (CSRF) protection tetap wajib. Setiap permintaan POST AJAX harus menyertakan CSRF token yang disediakan Django untuk memverifikasi bahwa permintaan berasal dari situs yang sah. Kedua, semua data yang dikirim dari klien, seperti nama pengguna dan kata sandi, harus divalidasi secara ketat di sisi server menggunakan Django Forms atau serializers untuk mencegah serangan seperti SQL Injection. Ketiga, komunikasi antara klien dan server harus selalu diamankan menggunakan HTTPS (SSL/TLS) untuk mengenkripsi data sensitif yang sedang transit. Terakhir, hindari mengirimkan pesan error yang terlalu detail ke klien, yang bisa dieksploitasi oleh penyerang; cukup berikan respons umum seperti "Login gagal" sambil mencatat detail kesalahan di log server.
  
  ## 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
  
  ### Jawab: 
  AJAX secara drastis meningkatkan pengalaman pengguna (User Experience) dengan membuat website terasa lebih cepat, interaktif, dan mulus. Dengan menghilangkan kebutuhan untuk memuat ulang seluruh halaman, AJAX memungkinkan pembaruan konten secara real-time dan instan. Contohnya, saat pengguna memberikan "suka" pada sebuah postingan, jumlah suka langsung bertambah tanpa jeda; atau saat mengisi formulir, validasi dapat dilakukan per-kolom secara langsung tanpa harus mengirim keseluruhan formulir terlebih dahulu. Interaksi yang responsif ini mengurangi waktu tunggu dan frustrasi pengguna, menciptakan alur penggunaan yang tidak terputus, dan memberikan nuansa seperti menggunakan aplikasi desktop yang canggih. Pada akhirnya, website yang menggunakan AJAX terasa lebih modern, efisien, dan memuaskan untuk digunakan.

  #### Referensi :
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS/Introducing
  https://www.geeksforgeeks.org/javascript/synchronous-and-asynchronous-in-javascript/
  https://realpython.com/learning-paths/django-web-development/
  https://www.nngroup.com/articles/the-top-ten-web-design-mistakes-of-1999/
  https://docs.djangoproject.com/en/5.2/ref/csrf/
  https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html
  https://www.smashingmagazine.com/2009/09/10-useful-usability-findings-and-guidelines/
</details>