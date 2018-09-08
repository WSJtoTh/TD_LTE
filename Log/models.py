
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tbatuc2I(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell_id = models.CharField(db_column='NCELL_ID', max_length=50)  # Field name made lowercase.
    ratio_all = models.FloatField(db_column='RATIO_ALL', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    cosite = models.SmallIntegerField(db_column='COSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUC2I'
        unique_together = (('sector_id', 'ncell_id'),)


class Tbatudata(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    cellid = models.CharField(db_column='CellID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    pci = models.SmallIntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    rsrp = models.FloatField(db_column='RSRP', blank=True, null=True)  # Field name made lowercase.
    rs_sinr = models.FloatField(db_column='RS_SINR', blank=True, null=True)  # Field name made lowercase.
    ncell_id_1 = models.CharField(db_column='NCell_ID_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_1 = models.IntegerField(db_column='NCell_EARFCN_1', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_1 = models.SmallIntegerField(db_column='NCell_PCI_1', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_1 = models.FloatField(db_column='NCell_RSRP_1', blank=True, null=True)  # Field name made lowercase.
    ncell_id_2 = models.CharField(db_column='NCell_ID_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_2 = models.IntegerField(db_column='NCell_EARFCN_2', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_2 = models.SmallIntegerField(db_column='NCell_PCI_2', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_2 = models.FloatField(db_column='NCell_RSRP_2', blank=True, null=True)  # Field name made lowercase.
    ncell_id_3 = models.CharField(db_column='NCell_ID_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_3 = models.IntegerField(db_column='NCell_EARFCN_3', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_3 = models.SmallIntegerField(db_column='NCell_PCI_3', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_3 = models.FloatField(db_column='NCell_RSRP_3', blank=True, null=True)  # Field name made lowercase.
    ncell_id_4 = models.CharField(db_column='NCell_ID_4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_4 = models.IntegerField(db_column='NCell_EARFCN_4', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_4 = models.SmallIntegerField(db_column='NCell_PCI_4', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_4 = models.FloatField(db_column='NCell_RSRP_4', blank=True, null=True)  # Field name made lowercase.
    ncell_id_5 = models.CharField(db_column='NCell_ID_5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_5 = models.IntegerField(db_column='NCell_EARFCN_5', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_5 = models.SmallIntegerField(db_column='NCell_PCI_5', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_5 = models.FloatField(db_column='NCell_RSRP_5', blank=True, null=True)  # Field name made lowercase.
    ncell_id_6 = models.CharField(db_column='NCell_ID_6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_6 = models.IntegerField(db_column='NCell_EARFCN_6', blank=True, null=True)  # Field name made lowercase.
    ncell_pci_6 = models.SmallIntegerField(db_column='NCell_PCI_6', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_6 = models.FloatField(db_column='NCell_RSRP_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUData'
        unique_together = (('seq', 'filename'),)


class Tbatuhandover(models.Model):
    ssector_id = models.CharField(db_column='SSECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    nsector_id = models.CharField(db_column='NSECTOR_ID', max_length=50)  # Field name made lowercase.
    hoatt = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUHandOver'
        unique_together = (('ssector_id', 'nsector_id'),)


class Tbadjcell(models.Model):
    s_sector_id = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.
    s_earfcn = models.IntegerField(db_column='S_EARFCN', blank=True, null=True)  # Field name made lowercase.
    n_earfcn = models.IntegerField(db_column='N_EARFCN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbAdjCell'
        unique_together = (('s_sector_id', 'n_sector_id'),)


class Tbc2I(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.ForeignKey('Tbcell', models.DO_NOTHING, db_column='SCELL', primary_key=True)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=255)  # Field name made lowercase.
    prc2i9 = models.FloatField(db_column='PrC2I9', blank=True, null=True)  # Field name made lowercase.
    c2i_mean = models.FloatField(db_column='C2I_Mean', blank=True, null=True)  # Field name made lowercase.
    std = models.FloatField(db_column='Std', blank=True, null=True)  # Field name made lowercase.
    samplecount = models.FloatField(db_column='SampleCount', blank=True, null=True)  # Field name made lowercase.
    weightedc2i = models.FloatField(db_column='WeightedC2I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2I'
        unique_together = (('scell', 'ncell'),)


class Tbc2I3(models.Model):
    a_sector_id = models.CharField(db_column='A_sector_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    b_sector_id = models.CharField(db_column='B_sector_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_sector_id = models.CharField(db_column='C_sector_id', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2I3'


class Tbc2Inew(models.Model):
    scell = models.CharField(db_column='SCELL', max_length=255)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=255)  # Field name made lowercase.
    c2i_mean = models.FloatField(db_column='C2I_mean', blank=True, null=True)  # Field name made lowercase.
    std = models.FloatField(blank=True, null=True)
    prbc2i9 = models.FloatField(db_column='PrbC2I9', blank=True, null=True)  # Field name made lowercase.
    prbabs6 = models.FloatField(db_column='PrbABS6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2INew'


class Tbcell(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=255)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN')  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    azimuth = models.FloatField(db_column='AZIMUTH')  # Field name made lowercase.
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    electtilt = models.FloatField(db_column='ELECTTILT', blank=True, null=True)  # Field name made lowercase.
    mechtilt = models.FloatField(db_column='MECHTILT', blank=True, null=True)  # Field name made lowercase.
    totletilt = models.FloatField(db_column='TOTLETILT')  # Field name made lowercase.
    enodebid = models.IntegerField(db_column='ENODEBID')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    vendor = models.CharField(db_column='VENDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE')  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE')  # Field name made lowercase.
    style = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbCell'


class Tbhandover(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.CharField(db_column='SCELL', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=50)  # Field name made lowercase.
    hoatt = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.
    hosucc = models.IntegerField(db_column='HOSUCC', blank=True, null=True)  # Field name made lowercase.
    hosuccrate = models.DecimalField(db_column='HOSUCCRATE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbHandOver'
        unique_together = (('scell', 'ncell'),)


class Tbkpi(models.Model):
    starttime = models.DateField(db_column='startTime', primary_key=True)  # Field name made lowercase.
    turnround = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    cell_multi = models.CharField(max_length=255)
    cell = models.CharField(max_length=50, blank=True, null=True)
    suc_time = models.IntegerField(blank=True, null=True)
    req_time = models.IntegerField(blank=True, null=True)
    rrc_suc_rate = models.FloatField(db_column='RRC_suc_rate', blank=True, null=True)  # Field name made lowercase.
    suc_total = models.IntegerField(blank=True, null=True)
    try_total = models.IntegerField(blank=True, null=True)
    e_rab_suc_rate = models.FloatField(db_column='E_RAB_suc_rate', blank=True, null=True)  # Field name made lowercase.
    enodeb_exception = models.IntegerField(db_column='eNodeB_exception', blank=True, null=True)  # Field name made lowercase.
    cell_exception = models.IntegerField(blank=True, null=True)
    e_rab_offline = models.FloatField(db_column='E_RAB_offline', blank=True, null=True)  # Field name made lowercase.
    ay = models.FloatField(blank=True, null=True)
    enodeb_release_time = models.IntegerField(blank=True, null=True)
    ue_context_exception_time = models.IntegerField(db_column='UE_Context_exception_time', blank=True, null=True)  # Field name made lowercase.
    ue_context_suc_time = models.IntegerField(db_column='UE_Context_suc_time', blank=True, null=True)  # Field name made lowercase.
    wifi_offline_rate = models.FloatField(blank=True, null=True)
    t_field = models.IntegerField(db_column='t_', blank=True, null=True)  # Field renamed because it ended with '_'.
    u_field = models.IntegerField(db_column='u_', blank=True, null=True)  # Field renamed because it ended with '_'.
    v_field = models.IntegerField(db_column='v_', blank=True, null=True)  # Field renamed because it ended with '_'.
    w_field = models.IntegerField(db_column='w_', blank=True, null=True)  # Field renamed because it ended with '_'.
    x_field = models.IntegerField(db_column='x_', blank=True, null=True)  # Field renamed because it ended with '_'.
    y_field = models.IntegerField(db_column='y_', blank=True, null=True)  # Field renamed because it ended with '_'.
    z_field = models.IntegerField(db_column='z_', blank=True, null=True)  # Field renamed because it ended with '_'.
    aa_field = models.IntegerField(db_column='aa_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ab_field = models.FloatField(db_column='ab_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ac_field = models.FloatField(db_column='ac_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ad_field = models.FloatField(db_column='ad_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ae_field = models.FloatField(db_column='ae_', blank=True, null=True)  # Field renamed because it ended with '_'.
    af_field = models.FloatField(db_column='af_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ag_field = models.BigIntegerField(db_column='ag_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ah_field = models.BigIntegerField(db_column='ah_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ai_field = models.IntegerField(db_column='ai_', blank=True, null=True)  # Field renamed because it ended with '_'.
    aj_field = models.FloatField(db_column='aj_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ak_field = models.IntegerField(db_column='ak_', blank=True, null=True)  # Field renamed because it ended with '_'.
    al_field = models.IntegerField(db_column='al_', blank=True, null=True)  # Field renamed because it ended with '_'.
    am_field = models.IntegerField(db_column='am_', blank=True, null=True)  # Field renamed because it ended with '_'.
    an_field = models.IntegerField(db_column='an_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ao_field = models.IntegerField(db_column='ao_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ap_field = models.IntegerField(db_column='ap_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'tbKPI'
        unique_together = (('starttime', 'cell_multi'),)


class Tbmrodata(models.Model):
    timestamp = models.CharField(db_column='TimeStamp', primary_key=True, max_length=30)  # Field name made lowercase.
    servingsector = models.CharField(db_column='ServingSector', max_length=255)  # Field name made lowercase.
    interferingsector = models.CharField(db_column='InterferingSector', max_length=50)  # Field name made lowercase.
    ltescrsrp = models.IntegerField(db_column='LteScRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencrsrp = models.IntegerField(db_column='LteNcRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencearfcn = models.IntegerField(db_column='LteNcEarfcn', blank=True, null=True)  # Field name made lowercase.
    ltencpci = models.SmallIntegerField(db_column='LteNcPci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbMROData'
        unique_together = (('timestamp', 'servingsector', 'interferingsector'),)


class Tboptcell(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    cell_type = models.CharField(db_column='CELL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbOptCell'


class Tbpciassignment(models.Model):
    assign_id = models.AutoField(db_column='ASSIGN_ID', primary_key=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', max_length=200)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    enbodeb_id = models.IntegerField(db_column='ENBODEB_ID', blank=True, null=True)  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(max_length=50, blank=True, null=True)
    opt_datetime = models.DateTimeField(db_column='OPT_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPCIAssignment'
        unique_together = (('assign_id', 'sector_id'),)


class Tbprb(models.Model):
    starttime = models.DateTimeField(db_column='startTime', primary_key=True)  # Field name made lowercase.
    turnround = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    cell = models.CharField(max_length=255)
    cell_name = models.CharField(max_length=50, blank=True, null=True)
    prb0 = models.FloatField(db_column='PRB0', blank=True, null=True)  # Field name made lowercase.
    prb1 = models.FloatField(db_column='PRB1', blank=True, null=True)  # Field name made lowercase.
    prb2 = models.FloatField(db_column='PRB2', blank=True, null=True)  # Field name made lowercase.
    prb3 = models.FloatField(db_column='PRB3', blank=True, null=True)  # Field name made lowercase.
    prb4 = models.FloatField(db_column='PRB4', blank=True, null=True)  # Field name made lowercase.
    prb5 = models.FloatField(db_column='PRB5', blank=True, null=True)  # Field name made lowercase.
    prb6 = models.FloatField(db_column='PRB6', blank=True, null=True)  # Field name made lowercase.
    prb7 = models.FloatField(db_column='PRB7', blank=True, null=True)  # Field name made lowercase.
    prb8 = models.FloatField(db_column='PRB8', blank=True, null=True)  # Field name made lowercase.
    prb9 = models.FloatField(db_column='PRB9', blank=True, null=True)  # Field name made lowercase.
    prb10 = models.FloatField(db_column='PRB10', blank=True, null=True)  # Field name made lowercase.
    prb11 = models.FloatField(db_column='PRB11', blank=True, null=True)  # Field name made lowercase.
    prb12 = models.FloatField(db_column='PRB12', blank=True, null=True)  # Field name made lowercase.
    prb13 = models.FloatField(db_column='PRB13', blank=True, null=True)  # Field name made lowercase.
    prb14 = models.FloatField(db_column='PRB14', blank=True, null=True)  # Field name made lowercase.
    prb15 = models.FloatField(db_column='PRB15', blank=True, null=True)  # Field name made lowercase.
    prb16 = models.FloatField(db_column='PRB16', blank=True, null=True)  # Field name made lowercase.
    prb17 = models.FloatField(db_column='PRB17', blank=True, null=True)  # Field name made lowercase.
    prb18 = models.FloatField(db_column='PRB18', blank=True, null=True)  # Field name made lowercase.
    prb19 = models.FloatField(db_column='PRB19', blank=True, null=True)  # Field name made lowercase.
    prb20 = models.FloatField(db_column='PRB20', blank=True, null=True)  # Field name made lowercase.
    prb21 = models.FloatField(db_column='PRB21', blank=True, null=True)  # Field name made lowercase.
    prb22 = models.FloatField(db_column='PRB22', blank=True, null=True)  # Field name made lowercase.
    prb23 = models.FloatField(db_column='PRB23', blank=True, null=True)  # Field name made lowercase.
    prb24 = models.FloatField(db_column='PRB24', blank=True, null=True)  # Field name made lowercase.
    prb25 = models.FloatField(db_column='PRB25', blank=True, null=True)  # Field name made lowercase.
    prb26 = models.FloatField(db_column='PRB26', blank=True, null=True)  # Field name made lowercase.
    prb27 = models.FloatField(db_column='PRB27', blank=True, null=True)  # Field name made lowercase.
    prb28 = models.FloatField(db_column='PRB28', blank=True, null=True)  # Field name made lowercase.
    prb29 = models.FloatField(db_column='PRB29', blank=True, null=True)  # Field name made lowercase.
    prb30 = models.FloatField(db_column='PRB30', blank=True, null=True)  # Field name made lowercase.
    prb31 = models.FloatField(db_column='PRB31', blank=True, null=True)  # Field name made lowercase.
    prb32 = models.FloatField(db_column='PRB32', blank=True, null=True)  # Field name made lowercase.
    prb33 = models.FloatField(db_column='PRB33', blank=True, null=True)  # Field name made lowercase.
    prb34 = models.FloatField(db_column='PRB34', blank=True, null=True)  # Field name made lowercase.
    prb35 = models.FloatField(db_column='PRB35', blank=True, null=True)  # Field name made lowercase.
    prb36 = models.FloatField(db_column='PRB36', blank=True, null=True)  # Field name made lowercase.
    prb37 = models.FloatField(db_column='PRB37', blank=True, null=True)  # Field name made lowercase.
    prb38 = models.FloatField(db_column='PRB38', blank=True, null=True)  # Field name made lowercase.
    prb39 = models.FloatField(db_column='PRB39', blank=True, null=True)  # Field name made lowercase.
    prb40 = models.FloatField(db_column='PRB40', blank=True, null=True)  # Field name made lowercase.
    prb41 = models.FloatField(db_column='PRB41', blank=True, null=True)  # Field name made lowercase.
    prb42 = models.FloatField(db_column='PRB42', blank=True, null=True)  # Field name made lowercase.
    prb43 = models.FloatField(db_column='PRB43', blank=True, null=True)  # Field name made lowercase.
    prb44 = models.FloatField(db_column='PRB44', blank=True, null=True)  # Field name made lowercase.
    prb45 = models.FloatField(db_column='PRB45', blank=True, null=True)  # Field name made lowercase.
    prb46 = models.FloatField(db_column='PRB46', blank=True, null=True)  # Field name made lowercase.
    prb47 = models.FloatField(db_column='PRB47', blank=True, null=True)  # Field name made lowercase.
    prb48 = models.FloatField(db_column='PRB48', blank=True, null=True)  # Field name made lowercase.
    prb49 = models.FloatField(db_column='PRB49', blank=True, null=True)  # Field name made lowercase.
    prb50 = models.FloatField(db_column='PRB50', blank=True, null=True)  # Field name made lowercase.
    prb51 = models.FloatField(db_column='PRB51', blank=True, null=True)  # Field name made lowercase.
    prb52 = models.FloatField(db_column='PRB52', blank=True, null=True)  # Field name made lowercase.
    prb53 = models.FloatField(db_column='PRB53', blank=True, null=True)  # Field name made lowercase.
    prb54 = models.FloatField(db_column='PRB54', blank=True, null=True)  # Field name made lowercase.
    prb55 = models.FloatField(db_column='PRB55', blank=True, null=True)  # Field name made lowercase.
    prb56 = models.FloatField(db_column='PRB56', blank=True, null=True)  # Field name made lowercase.
    prb57 = models.FloatField(db_column='PRB57', blank=True, null=True)  # Field name made lowercase.
    prb58 = models.FloatField(db_column='PRB58', blank=True, null=True)  # Field name made lowercase.
    prb59 = models.FloatField(db_column='PRB59', blank=True, null=True)  # Field name made lowercase.
    prb60 = models.FloatField(db_column='PRB60', blank=True, null=True)  # Field name made lowercase.
    prb61 = models.FloatField(db_column='PRB61', blank=True, null=True)  # Field name made lowercase.
    prb62 = models.FloatField(db_column='PRB62', blank=True, null=True)  # Field name made lowercase.
    prb63 = models.FloatField(db_column='PRB63', blank=True, null=True)  # Field name made lowercase.
    prb64 = models.FloatField(db_column='PRB64', blank=True, null=True)  # Field name made lowercase.
    prb65 = models.FloatField(db_column='PRB65', blank=True, null=True)  # Field name made lowercase.
    prb66 = models.FloatField(db_column='PRB66', blank=True, null=True)  # Field name made lowercase.
    prb67 = models.FloatField(db_column='PRB67', blank=True, null=True)  # Field name made lowercase.
    prb68 = models.FloatField(db_column='PRB68', blank=True, null=True)  # Field name made lowercase.
    prb69 = models.FloatField(db_column='PRB69', blank=True, null=True)  # Field name made lowercase.
    prb70 = models.FloatField(db_column='PRB70', blank=True, null=True)  # Field name made lowercase.
    prb71 = models.FloatField(db_column='PRB71', blank=True, null=True)  # Field name made lowercase.
    prb72 = models.FloatField(db_column='PRB72', blank=True, null=True)  # Field name made lowercase.
    prb73 = models.FloatField(db_column='PRB73', blank=True, null=True)  # Field name made lowercase.
    prb74 = models.FloatField(db_column='PRB74', blank=True, null=True)  # Field name made lowercase.
    prb75 = models.FloatField(db_column='PRB75', blank=True, null=True)  # Field name made lowercase.
    prb76 = models.FloatField(db_column='PRB76', blank=True, null=True)  # Field name made lowercase.
    prb77 = models.FloatField(db_column='PRB77', blank=True, null=True)  # Field name made lowercase.
    prb78 = models.FloatField(db_column='PRB78', blank=True, null=True)  # Field name made lowercase.
    prb79 = models.FloatField(db_column='PRB79', blank=True, null=True)  # Field name made lowercase.
    prb80 = models.FloatField(db_column='PRB80', blank=True, null=True)  # Field name made lowercase.
    prb81 = models.FloatField(db_column='PRB81', blank=True, null=True)  # Field name made lowercase.
    prb82 = models.FloatField(db_column='PRB82', blank=True, null=True)  # Field name made lowercase.
    prb83 = models.FloatField(db_column='PRB83', blank=True, null=True)  # Field name made lowercase.
    prb84 = models.FloatField(db_column='PRB84', blank=True, null=True)  # Field name made lowercase.
    prb85 = models.FloatField(db_column='PRB85', blank=True, null=True)  # Field name made lowercase.
    prb86 = models.FloatField(db_column='PRB86', blank=True, null=True)  # Field name made lowercase.
    prb87 = models.FloatField(db_column='PRB87', blank=True, null=True)  # Field name made lowercase.
    prb88 = models.FloatField(db_column='PRB88', blank=True, null=True)  # Field name made lowercase.
    prb89 = models.FloatField(db_column='PRB89', blank=True, null=True)  # Field name made lowercase.
    prb90 = models.FloatField(db_column='PRB90', blank=True, null=True)  # Field name made lowercase.
    prb91 = models.FloatField(db_column='PRB91', blank=True, null=True)  # Field name made lowercase.
    prb92 = models.FloatField(db_column='PRB92', blank=True, null=True)  # Field name made lowercase.
    prb93 = models.FloatField(db_column='PRB93', blank=True, null=True)  # Field name made lowercase.
    prb94 = models.FloatField(db_column='PRB94', blank=True, null=True)  # Field name made lowercase.
    prb95 = models.FloatField(db_column='PRB95', blank=True, null=True)  # Field name made lowercase.
    prb96 = models.FloatField(db_column='PRB96', blank=True, null=True)  # Field name made lowercase.
    prb97 = models.FloatField(db_column='PRB97', blank=True, null=True)  # Field name made lowercase.
    prb98 = models.FloatField(db_column='PRB98', blank=True, null=True)  # Field name made lowercase.
    prb99 = models.FloatField(db_column='PRB99', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPRB'
        unique_together = (('starttime', 'cell'),)


class Tbprbnew(models.Model):
    starttime = models.CharField(db_column='startTime', primary_key=True, max_length=50)  # Field name made lowercase.
    turnround = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    cell = models.CharField(max_length=255)
    cell_name = models.CharField(max_length=50, blank=True, null=True)
    prb0 = models.FloatField(db_column='PRB0', blank=True, null=True)  # Field name made lowercase.
    prb1 = models.FloatField(db_column='PRB1', blank=True, null=True)  # Field name made lowercase.
    prb2 = models.FloatField(db_column='PRB2', blank=True, null=True)  # Field name made lowercase.
    prb3 = models.FloatField(db_column='PRB3', blank=True, null=True)  # Field name made lowercase.
    prb4 = models.FloatField(db_column='PRB4', blank=True, null=True)  # Field name made lowercase.
    prb5 = models.FloatField(db_column='PRB5', blank=True, null=True)  # Field name made lowercase.
    prb6 = models.FloatField(db_column='PRB6', blank=True, null=True)  # Field name made lowercase.
    prb7 = models.FloatField(db_column='PRB7', blank=True, null=True)  # Field name made lowercase.
    prb8 = models.FloatField(db_column='PRB8', blank=True, null=True)  # Field name made lowercase.
    prb9 = models.FloatField(db_column='PRB9', blank=True, null=True)  # Field name made lowercase.
    prb10 = models.FloatField(db_column='PRB10', blank=True, null=True)  # Field name made lowercase.
    prb11 = models.FloatField(db_column='PRB11', blank=True, null=True)  # Field name made lowercase.
    prb12 = models.FloatField(db_column='PRB12', blank=True, null=True)  # Field name made lowercase.
    prb13 = models.FloatField(db_column='PRB13', blank=True, null=True)  # Field name made lowercase.
    prb14 = models.FloatField(db_column='PRB14', blank=True, null=True)  # Field name made lowercase.
    prb15 = models.FloatField(db_column='PRB15', blank=True, null=True)  # Field name made lowercase.
    prb16 = models.FloatField(db_column='PRB16', blank=True, null=True)  # Field name made lowercase.
    prb17 = models.FloatField(db_column='PRB17', blank=True, null=True)  # Field name made lowercase.
    prb18 = models.FloatField(db_column='PRB18', blank=True, null=True)  # Field name made lowercase.
    prb19 = models.FloatField(db_column='PRB19', blank=True, null=True)  # Field name made lowercase.
    prb20 = models.FloatField(db_column='PRB20', blank=True, null=True)  # Field name made lowercase.
    prb21 = models.FloatField(db_column='PRB21', blank=True, null=True)  # Field name made lowercase.
    prb22 = models.FloatField(db_column='PRB22', blank=True, null=True)  # Field name made lowercase.
    prb23 = models.FloatField(db_column='PRB23', blank=True, null=True)  # Field name made lowercase.
    prb24 = models.FloatField(db_column='PRB24', blank=True, null=True)  # Field name made lowercase.
    prb25 = models.FloatField(db_column='PRB25', blank=True, null=True)  # Field name made lowercase.
    prb26 = models.FloatField(db_column='PRB26', blank=True, null=True)  # Field name made lowercase.
    prb27 = models.FloatField(db_column='PRB27', blank=True, null=True)  # Field name made lowercase.
    prb28 = models.FloatField(db_column='PRB28', blank=True, null=True)  # Field name made lowercase.
    prb29 = models.FloatField(db_column='PRB29', blank=True, null=True)  # Field name made lowercase.
    prb30 = models.FloatField(db_column='PRB30', blank=True, null=True)  # Field name made lowercase.
    prb31 = models.FloatField(db_column='PRB31', blank=True, null=True)  # Field name made lowercase.
    prb32 = models.FloatField(db_column='PRB32', blank=True, null=True)  # Field name made lowercase.
    prb33 = models.FloatField(db_column='PRB33', blank=True, null=True)  # Field name made lowercase.
    prb34 = models.FloatField(db_column='PRB34', blank=True, null=True)  # Field name made lowercase.
    prb35 = models.FloatField(db_column='PRB35', blank=True, null=True)  # Field name made lowercase.
    prb36 = models.FloatField(db_column='PRB36', blank=True, null=True)  # Field name made lowercase.
    prb37 = models.FloatField(db_column='PRB37', blank=True, null=True)  # Field name made lowercase.
    prb38 = models.FloatField(db_column='PRB38', blank=True, null=True)  # Field name made lowercase.
    prb39 = models.FloatField(db_column='PRB39', blank=True, null=True)  # Field name made lowercase.
    prb40 = models.FloatField(db_column='PRB40', blank=True, null=True)  # Field name made lowercase.
    prb41 = models.FloatField(db_column='PRB41', blank=True, null=True)  # Field name made lowercase.
    prb42 = models.FloatField(db_column='PRB42', blank=True, null=True)  # Field name made lowercase.
    prb43 = models.FloatField(db_column='PRB43', blank=True, null=True)  # Field name made lowercase.
    prb44 = models.FloatField(db_column='PRB44', blank=True, null=True)  # Field name made lowercase.
    prb45 = models.FloatField(db_column='PRB45', blank=True, null=True)  # Field name made lowercase.
    prb46 = models.FloatField(db_column='PRB46', blank=True, null=True)  # Field name made lowercase.
    prb47 = models.FloatField(db_column='PRB47', blank=True, null=True)  # Field name made lowercase.
    prb48 = models.FloatField(db_column='PRB48', blank=True, null=True)  # Field name made lowercase.
    prb49 = models.FloatField(db_column='PRB49', blank=True, null=True)  # Field name made lowercase.
    prb50 = models.FloatField(db_column='PRB50', blank=True, null=True)  # Field name made lowercase.
    prb51 = models.FloatField(db_column='PRB51', blank=True, null=True)  # Field name made lowercase.
    prb52 = models.FloatField(db_column='PRB52', blank=True, null=True)  # Field name made lowercase.
    prb53 = models.FloatField(db_column='PRB53', blank=True, null=True)  # Field name made lowercase.
    prb54 = models.FloatField(db_column='PRB54', blank=True, null=True)  # Field name made lowercase.
    prb55 = models.FloatField(db_column='PRB55', blank=True, null=True)  # Field name made lowercase.
    prb56 = models.FloatField(db_column='PRB56', blank=True, null=True)  # Field name made lowercase.
    prb57 = models.FloatField(db_column='PRB57', blank=True, null=True)  # Field name made lowercase.
    prb58 = models.FloatField(db_column='PRB58', blank=True, null=True)  # Field name made lowercase.
    prb59 = models.FloatField(db_column='PRB59', blank=True, null=True)  # Field name made lowercase.
    prb60 = models.FloatField(db_column='PRB60', blank=True, null=True)  # Field name made lowercase.
    prb61 = models.FloatField(db_column='PRB61', blank=True, null=True)  # Field name made lowercase.
    prb62 = models.FloatField(db_column='PRB62', blank=True, null=True)  # Field name made lowercase.
    prb63 = models.FloatField(db_column='PRB63', blank=True, null=True)  # Field name made lowercase.
    prb64 = models.FloatField(db_column='PRB64', blank=True, null=True)  # Field name made lowercase.
    prb65 = models.FloatField(db_column='PRB65', blank=True, null=True)  # Field name made lowercase.
    prb66 = models.FloatField(db_column='PRB66', blank=True, null=True)  # Field name made lowercase.
    prb67 = models.FloatField(db_column='PRB67', blank=True, null=True)  # Field name made lowercase.
    prb68 = models.FloatField(db_column='PRB68', blank=True, null=True)  # Field name made lowercase.
    prb69 = models.FloatField(db_column='PRB69', blank=True, null=True)  # Field name made lowercase.
    prb70 = models.FloatField(db_column='PRB70', blank=True, null=True)  # Field name made lowercase.
    prb71 = models.FloatField(db_column='PRB71', blank=True, null=True)  # Field name made lowercase.
    prb72 = models.FloatField(db_column='PRB72', blank=True, null=True)  # Field name made lowercase.
    prb73 = models.FloatField(db_column='PRB73', blank=True, null=True)  # Field name made lowercase.
    prb74 = models.FloatField(db_column='PRB74', blank=True, null=True)  # Field name made lowercase.
    prb75 = models.FloatField(db_column='PRB75', blank=True, null=True)  # Field name made lowercase.
    prb76 = models.FloatField(db_column='PRB76', blank=True, null=True)  # Field name made lowercase.
    prb77 = models.FloatField(db_column='PRB77', blank=True, null=True)  # Field name made lowercase.
    prb78 = models.FloatField(db_column='PRB78', blank=True, null=True)  # Field name made lowercase.
    prb79 = models.FloatField(db_column='PRB79', blank=True, null=True)  # Field name made lowercase.
    prb80 = models.FloatField(db_column='PRB80', blank=True, null=True)  # Field name made lowercase.
    prb81 = models.FloatField(db_column='PRB81', blank=True, null=True)  # Field name made lowercase.
    prb82 = models.FloatField(db_column='PRB82', blank=True, null=True)  # Field name made lowercase.
    prb83 = models.FloatField(db_column='PRB83', blank=True, null=True)  # Field name made lowercase.
    prb84 = models.FloatField(db_column='PRB84', blank=True, null=True)  # Field name made lowercase.
    prb85 = models.FloatField(db_column='PRB85', blank=True, null=True)  # Field name made lowercase.
    prb86 = models.FloatField(db_column='PRB86', blank=True, null=True)  # Field name made lowercase.
    prb87 = models.FloatField(db_column='PRB87', blank=True, null=True)  # Field name made lowercase.
    prb88 = models.FloatField(db_column='PRB88', blank=True, null=True)  # Field name made lowercase.
    prb89 = models.FloatField(db_column='PRB89', blank=True, null=True)  # Field name made lowercase.
    prb90 = models.FloatField(db_column='PRB90', blank=True, null=True)  # Field name made lowercase.
    prb91 = models.FloatField(db_column='PRB91', blank=True, null=True)  # Field name made lowercase.
    prb92 = models.FloatField(db_column='PRB92', blank=True, null=True)  # Field name made lowercase.
    prb93 = models.FloatField(db_column='PRB93', blank=True, null=True)  # Field name made lowercase.
    prb94 = models.FloatField(db_column='PRB94', blank=True, null=True)  # Field name made lowercase.
    prb95 = models.FloatField(db_column='PRB95', blank=True, null=True)  # Field name made lowercase.
    prb96 = models.FloatField(db_column='PRB96', blank=True, null=True)  # Field name made lowercase.
    prb97 = models.FloatField(db_column='PRB97', blank=True, null=True)  # Field name made lowercase.
    prb98 = models.FloatField(db_column='PRB98', blank=True, null=True)  # Field name made lowercase.
    prb99 = models.FloatField(db_column='PRB99', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPRBNew'
        unique_together = (('starttime', 'cell'),)


class Tbsecadjcell(models.Model):
    s_sector_id = models.CharField(db_column='S_SECTOR_ID', max_length=50)  # Field name made lowercase.
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbSecAdjCell'


class Userlist2(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlist2'
