from django.db import models

class Siswa(models.Model):
    # Di bawah ini adalah contoh kolom/field tabelnya, silakan sesuaikan dengan kebutuhanmu
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50)

    class Meta:
        db_table = 'siswa'  # Ini wajib supaya nama tabel di database murni bernama "siswa"