from django.db import models

class District(models.Model):
    Id = models.AutoField(primary_key=True, db_column='DistrictID')
    DistrictCode = models.CharField(max_length=50,db_column='DistrictCode')
    DistrictName = models.CharField(max_length=100,db_column='DistrictName', null=False)
    DivisionId = models.IntegerField(db_column='DivisionID', null=False)

    class Meta:
        managed = False
        db_table = 'district'

    def __str__(self):
        return '{}, {}'.format(self.Id, self.DistrictName)


class FairEntryPoint(models.Model):
    Id = models.AutoField(primary_key=True, db_column='Id')
    ImagePath = models.CharField(max_length=250,db_column='ImagePath')
    Gender = models.CharField(max_length=10, db_column='Gender')
    AgeLow = models.FloatField(db_column='AgeLow')
    AgeHigh = models.FloatField(db_column='AgeHigh')
    EmotionCalm = models.FloatField(db_column='EmotionCalm')
    EmotionHappy = models.FloatField(db_column='EmotionHappy')
    EmotionSurprised = models.FloatField(db_column='EmotionSurprised')
    EmotionSad = models.FloatField(db_column='EmotionSad')
    EntryDate = models.DateTimeField()
    Smile = models.CharField(max_length=10, db_column='Smile')
    Eyeglasses = models.CharField(max_length=10, db_column='Eyeglasses')
    Sunglasses = models.CharField(max_length=10, db_column='Sunglasses')
    Beard = models.CharField(max_length=10, db_column='Beard')
    Mustache = models.CharField(max_length=10, db_column='Mustache')

    class Meta:
        managed = False
        db_table = 'FairEntryPoint'

