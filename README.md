`def diamondGlenn(height):
    if height % 2 == 0:
        height += 1`

pada bagian ini merupakan insialisasi dan pembuatan function yang mana akan digunakan untuk kalkulasi dari user input. `height % 2 == 0` kode ini berguna untuk mengecek nilai input height tersebut apakah angka genap,
jika angka genap maka hasil dari modulus 2 akan selalu 0, ketika angka tersebut 0 maka value height akan ditambah 1 sehingga menjadi angka ganjil.

`for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)
        # print(" " * spaces + "*" * i)`

pada bagian ini looping akan digunakan untuk mengkalkulasi icon star atau "*" agar nilainya mengalami kenaikan sesuai dengan angka genap, sebagai contoh apabila saya memasukan angka `5` untuk height value,
blok untuk for loop ini akan menghasilkan sequence [1, 3, 5] ini bisa ditunjukan dari parameter range yang dipakai yaitu `range(1, height + 1, 2)`. Setelah itu value dari height akan dikurangi dengan nilai index [1, 3, 5] 
secara berurutan dan nilai tersebut akan dibagi yang mana hasil dari kalkulasi ini akan disimpan dalam variabel space. 

` print(" " * spaces + "*" * i + " " * spaces)
        # print(" " * spaces + "*" * i)`

nilai space akan dikali dengan string yang akan berguna sebagai spaces dan nilai index akan dikali dengan tanda bintang "*" . Kita bisa menggunakan ` print(" " * spaces + "*" * i)` atau menggunakan `print(" " * spaces + "*" * i + " " * spaces)`
keduanya mempunyai output yang sama namun pada kode program `print(" " * spaces + "*" * i)` ini lebih efisien karena dia hanya mengatur space dari sisi kiri dan secara otommatis akan membuat sisi bagian kanan dari tanda bintang 
akan memberikan space yang sama dengan sebelah kiri, namun jika anda ingin membuat logic nya lebih mudah dipahami bisa menggunakan kode `print(" " * spaces + "*" * i + " " * spaces)`, pada kode program ini akan mengatur bagian
sisi kiri dan kanan spaces nya.

`for i in range(height-2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)
        # print(" " * spaces + "*" * i)`

pada bagian ini akan menjalankan program untuk membentuk bagian diamond di sisi bagian bawah, dimana sebelumnya program telah membuat sequence [1,3,5] ketika telah sampai pada index ke 5 akan berhenti, berbeda dengan kode program for loop ini
dimana program akan dijalankan sampai nilai index nya `0` dan akan dibuat nilai index dari tinggi ke rendah dengan pengurangan nilai `-2` ini yang akan membuat nilai height jika kita beri angka 5 maka nilai sequence nya
akan berlaku [5,3,1] karena dikurangi `-2` namun jika kita menggunakan [5,3,1] maka diamond tidak akan terbentuk sempurna karena hasilnya akan seperti ini

![image](https://github.com/Glennimmanuell/Diamond-Python/assets/118232825/63058979-08cc-4486-b5e4-f22384554817)

ini bukan hasil yang kita mau, untuk membentuk agar sesuai bentuk diamond yang kita mau maka kita harus mengatur sequence nya [3, 1]. Oleh karena itu, pad blok kode itu terdapat parameter range nya `height-2` yang bertujuan
jika nilai height nya 5, maka nilai nya akan dimulai dari `5-2` yaitu `3` dengan modifikasi ini sequence nya akan [3, 1]. Dengan cara ini kita berhasil membuat bentuk diamond yang tepat 

![image](https://github.com/Glennimmanuell/Diamond-Python/assets/118232825/d7a2137b-638b-403d-8b35-b35f089ca8d9)

`tinggiDiamond = int(input("hayo mau setinggi apa: "))
diamondGlenn(tinggiDiamond)`

Pada bagian ini program meng-handle user input yang mana diatur untuk nilai integer supaya tidak mengacaukan sequence yang akan dibuat pada for loop calculation, pada bagian akhir function yang telah kita buat sebelumnya
dipanggil dengan parameter dari user input tersebut, sehingga apapun value yang masuk dari user input akan masuk ke paramter height pada function `diamondGlenn`

        
