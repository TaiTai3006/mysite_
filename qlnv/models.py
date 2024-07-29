from django.db import models

class NhanVien(models.Model):
    ma_nhan_vien = models.CharField(max_length=10, unique=True)
    ho_ten_nhan_vien = models.CharField(max_length=100)
    luong_co_ban = models.IntegerField()
    loai_nhan_vien = models.CharField(max_length=10)
    luong_hang_thang = models.IntegerField()

    def tinhluong(self, *args, **kwargs):
        print('hgchgsdf')
        if self.loai_nhan_vien == 'kinhdoanh':
            self.luong_hang_thang = self.luong_co_ban * 2
        else:
            self.luong_hang_thang = self.luong_co_ban * 1.5
        super().save(*args, **kwargs)

    class Meta:  
        db_table = "tbl_nhavien"