# Fitur .append()
print(">>> Fitur .append()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)
# Fitur .clear()
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)
# Fitur .copy()
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan1)
print(list_makanan2)
# Fitur .count()
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3
# Fitur .extend()
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)


# index,insert,pop,remove,sort,



# tentang set => union, isdisjoint, issubset, issuperset, intersection, differencem symmetric_difference
  
  print(">>> Fitur .union()")
  parcel1 = {'Anggur','Apel','Jeruk'}
  parcel2 = {'Apel','Kiwi','Melon'}
  parcel3 = parcel1.union(parcel2)
  print(parcel1)
  print(parcel3)

  # Fitur .isdisjoint()
  print(">>> Fitur .isdisjoint()")
  parcel1 = {'Anggur','Apel','Jeruk'}
  parcel2 = {'Kiwi','Melon','Pisang'}
  parcel3 = {'Apel','Srikaya','Semangka'}
  parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
  print(parcel1_parcel2_disjoint)
  parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
  print(parcel1_parcel3_disjoint)

  # Fitur .issubset()
  print(">>> Fitur .issubset()")
  parcel_A = {'Anggur', 'Apel'}
  parcel_B = {'Durian','Semangka','Apel'}
  parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
  parcel_A_dalam_C = parcel_A.issubset(parcel_C)
  parcel_B_dalam_C = parcel_B.issubset(parcel_C)
  print(parcel_A_dalam_C)
  print(parcel_B_dalam_C)
  # Fitur .issuperset()
  print(">>> Fitur .issuperset()")
  parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
  parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
  print(parcel_C_mengandung_A)
  print(parcel_C_mengandung_B)

  # Fitur .intersection()
  print(">>> Fitur .intersection()")
  parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
  parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
  parcel_C = parcel_A.intersection(parcel_B)
  print(parcel_C)


  # Fitur .difference()
  print(">>> Fitur .difference()")
  parcel_C = parcel_A.difference(parcel_B)
  print(parcel_C)
  # Fitur .symmetric_difference()
  print(">>> Fitur .symmetric_difference()")
  parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
  parcel_B = {'Apel','Jeruk','Semangka','Leci'}
  parcel_C = parcel_A.symmetric_difference(parcel_B)
  print(parcel_C)



