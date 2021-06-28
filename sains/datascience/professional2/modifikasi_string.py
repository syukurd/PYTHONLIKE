# Fitur .split()
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)
# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)


# Fitur .replace()
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel","jeruk")
print(kalimat)

teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
print(">>> Fitur .find()")
print(teks.find("Apel"))
print(teks.find("malang"))
# Fitur .count()
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel)



# Fitur .startswith()
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
# Fitur .endswith()
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))