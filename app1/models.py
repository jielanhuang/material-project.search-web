# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Calculations(models.Model):
    configuration = models.CharField(max_length=15, blank=True, null=True)
    label = models.CharField(max_length=63)
    # entry = models.ForeignKey('Entries', models.DO_NOTHING, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    composition = models.ForeignKey('Compositions', models.DO_NOTHING, blank=True, null=True)
    natoms = models.IntegerField(blank=True, null=True)
    # input = models.ForeignKey('Structures', models.DO_NOTHING, blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    # output = models.ForeignKey('Structures', models.DO_NOTHING, blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    energy_pa = models.FloatField(blank=True, null=True)
    magmom = models.FloatField(blank=True, null=True)
    magmom_pa = models.FloatField(blank=True, null=True)
    # dos = models.ForeignKey('Dos', models.DO_NOTHING, blank=True, null=True)
    band_gap = models.FloatField(blank=True, null=True)
    irreducible_kpoints = models.FloatField(blank=True, null=True)
    attempt = models.IntegerField(blank=True, null=True)
    nsteps = models.IntegerField(blank=True, null=True)
    converged = models.IntegerField(blank=True, null=True)
    runtime = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculations'


class Compositions(models.Model):
    formula = models.CharField(primary_key=True, max_length=255)
    generic = models.CharField(max_length=255, blank=True, null=True)
    ntypes = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    meidema = models.FloatField(blank=True, null=True)
    # structure = models.ForeignKey('Structures', models.DO_NOTHING, blank=True, null=True)
    element_list = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compositions'


