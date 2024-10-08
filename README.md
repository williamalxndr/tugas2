TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Saya menggunakan tutorial untuk mengimplementasikan checklist checklist dan menggunakan youtube dan slide materi MTV untuk memahami lebih dalam konsep MTV dalam django dan apa yang dilakukan oleh suatu perintah dalam django, contohnya makemigrations dan migrate.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   urls.py (urls.py akan membaca path yang direquest user semisal /login) <==> views.py (views akan membaca request dan memberi respon berupa berkas html dan juga data dari model) <==> template/berkas html, views akan memberi respon berkas html  <==> models.py (views akan merequest data, dan models akan mengakses database dan memberikan respon data yang diminta)

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   git berguna sebagai version control system. Semisal kita sudah menyelesaikan suatu project perangkat lunak dan ingin menyimpannya, kita dapat menyimpan di git. Jika suatu saat akan ada update pada perangkat lunak tersebut, kita dapat menyimpan kembali di git. Lalu, jika ternyata update tersebut tidak jadi ingin dipakai, kita dapat memakai kembali versi pertama yang sudah disimpan di git. Kemudian, di git juga terdapat branch, dimana kita dapat membuat berbagai versi dari perangkat lunak yang kita kembangkan. Semisal, developer mengembangkan suatu aplikasi ojek online, kemudian ia ingin menambahkan fitur baru untuk taxi online, ia dapat mengembangkan fitur baru di branch lain sebelum diimplementasikan ke branch utama sehingga tidak akan mengganggu branch utama.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Django memiliki fitur yang lengkap untuk mendevelop perangkat lunak, django didasarkan struktur MVT yang memungkinkan developer untuk mengerjakan masing masing tugas pada file yang terpisah sehingga nyaman untuk pemula. Selain itu, django juga menyediakan built-in admin interface yang memudahkan developer untuk mengelola data tanpa perlu melakukan coding.

5. Mengapa model pada Django disebut sebagai ORM?
   Model pada django disebut ORM (Object Relational Mapping) karena fungsinya adalah memetakan object python ke database tanpa perlu menulis SQL secara langsung. 


TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery dalam sebuah platform diperlukan untuk komunikasi antara client-side dengan server-side. Ini membuat user dapat berinteraksi dengan efektif dalam platform seperti contohnya untuk menelusuri konten, mengirim form, melakukan pembaruan secara real-time. Dalam hal ini, data yang dikirim dapat berupa data pengguna seperti foto profil, deskripsi pengguna ataupun data API external yang digunakan sebagai pertukaran data antar aplikasi. Data delivery yang efisien akan berpengaruh terhadap user experience. Data delivery yang cepat akan membuat user dapat mengakses aplikasi dengan lebih cepat.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, saya akan lebih memilih JSON dibandingkan XML karena JSON lebih readable dibandingkan XML. JSON berbentuk seperti sebuah HashMap/dictionary (key:value), sedangkan XML berbentuk tag html. Hal ini juga berpengaruh pada ukuran file, membuat JSON lebih kecil dalam ukuran file dibandingkan XML. Hal yang membuat JSON lebih populer dibandingkan XML seperti poin poin yang sudah saya sebutkan, ditambah lagi karena syntax JSON lebih mudah dibanding XML. (source:https://aws.amazon.com/compare/the-difference-between-json-xml/)

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    method is_valid() berfungsi untuk memvalidasi isi dari form yang disubmit apakah sudah sesuai. Jika ada field yang belum terisi atau ada field yang tidak sesuai dengan tipe datanya, semisal data .CharField() tapi kita menginput integer, maka method is_valid() akan mereturn False. Jika data sudah valid (is_valid True) maka data akan dimasukkan ke database.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf sendiri adalah singkatan dari cross site request forgery. Artinya, request dari website yang berbeda dapat diteruskan ke request website awal. Hal ini dapat berbahaya jika ada penyerang yang membuat duplikasi website dari suatu website dan menyamar seakan akan sebagai pihak website asli dan meminta request yang berbahaya. csrf_token adalah token keamanan unik yang akan dibuat setiap kali user akan mengirimkan data dari form untuk mencegah serangan csrf. Dengan csrf token, setiap kali form disubmit akan memiliki satu token csrf yang unik, sehingga tidak akan ada form palsu.  Jika tidak ada csrf_token, selama kita masih ada di halaman website awal, dan kemudian kita mengakses website dari penyerang, form yang kita kirimkan dari website penyerang dapat diteruskan menjadi request di website awal. (source: https://www.youtube.com/watch?v=MoN2CNCjRjc)

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Saya menggunakan tutorial untuk mengimplementasikan checklist secara garis besar, kemudian saya menggunakan youtube, chatGPT, dan website website untuk memahami kode dan konsep form pada django. 

Screenshot Postman: 
![Screenshot Postman JSON](screenshot-postman-json.png)
![Screenshot Postman XML](screenshot-postman-xml.png)

TUGAS 4

1.  Apa perbedaan antara HttpResponseRedirect() dan redirect()
    HttpResponseRedirect() hanya bisa menerima argumen berupa url, sedangkan redirect() dapat menerima model, view, atau url sebagai argumen. Keduanya sama sama melakukan hal yang sama, yaitu mengalihkan user ke url lain.
2.  Jelaskan cara kerja penghubungan model Product dengan User!
    Penghubungan model Product dengan User dilakukan dengan menggunakan ForeignKey. ForeignKey adalah suatu relasi yang memungkinkan kita menghubungkan satu ke banyak. Dimana disini satu user dapat memiliki banyak product. Setiap kali form disubmit, database akan menerima data user siapa yang mengirim form tersebut, dan user itulah yang akan dijadikan milik dari product.
3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep  tersebut.
    Authentication adalah proses yang memverifikasi siapa user yang ingin mengakses website kita, apakah user ini sudah terdaftar dalam database kita. Sedangkan authorization adalah proses yang memverifikasi apakah user dapat melakukan aksi tertentu. Yang terjadi ketika user login, pertama saat user mengklik submit/login pada halaman login, data username dan password akan dicocokkan dengan yang ada di database, jika terverifikasi, user akan dialihkan ke halaman lain. Lalu, terjadi authorization, sistem akan menggunakan authorization untuk memastikan tindakan apa saja yang boleh dilakukan user, semisal apakah boleh membuat blog baru atau hanya boleh sekedar melihat lihat. Django sudah menyediakan beberapa built in views yang bisa digunakan untuk authentication dan authorization seperti login, logout, password reset. Django mengimplementasikan authentication dan authorization ketika user log in, django akan membuat session id dan cookies untuk user itu dan dari situ django akan melihat akses apa yang bisa dilakukan user (authorization).
    (source: https://www.linkedin.com/pulse/understanding-djangos-authentication-system-guide-rashid-mahmood)
4.  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
    Django mengingat pengguna yang telah login menggunakan session id kemudian django menyimpan session id dalam bentuk cookie. Setiap kali pengguna mengakses halaman itu, cookie dikirim bersama request ke server. Kegunaan lain dari cookies: authentication otomatis (Remember me), menyimpan preferensi pengguna, keranjang belanja. Tidak semua cookies aman, contoh ancamannya adalah XSS, jika sebuah website rentan terhadap XSS, penyerang dapat menyisipkan skrip berbahaya ke halaman web dan mencuri cookies pengguna. Cookies yang dicuri dapat berupa informasi sensitif pengguna yang dapat digunakan untuk mengambil akun pengguna.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Menggunakan ppt dari scele, internet(stackoverflow, dokumentasi django), tutorial 3


TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    1. Urutan prioritas tertinggi adalah jika elemen css diikuti !important, contoh: color: red !important;
    2. Urutan prioritas tertinggi kedua adalah inline style, ini artinya elemen css dibuat pada tag html. Contoh: <div style="color: blue; text-align: center;"> Hal ini dikarenakan style pada tag html akan meng-overwrite style sebelumnya karena css diload di awal.
    3. ID selector, selector menggunakan id (#). Contoh: #btn-1 {color: red;}
    4. class selector, selector menggunakan class (.). Contoh: .box {color: blue}
2.  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
    Responsive design berguna agar pengguna dapat mengakses aplikasi web dalam berbagai perangkat dengan ukuran layar yang berbeda beda. Hal ini dapat meningkatkan pengalaman pengguna. Contoh aplikasi yang sudah menerapkan responsive design: twitter, youtube. Belum menerapkan responsive design: https://getbootstrap.com/docs/3.4/examples/non-responsive/

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    Margin adalah ruang di luar elemen, contoh implementasinya adalah untuk mengatur jarak antara elemen tersebut dengan elemen lain di sekitarnya. Border adalah elemen yang mengelilingi content, contoh implementasinya untuk batas visual untuk memudahkan visualisasi untuk mengatur layout. Padding adalah elemen yang mengatur jarak antara content ke border, contoh implementasi nya pada button, jika kita ingin text dalam button agar tidak terlalu mepet dengan kotak button nya, kita dapat memperbesar paddingnya.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    Flexbox adalah model layout satu dimensi yang memungkinkan elemen dalam sebuah kontainer untuk beradaptasi dengan ruang yang tersedia. Elemen dapat diatur dalam satu baris (horizontal) atau satu kolom (vertikal). Grid layout adalah model layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    Saya menggunakan dokumentasi tailwind untuk mengetahui class class yang dapat dipakai dan kegunaannya, dari youtube untuk melihat contoh implementasi, melihat tutorial untuk melihat template nya, dan menggunakan ai untuk proses debugging.

TUGAS 6
1.  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
    Javascript berguna agar membuat web lebih interaktif, sebagai contoh javascript dapat membuat efek animasi, efek pop up, dll. Kemudian, javascript juga dapat berguna untuk memanipulasi DOM, sehingga dapat menambah, menghapus, atau mengubah suatu elemen html sebagai contoh dapat membuat suatu event listener pada suatu elemen html. Javascript juga berguna untuk debugging dalam proses pengembangan website, menggunakan console. Lalu, dengan javascript, website dapat mengimplementasikan komunikasi asinkron dengan AJAX, dengan AJAX, data dapat dikirim ke server dan dikembalikan tanpa perlu me-reload seluruh halaman.
    
2.  Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
    Fungsi penggunaan await ketika kita menggunakan fetch() adalah untuk menunggu sampai promise yang dihasilkan oleh fetch() selesai atau terpenuhi (entah berhasil atau gagal) sebelum melanjutkan eksekusi ke baris kode berikutnya. fetch() adalah fungsi asynchronous yang mengembalikan sebuah promise. Dengan await, kita dapat menangani hasil dari promise tersebut secara sinkron. Jika kita tidak menggunakan await, maka fetch() akan mengembalikan promise secara langsung (bukan data yang diinginkan), dan kode berikutnya akan langsung dijalankan tanpa menunggu hasil dari request.

3.  Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST
    Django mewajibkan kita untuk menggunakan csrf token setiap kali mensubmit form. Namun pada AJAX POST kita, kita tidak menggunakan csrf_token, agar kita tetap bisa mensubmit form tanpa csrf_token, kita memerlukan decorator csrf_exempt.

4.  Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
    Frontend dapat dimanipulasi pengguna, pengguna dapat mengubah kode javascript di browser dan menonaktifkan javascript untuk melakukan serangan cross-site scripting(XSS) atau serangan penyalahgunaan data input lainnya. Sedangkan backend tidak dapat diakses langsung atau diubah oleh pengguna.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    Menggunakan tutorial asynchronous javascript di youtube dan slides untuk memahami konsep, stackoverflow dan ai untuk debugging.