# TP1DPBO2024

Saya Daffa Fakhry Anshori dengan NIM 2200337 mengerjakan soal TP 1 dalam Praktikum mata kuliah Desain dan Pemrograman Berbasis Objek, 
untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamin.

# Desain Kelas
![Desain TP1 DPBO](https://github.com/daffahag123/TP1DPBO2024/assets/135239333/095c91cd-d296-4e1f-aad2-da6408c13b4a)

# Desain Program
Disini saya membutuhkan total 14 kelas untuk membuat program simulasi game, penjelasan kelas masing-masing dibawah ini.
1.	Kelas Player
   - Kelas mandiri.
   - Berisi atribut pribadinya yaitu (name_player, gender, dan character).
   - Memiliki sebuah object character tujuannya untuk menyimpan karakter utama (MainCharacter) yg dipilih oleh seorang pemain. Komposisi dengan kelas MC.
     
2.	Kelas Character
   - Kelas induk dari kelas MC dan NPC.
   - Berisi atribut pribadinya yaitu (id_character, name_character, gender, role, hp, dan defense, weapon, dan skill).
   - Memiliki sebuah object senjata tujuannya untuk menyimpan sebuah senjata, disini saya asumsikan satu karakter cuma bisa memegang satu senjata saja. Komposisi dengan kelas Weapon.
   - Memiliki array of object skill tujuannya untuk menyimpan skill-skill yang dimiliki setiap karakter (bisa punya banyak skill). Komposisi dengan kelas Skill.
     
3.	Kelas Skill
   - Kelas mandiri.
   - Berisi atribut pribadinya yaitu (name_skill, skill_type, dan value).
   - Memiliki sebuah object value tujuannya untuk memberi nilai apakah skill ini tipe nya penyerangan / penyembuhan. Komposisi dengan kelas Penyerangan & kelas Penyembuhan.
     
4.	Kelas Weapon
   - Kelas mandiri
   - Berisi atribut pribadinya yaitu (item_type, name_weapon, weapon_type, value, dan price).
   - Memiliki sebuah object value tujuannya untuk memberi nilai senjata ini memiliki tipe penyerangan. Karena senjata yg dimiliki semua karakter diset senjatanya bertipe penyerangan. Komposisi dengan kelas Penyerangan
     
5.	Kelas Penyerangan
   -	Kelas mandiri
   -	Berisi atribut pribadinya yaitu (attack dan damge). Jadi senjata dan skill itu memiliki jenis yg bisa menyerang kepada musuh.
     
6.	Kelas Penyembuhan
-	Kelas mandiri
-	Berisi atribut pribadinya yaitu (heal dan defense). Jadi skill itu memiliki jenis yg bisa menyembuhkan dirinya sendiri.
  
Penjelasan mengenai skill dan senjata ini setiap karakter diset mempunya satu unit senjata yg diberi tipe penyerangan. Jadi tidak ada senjata yg tipe nya penyembuhan, tujuannya pada saat melawan satu sama lain bisa saling berantem. Untuk skill tipe nya bisa keduanya yaitu penyerangan dan penyembuhan.

7.	Kelas MC (MainCharacter)
   - Kelas turunan dari kelas Character.
   - Berisi atribut pribadinya yaitu (level, exp, dan inventory).
   - Memiliki sebuah object inventory tujuannya untuk menyimpan seluruh peralatan yang di dapat nantinya. Komposisi dengan kelas Inventory.
     
Jadi nantinya setiap karakter yg akan dimainkan oleh player ini memiliki sebuah inventory/tas guna untuk menyimpan seluruh barang yg nantinya akan di dapatkan ketika menyelesaikan misi, membeli barang dan membunuh musuh. Setiap karakter akan memiliki level, dan semua karakternya ini diset dari level 0. Untuk menaikkan level ini dengan cara memperoleh exp. Setiap mendapatkan exp 100 maka akan naik level nya.

8.	Kelas Inventory
   - Kelas mandiri.
   - Berisi atribut pribadinya yaitu (coin, key, poition, dan weapon). Jadi dalam inventory ini saya buat untuk menyimpan 4 kategori barang itu. Komposisi dengan kelas Key, kelas Potion, dan kelas Weapon.

Dalam program saya ini, Main Character dan NPC yang baik memiliki satu buah inventory/tas. Semua barang yg bisa didapatkan di dalam game nya ini berupa coin, kunci, ramuan, dan senjata. Dimana coin dalam program saya digunakan sebagai uang dalam game untuk membeli barang dari inventory NPC baik.

9.	Kelas Potion
   - Kelas mandiri.
   - Berisi atribut pribadinya yaitu (item_type, name_potion, potion_type, value, dan price).
   - Memiliki sebuah object value tujuannya untuk memberi nilai apakah potion ini tipe nya penyerangan (untuk memperkuat senjata) / penyembuhan (untuk penyembuhan diri sendiri). Komposisi dengan kelas Penyerangan & kelas Penyembuhan.

10. Kelas Key
    - Kelas mandiri.
    - Berisi atribut pribadinya yaitu (item_type, name_key, type_key, dan price).
      
Desain kelas saya ini sebenarnya ada beberapa kelas yg mirip atribut nya yaitu kelas Weapon,kelas Potion, dan kelas Key. Namun saya buatkan terpisah karena untuk pengembangan desain game ke depan nantinya. Alasan lainnya:
a. Dalam kelas Key tidak dicantumkan value, karena tidak membutuhkan itu.
b.	Dalam kelas Weapon dan kelas Potion atributnya mirip, tapi saya bedakan kelasnya karena nanti dalam satu kelas aka nada penambahan atribut. Contohnya, penambahan skin/aksesoris dalam kelas Weapon.
c.	Dalam program yang saya buatkan pun barang yang disediakan hanya kunci, ramuan, dan senjata. Jadi saya bisa lebih gampang untuk lebih mengatur jika ketiga barang itu dibuatkan kelas masing-masing.
Kemudian ke-3 kelas ini memiliki atribut price, dimana nantinya barang kunci, ramuan, dan senjata bisa dijual barang nya dan dapat dibeli juga. 

11. Kelas NPC
    - Kelas turunan dari kelas Character.
    - Berisi atribut pribadinya yaitu (NPC_type dan location). Jadi pembuatan kelas ini nantinya untuk membedakan mana NPC yang baik, dan NPC yang jahat.

12. Kelas goodNPC
    - Kelas turunan dari kelas NPC.
    - Berisi atribut pribadinya yaitu (quest dan inventory).
    - Memiliki array of object quest tujuannya untuk menyimpan semua misi yang dimiliki oleh NPC baik ini. Komposisi dengan kelas Quest.
    - Memiliki sebuah object inventory tujuannya untuk menyimpan seluruh barang yang nanti akan dijual kepada MainCharacter. Komposisi dengan kelas Inventory.
      
13. Kelas Quest
    - Kelas mandiri.
    - Berisi atribut pribadinya yaitu (id_quest, name_quest, description, reward, dan status).
    - Memiliki reward yang isinya yaitu (EXP, Coin, dan Item). Item ini akan berisi barang berupa kunci, potion, atau senjata. Jadi semua quest akan memberikan 3 macam itu. Maka dari itu, kelas ini komposisi dengan kelas Key, kelas Potion, dan kelas Weapon.
      
14. Kelas badNPC
    - Kelas turunan dari kelas NPC
    - Berisi atribut pribadinya yaitu (difficulty_level, reward, dan status)
    - Memiliki reward yang isinya yaitu (EXP, Coin, dan Item). Item ini akan berisi barang berupa kunci, potion, atau senjata. Jadi semua quest akan memberikan 3 macam itu. Maka dari itu, kelas ini komposisi dengan kelas Key, kelas Potion, dan kelas Weapon.
      
Penjelasan akan mendapat reward itu setelah kalian menjalankan quest dan bisa mengalahkan musuh.


