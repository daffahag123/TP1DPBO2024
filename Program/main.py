# Saya Daffa Fakhry Anshori dengan NIM 2200337 mengerjakan soal TP 1 
# dalam Praktikum mata kuliah Desain dan Pemrograman Berbasis Objek, untuk keberkahan-Nya
# maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamin.

# Untuk Potion-Attack : Dibalurkan ke senjata
# Untuk Potion-Heal : Diminum sama karakter
# Item type : Potion, Weapon, Key

# Import kelas
from Player import Player
from Character import Character
from Skill import Skill
from Weapon import Weapon
from Potion import Potion
from Attack import Attack
from Heal import Heal
from MC import MC
from NPC import NPC
from Inventory import Inventory
from BadNPC import BadNPC
from GoodNPC import GoodNPC
from Quest import Quest
from Key import Key

# -------------------------------------- Mempersiapkan Main Character (MC) -------------------------------------

# Senjata untuk para karakter
sword_weapon = Weapon(item_type="Weapon", name_weapon="Sword", weapon_type="Melee", value=Attack(attack=18, damage=45), price=25)
mace_weapon = Weapon(item_type="Weapon", name_weapon="Mace", weapon_type="Melee", value=Attack(attack=14, damage=35), price=20)
staff_weapon = Weapon(item_type="Weapon", name_weapon="Staff", weapon_type="Magic", value=Attack(attack=20, damage=50), price=30)
longbow_weapon = Weapon(item_type="Weapon", name_weapon="Longbow", weapon_type="Ranged", value=Attack(attack=16, damage=40), price=22)

# Skill untuk Barbarian
berserker_rage_skill = Skill(name_skill="Berserker Rage", skill_type="Offensive", value=Attack(attack=20, damage=30))
brutal_strike_skill = Skill(name_skill="Brutal Strike", skill_type="Offensive", value=Attack(attack=25, damage=40))
# Skill untuk Cleric
divine_light_skill = Skill(name_skill="Divine Light", skill_type="Defensive", value=Heal(heal=40, defense=5))
smite_evil_skill = Skill(name_skill="Smite Evil", skill_type="Offensive", value=Attack(attack=30, damage=45))
# Skill untuk Wizard
fireball_skill = Skill(name_skill="Fireball", skill_type="Offensive", value=Attack(attack=35, damage=50))
teleportation_skill = Skill(name_skill="Teleportation", skill_type="Utility", value=None)
# Skill untuk Archer
armor_piercing_shot_skill = Skill(name_skill="Swift Strike", skill_type="Offensive", value=Attack(attack=35, damage=70))
precision_shot_skill = Skill(name_skill="Precision Shot", skill_type="Offensive", value=Attack(attack=22, damage=55))

# Instansiasi membuat objek Karakter
nova_mc = MC(level=1, exp=0, inventory=Inventory(), id_character="M1", name_character="Nova", gender="Male", role="Barbarian", hp=100, defense=20, weapon=sword_weapon, skills=[berserker_rage_skill, brutal_strike_skill])
jane_mc = MC(level=1, exp=0, inventory=Inventory(), id_character="M2", name_character="Jane", gender="Female", role="Cleric", hp=100, defense=15, weapon=mace_weapon, skills=[divine_light_skill, smite_evil_skill])
sora_mc = MC(level=1, exp=0, inventory=Inventory(), id_character="M3", name_character="Sora", gender="Male", role="Wizard", hp=100, defense=20, weapon=staff_weapon, skills=[fireball_skill, teleportation_skill])
aloy_mc = MC(level=1, exp=0, inventory=Inventory(), id_character="M4", name_character="Aloy", gender="Female", role="Archer", hp=100, defense=15, weapon=longbow_weapon, skills=[armor_piercing_shot_skill, precision_shot_skill])

# ---------------------------------- Mempersiapkan Non-Played Character (NPC) ----------------------------------

# ----- NPC Baik -----

# Item yang diberikan oleh NPC
adrian_item1 = Potion(item_type="Potion", name_potion="Health Potion", potion_type="Potion-Heal", value=Heal(heal=50, defense=2), price=25)
adrian_item2 = Key(item_type="Key", name_key="Golden Key", key_type="Kunci Harta Karun", price=15)
lyra_item1 = Weapon(item_type="Weapon", name_weapon="Catapult", weapon_type="Ranged", value=Attack(attack=20, damage=35), price=23)
lyra_item2 = Key(item_type="Key", name_key="Silver Key", key_type="Kunci Harta Karun", price=10)

# Reward yang diberikan oleh NPC termasuk item
adrian_reward1 = {"EXP": 100, "Coin": 150, "Item": [adrian_item1]}
adrian_reward2 = {"EXP": 100, "Coin": 120, "Item": [adrian_item2]}
lyra_reward1 = {"EXP": 100, "Coin": 200, "Item": [lyra_item1]}
lyra_reward2 = {"EXP": 100, "Coin": 140, "Item": [lyra_item2]}

# Quest yang dimiliki Adrian 
adrian_quest1 = Quest(id_quest="Q1", name_quest="Mengumpulkan Ramuan", description="Kumpulkan 10 ramuan obat dari hutan.", reward=adrian_reward1, status="Incomplete")
adrian_quest2 = Quest(id_quest="Q2", name_quest="Mengantar Barang", description="Antar sebuah paket ke desa tetangga.", reward=adrian_reward2, status="Incomplete")

# Quest yang dimiliki Lyra
lyra_quest1 = Quest(id_quest="Q3", name_quest="Mencuri Informasi", description="Curi informasi rahasia dari markas musuh.", reward=lyra_reward1, status="Incomplete")
lyra_quest2 = Quest(id_quest="Q4", name_quest="Menemukan Barang Hilang", description="Temukan barang hilang yang tersimpan di dalam gua gelap.", reward=lyra_reward2, status="Incomplete")

# Key untuk disimpan di inventaris NPC
inv_adrian_key1 = Key(item_type="Key", name_key="Kunci Surga", key_type="Kunci Akses Tempat", price=24)
inv_adrian_key2 = Key(item_type="Key", name_key="Kunci Neraka", key_type="Kunci Akses Tempat", price=20)
inv_lyra_key1 = Key(item_type="Key", name_key="Kunci Goa", key_type="Kunci Akses Tempat", price=18)
inv_lyra_key2 = Key(item_type="Key", name_key="Kunci Castle", key_type="Kunci Akses Tempat", price=22)

# Potion untuk disimpan di inventaris NPC
inv_adrian_potion1 = Potion(item_type="Potion", name_potion="Health Potion", potion_type="Potion-Heal", value=Heal(heal=50, defense=2), price=20)
inv_adrian_potion2 = Potion(item_type="Potion", name_potion="Strength Potion", potion_type="Potion-Attack", value=Attack(attack=10, damage=0), price=16)
inv_lyra_potion1 = Potion(item_type="Potion", name_potion="Energy Potion", potion_type="Potion-Heal", value=Heal(heal=40, defense=3), price=18)
inv_lyra_potion2 = Potion(item_type="Potion", name_potion="Attack Booster", potion_type="Potion-Attack", value=Attack(attack=15, damage=20), price=20)

