# Tanda Tangan Elektronik untuk Dokumen Digital Berbasis Blockchain

Aplikasi ini deikembangkan dalam rangka memenuhi Tugas Akhir program studi S1 Informatika Telkom University oleh Muhammad Mujaddid Ashtsaqofi (1301174184). Aplikasi ini merupakan aplikasi berbasis web yang dapat digunakan untuk menandatangani dokumen PDF secara digital. Aplikasi ini juga menggunakan teknologi blokchain yaitu ethereum khususnya smart contract untuk validasi dokumen.

Aplikasi ini menggunakan front-end Vue JS dan back-end Django dan saat ini masih menggunakan [ganache ](http://trufflesuite.com/ganache/) untuk local ethereum blockchain. Selain itu aplikasi ini menggunakan IPFS sebagai pengimpanan file yang ada didalam aplikasi ini.

## Instalasi Aplikasi

Saat ini direkomendasikan untuk menggunakan OS Windows dan juga menggunakan browser google chrome dalam menjalankan aplikasi ini

### WINDOWS

#### 1. Install openssl dan set up environment
- install chocholatey
- buka windows powershell dengan administrator dan jalankan
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
- kemudian install openssl dengan menjalankan `choco install openssl`

#### 2. Clone Repository

``git clone https://github.com/mjaddid/TA-TTE.git``


#### 3. Konfigurasi Ganache untuk local ethereum blockchain

- download dan install ganache [KLIK DISINI](http://trufflesuite.com/ganache/)
- buat workspace baru ethereum
- ubah workspace name menjadi `Digital Signer`
- add project dan arahkan ke file `truffle-config.js` pada folder `tte_vue`
- pilih tab `chain` dan ubah gas fee menjadi 0
- save project
- biarkan ganache tetap menjalankan workspace `Digital Signer`


#### 4. Install Metamask Wallet

- download dan install metamask pada web browser [KLIK DISINI](https://metamask.io/download.html)
- buat wallet di metamask 
- buat network baru
- network name Digital-Signer
- buat network baru :

``bash
Network Name = digital-signer
New RPC URL = HTTP://127.0.0.1:7545
Chain ID = 1337
``

#### 5. Konfigurasi Database 

- buka mysql (XAMPP,Laragon,dsb)
- buat database baru dengan nama `dbtte`
- buka `setting.py` pada folder `\tte_django\tte-django`
- pada bagian database ubah nama, user, dan password sesuai dengan mysql pada pc
- jangan lupa di save

#### 6. Konfigurasi Python Virtual Environment

- buat virtual environment
```bash
python -m venv digital-signer-env
.\digital-signer-env\Scripts\activate.bat
pip install -r requirements.txt
cd tte_django
python manage.py migrate
```

#### 7. Menjalankan Django (Back-End)

- buka command prompt pada directory `tte_django`
- untuk membuat user admin jalankan
```bash
py manage.py createsuperuser
```
- isi email dan password untuk admin
- kemudian jalankan django dengan
```bash
py manage.py runserver
```
- biarkan command prompt tersebut berjalan
- untuk mengakses admin dashboard buka `http://localhost:8000/admin` pada web browser dam login menggunakan user admin yang sebelumnya dibuat

#### 8. Menjalankan VueJS (Front-End)

- jika belum ada Node JS [KLIK DISINI](https://nodejs.org/en/)
- jika belum ada truffle suit jalankan `npm install truffle -g`
- buka command prompt baru pada directory `tte_vue`
- install package dengan
```bash
npm install
```

- kemudian deploy smart contract dengan menjalankan
```bash
truffle migrate
```

- jalankan VueJs dengan
```bash
npm run serve
```
- jika ada permintaan keamanan pilih allow accsess

#### 9. Menjalankan Aplikasi Tanda Tangan Elektronik

- jalankan aplikasi dengan membuka `http://localhost:8080/` sesuaikan dengan tampilan yang muncul pada command promt sebelumnya


## Cara menggunakan Aplikasi

#### 1. Registrasi Account

- untuk registrasi akun pilih `Don't Have Account` pada halaman utama
- isikan semua field yang ada
- klik sign up
- akan muncul tampilan dari metamask untuk koneksi dengan aplikasi pilih confirm/connect
- jika akun berhasil dibuat akun tersebut masih belum terverifikasi

#### 2. Verifikasi Account

- akun hanya bisa diverifikasi oleh admin
- untuk verifikasi akun buka `http://localhost:8000/admin` dan login menggunakan akun admin
- pilih Accounts kemudian pilih akun yang akan diverifikasi
- periksa data user jika valid centang pada is Verified dan save
- akun user sudah diverifikasi

#### 3. Membuat Digital Certificate
- untuk bisa membuat digital certificate user harus sudah terverifikasi
- untuk membuat digital certificate buka tab `profile` kemudian pilih `digital certificate`
- pilih create new dan isi password untuk digital certificate (password ini digunakan dalam menandatangani dokumen nantinya) lalu confirm
- akan muncul pop up dari metamas untuk konfirmasi interaksi smart contract pilih comfirm
- log out dan log in kembali 

#### 4. Tanda Tangan Elektronik pada Dokumen PDF
- untuk bisa menandatangani dokumen user harus sudah terverifikasi dan membuat digital certificate
- tanda tangan elektronik terdiri dari 3 jenis, yaitu :
    - Self Sign
        Menandatangani sendiri dokumen yang telah diupload
    - Sign and Request
        Menandatangani sendiri dokumen yang telah diupload dan meminta orang lain untuk menandatangani dokumen itu juga
    - Request from Other
        Meminta orang lain untuk menandatangani dokumen yang diupload
    
    *Note:* Hanya dapat meminta tanda tangan dari user yang terdaftar dalam aplikasi ini
