class Karyawan :
    nama_perusahaan = "AC"
perusahaanAnji = Karyawan()
print(perusahaanAnji.__class__.nama_perusahaan)
perusahaanAnji.__class__.nama_perusahaan = "Babelonia"
print(perusahaanAnji.__class__.nama_perusahaan)



class Tengah :
    def __init__(self,nama,email,gaji) -> None:
        self.nama = nama
        self.email = email
        self.gaji = gaji
syukur = Tengah('Syukur','syukur@gmail.com',1300000)
print(syukur.nama + ' ' + syukur.email + ' ' + str(syukur.gaji))
