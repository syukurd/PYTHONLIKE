keuangan = {'pengeluaran' : [4,34,5,5,65,7,78,54,34],
'pemasukan' : [3,5,7,5,4,6,3,6,7]
}

total_pengeluaran = 0
total_pemasukan = 0

for i in keuangan['pengeluaran'] :
    total_pengeluaran += i
for i in keuangan['pemasukan'] :
    total_pemasukan += i

rata_pengeluaran = total_pengeluaran / len(keuangan['pengeluaran'])
rata_pemasukan = total_pemasukan/ len(keuangan['pemasukan'])

print(rata_pengeluaran)
print(rata_pemasukan)