# Senjata untuk disimpan di inventaris NPC
inv_adrian_weapon1 = Weapon(item_type="Weapon", name_weapon="Greatsword", weapon_type="Melee", value=Attack(attack=22, damage=50), price=24)
inv_adrian_weapon2 = Weapon(item_type="Weapon", name_weapon="Battle Axe", weapon_type="Melee", value=Attack(attack=25, damage=55), price=26)
inv_lyra_weapon1 = Weapon(item_type="Weapon", name_weapon="Dagger of Shadows", weapon_type="Melee", value=Attack(attack=20, damage=40), price=22)
inv_lyra_weapon2 = Weapon(item_type="Weapon", name_weapon="Poisoned Dagger", weapon_type="Melee", value=Attack(attack=18, damage=35), price=20)

# Inventory yang dimiliki NPC 
adrian_inventory = Inventory(coin=0, keys=[inv_adrian_key1, inv_adrian_key2], potions=[inv_adrian_potion1, inv_adrian_potion2], weapons=[inv_adrian_weapon1, inv_adrian_weapon2])
lyra_inventory = Inventory(coin=0, keys=[inv_lyra_key1, inv_lyra_key2], potions=[inv_lyra_potion1, inv_lyra_potion2], weapons=[inv_lyra_weapon1, inv_lyra_weapon2])

# Senjata untuk NPC Baik
axe_weapon = Weapon(item_type="Weapon", name_weapon="Axe", weapon_type="Melee", value=Attack(attack=20, damage=50), price=0)
dagger_weapon = Weapon(item_type="Weapon", name_weapon="Dagger", weapon_type="Melee", value=Attack(attack=15, damage=30), price=0)

# Skill untuk NPC Baik
heroic_strike_skill = Skill(name_skill="Heroic Strike", skill_type="Offensive", value=Attack(attack=25, damage=40))
shuriken_throw_skill = Skill(name_skill="Shuriken Throw", skill_type="Offensive", value=Attack(attack=22, damage=40))

# Instansiasi membuat objek Non-Played Character (NPC) Baik
adrian_npc = GoodNPC(quest=[adrian_quest1, adrian_quest2], inventory=adrian_inventory, id_character="N1", name_character="Adrian", gender="Male", role="Warrior", hp=100, defense=25, weapon=axe_weapon, skills=[heroic_strike_skill], NPC_type="Baik", location="Forest")
lyra_npc = GoodNPC(quest=[lyra_quest1, lyra_quest2], inventory=lyra_inventory, id_character="N2", name_character="Lyra", gender="Female", role="Rogue", hp=100, defense=15, weapon=dagger_weapon, skills=[shuriken_throw_skill], NPC_type="Baik", location="City")


# ----- NPC Jahat -----

# Item yang diberikan oleh Musuh
thor_item1 = Potion(item_type="Potion", name_potion="Lightning Potion", potion_type="Potion-Attack", value=Attack(attack=35, damage=60), price=28)
thor_item2 = Key(item_type="Key", name_key="Hammer Key", key_type="Kunci Akses Tempat", price=18)
zara_item1 = Weapon(item_type="Weapon", name_weapon="Shadow Blade", weapon_type="Melee", value=Attack(attack=15, damage=25), price=24)
zara_item2 = Key(item_type="Key", name_key="Skeleton Key", key_type="Kunci Akses Tempat", price=20)

# Reward yang diberikan oleh Musuh termasuk item
thor_reward = {"EXP": 100, "Coin": 150, "Item": [thor_item1, thor_item2]}
zara_reward = {"EXP": 100, "Coin": 100, "Item": [zara_item1, zara_item2]}

# Senjata untuk Musuh
hammer_weapon = Weapon(item_type="Weapon", name_weapon="Hammer", weapon_type="Melee", value=Attack(attack=20, damage=20), price=0)
dark_blade_weapon = Weapon(item_type="Weapon", name_weapon="Dark Blade", weapon_type="Melee", value=Attack(attack=18, damage=30), price=0)

# Skill untuk Thor
thor_skill1 = Skill(name_skill="Lightning Strike", skill_type="Offensive", value=Attack(attack=30, damage=40))
thor_skill2 = Skill(name_skill="Thunderous Roar", skill_type="Offensive", value=Attack(attack=35, damage=45))
zara_skill1 = Skill(name_skill="Assassin's Strike", skill_type="Offensive", value=Attack(attack=25, damage=30))
zara_skill2 = Skill(name_skill="Poisoned Blade", skill_type="Offensive", value=Attack(attack=22, damage=35))

# Instansiasi membuat objek Non-Played Character (NPC) Jahat / Musuh
thor_enemy = BadNPC(difficulty_level="Medium", reward=thor_reward, id_character="E1", name_character="Thor", gender="Male", role="Warrior", hp=100, defense=15, weapon=hammer_weapon, skills=[thor_skill1, thor_skill2], NPC_type="Jahat", location="Mountains")
zara_enemy = BadNPC(difficulty_level="Easy", reward=zara_reward, id_character="E2", name_character="Zara", gender="Female", role="Assassin", hp=100, defense=12, weapon=dark_blade_weapon, skills=[zara_skill1, zara_skill2], NPC_type="Jahat", location="Forest")

# --------------------------------------------- Memulai Permainan ----------------------------------------------

# Daftar karakter utama
main_characters = [nova_mc, jane_mc, sora_mc, aloy_mc]
# Daftar karakkter NPC Baik
good_npc = [adrian_npc, lyra_npc]
# Daftar karakkter NPC Jahat
bad_npc = [thor_enemy, zara_enemy]

# Daftar Quest Adrian
adrian_quest = [adrian_quest1, adrian_quest2]
# Daftar Quest Lyra
lyra_quest = [lyra_quest1, lyra_quest2]
# Penggabungan Quest untuk di perulangan nantinya
npc_quests = {
    "Adrian": adrian_quest,
    "Lyra": lyra_quest,
}

# Pesan untuk mengisi data diri
print("\n> Halo Player!")
print("  Sebelum memulai petualanganmu, kami perlu mengenalimu lebih baik.")
print("  Mohon isi data dirimu terlebih dahulu!")

# Meminta data diri pemain
print("\n+-------------------------+")
print("|     Data Diri Pemain    |")
print("+-------------------------+")
name_player = input("  Nama kamu: ")
gender_player = input("  Gender kamu: ")
print("+-------------------------+")

# Memberikan informasi bahwa data diri telah berhasil dibuat
print("\n> SUCCESS!")
print("  Data diri berhasil dibuat!")

# Ucapan selamat datang masuk ke dalam game
print(f"\n> Selamat datang, {name_player}! Persiapkan dirimu untuk petualangan seru di Dunia Misterius!")
print("  Silakan pilih karakter utama untuk memulai petualanganmu")

# Variabel untuk melacak apakah karakter ditemukan
found = False   

while not found:
    # Tampilkan daftar karakter utama
    print("\n+====================================================+")
    print("|        Daftar Karakter Utama yang Tersedia         |")
    print("+====================================================+")
    for mc in main_characters:
        print(f" > {mc.get_name_character()} ({mc.get_role()}) ")
        print(f"    - Senjata: {mc.get_weapon().get_name_weapon()} (Attack: {mc.get_weapon().get_value().get_attack()}, Damage: {mc.get_weapon().get_value().get_damage()})")
        print(f"    - HP: {mc.get_hp()}")
        print(f"    - Defense: {mc.get_defense()}")
    print("+====================================================+")
    
    # Meminta input pemain untuk memilih karakter
    selected_character = input("\nPilih karakter utama: ")

    # Memeriksa kembali apakah karakter yang dipilih ada dalam daftar karakter utama
    for mc in main_characters:
        if selected_character.lower() == mc.get_name_character().lower():
            selected_mc = mc
            # Ubah nilai found menjadi True jika karakter ditemukan
            found = True

    # Jika karakter ditemukan, keluar dari loop
    if found:
        print("\n> SUCCES!")
        print(f"  Kamu telah memilih {selected_mc.get_name_character()} sebagai karakter utama kamu.")
        player = Player(name_player, gender_player, character=selected_mc)
    else:
        print("\n> ERROR!")
        print("  Karakter yang kamu pilih tidak ditemukan dalam daftar.")
        print("  Mohon pilih karakter utama yang valid!")
        
