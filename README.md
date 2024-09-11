1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
Saya menggunakan tutorial untuk mengimplementasikan checklist checklist dan menggunakan youtube dan slide materi MTV untuk memahami lebih dalam konsep MTV
dalam django dan apa yang dilakukan oleh suatu perintah dalam django, contohnya makemigrations dan migrate.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   
urls.py (urls.py akan membaca path yang direquest user semisal /login) <==> views.py (views akan membaca request dan memberi respon berupa berkas html dan juga data dari model)
<==> template/berkas html, views akan memberi respon berkas html  <==> models.py (views akan merequest data, dan models akan mengakses database dan memberikan respon data yang diminta)

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   
git berguna sebagai version control system. Semisal kita sudah menyelesaikan suatu project perangkat lunak dan ingin menyimpannya, kita dapat menyimpan di git. Jika suatu saat akan ada
update pada perangkat lunak tersebut, kita dapat menyimpan kembali di git. Lalu, jika ternyata update tersebut tidak jadi ingin dipakai, kita dapat memakai kembali versi pertama yang sudah
disimpan di git. Kemudian, di git juga terdapat branch, dimana kita dapat membuat berbagai versi dari perangkat lunak yang kita kembangkan. Semisal, developer mengembangkan suatu aplikasi
ojek online, kemudian ia ingin menambahkan fitur baru untuk taxi online, ia dapat mengembangkan fitur baru di branch lain sebelum diimplementasikan ke branch utama sehingga tidak akan
mengganggu branch utama.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   
Django memiliki fitur yang lengkap untuk mendevelop perangkat lunak, django didasarkan struktur MVT yang memungkinkan developer untuk mengerjakan masing masing tugas pada file yang terpisah
sehingga nyaman untuk pemula. Selain itu, django juga menyediakan built-in admin interface yang memudahkan developer untuk mengelola data tanpa perlu melakukan coding.

5. Mengapa model pada Django disebut sebagai ORM?
   
Model pada django disebut ORM (Object Relational Mapping) karena fungsinya adalah memetakan object python ke database tanpa perlu menulis SQL secara langsung. 
