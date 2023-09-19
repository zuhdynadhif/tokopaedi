## Table of Content
1. [Tugas 1](#tugas-1)
2. [Tugas 2](#tugas-2)
3. [Tugas 3](#tugas-3)
4. [Tugas 4](#tugas-4)

## Tugas 1
[Contents](#table-of-content)
### 1. Impelementasi checklist.
Saya pergi ke repository lokal yang berisi tugas PBP dan menyiapkan satu folder untuk tugas-tugas yang berhubungan dengan github pada “PBP/GITHUB Connect”
Saya membuat virtual environment denan command ```python -m venv env```
Saya membuat project django app di dalam GITHUB Connect dengan menggunakan command ```django-admin startproject tokopaedi```


Setelah itu saya masuk ke direktori utama “/tokopaedi” untuk kemudian membuat app baru bernama main dengan menggunakan command ```django-admin startapp main```


Kemudian, saya melakukan setup pada settings.py agar semua HOST dapat mengakses project ini dan juga menginstall app main sehingga terdapat line berikut ini

```python
ALLOWED_HOST = [‘*’]

INSTALLED_APPS = [
    …
    …
   ‘main’,
]
```
Sehingga, app main berhasil di install dalam proyek tokopaedi


Kemudian, saya melakukan setup routing pada app main denganmenambahkan file "urls.py" pada app main sehingga terbentuk file baru "main/urls.py". File tersebut diisi dengan
```python
from django.urls import path
from main.views import show_main

# tugas 2: menjadikan main sebagai app
app_name = 'main'

# url untuk mengakses app main
urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Setelah itu saya membuat path baru pada urls.py yang ada dalam direktori proyek untuk bisa mengakses file urls yang ada dalam app main, dengan menambahkan baris kode
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
]
```
Kemudian, saya mempersiapkan models.py pada app main. Saya membuat sebuah class Product yang memiliki atribut name, price, amount, dan juga description. Tampilan class tersebut adalah seperti ini:
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
```
Untuk membuat tampilan utama app main saya membuat template dengan menyiapkan direktori baru bernama "main/templates/main" dan akan dibuat satu file main.html.

Langkah selanjutnya adalah mempersiapkan views.py pada app main yang dapat menghubungkan models.py dan juga file template pada "main/templates/main". Pada "main/views.py" saya menambahkan function show_main yang akan mengenerate models yang saya miliki ke "templates/main/main.html"
```python
# tugas 2: function untuk show app main
def show_main(request):
    context = {
        'name': 'Kursi Gaming',
        'price' : '2000000',
        'amount' : '1',
        'description' : 'Kursi Gaming dengan desain menyerupai mobil sport akan meningkatkan kemampuan coding anda sebanyak 250%'
    }
    return render(request, "main.html", context)
```
selanjutnya, saya melakukan migrasi model dengan menjalankan perintah ```python manage.py makemigrations``` dan ```python manage.py migrate```

### 2. Bagan request client ke web aplikasi

![Bagan](images/Bagan_Django.png)
Pada bagan tersebut client melakukan request HTTP dan mengirimkannya ke Django melalui browser, request ini akan diarahkan ke tokopedia/urls.py untuk kemudian diteruskan ke views.py yang sesuai dengan request. views.py akan mengambil data melalui models.py dan kemudian me-render hasilnya dengan templates. Setelah proses tersebut selesai, views.py akan me-return HTTP response dan akan diberikan ke browser client.

### 3. Virtual environment
Dengan menggunakan virtual environment pada proyek Django, kita bisa mengeliminasi permasalahan dependency pada berbagai package yang dibutuhkan oleh proyek kita, dengan kata lain segala kebutuhan yang kita download hanya berpengaruh pada environment khusus tersebut dan kita tidak perlu melakukan download berkali-kali. Namun, kita tetap bisa membuat proyek Django tanpa menggunakan virtual environment degnan konsekuensi harus melacak setiap package yang ada dan akan menyusahkan kita sendiri terutama dalam melakukan kolaborasi dengan engineer lain.

### 4. Penjelasan tentang MVC, MVTM, dan MVVM
Baik MVC, MVT, maupun MVVM adalah arsitektur aplikasi yang bertujuan untuk memudahkan developer dalam mengelola aplikasi.
#### a. MVC
MVC adalah arsitektur yang membagi aplikasi menjadi 3 bagian utama yaitu Model, View, dan Controller. Model menjadi bagian yang bertanggung jawab untuk mengatur data yang ada seperti mengubah data sesuai dengan kebutuhan yang ada dan mengambil data dari database. View bertanggung jawab untuk mengatur tampilan aplikasi, biasanya berbentuk .html dalam web development. Controller bertanggung jawab untuk mengatur seluruh flow aplikasi terutama bagaimana data yang diberikan oleh Model dapat diteruskan ke View.
#### b. MVT
MVT adalah arsitektur yang membagi aplikasi menjadi 3 bagian utama yaitu Model, View, dan Template. Model pada MVT memiliki karakter yang sama dengan model pada MVC. View pada arsitektur MVT memiliki karakteristikk yang serupa dengan Controller pada arsitektur MVC. Sedangkan template, memiliki tanggung jawab yang sama dengan view pada MVC.
#### c. MVVM
MVVM adalah arsitektur yang membagi aplikasi menjadi 3 bagian utama yaitu Model, View, dan ViewModel. Dalam arsitektur MVVM, Model bertugas untuk mengelola logika bisnis yang ada, lalu ViewModel akan mengelola logika bisnis yang ada dan meneruskannya pada View untuk ditampilkan ke pengguna.

Perbedaan ketiganya adalah pada Impelemntasi pengelolaan arsitekturnya. Pada MVC, controller hanya bertugas untuk menghubungkan Model dan juga View. Pada MVT, View bertugas menerima HTTP request dan mengembalikan HTTP response. Pada MVVM fungsionalitas elemen pada View diatur sedemikian rupa oleh ViewModel.

## Tugas 2
[Contents](#table-of-content)
### 1. Perbedaan antara form `POST` dan `GET`
#### a. POST
#### b. GET

### 2. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

### 3. Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern

### 4. Impelementasi _checklist_

#### a. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

#### b. Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

#### c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

#### d. Menjawab beberapa pertanyaan berikut pada README.md pada root folder.


## Tugas 3
[Contents](#table-of-content)
## Tugas 4
[Contents](#table-of-content)