# Perulangan terus menerus selama pemain tidak ingin keluar dari game
while True:
    # Daftar kegiatan yg bisa dilakukan oleh pemain
    print("\nApa yang ingin dilakukan karakter kamu?")
    print("1. Berbicara dengan NPC")
    print("2. Bertarung dengan Musuh")
    print("3. Melihat Status Karakter")
    print("4. Melihat Inventory Karakter")
    print("5. Keluar")
    
    # Meminta input pemain untuk memilih opsi kegiatan karakter
    selected_action = input("Pilih aksi (1/2/3/4/5): ")
    
    # Memilih berbicara dengan NPC
    if selected_action == "1":
        print("Kamu memilih untuk berbicara dengan NPC.")
        
        # Menampilkan NPC yg bersedia untuk diajak bicara
        print("\n+-------------------------+")
        print("|    NPC yang tersedia    |")
        print("+-------------------------+")
        for npc in good_npc:
            print(f" > {npc.get_name_character()}")
        print("+-------------------------+")

        # Meminta input pemain untuk memilih npc
        selected_npc = input("\nPilih NPC yang ingin diajak bicara: ")
        
        # Memeriksa kembali apakah karakter npc yang dipilih ada dalam daftar karakter npc
        for npc in good_npc:
            if selected_npc.lower() == npc.get_name_character().lower():
                # Logika untuk berbicara dengan NPC yang dipilih
                print(f"\n{npc.get_name_character()} menawarkan beberapa pilihan bagi kamu:")
                print("1. Menjalankan Quest")
                print(f"2. Melihat Status {npc.get_name_character()}")
                print(f"3. Membeli Barang dari Inventory {npc.get_name_character()}")
                
                # Meminta input pemain untuk memilih aksi
                selected_tawaran = input("Pilih aksi (1/2/3): ")
                
                # Menjalankan Quest
                if selected_tawaran == "1":
                    while True:
                        # Inisialisasi daftar untuk menyimpan quest yang tersedia
                        available_quests = []

                        # Menambahkan quest yang belum diselesaikan ke dalam daftar available_quests
                        for npc_name, npc_quest in npc_quests.items():
                            if npc.get_name_character() == npc_name:
                                for i, quest in enumerate(npc_quest, start=1):
                                    # Memeriksa apakah quest belum diselesaikan
                                    if quest.get_status() != "Completed":
                                        available_quests.append(quest)

                        # Memeriksa apakah ada quest yang tersedia
                        if available_quests:
                            # Cetak quest yang tersedia
                            print("\nQUEST TERSEDIA")
                            print("------------------------------------------------------")
                            for i, quest in enumerate(available_quests, start=1):
                                print(" ID QUEST ->", quest.get_id_quest())
                                print("    - Judul      :", quest.get_name_quest())
                                print("    - Deskripsi  :", quest.get_description())
                                reward = quest.get_reward()
                                for reward_type, reward_value in reward.items():
                                    if reward_type == "Item":
                                        for item in reward_value:
                                            if isinstance(item, Potion):
                                                print("    - Bonus Item :", item.get_name_potion())   # Mengakses atribut nama untuk Potion
                                            elif isinstance(item, Key):
                                                print("    - Bonus Item :", item.get_name_key())      # Mengakses atribut nama untuk Key
                                            elif isinstance(item, Weapon):
                                                print("    - Bonus Item :", item.get_name_weapon())   # Mengakses atribut nama untuk Weapon
                                    else:
                                        print(f"    - Bonus {reward_type.ljust(5)}: {reward_value}")
                                print("------------------------------------------------------")
                        # Keluar dari loop jika tidak ada quest yang tersedia
                        else:
                            print(f"\n+------------------------------------+")
                            print(f" {npc.get_name_character()} tidak memiliki quest saat ini")
                            print(f"+------------------------------------+")
                            break   
                        
                        # Meminta inputan untuk memilih quest
                        selected_quest_id = input("Masukkan ID Quest: ")
    
                        # Memeriksa apakah input valid
                        selected_quest = None
                        for npc_name, npc_quest in npc_quests.items():
                            if npc.get_name_character() == npc_name:
                                for quest in npc_quest:
                                    if quest.get_id_quest().lower() == selected_quest_id.lower():
                                        selected_quest = quest
                                        break
                                    
                        # Jika quest tersedia
                        if selected_quest:
                            # Menampilkan pesan bahwa NPC memerintahkan karakter untuk menyelesaikan quest tertentu
                            print(f"\n> {npc.get_name_character()} (NPC) memerintahkan {player.get_character().get_name_character()} untuk menyelesaikan quest '{selected_quest.get_name_quest()}'.")
                            
                            # Meminta konfirmasi dari pemain untuk menyelesaikan misi
                            confirmation = input("  Apakah kamu yakin ingin menyelesaikan misi ini? (yes): ").lower()
                            
                            if confirmation == "yes":
                                # Menampilkan pesan bahwa quest berhasil diselesaikan
                                print("\n>>>>> QUEST COMPLETE! <<<<<")
                                print("+-------------------------+")
                                print("|         REWARD!         |")
                                print("+-------------------------+")
                                
                                # Menampilkan reward dari quest yang diselesaikan
                                reward = selected_quest.get_reward()
                                for reward_type, reward_value in reward.items():
                                    # Jika reward nya berbentuk item
                                    if reward_type == "Item":
                                        print(" Item :", end=" ")
                                        for index, item in enumerate(reward_value):
                                            if index > 0:
                                                print(",", end=" ")                 
                                            # Cetak nama item sesuai dengan tipe item
                                            if isinstance(item, Potion):
                                                print(item.get_name_potion(), end=" ")   
                                            elif isinstance(item, Key):
                                                print(item.get_name_key(), end=" ")      
                                            elif isinstance(item, Weapon):
                                                print(item.get_name_weapon(), end=" ")     
                                                
                                            # Jika tipe item adalah "Key", tambahkan ke inventaris
                                            if item.get_item_type() == "Key":
                                                player.get_character().get_inventory().tambah_key(item)
                                            # Jika tipe item adalah "Potion", tambahkan ke inventaris
                                            elif item.get_item_type() == "Potion":
                                                player.get_character().get_inventory().tambah_potion(item)
                                            # Jika tipe item adalah "Weapon", tambahkan ke inventaris
                                            elif item.get_item_type() == "Weapon":
                                                player.get_character().get_inventory().tambah_weapon(item)
                                        print()  
                                    # Jika reward nya berbentuk exp dan coin                                  
                                    else:
                                        print(f" {reward_type.ljust(5)}: {reward_value}")
                                        if reward_type == "EXP":
                                            get_exp = reward_value
                                        elif reward_type == "Coin":
                                            get_coin = reward_value
                                print("+-------------------------+\n")
                                # EXP dari karakter kamu bertambah
                                player.get_character().tambah_exp(get_exp)                     
                                print("Kamu telah berhasil menyelesaikan quest ini!")
                                # Uang / Coin kamu bertambah setelah menyelesaikan quest
                                player.get_character().get_inventory().tambah_coin(get_coin)  
                                # Set quest yg sudah dijalankan, berubah status 
                                selected_quest.set_status("Completed")                                   
                                
                                # Tanyakan kepada pemain apakah ingin menjalankan misi lagi
                                lanjut_misi = input("\nApakah kamu ingin menjalankan quest lagi? (yes/no): ").lower()
                                if lanjut_misi == "yes":
                                    continue  
                                else:
                                    break  
                                
                        # Jika quest tidak ditemukan
                        else:
                            print("Quest tidak ditemukan. Masukkan ID Quest yang valid.") 
                
                # Menampilkan status NPC            
                if selected_tawaran == "2":
                    print("\nSTATUS NPC")
                    print("------------------------------------------------------")
                    print("Nama     :", npc.get_name_character())
                    print("Gender   :", npc.get_gender())
                    print("Role     :", npc.get_role())
                    print("HP       :", npc.get_hp())
                    print("Defense  :", npc.get_defense())
                    print("Tipe NPC :", npc.get_NPC_type())
                    print("Domisili :", npc.get_location())
                    print("------------------------------------------------------")
                    weapon = npc.get_weapon()
                    print("Senjata Dimiliki")
                    print("- Nama Senjata :", weapon.get_name_weapon())
                    value = weapon.get_value()
                    if isinstance(value, Attack):
                        print("  Attack       :", value.get_attack())
                        print("  Damage       :", value.get_damage())
                    elif isinstance(value, Heal):
                        print("  Heal         :", value.get_heal())
                        print("  Defense      :", value.get_defense())
                    print("------------------------------------------------------")
                    print("Skill Dimiliki")  
                    for skill in npc.get_skills():
                        print("- Nama Skill   :", skill.get_name_skill())
                        value = skill.get_value()
                        if isinstance(value, Attack):
                            print("  Attack       :", value.get_attack())
                            print("  Damage       :", value.get_damage())
                        elif isinstance(value, Heal):
                            print("  Heal         :", value.get_heal())
                            print("  Defense      :", value.get_defense())
                    print("------------------------------------------------------")
                    
                # Menampilkan tawaran barang yg dijual oleh NPC
                if selected_tawaran == "3":
                    coin_saya = player.get_character().get_inventory().get_coin()
                    # Menampilkan uang agar bisa melihat barang yg dibeli cukup tidak dengan uang yg dimiliki
                    print("\n+-------------------------+")
                    print("|   Uang Kamu Sekarang    |")
                    print("+-------------------------+")
                    print("  Coin :", coin_saya)
                    print("+-------------------------+")
                    inventory = npc.get_inventory()
                    
                    # Memeriksa apakah inventory NPC kosong
                    if not inventory.get_keys() and not inventory.get_potions() and not inventory.get_weapons():
                        print(f"\n+---------------------------------------------------+")
                        print(f" {npc.get_name_character()} tidak memiliki item dalam inventory saat ini")
                        print(f"+---------------------------------------------------+")
                    # Menampilkan inventory NPC
                    else:
                        print(f"\nInventory {npc.get_name_character()}")
                        print("------------------------------------------------------")
                        
                        # Menampilkan keys
                        keys = inventory.get_keys()
                        if keys:
                            for i, key in enumerate(keys, 1):
                                print(f"{i}. {key.get_name_key()}")
                                print(f"   Tipe  : {key.get_key_type()}")
                                print(f"   Harga : {key.get_price()}")
                            print("------------------------------------------------------")

                        # Menampilkan potions
                        potions = inventory.get_potions()
                        if potions:
                            for i, potion in enumerate(potions, len(keys) + 1):
                                print(f"{i}. {potion.get_name_potion()}")
                                print(f"   Tipe  : {potion.get_potion_type()}")
                                print(f"   Harga : {potion.get_price()}")
                            print("------------------------------------------------------")

                        # Menampilkan weapons
                        weapons = inventory.get_weapons()
                        if weapons:
                            for i, weapon in enumerate(weapons, len(keys) + len(potions) + 1):
                                print(f"{i}. {weapon.get_name_weapon()}")
                                print(f"   Tipe  : {weapon.get_weapon_type()}")
                                print(f"   Harga : {weapon.get_price()}")
                            print("------------------------------------------------------")
                                        
                        # Meminta inputan untuk memilih salah satu barang yg ingin dibeli
                        select_buy_item = input("Pilih item yang ingin dibeli (1/2/3/4/5/6): ")
                        
                        # Sesuaikan untuk pengindeksan berbasis nol
                        indeks_item = int(select_buy_item) - 1  
                        
                        if indeks_item >= 0:
                            if indeks_item < len(keys):
                                # Menampung item yang dibeli yaitu "Kunci"
                                item_yang_dibeli = keys[indeks_item]
                            elif indeks_item < len(keys) + len(potions):
                                indeks_potion = indeks_item - len(keys)
                                # Menampung item yang dibeli yaitu "Potion"
                                item_yang_dibeli = potions[indeks_potion]
                            elif indeks_item < len(keys) + len(potions) + len(weapons):
                                indeks_weapon = indeks_item - len(keys) - len(potions)
                                # Menampung item yang dibeli yaitu "Senjata"
                                item_yang_dibeli = weapons[indeks_weapon]
                            else:
                                print("Item tidak ditemukan.")
                                continue  # Lanjutkan ke iterasi berikutnya

                            # Periksa apakah koin cukup:
                            if coin_saya >= item_yang_dibeli.get_price():
                                
                                # Tambahkan item yang dibeli ke inventaris Karakter kita sesuai dengan jenisnya
                                if isinstance(item_yang_dibeli, Key):
                                    player.get_character().get_inventory().tambah_key(item_yang_dibeli) 
                                    inventory.hapus_key(item_yang_dibeli)
                                    print(f"Kamu berhasil membeli {item_yang_dibeli.get_name_key()}!")
                                elif isinstance(item_yang_dibeli, Potion):
                                    player.get_character().get_inventory().tambah_potion(item_yang_dibeli)
                                    inventory.hapus_potion(item_yang_dibeli)
                                    print(f"Kamu berhasil membeli {item_yang_dibeli.get_name_potion()}!")
                                elif isinstance(item_yang_dibeli, Weapon):
                                    player.get_character().get_inventory().tambah_weapon(item_yang_dibeli)
                                    inventory.hapus_weapon(item_yang_dibeli)
                                    print(f"Kamu berhasil membeli {item_yang_dibeli.get_name_weapon()}!")
                                    
                                # Uang / Coin kamu berkurang karena membeli salah satu barang
                                coin_saya -= item_yang_dibeli.get_price()
                                # Menampilkan uang saat ini
                                print(f"Sisa koin kamu: {coin_saya}")
                                player.get_character().get_inventory().set_coin(coin_saya) 
                            else:
                                print("Uang kamu tidak cukup untuk membeli item ini.")
                        else:
                            print("Pilihan item tidak valid.")

    # Memilih untuk bertarung dengan musuh
    elif selected_action == "2":
        print("Kamu memilih untuk bertarung dengan musuh.")
        
        # Cek apakah ada musuh yang masih hidup
        ada_musuh_hidup = any(enemy.get_status() == "Hidup" for enemy in bad_npc)

        if ada_musuh_hidup:
            # Menampilkan daftar musuh
            print("\n+---------------------------+")
            print("|    Musuh yang tersedia    |")
            print("+---------------------------+")
            for enemy in bad_npc:
                if enemy.get_status() == "Hidup":
                    print(f" > {enemy.get_name_character()}")
            print("+---------------------------+")
        
            # Meminta input pemain untuk memilih musuh
            selected_enemy = input("\nPilih Musuh yang ingin diajak berantem: ")
            
            # Validasi pilihan musuh
            selected_enemy_found = False
            enemy = None
            for enemy_npc in bad_npc:
                if selected_enemy.lower() == enemy_npc.get_name_character().lower():
                    selected_enemy_found = True
                    enemy = enemy_npc
                    break

            # Jika musuh tidak ditemukan
            if not selected_enemy_found:
                print("Musuh yang dipilih tidak ditemukan. Silakan pilih musuh yang valid.")
            # Jika musuh ditemukan
            else:
                # Inisiasi pertarungan
                print(f"Mulai pertarungan dengan {enemy.get_name_character()}...")
                # Informasi tentang musuh
                print("\nINFORMASI MUSUH")
                print("------------------------------------------------------")
                print("Nama     :", enemy.get_name_character())
                print("Gender   :", enemy.get_gender())
                print("Role     :", enemy.get_role())
                print("HP       :", enemy.get_hp())
                print("Defense  :", enemy.get_defense())
                print("Tipe NPC :", enemy.get_NPC_type())
                print("Domisili :", enemy.get_location())
                print("Level Kesulitan :", enemy.get_difficulty_level())
                print("------------------------------------------------------")
                weapon = enemy.get_weapon()
                print("Senjata Dimiliki")
                print("- Nama Senjata  :", weapon.get_name_weapon())
                value = weapon.get_value()
                if isinstance(value, Attack):
                    print("  Attack        :", value.get_attack())
                    print("  Damage        :", value.get_damage())
                elif isinstance(value, Heal):
                    print("  Heal          :", value.get_heal())
                    print("  Defense       :", value.get_defense())
                print("------------------------------------------------------")
                print("Skill Dimiliki")  
                for skill in enemy.get_skills():
                    print("- Nama Skill    :", skill.get_name_skill())
                    value = skill.get_value()
                    if isinstance(value, Attack):
                        print("  Attack        :", value.get_attack())
                        print("  Damage        :", value.get_damage())
                    elif isinstance(value, Heal):
                        print("  Heal          :", value.get_heal())
                        print("  Defense       :", value.get_defense())
                print("------------------------------------------------------")
                
                # Meminta konfirmasi dari pemain untuk memulai pertarungan
                confirmation = input("\nApakah kamu yakin ingin melawan musuh ini? (yes/no): ").lower()

                if confirmation == "yes":
                    # Implementasi mekanisme pertarungan dengan jalan pertama (kamu) jalan kedua (musuh)
                    print("\n>>> Giliran karakter kamu menyerang musuh <<<")

                    # Memilih serangan menggunakan senjata atau skill
                    while True:
                        # Pilih serangan
                        attack_choice = input("\nApakah ingin menggunakan senjata atau skill? (senjata/skill): ").lower()

                        # Karakter kamu menyerang dengan senjata
                        if attack_choice == "senjata":
                            # Mendapatkan nilai serangan dari senjata karakter
                            player_attack = player.get_character().get_weapon().get_value().get_attack()
                            # Mendapatkan nilai pertahanan musuh
                            enemy_defense = enemy.get_defense()
                            
                            print("\nFight!")
                            # Implementasi serangan menggunakan senjata 
                            print(f"Karakter kamu menyerang {enemy.get_name_character()} (musuh) menggunakan senjata {player.get_character().get_weapon().get_name_weapon()} dengan attack sebesar {player_attack}")
                            print(f"{enemy.get_name_character()} (musuh) memiliki pertahanan sebesar {enemy_defense}")
                            
                            # Melakukan perhitungan untuk menentukan apakah pemain bisa melakukan hit
                            if player_attack >= enemy_defense:
                                print("\nKamu berhasil melakukan hit!")
                                # Mendapatkan nilai damage dari senjata karakter
                                player_damage = player.get_character().get_weapon().get_value().get_damage()
                                # Mengurangi HP musuh berdasarkan damage senjata karakter
                                hp_damage = enemy.get_hp() - player_damage
                                enemy.set_hp(hp_damage)
                                print(f"Kamu memberikan {player_damage} damage kepada {enemy.get_name_character()}.")
                            else:
                                print("Serangan kamu tidak cukup kuat untuk menembus pertahanan musuh.")
                            
                            if enemy.get_hp() <= 0:
                                enemy.set_hp(0)
                                
                            # Menampilkan hasil dari serangan karakter kamu
                            print("\n+-------------------------+")
                            print("|         RESULT!         |")
                            print("+-------------------------+")
                            print(" - HP Karakter :", player.get_character().get_hp())
                            print(" - HP Musuh    :", enemy.get_hp())
                            print("+-------------------------+")
                            
                            # Menyerang balik jika musuh masih hidup
                            if enemy.get_hp() > 0:
                                # Musuh juga menyerang dengan senjata
                                print("\n>>> Giliran musuh menyerang kamu <<<")

                                # Mendapatkan nilai serangan musuh
                                enemy_attack = enemy.get_weapon().get_value().get_attack()
                                # Mendapatkan nilai pertahanan karakter kamu
                                player_defense = player.get_character().get_defense()

                                print("\nFight!")
                                # Implementasi serangan musuh
                                print(f"{enemy.get_name_character()} menyerang kamu menggunakan senjata {enemy.get_weapon().get_name_weapon()} dengan attack sebesar {enemy_attack}.")
                                print(f"Karakter kamu memiliki pertahanan sebesar {player_defense}.")

                                # Melakukan perhitungan untuk menentukan apakah musuh bisa melakukan hit
                                if enemy_attack >= player_defense:
                                    print("\nMusuh berhasil melakukan hit ke kamu!")
                                    # Mendapatkan nilai damage dari senjata musuh
                                    enemy_damage = enemy.get_weapon().get_value().get_damage()
                                    # Mengurangi HP karakter kamu berdasarkan serangan musuh
                                    hp_damage = player.get_character().get_hp() - enemy_damage
                                    player.get_character().set_hp(hp_damage)
                                    print(f"{enemy.get_name_character()} memberikan {enemy_damage} damage kepada kamu.")
                                else:
                                    print("Serangan musuh tidak cukup kuat untuk menembus pertahanan kamu.")

                                if player.get_character().get_hp() <= 0:
                                    player.get_character().set_hp(0)
                                
                                # Menampilkan hasil dari serangan musuh
                                print("\n+-------------------------+")
                                print("|         RESULT!         |")
                                print("+-------------------------+")
                                print(" - HP Karakter :", player.get_character().get_hp())
                                print(" - HP Musuh    :", enemy.get_hp())
                                print("+-------------------------+")

                                # Memeriksa apakah karakter kamu masih hidup
                                if player.get_character().get_hp() <= 0:
                                    print("\nKamu kalah dalam pertarungan!")
                                    break  # Keluar dari loop karena karakter kamu sudah mati

                            # Memeriksa apakah musuh masih hidup
                            if enemy.get_hp() <= 0:
                                print(f"\nSelamat! Kamu berhasil mengalahkan {enemy.get_name_character()}!")
                                print("Sebagai hadiah kemenangan, kamu akan menerima reward yang berharga!")
                                
                                # Menampilkan reward yg diberikan ketika mengalahkan musuh
                                print("\n+-------------------------+")
                                print("|         REWARD!         |")
                                print("+-------------------------+")
                                
                                reward = enemy.get_reward()
                                for reward_type, reward_value in reward.items():
                                    # Jika yg diberikan item
                                    if reward_type == "Item":
                                        print(" Item :", end=" ")
                                        for index, item in enumerate(reward_value):
                                            if index > 0:
                                                print(",", end=" ")                 
                                            # Cetak nama item sesuai dengan tipe item
                                            if isinstance(item, Potion):
                                                print(item.get_name_potion(), end="")   
                                            elif isinstance(item, Key):
                                                print(item.get_name_key(), end="")      
                                            elif isinstance(item, Weapon):
                                                print(item.get_name_weapon(), end="")     
                                                
                                            # Jika tipe item adalah "Key", tambahkan ke inventaris
                                            if item.get_item_type() == "Key":
                                                player.get_character().get_inventory().tambah_key(item)
                                            # Jika tipe item adalah "Potion", tambahkan ke inventaris
                                            elif item.get_item_type() == "Potion":
                                                player.get_character().get_inventory().tambah_potion(item)
                                            # Jika tipe item adalah "Weapon", tambahkan ke inventaris
                                            elif item.get_item_type() == "Weapon":
                                                player.get_character().get_inventory().tambah_weapon(item)
                                        print()  
                                    # Jika yg diberikan exp dan coin                                  
                                    else:
                                        print(f" {reward_type.ljust(5)}: {reward_value}")
                                        if reward_type == "EXP":
                                            get_exp = reward_value
                                        elif reward_type == "Coin":
                                            get_coin = reward_value
                                            
                                print("+-------------------------+\n")
                                # EXP bertambah ketika sudah mengalahkan musuh
                                player.get_character().tambah_exp(get_exp)    
                                # Uang bertambah                 
                                player.get_character().get_inventory().tambah_coin(get_coin)
                                # Set status musuh jika berhasil dikalahkan
                                enemy.set_status("Mati")
                                    
                                break  # Keluar dari loop karena musuh sudah mati
                        
                        # Karakter kamu menyerang dengan skill
                        elif attack_choice == "skill":
                            # Implementasi serangan menggunakan skill 
                            print("Kamu memilih untuk menyerang dengan skill.")
                            
                            # Memeriksa apakah karakter memiliki skill
                            player_skills = player.get_character().get_skills()
                            if player_skills:
                                print("\nDaftar Skill yang Dimiliki:")
                                for index, skill in enumerate(player_skills, 1):
                                    print(f"{index}. {skill.get_name_skill()}")
                                    print(f"   Tipe   : {skill.get_skill_type()}")
                                    value = skill.get_value()
                                    # Jika skill adalah Attack
                                    if isinstance(value, Attack):
                                        print(f"   Attack : {value.get_attack()}")  # Mendapatkan nilai attack
                                        print(f"   Damage : {value.get_damage()}")  # Mendapatkan nilai damage
                                    # Jika skill adalah Heal
                                    elif isinstance(value, Heal):
                                        print(f"   Heal    : {value.get_heal()}")       # Mendapatkan nilai heal
                                        print(f"   Defense : {value.get_defense()}")    # Mendapatkan nilai defense
                                        
                                # Meminta pengguna untuk memilih skill
                                selected_skill_index = int(input("\nPilih skill yang ingin digunakan (1/2): ")) - 1

                                # Memeriksa apakah indeks yang dipilih berada dalam rentang yang valid
                                if 0 <= selected_skill_index < len(player_skills):
                                    selected_skill = player_skills[selected_skill_index]
                                    value = selected_skill.get_value()
                                    
                                    # Karakter menyerang menggunakan skill ATK
                                    if isinstance(value, Attack):
                                        # Mendapatkan nilai serangan dari skill yang dipilih karakter
                                        player_attack = value.get_attack()
                                        # Mendapatkan nilai pertahanan musuh
                                        enemy_defense = enemy.get_defense()
                                        
                                        print("\nFight!")
                                        # Implementasi serangan menggunakan skill
                                        print(f"Karakter kamu menyerang {enemy.get_name_character()} (musuh) menggunakan skill {selected_skill.get_name_skill()} dengan attack sebesar {player_attack}")
                                        print(f"{enemy.get_name_character()} (musuh) memiliki pertahanan sebesar {enemy_defense}")
                                        
                                        # Melakukan perhitungan untuk menentukan apakah pemain bisa melakukan hit
                                        if player_attack >= enemy_defense:
                                            print("\nKamu berhasil melakukan hit!")
                                            # Mendapatkan nilai damage dari skill karakter
                                            player_damage = value.get_damage()
                                            # Mengurangi HP musuh berdasarkan damage skill karakter
                                            hp_damage = enemy.get_hp() - player_damage
                                            enemy.set_hp(hp_damage)
                                            print(f"Kamu memberikan {player_damage} damage kepada {enemy.get_name_character()}.")
                                        else:
                                            print("Serangan kamu tidak cukup kuat untuk menembus pertahanan musuh.")
                                            
                                        if enemy.get_hp() <= 0:
                                            enemy.set_hp(0)
                                            
                                        # Menampilkan hasil dari serangan karakter kamu
                                        print("\n+-------------------------+")
                                        print("|         RESULT!         |")
                                        print("+-------------------------+")
                                        print(" - HP Karakter :", player.get_character().get_hp())
                                        print(" - HP Musuh    :", enemy.get_hp())
                                        print("+-------------------------+")
                                        
                                        # Menyerang balik jika musuh masih hidup
                                        if enemy.get_hp() > 0:
                                            print("\n>>> Giliran musuh menyerang kamu <<<")

                                            # Implementasi giliran musuh menyerang menggunakan skill secara bergantian
                                            enemy_skills = enemy.get_skills()
                                            if enemy_skills:
                                                # Mengambil indeks skill musuh yang akan digunakan pada giliran ini
                                                enemy_selected_skill_index = selected_skill_index
                                                
                                                # Memilih skill yang sesuai dengan indeks yang sudah ditentukan
                                                enemy_selected_skill = enemy_skills[enemy_selected_skill_index]
                                                value = enemy_selected_skill.get_value()
                                                
                                                # Musuh menyerang menggunakan skill ATK
                                                if isinstance(value, Attack):
                                                    # Mendapatkan nilai serangan dari skill musuh yang dipilih
                                                    enemy_attack = value.get_attack()
                                                    # Mendapatkan nilai pertahanan karakter kamu
                                                    player_defense = player.get_character().get_defense()
                                                    
                                                    print("\nFight!")
                                                    # Implementasi serangan musuh menggunakan skill
                                                    print(f"{enemy.get_name_character()} menyerang kamu menggunakan skill {enemy_selected_skill.get_name_skill()} dengan attack sebesar {enemy_attack}.")
                                                    print(f"Karakter kamu memiliki pertahanan sebesar {player_defense}.")
                                                    
                                                    # Melakukan perhitungan untuk menentukan apakah musuh bisa melakukan hit
                                                    if enemy_attack >= player_defense:
                                                        print("\nMusuh berhasil melakukan hit ke kamu!")
                                                        # Mendapatkan nilai damage dari skill musuh
                                                        enemy_damage = value.get_damage()
                                                        # Mengurangi HP karakter kamu berdasarkan serangan musuh
                                                        hp_damage = player.get_character().get_hp() - enemy_damage
                                                        player.get_character().set_hp(hp_damage)
                                                        print(f"{enemy.get_name_character()} memberikan {enemy_damage} damage kepada kamu.")
                                                    else:
                                                        print("Serangan musuh tidak cukup kuat untuk menembus pertahanan kamu.")

                                                    if player.get_character().get_hp() <= 0:
                                                        player.get_character().set_hp(0)
                                                    
                                                    # Menampilkan hasil dari serangan musuh
                                                    print("\n+-------------------------+")
                                                    print("|         RESULT!         |")
                                                    print("+-------------------------+")
                                                    print(" - HP Karakter :", player.get_character().get_hp())
                                                    print(" - HP Musuh    :", enemy.get_hp())
                                                    print("+-------------------------+")

                                                    # Memeriksa apakah karakter kamu masih hidup
                                                    if player.get_character().get_hp() <= 0:
                                                        print("\nKamu kalah dalam pertarungan!")
                                                        break  # Keluar dari loop karena karakter kamu sudah mati
                                                    
                                                # Musuh bertahan menggunakan skill Heal
                                                elif isinstance(value, Heal):
                                                    # Mendapatkan nilai pertahanan dari skill yang dipilih
                                                    enemy_heal = value.get_heal()
                                                    enemy_defense = value.get_defense()
                                                    
                                                    print(f"\n{enemy.get_name_character()} menggunakan skill {enemy_selected_skill.get_name_skill()} untuk menyembuhkan darah sebesar {enemy_heal}") 
                                                    print(f"sekaligus mendapatkan pertahanan sebesar {enemy_defense}.")
                                                    
                                                    # Menambahkan heal dan defense ke musuh
                                                    hp_enemy = enemy.get_hp() + enemy_heal
                                                    defense_enemy = enemy.get_defense() + enemy_defense
                                                    # Mengatur nilai hp dan defense
                                                    enemy.set_hp(hp_enemy)
                                                    enemy.set_defense(defense_enemy)
                                                    
                                                    if player.get_character().get_hp() <= 0:
                                                        player.get_character().set_hp(0)
                                                        
                                                    # Hasil dari memberi heal dari musuh
                                                    print("\n+-------------------------+")
                                                    print("|         RESULT!         |")
                                                    print("+-------------------------+")
                                                    print(" - HP Karakter :", player.get_character().get_hp())
                                                    print(" - HP Musuh    :", enemy.get_hp())
                                                    print("+-------------------------+")
                                                    
                                        # Memeriksa apakah musuh masih hidup
                                        if enemy.get_hp() <= 0:
                                            print(f"\nSelamat! Kamu berhasil mengalahkan {enemy.get_name_character()}!")
                                            print("Sebagai hadiah kemenangan, kamu akan menerima reward yang berharga!")
                                            
                                            # Menampilkan reward yg diberikan ketika mengalahkan musuh
                                            print("\n+-------------------------+")
                                            print("|         REWARD!         |")
                                            print("+-------------------------+")
                                            
                                            reward = enemy.get_reward()
                                            for reward_type, reward_value in reward.items():
                                                # Ketika yg diberikan item
                                                if reward_type == "Item":
                                                    print(" Item :", end=" ")
                                                    for index, item in enumerate(reward_value):
                                                        if index > 0:
                                                            print(",", end=" ")                 
                                                        # Cetak nama item sesuai dengan tipe item
                                                        if isinstance(item, Potion):
                                                            print(item.get_name_potion(), end="")   
                                                        elif isinstance(item, Key):
                                                            print(item.get_name_key(), end="")     
                                                        elif isinstance(item, Weapon):
                                                            print(item.get_name_weapon(), end="")     
                                                            
                                                        # Jika tipe item adalah "Key", tambahkan ke inventaris
                                                        if item.get_item_type() == "Key":
                                                            player.get_character().get_inventory().tambah_key(item)
                                                        # Jika tipe item adalah "Potion", tambahkan ke inventaris
                                                        elif item.get_item_type() == "Potion":
                                                            player.get_character().get_inventory().tambah_potion(item)
                                                        # Jika tipe item adalah "Weapon", tambahkan ke inventaris
                                                        elif item.get_item_type() == "Weapon":
                                                            player.get_character().get_inventory().tambah_weapon(item)
                                                    print()    
                                                # Ketika yg diberikan exp dan coin                                
                                                else:
                                                    print(f" {reward_type.ljust(5)}: {reward_value}")
                                                    if reward_type == "EXP":
                                                        get_exp = reward_value
                                                    elif reward_type == "Coin":
                                                        get_coin = reward_value
                                                        
                                            print("+-------------------------+\n")
                                            # EXP bertambah ketika sudah mengalahkan musuh
                                            player.get_character().tambah_exp(get_exp)    
                                            # Uang bertambah                 
                                            player.get_character().get_inventory().tambah_coin(get_coin)
                                            # Set status musuh jika berhasil dikalahkan
                                            enemy.set_status("Mati")
                                                
                                            break  # Keluar dari loop karena musuh sudah mati

                                    # Karakter bertahan menggunakan skill HEAL
                                    elif isinstance(value, Heal):
                                        # Mendapatkan nilai pertahanan dari skill yang dipilih
                                        player_heal = value.get_heal()
                                        player_defense = value.get_defense()
                                        
                                        print(f"\nAnda menggunakan skill {selected_skill.get_name_skill()} untuk menyembuhkan darah sebesar {player_heal}") 
                                        print(f"sekaligus mendapatkan pertahanan sebesar {player_defense}.")
                                        
                                        # Menambahkan heal dan defense ke karakter
                                        hp_player = player.get_character().get_hp() + player_heal
                                        defense_player = player.get_character().get_defense() + player_defense
                                        # Mengatur nilai hp dan defense
                                        player.get_character().set_hp(hp_player)
                                        player.get_character().set_defense(defense_player)
                                        
                                        if enemy.get_hp() <= 0:
                                            enemy.set_hp(0)
                                            
                                        # Hasil dari memberi heal dari karakter kamu
                                        print("\n+-------------------------+")
                                        print("|         RESULT!         |")
                                        print("+-------------------------+")
                                        print(" - HP Karakter :", player.get_character().get_hp())
                                        print(" - HP Musuh    :", enemy.get_hp())
                                        print("+-------------------------+")
                                        
                                        # Menyerang balik jika musuh masih hidup
                                        if enemy.get_hp() > 0:
                                            print("\n>>> Giliran musuh menyerang kamu <<<")

                                            # Implementasi giliran musuh menyerang menggunakan skill secara bergantian
                                            enemy_skills = enemy.get_skills()
                                            if enemy_skills:
                                                # Mengambil indeks skill musuh yang akan digunakan pada giliran ini
                                                enemy_selected_skill_index = selected_skill_index
                                                
                                                # Memilih skill yang sesuai dengan indeks yang sudah ditentukan
                                                enemy_selected_skill = enemy_skills[enemy_selected_skill_index]
                                                value = enemy_selected_skill.get_value()
                                                
                                                # Musuh menyerang menggunakan skill ATK
                                                if isinstance(value, Attack):
                                                    # Mendapatkan nilai serangan dari skill musuh yang dipilih
                                                    enemy_attack = value.get_attack()
                                                    # Mendapatkan nilai pertahanan karakter kamu
                                                    player_defense = player.get_character().get_defense()
                                                    
                                                    print("\nFight!")
                                                    # Implementasi serangan musuh menggunakan skill
                                                    print(f"{enemy.get_name_character()} menyerang kamu menggunakan skill {enemy_selected_skill.get_name_skill()} dengan attack sebesar {enemy_attack}.")
                                                    print(f"Karakter kamu memiliki pertahanan sebesar {player_defense}.")
                                                    
                                                    # Melakukan perhitungan untuk menentukan apakah musuh bisa melakukan hit
                                                    if enemy_attack >= player_defense:
                                                        print("\nMusuh berhasil melakukan hit ke kamu!")
                                                        # Mendapatkan nilai damage dari skill musuh
                                                        enemy_damage = value.get_damage()
                                                        # Mengurangi HP karakter kamu berdasarkan serangan musuh
                                                        hp_damage = player.get_character().get_hp() - enemy_damage
                                                        player.get_character().set_hp(hp_damage)
                                                        print(f"{enemy.get_name_character()} memberikan {enemy_damage} damage kepada kamu.")
                                                    else:
                                                        print("Serangan musuh tidak cukup kuat untuk menembus pertahanan kamu.")

                                                    if player.get_character().get_hp() <= 0:
                                                        player.get_character().set_hp(0)
                                                    
                                                    # Hasil dari serangan musuh
                                                    print("\n+-------------------------+")
                                                    print("|         RESULT!         |")
                                                    print("+-------------------------+")
                                                    print(" - HP Karakter :", player.get_character().get_hp())
                                                    print(" - HP Musuh    :", enemy.get_hp())
                                                    print("+-------------------------+")

                                                    # Memeriksa apakah karakter kamu masih hidup
                                                    if player.get_character().get_hp() <= 0:
                                                        print("\nKamu kalah dalam pertarungan!")
                                                        break  # Keluar dari loop karena karakter kamu sudah mati
                                                    
                                                # Musuh bertahan menggunakan skill HEAL
                                                elif isinstance(value, Heal):
                                                    # Mendapatkan nilai pertahanan dari skill yang dipilih
                                                    enemy_heal = value.get_heal()
                                                    enemy_defense = value.get_defense()
                                                    
                                                    print(f"\n{enemy.get_name_character()} menggunakan skill {enemy_selected_skill.get_name_skill()} untuk menyembuhkan darah sebesar {enemy_heal}") 
                                                    print(f"sekaligus mendapatkan pertahanan sebesar {enemy_defense}.")
                                                    
                                                    # Menambahkan heal dan defense ke musuh
                                                    hp_enemy = enemy.get_hp() + enemy_heal
                                                    defense_enemy = enemy.get_defense() + enemy_defense
                                                    # Mengatur nilai hp dan defense
                                                    enemy.set_hp(hp_enemy)
                                                    enemy.set_defense(defense_enemy)
                                                    
                                                    if player.get_character().get_hp() <= 0:
                                                        player.get_character().set_hp(0)
                                                        
                                                    # Hasil dari memberi heal dari musuh
                                                    print("\n+-------------------------+")
                                                    print("|         RESULT!         |")
                                                    print("+-------------------------+")
                                                    print(" - HP Karakter :", player.get_character().get_hp())
                                                    print(" - HP Musuh    :", enemy.get_hp())
                                                    print("+-------------------------+")
                                # Skill yg dipilih salah
                                else:
                                    print("Pilihan skill tidak valid.")
                            # Jika tidak punya skill              
                            else:
                                print("\nKarakter kamu tidak memiliki skill.")
                                print("Silahkan memilih serangan menggunakan senjata!")
                        # Hanya bisa input "senjata" dan "skill"
                        else:
                            print("Pilihan tidak valid. Silakan pilih antara senjata atau skill.")
                # Jika tidak ingin bertanding dengan musuh                            
                elif confirmation == "no":
                    print("Pertarungan dibatalkan.")    
                else:
                    print("Pilihan tidak valid. Pertarungan dibatalkan.")
        else:
            # Jika tidak ada musuh yang hidup, tampilkan pesan
            print("\n+-----------------------------------------+")
            print(" Tidak ada musuh yang tersedia saat ini. ")
            print("+-----------------------------------------+")
        
    # Menampilkan status karakter kamu
    elif selected_action == "3":
        print("Kamu memilih untuk melihat status karakter.")
        # Tambahkan logika untuk melihat status karakter di sini
        print("\nSTATUS SAYA")
        print("------------------------------------------------------")
        print("Nama     :", player.get_character().get_name_character())
        print("Gender   :", player.get_character().get_gender())
        print("Role     :", player.get_character().get_role())
        print("HP       :", player.get_character().get_hp())
        print("Defense  :", player.get_character().get_defense())
        print("Level    :", player.get_character().get_level())
        print(f"EXP      : {player.get_character().get_exp()} / 100")
        print("------------------------------------------------------")
        weapon = player.get_character().get_weapon()
        print("Senjata Dimiliki")
        print("- Nama Senjata :", weapon.get_name_weapon())
        value = weapon.get_value()
        if isinstance(value, Attack):
            print("  Attack       :", value.get_attack())
            print("  Damage       :", value.get_damage())
        elif isinstance(value, Heal):
            print("  Heal         :", value.get_heal())
            print("  Defense      :", value.get_defense())
        print("------------------------------------------------------")
        print("Skill Dimiliki")  
        for skill in player.get_character().get_skills():
            print("- Nama Skill   :", skill.get_name_skill())
            value = skill.get_value()
            if isinstance(value, Attack):
                print("  Attack       :", value.get_attack())
                print("  Damage       :", value.get_damage())
            elif isinstance(value, Heal):
                print("  Heal         :", value.get_heal())
                print("  Defense      :", value.get_defense())
        print("------------------------------------------------------")
    
    # Menampilkan inventory / barang yg dimiliki karakter kamu
    elif selected_action == "4":
        print("Kamu memilih untuk melihat inventory karakter.")
        
        # Menampilkan uang yg dimiliki dalam inventory
        coin_saya = player.get_character().get_inventory().get_coin()
        print("\n+-------------------------+")
        print("|        Uang Saya        |")
        print("+-------------------------+")
        print("  Coin :", coin_saya)
        print("+-------------------------+")
        
        inventory = player.get_character().get_inventory()
        # Memeriksa apakah inventory Saya kosong
        if not inventory.get_keys() and not inventory.get_potions() and not inventory.get_weapons():
            print("\n+---------------------------------------------------+")
            print(f" {player.get_character().get_name_character()} tidak memiliki item dalam inventory saat ini")
            print("+---------------------------------------------------+")
        # Menampilkan seluruh barang dalam inventory
        else:
            print("\nINVENTORY SAYA")
            print("------------------------------------------------------")
            # Menampilkan keys
            keys = inventory.get_keys()
            if keys:
                for i, key in enumerate(keys, 1):
                    print(f"{i}. {key.get_name_key()}")
                    print(f"   Tipe  : {key.get_key_type()}")
                    print(f"   Harga : {key.get_price()}")
                print("------------------------------------------------------")

            # Menampilkan potions
            potions = inventory.get_potions()
            if potions:
                for i, potion in enumerate(potions, len(keys) + 1):
                    print(f"{i}. {potion.get_name_potion()}")
                    print(f"   Tipe  : {potion.get_potion_type()}")
                    print(f"   Harga : {potion.get_price()}")
                print("------------------------------------------------------")

            # Menampilkan weapons
            weapons = inventory.get_weapons()
            if weapons:
                for i, weapon in enumerate(weapons, len(keys) + len(potions) + 1):
                    print(f"{i}. {weapon.get_name_weapon()}")
                    print(f"   Tipe  : {weapon.get_weapon_type()}")
                    print(f"   Harga : {weapon.get_price()}")
                print("------------------------------------------------------")
                
    # Keluar game
    elif selected_action == "5":
        print("Kamu memilih untuk keluar dari permainan.")
        print("\n+---------------------------------------------------+")
        print("  Terima kasih telah merasakan keajaiban dunia ini.")
        print("  Semoga kita bertemu lagi!")
        print("+---------------------------------------------------+")
        break  # Keluar dari perulangan while
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

            
            

