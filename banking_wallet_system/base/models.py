# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    accountid = models.BigAutoField(db_column='accountID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    accountnumber = models.CharField(db_column='accountNumber', unique=True, max_length=50)  # Field name made lowercase.
    accounttype = models.CharField(db_column='accountType', max_length=10)  # Field name made lowercase.
    balance = models.DecimalField(max_digits=20, decimal_places=4)
    status = models.CharField(max_length=10)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts'


class Auditlog(models.Model):
    logid = models.BigAutoField(db_column='logID', primary_key=True)  # Field name made lowercase.
    entityname = models.CharField(db_column='entityName', max_length=50)  # Field name made lowercase.
    entityid = models.BigIntegerField(db_column='entityID')  # Field name made lowercase.
    action = models.CharField(max_length=50)
    performedby = models.BigIntegerField(db_column='performedBy')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditlog'


class Ledgerentries(models.Model):
    ledgerid = models.BigAutoField(db_column='ledgerID', primary_key=True)  # Field name made lowercase.
    transactionid = models.ForeignKey('Transactions', models.DO_NOTHING, db_column='transactionID')  # Field name made lowercase.
    accountid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='accountID')  # Field name made lowercase.
    entrytype = models.CharField(db_column='entryType', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=20, decimal_places=5)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ledgerentries'


class Transactions(models.Model):
    transactionid = models.BigAutoField(db_column='transactionID', primary_key=True)  # Field name made lowercase.
    fromaccountid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='fromAccountID')  # Field name made lowercase.
    toaccountid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='toAccountID', related_name='transactions_toaccountid_set')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transactiontype = models.CharField(db_column='transactionType', max_length=10)  # Field name made lowercase.
    statusid = models.ForeignKey('Transactionstatus', models.DO_NOTHING, db_column='statusID')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactions'


class Transactionstatus(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    statusname = models.CharField(db_column='statusName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactionstatus'


class Users(models.Model):
    userid = models.BigAutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)
    phone = models.CharField(unique=True, max_length=10)
    status = models.CharField(max_length=10)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
