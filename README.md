# BL-COMMENT-KAY-VER

💬 Mesin komen auto-backlink edisi Kanya.  
Karena ngetik komen manis manual itu buang waktu, mending suruh script yang kerja.  
Mau dofollow? Mau nofollow? Semua bisa... asal jangan follow mantan. 🙃

---

## ⚡ Cara Pakai (versi manusia malas)
1. Buka file `dofollow.json` atau `nofollow.json` di folder `lib/data/`
2. Edit sesuai format:  

   **Untuk `dofollow.json`:**
   - **ManusiaBaik** → nama/keyword tujuan lo (bakal jadi nama yang muncul di backlink).  
   - **AlamatPalsu** → email (bebas, asli/palsu bodo amat).  
   - **Bacot** → isi komentar lo.  

   **Untuk `nofollow.json`:**
   - **ManusiaBaik** → nama/keyword tujuan lo.  
   - **AlamatPalsu** → email.  
   - **TembakLink** → URL/website target buat backlink komen.  
   - **Bacot** → isi komentar lo.  

3. Masukin daftar link target yang mau ditembak ke:
   - `lib/files/list_dofollow.txt` → buat backlink dofollow.  
   - `lib/files/list_nofollow.txt` → buat backlink nofollow.  

4. Kalau datanya udah cakep → jalanin tools.  
5. Pilih jenis komentar di terminal:  
   - `1` = Dofollow  
   - `2` = Nofollow  
6. Duduk manis, biarin script yang kerja.  
7. Sip, backlink masuk. GG Gaming. 🥶

---

## 🚀 Cara Jalanin
```bash
python3 main.py
````

---

## 📂 Struktur Folder

```
BL-COMMENT-KAY-VER
├── main.py                # entrypoint eksekusi
├── lib
│   ├── data
│   │   ├── dofollow.json  # isi data buat backlink dofollow
│   │   └── nofollow.json  # isi data buat backlink nofollow
│   ├── files
│   │   ├── result_done.txt   # hasil backlink sukses
│   │   ├── result_fail.txt   # hasil backlink gagal
│   │   ├── user_agent.txt    # daftar user-agent yang diambil
│   │   ├── list_dofollow.txt # daftar link dofollow target
│   │   ├── list_nofollow.txt # daftar link nofollow target
│   │   └── proxy.txt         # daftar proxy yang diambil
│   └── tools
│       ├── colors.py             # definisi warna terminal
│       ├── drivers_proxy.py      # logic buat dapetin proxy
│       ├── drivers_user_agent.py # logic buat dapetin user-agent
│       └── utils.py              # banner & style tambahan
└── requirements.txt              # dependencies yang mesti diinstall
```

---

## 🐸 Catatan

* Tools ini buat belajar doang (cie belajar SEO).
* Spam = tanggung jawab lo sendiri, jangan salahin gua.
* Ingat: backlink boleh, jadi beban hidup jangan.
* ⚠️ **TOOLS INI BELUM MEMILIKI CAPTCHA SOLVER** → kalau nemu situs yang pake captcha, **AUTO GAGAL**.

---

## 🌌 Get Inspired

Script ini gue fork dari [bapakgacor/auto-komen](https://github.com/bapakgacor/auto-komen)
— versi gue diedit biar hidup gak gitu-gitu aja.
Mau gua tambahin juga **contoh isi file `list_dofollow.txt` dan `list_nofollow.txt`** biar user gak bingung formatnya?
```
