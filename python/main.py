#   Funksiya

# def salom_ber():
# 	"""Salom beruvchi funksiya."""
# 	print("Salom, dunyo!")	

# salom_ber()   
# # har bir funksiyani ichida funksiya haqida ma'lumot bo'ladi Docstring degan misol yuqorida """Salom beruvchi funksiya.""" deb yozilgan ga oxshash va shu malumotni boshqa dasturchilar qanday koradi 2 ta yuli bor:
# # 1. help(salom_ber) - bu funksiya haqida ma'lumot
# # 2. salom_ber.__doc__ - bu funksiya haqida ma'lumot
# # 3. Salom_ber() shu ikki qavus ichiga mishkani qoysangiz malumotlarni korasiz
# help(salom_ber)  # funksiya haqida ma'lumot
# salom_ber.__doc__  # funksiya haqida ma'lumot

# def salom_ber(ism):
# 	"""Foydalanuvchi ismini qabul qilib, salom beradi."""
# 	print(f"Salom, {ism.title()}!")

# salom_ber("ali")  # Foydalanuvchi ismini kiritamiz
# salom_ber("vali")  # Boshqa foydalanuvchi ismini kiritamiz

# def toliq_ism(ism, familiya):
# 	"""Foydalanuvchi ismi va familiyasini qabul qilib, to'liq ismni qaytaradi."""
# 	print(f"Foydalanuvchi ismi: {ism.title()}\nFoydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism("ali", "valiyev")  # Foydalanuvchi ismi va familiyasini kiritamiz
# toliq_ism("vali", "qodirov")  # Boshqa foydalanuvchi ismi va familiyasini kiritamiz	

# def yosh_hisobla(ism, tugilgan_yil):
# 	"""Foydalanuvchi ismi va tug'ilgan yilini qabul qilib, yoshini hisoblaydi."""
# 	yosh = 2025 - tugilgan_yil  # Hozirgi yil 2025 deb olamiz
# 	print(f"{ism.title()}ning yoshi: - {2025-tugilgan_yil}da")

# yosh_hisobla(tugilgan_yil=2000, ism='ali')  # Foydalanuvchi ismi va tug'ilgan yilini kiritamiz
# yosh_hisobla(ism='umar', tugilgan_yil=1994)  # Boshqa foydalanuvchi ismi va tug'ilgan yilini kiritamiz

# def yosh_hisoblaa(tugilgan_yil, joriy_yil=2025):
# 	"""Foydalanuvchi tug'ilgan yilini qabul qilib, yoshini hisoblaydi."""
# 	print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz.")

# yosh_hisoblaa(2000)  # Foydalanuvchi tug'ilgan yilini kiritamiz

