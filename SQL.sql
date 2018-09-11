CREATE DATABASE TD_LTE
ON PRIMARY
  (NAME='TD-LTE_Primary',
    FILENAME=
       'c:\Program Files\Microsoft SQL Server\MSSQL10_50.SQLEXPRESS\MSSQL\data\TD-LTE_Prm.mdf',
    SIZE=50MB,
    MAXSIZE=100MB,
    FILEGROWTH=1MB),
FILEGROUP TD_LTE_FG1
  (NAME = 'TD-LTE_FG1_Dat1',
    FILENAME =
       'D:\SQL server\�ű�\data\TD-LTE_FG1_1.ndf ',
    SIZE = 30MB,
    MAXSIZE=50MB,
    FILEGROWTH=1MB),
  ( NAME = 'TD-LTE_FG1_Dat2',
    FILENAME =
	   'D:\SQL server\�ű�\data\TD-LTE_FG1_2.ndf ',
    SIZE = 30MB,
    MAXSIZE=50MB,
    FILEGROWTH=1MB)
LOG ON
  ( NAME='TD-LTE_log',
    FILENAME =
		'E:\sql-log\data\TD-LTE.ldf',
    SIZE=10MB,
    MAXSIZE=50MB,
    FILEGROWTH=1MB);
GO*/

use TD_LTE
go
/*create table tbCell(
	CITY nvarchar(255) null,
	SECTOR_ID nvarchar(255) not null,
	SECTOR_NAME nvarchar(255) not null,
	EARFCN int not null
	constraint EARFCN_tbCell check (EARFCN in (38350,38400,38098,38100,37900,37902,40936,40938,40940,38950,39052,39148,39250,38496,38544)),
	PCI int null
	constraint PCI_tbCell check (PCI is null or (PCI between 0 and 503)),
	PSS int null
	constraint PSS_tbCell check (PSS is null or (PSS in (0,1,2))),
	SSS int null
	constraint SSS_tbCell check (SSS is null or (SSS between 0 and 167)),
	TAC int null,
	AZIMUTH float not null,
	HEIGHT float null,
	ELECTTILT float null,
	MECHTILT float null,
	TOTLETILT float not null,
	ENODEBID int not null,
	ENODEB_NAME nvarchar(255) not null,
	VENDOR nvarchar(255) null
	constraint VENDOR_tbCell check(VENDOR is null or (VENDOR in('��Ϊ','����','ŵ��','������','����','����'))),
	LONGITUDE float not null
	constraint LONGITUDE_tbCell check (LONGITUDE between -180.00000 and 180.00000),
	LATITUDE float not null
	constraint LATITUDE_tbCell check (LATITUDE between -90.00000 and 90.00000),
	style nvarchar(255) null
	constraint STYLE_tbCell check (STYLE is null or (STYLE in ('��վ','����','����','�ҷ�'))),
	primary key(SECTOR_ID)
)
CREATE NONCLUSTERED INDEX IX_tbCell ON tbCell (SECTOR_NAME)

create table tbOptCell(
	SECTOR_ID nvarchar(50) not null,
	EARFCN int null
	constraint EARFCN_tbOptCell check (EARFCN in (38350,38400,38098,38100,37900,37902,40936,40938,40940,38950,39052,39148,39250,38496,38544)),
	CELL_TYPE nvarchar(50) null
	constraint CELL_TYPE_tbOptCell check (CELL_TYPE is null or (CELL_TYPE in ('�Ż���','������'))),
	primary key(SECTOR_ID)
)

create table tbAdjCell(
	S_SECTOR_ID nvarchar(50) not null,
	N_SECTOR_ID nvarchar(50) not null,
	S_EARFCN int null
	constraint S_EARFCN_tbAdjCel check (S_EARFCN in (38350,38400,38098,38100,37900,37902,40936,40938,40940,38950,39052,39148,39250,38496,38544)),
	N_EARFCN int null
	constraint N_EARFCN_tbAdjCel check (N_EARFCN in (38350,38400,38098,38100,37900,37902,40936,40938,40940,38950,39052,39148,39250,38496,38544)),
	primary key(S_SECTOR_ID,N_SECTOR_ID)
)

create table tbSecAdjCell(
	S_SECTOR_ID varchar(50) not null,
	N_SECTOR_ID varchar(50) not null,
	primary key(S_SECTOR_ID,N_SECTOR_ID)
)
create table tbPCIAssignment(
	ASSIGN_ID smallint identity(1,1),
	EARFCN int null
	constraint EARFCN_tbPCIAssignment check (EARFCN in (38350,38400,38098,38100,37900,37902,40936,40938,40940,38950,39052,39148,39250,38496,38544)),
	SECTOR_ID nvarchar(200) not null,
	SECTOR_NAME nvarchar(200) null,
	ENBODEB_ID int null,
	PCI int null,
	PSS int null,
	constraint PSS_tbPCIAssignment check(PSS=PCI%3),
	SSS int null,
	constraint SSS_tbPCIAssignment check(SSS=PCI/3),
	LONGITUDE float null,
	LATITUDE float null,
	style varchar(50)null
	constraint STYLE_tbPCIAssignment check (STYLE is null or (STYLE in ('��վ','����','����'))),
	OPT_DATETIME datetime null default getdate(),
	primary key(ASSIGN_ID,SECTOR_ID)

)

create table tbATUData(
	seq bigint not null,
	FileName nvarchar(255) not null,
	Time varchar(100),
	Longitude float,
	Latitude float,
	CellID nvarchar(50),
	TAC int,
	EARFCN int,
	PCI smallint,
	RSRP float,
	RS_SINR float,
	NCell_ID_1 nvarchar(50),
	NCell_EARFCN_1 int,
	NCell_PCI_1 smallint,
	NCell_RSRP_1 float,
	NCell_ID_2 nvarchar(50),
	NCell_EARFCN_2 int,
	NCell_PCI_2 smallint,
	NCell_RSRP_2 float,
	NCell_ID_3 nvarchar(50),
	NCell_EARFCN_3 int,
	NCell_PCI_3 smallint,
	NCell_RSRP_3 float,
	NCell_ID_4 nvarchar(50),
	NCell_EARFCN_4 int,
	NCell_PCI_4 smallint,
	NCell_RSRP_4 float,
	NCell_ID_5 nvarchar(50),
	NCell_EARFCN_5 int,
	NCell_PCI_5 smallint,
	NCell_RSRP_5 float,
	NCell_ID_6 nvarchar(50),
	NCell_EARFCN_6 int,
	NCell_PCI_6 smallint,
	NCell_RSRP_6 float,
	primary key(seq,FileName)
)

create table tbATUC2I(
	SECTOR_ID nvarchar(50) not null,
	NCELL_ID nvarchar(50)not null,
	RATIO_ALL float,
	RANK int,
	COSITE tinyint
	constraint COSITE_tbATUC2I check (COSITE is null or (COSITE in (0,1))),
	primary key(SECTOR_ID,NCELL_ID)
)

create table tbATUHandOver(
	SSECTOR_ID nvarchar(50),
	NSECTOR_ID varchar(50),
	HOATT int
)

create table tbMROData(
	TimeStamp nvarchar(30) not null,
	ServingSector nvarchar(255) not null,
	InterferingSector nvarchar(50) not null,
	LteScRSRP float,
	LteNcRSRP float,
	LteNcEarfcn int,
	LteNcPci smallint
	primary key(Timestamp,ServingSector,InterFeringSector)
)
CREATE NONCLUSTERED INDEX IX_tbMROData ON tbMROData (ServingSector,InterferingSector)

create table tbC2I(
	CITY nvarchar(255),
	SCELL nvarchar(255) not null,
	NCELL nvarchar(255) not null,
	PrC2I9 float,
	C2I_Mean float,
	Std float,
	SampleCount float,
	WeightedC2I float,
	foreign key (SCELL) references tbCell(Sector_ID)
)

create table tbC2INew(
	SCELL nvarchar(255) not null,
	NCELL nvarchar(255) not null,
	C2I_mean float,
	std float,
	PrbC2I9 float,
	PrbABS6 float,
	primary key(SCELL,NCELL)
)

create table tbHandOver(
	CITY nvarchar(255),
	SCELL varchar(50) not null,
	NCELL varchar(50) not null,
	HOATT int,
	HOSUCC int,
	HOSUCCRATE numeric(7,4),
	primary key(SCELL,NCELL),
)

create table tbKPI(
	--	eNodeB����Ƶ�л����ɹ����� (��)	eNodeB����Ƶ�л������Դ��� (��)	eNodeB��ͬƵ�л����ɹ����� (��)	eNodeB��ͬƵ�л������Դ��� (��)	eNodeB����Ƶ�л����ɹ����� (��)	eNodeB����Ƶ�л������Դ��� (��)	eNodeB��ͬƵ�л����ɹ����� (��)	eNodeB��ͬƵ�л������Դ��� (��)	eNB���л��ɹ��� (%)	eNB���л��ɹ��� (%)	ͬƵ�л��ɹ���zsp (%)	��Ƶ�л��ɹ���zsp (%)	�л��ɹ��� (%)	С��PDCP�������յ����������ݵ��������� (����)	С��PDCP�������͵��������ݵ��������� (����)	RRC�ؽ�������� (��)	RRC�����ؽ����� (%)	ͨ���ؽ���ԴС����eNodeB��ͬƵ�л���ִ�гɹ����� (��)	ͨ���ؽ���ԴС����eNodeB����Ƶ�л���ִ�гɹ����� (��)	ͨ���ؽ���ԴС����eNodeB��ͬƵ�л���ִ�гɹ����� (��)	ͨ���ؽ���ԴС����eNodeB����Ƶ�л���ִ�гɹ����� (��)	eNB���л����ɹ����� (��)	eNB���л���������� (��)
	startTime date not null,
	turnround int,
	name nvarchar(50),
	cell_multi nvarchar(255) not null,
	cell nvarchar(50),
	suc_time int,
	req_time int,
	RRC_suc_rate float,
	suc_total int,
	try_total int,
	E_RAB_suc_rate float,
	eNodeB_exception int,
	cell_exception int,
	E_RAB_offline float,
	ay float,
	enodeb_release_time int,
	UE_Context_exception_time int,
	UE_Context_suc_time int,
	wifi_offline_rate float,
	t_ int,
	u_ int,
	v_ int,
	w_ int,
	x_ int,
	y_ int,
	z_ int,
	aa_ int,
	ab_ float,  --NIL????
	ac_ float,
	ad_ float,
	ae_ float, --NIL����Ϊ0
	af_ float,
	ag_ bigint,
	ah_ bigint,
	ai_ int,
	aj_ float,
	ak_ int,
	al_ int,
	am_ int,
	an_ int,
	ao_ int,
	ap_ int��
	primary key(startTime,cell_multi)
)
CREATE NONCLUSTERED INDEX IX_tbKPI ON tbKPI (name,starttime)

create table tbPRB(
	startTime datetime not null,
	turnround int,
	name nvarchar(50),
	cell nvarchar(255) not null,
	cell_name nvarchar(50),
	PRB0 float,
	PRB1 float,
	PRB2 float,
	PRB3 float,
	PRB4 float,
	PRB5 float,
	PRB6 float,
	PRB7 float,
	PRB8 float,
	PRB9 float,
	PRB10 float,
	PRB11 float,
	PRB12 float,
	PRB13 float,
	PRB14 float,
	PRB15 float,
	PRB16 float,
	PRB17 float,
	PRB18 float,
	PRB19 float,
	PRB20 float,
	PRB21 float,
	PRB22 float,
	PRB23 float,
	PRB24 float,
	PRB25 float,
	PRB26 float,
	PRB27 float,
	PRB28 float,
	PRB29 float,
	PRB30 float,
	PRB31 float,
	PRB32 float,
	PRB33 float,
	PRB34 float,
	PRB35 float,
	PRB36 float,
	PRB37 float,
	PRB38 float,
	PRB39 float,
	PRB40 float,
	PRB41 float,
	PRB42 float,
	PRB43 float,
	PRB44 float,
	PRB45 float,
	PRB46 float,
	PRB47 float,
	PRB48 float,
	PRB49 float,
	PRB50 float,
	PRB51 float,
	PRB52 float,
	PRB53 float,
	PRB54 float,
	PRB55 float,
	PRB56 float,
	PRB57 float,
	PRB58 float,
	PRB59 float,
	PRB60 float,
	PRB61 float,
	PRB62 float,
	PRB63 float,
	PRB64 float,
	PRB65 float,
	PRB66 float,
	PRB67 float,
	PRB68 float,
	PRB69 float,
	PRB70 float,
	PRB71 float,
	PRB72 float,
	PRB73 float,
	PRB74 float,
	PRB75 float,
	PRB76 float,
	PRB77 float,
	PRB78 float,
	PRB79 float,
	PRB80 float,
	PRB81 float,
	PRB82 float,
	PRB83 float,
	PRB84 float,
	PRB85 float,
	PRB86 float,
	PRB87 float,
	PRB88 float,
	PRB89 float,
	PRB90 float,
	PRB91 float,
	PRB92 float,
	PRB93 float,
	PRB94 float,
	PRB95 float,
	PRB96 float,
	PRB97 float,
	PRB98 float,
	PRB99 float,
	primary key(startTime,cell)
)

create table tbPRBNew(
	startTime nvarchar(50) not null,
	turnround int,
	name nvarchar(50),
	cell nvarchar(255) not null,
	cell_name nvarchar(50),
	PRB0 float,
	PRB1 float,
	PRB2 float,
	PRB3 float,
	PRB4 float,
	PRB5 float,
	PRB6 float,
	PRB7 float,
	PRB8 float,
	PRB9 float,
	PRB10 float,
	PRB11 float,
	PRB12 float,
	PRB13 float,
	PRB14 float,
	PRB15 float,
	PRB16 float,
	PRB17 float,
	PRB18 float,
	PRB19 float,
	PRB20 float,
	PRB21 float,
	PRB22 float,
	PRB23 float,
	PRB24 float,
	PRB25 float,
	PRB26 float,
	PRB27 float,
	PRB28 float,
	PRB29 float,
	PRB30 float,
	PRB31 float,
	PRB32 float,
	PRB33 float,
	PRB34 float,
	PRB35 float,
	PRB36 float,
	PRB37 float,
	PRB38 float,
	PRB39 float,
	PRB40 float,
	PRB41 float,
	PRB42 float,
	PRB43 float,
	PRB44 float,
	PRB45 float,
	PRB46 float,
	PRB47 float,
	PRB48 float,
	PRB49 float,
	PRB50 float,
	PRB51 float,
	PRB52 float,
	PRB53 float,
	PRB54 float,
	PRB55 float,
	PRB56 float,
	PRB57 float,
	PRB58 float,
	PRB59 float,
	PRB60 float,
	PRB61 float,
	PRB62 float,
	PRB63 float,
	PRB64 float,
	PRB65 float,
	PRB66 float,
	PRB67 float,
	PRB68 float,
	PRB69 float,
	PRB70 float,
	PRB71 float,
	PRB72 float,
	PRB73 float,
	PRB74 float,
	PRB75 float,
	PRB76 float,
	PRB77 float,
	PRB78 float,
	PRB79 float,
	PRB80 float,
	PRB81 float,
	PRB82 float,
	PRB83 float,
	PRB84 float,
	PRB85 float,
	PRB86 float,
	PRB87 float,
	PRB88 float,
	PRB89 float,
	PRB90 float,
	PRB91 float,
	PRB92 float,
	PRB93 float,
	PRB94 float,
	PRB95 float,
	PRB96 float,
	PRB97 float,
	PRB98 float,
	PRB99 float,
	primary key(startTime,cell)
)

create table userlist(
	username nvarchar(50),
	password nvarchar(50), 
	type int,  --1��vip��0����ͨ�û�
	state int,  --1��ʾ���ߣ�0��ʾ����
	primary key(username)
)

create table tbC2I3(
	A_sector_id nvarchar(50),
	B_sector_id nvarchar(50),
	C_sector_id nvarchar(50)
)
CREATE NONCLUSTERED INDEX IX_tbAdjCell ON tbAdjCell (S_EARFCN)--�����Ǿۼ�����
go
*/

/*--ע�᣺
insert into userlist(username,password,type,state)values('xxx','xx',1,0)

--��¼��ѯ��
select username from userlist where username='xxx' and password='xxx'*/

--����
/*bulk insert tbCell
from 'D:\���ݿ�\���ݿ�ϵͳԭ��γ����-18\����Ͽ����TD-LTE��������-2017-03\1.tbCell.xlsx'
with
(	
	FIELDTERMINATOR = ' ',
    ROWTERMINATOR = '\n',
	datafiletype='char',
	batchsize=50,
	CHECK_CONSTRAINTS,
	ERRORFILE ='E:\sql-log\data\error.txt'
);*/


--����xp_cmdshell
/*EXEC sp_configure 'show advanced options', 1
GO
RECONFIGURE
GO
EXEC sp_configure 'xp_cmdshell', 1
GO
RECONFIGURE
GO*/

--�������ݱ�
--����tbOptCell
/*if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable1'))
drop table TD_LTE..TempTable1
go
select * into TD_LTE..temptable1 from(
select 'SECTOR_ID'as [1],'EARFCN' as [2],'CELL_TYPE' as [3]
union all
select SECTOR_ID, convert(nvarchar(50),EARFCN),CELL_TYPE from tbOptcell )as temptable1
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable1" queryout "E:\sql-log\data\test1.xls" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable1  --ɾ����ʱ��*/

--����tbAdjCell
/*if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable2'))
drop table TD_LTE..TempTable2
go
select * into TD_LTE..temptable2 from(
select 'S_SECTOR_ID'as [1],'N_SECTOR_ID'as [2],'S_EARFCN	' as [3],'N_EARFCN' as [4]
union all
select convert(char(15),S_SECTOR_ID),convert(char(15),N_SECTOR_ID), convert(char(15),S_EARFCN),  convert(char(15),N_EARFCN)from tbAdjcell )as temptable2
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable2" queryout "E:\sql-log\data\test2.txt" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable2  --ɾ����ʱ��*/

--����tbATUHandOver
/*if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable3'))
drop table TD_LTE..TempTable3
go
select * into TD_LTE..temptable3 from(
select 'SSECTOR_ID'as [1],'NSECTOR_ID'as [2],'HOATT' as [3]
union all
select convert(char(20),SSECTOR_ID),convert(char(20),NSECTOR_ID), convert(char(15),HOATT)from tbATUHandOver )as temptable3
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable3" queryout "E:\sql-log\data\test3.txt" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable3*/

/*--Ԥ��ǰһ��������
select top 100* from tbOptCell
*/


--������ͻ������ tbCell
if exists (select * from sysobjects where name = 'tri_Cell')
drop trigger tri_Cell
go
create trigger tri_Cell on tbCell instead of insert as
declare @sector_id nvarchar(255)
declare @count int
select @sector_id=Sector_id from inserted
begin
select @count=count(*) from tbCell where SECTOR_ID=@sector_id
if(@count=0)
	begin
		insert into tbCell select* from inserted
	end
else
	begin
		delete tbCell where SECTOR_ID=@sector_id
		insert into tbCell select* from inserted
	end
end
go



--tbKPI������ͻ������
if exists (select * from sysobjects where name = 'tri_KPI')
drop trigger tri_KPI
go
create trigger tri_KPI on tbKPI instead of insert as
declare @startTime date
declare @cell_multi nvarchar(255)
declare @count int
select @startTime=startTime,@cell_multi=cell_multi from inserted
begin
select @count=count(*) from tbKPI where startTime=@startTime and cell_multi=@cell_multi
if(@count=0)
	begin
		insert into tbKPI select* from inserted
	end
else
	begin
		delete tbKPI where  startTime=@startTime and cell_multi=@cell_multi
		insert into tbKPI select* from inserted
	end
end
go


--tbPRB������ͻ������
if exists (select * from sysobjects where name = 'tri_PRB')
drop trigger tri_PRB
go
create trigger tri_PRB on tbPRB instead of insert as
declare @startTime datetime
declare @cell nvarchar(255)
declare @count int
select @startTime=startTime,@cell=cell from inserted
begin
select @count=count(*) from tbPRB where startTime=@startTime and cell=@cell
if(@count=0)
	begin
		insert into tbPRB select* from inserted
	end
else
	begin
		delete tbPRB where  startTime=@startTime and cell=@cell
		insert into tbPRB select* from inserted
	end
end
go

--MROData������
if exists (select * from sysobjects where name = 'tri_MROData')
drop trigger tri_MROData
go
create trigger tri_MROData on tbMROData instead of insert as
declare @TimeStamp nvarchar(30)
declare @servingsector nvarchar(255)
declare @interferingsector nvarchar(50)
declare @LteScRSRP int
declare @LteNcRSRP int
declare @LteNcEarfcn int
declare @LteNcPci int
declare  cur_new insensitive cursor
for select TimeStamp,servingsector ,interferingsector,LteScRSRP,LteNcRSRP,LteNcEarfcn,LteNcPci from inserted
open cur_new
fetch next from cur_new into @TimeStamp,@servingsector,@interferingsector,@LteScRSRP,@LteNcRSRP,@LteNcEarfcn,@LteNcPci
while @@fetch_status <> -1
begin
delete tbMROData where TimeStamp=@TimeStamp and servingsector=@servingsector and interferingsector=@interferingsector and LteScRSRP=@LteScRSRP and LteNcRSRP=@LteNcRSRP
insert into tbMROData values( @TimeStamp,@servingsector,@interferingsector,@LteScRSRP,@LteNcRSRP,@LteNcEarfcn,@LteNcPci )
fetch next from cur_new into @TimeStamp,@servingsector,@interferingsector,@LteScRSRP,@LteNcRSRP,@LteNcEarfcn,@LteNcPci
end
close cur_new
deallocate cur_new
go

--tbC2I������ͻ������
if exists (select * from sysobjects where name = 'tri_C2INew')
drop trigger tri_C2INew
go
create trigger tri_C2INew on tbC2INew instead of insert as
declare @SCELL nvarchar(255)
declare @NCELL nvarchar(255)
declare @C2I_mean float
declare @std float
declare  cur_new insensitive cursor
for select SCELL,NCELL,C2I_mean,std from inserted
open cur_new
fetch next from cur_new into @SCELL,@NCELL,@C2I_mean,@std
while @@fetch_status <> -1
begin
delete tbC2INew where SCELL=@SCELL and NCELL=@NCELL
insert into tbC2INew(SCELL,NCELL,C2I_mean,std) values(@SCELL,@NCELL,@C2I_mean,@std)
fetch next from cur_new into @SCELL,@NCELL,@C2I_mean,@std
end
close cur_new
deallocate cur_new
go



----3.3��Ϣ��ѯ
--1.С��������Ϣ��ѯ
select SECTOR_ID from tbCell
select distinct SECTOR_NAME from tbCell
select * from tbCell where SECTOR_ID='111' or SECTOR_NAME='mmmm'

--2.��վeNodeB��Ϣ��ѯ
select distinct ENODEBID from tbCell
select distinct ENODEB_NAME from tbCell
select* from tbCell where ENODEBID=1 or ENODEB_NAME='hhh'

--3.KPIָ����Ϣ��ѯ
select distinct name from tbKPI
select suc_time from tbKPI where startTime between 07/17/2016 and 07/19/2016 and name='����Ͽ����������ٶ�-HLHF'
--��Ԫ�����ԡ�ʱ��ο�ѡ

--4.PRB��Ϣͳ�����ѯ
--�洢��������tbPRBNew
create proc create_PRBNew as 
begin
insert into tbPRBNew
select substring(convert(varchar(13),starttime,20)+':00',1,16) ,sum(turnround)as turnaroud,name as name,cell,cell_name,avg(PRB0*1.0),avg(PRB1*1.0),avg(PRB2*1.0),avg(PRB3*1.0),avg(PRB4*1.0),avg(PRB5*1.0),avg(PRB6*1.0),avg(PRB7*1.0),avg(PRB8*1.0),avg(PRB9*1.0),avg(PRB10*1.0),avg(PRB11*1.0),avg(PRB12*1.0),avg(PRB13*1.0),avg(PRB14*1.0),avg(PRB15*1.0),avg(PRB16*1.0),avg(PRB17*1.0),avg(PRB18*1.0),avg(PRB19*1.0),avg(PRB20*1.0),avg(PRB21*1.0),avg(PRB22*1.0),avg(PRB23*1.0),avg(PRB24*1.0),avg(PRB25*1.0),avg(PRB26*1.0),avg(PRB27*1.0),avg(PRB28*1.0),avg(PRB29*1.0),avg(PRB30*1.0),avg(PRB31*1.0),avg(PRB32*1.0),
avg(PRB33*1.0),avg(PRB34*1.0),avg(PRB35*1.0),avg(PRB36*1.0),avg(PRB37*1.0),avg(PRB38*1.0),avg(PRB39*1.0),avg(PRB40*1.0),avg(PRB41*1.0),avg(PRB42*1.0),avg(PRB43*1.0),avg(PRB44*1.0),avg(PRB45*1.0),avg(PRB46*1.0),avg(PRB47*1.0),avg(PRB48*1.0),avg(PRB49*1.0),avg(PRB50*1.0),avg(PRB51*1.0),avg(PRB52*1.0),avg(PRB53*1.0),avg(PRB54*1.0),avg(PRB55*1.0),avg(PRB56*1.0),avg(PRB57*1.0),avg(PRB58*1.0),avg(PRB59*1.0),avg(PRB60*1.0),avg(PRB61*1.0),avg(PRB62*1.0),avg(PRB63*1.0),avg(PRB64*1.0),avg(PRB65*1.0),avg(PRB66*1.0),avg(PRB67*1.0),avg(PRB68*1.0),avg(PRB69*1.0),avg(PRB70*1.0),avg(PRB71*1.0),avg(PRB72*1.0),avg(PRB73*1.0),avg(PRB74*1.0),avg(PRB75*1.0),avg(PRB76*1.0),avg(PRB77*1.0),avg(PRB78*1.0),avg(PRB79*1.0),avg(PRB80*1.0),avg(PRB81*1.0),avg(PRB82*1.0),avg(PRB83*1.0),avg(PRB84*1.0),avg(PRB85*1.0),avg(PRB86*1.0),avg(PRB87*1.0),avg(PRB88*1.0),avg(PRB89*1.0),avg(PRB90*1.0),avg(PRB91*1.0),avg(PRB92*1.0),avg(PRB93*1.0),avg(PRB94*1.0),avg(PRB95*1.0),avg(PRB96*1.0),
avg(PRB97*1.0),avg(PRB98*1.0),avg(PRB99*1.0)
from tbPRB
group by name ,cell,cell_name,substring(convert(varchar(13),starttime,20)+':00',1,16)
end
 
--�����ⲿexcel
--����Ԥ��
 select top 100* from tbPRBNew
 --����tbPRBNew
 if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable'))
drop table TD_LTE..TempTable
go
select * into TD_LTE..temptable from(
select '��ʼʱ��'as [1],'����' as [2],'��Ԫ����' as [3],'С��' as [4],'С����' as [5],
'PRB0' as [6],'PRB1' as [7],'PRB2' as [8],'PRB3' as [9],'PRB4' as [10],'PRB5' as [11],'PRB6' as [12],'PRB7' as [13],
'PRB8' as [14],'PRB9' as [15],'PRB10' as [16],'PRB11' as [17],'PRB12' as [18],'PRB13' as [19],'PRB14' as [20],'PRB15' as [21],
'PRB16' as [22],'PRB17' as [23],'PRB18' as [24],'PRB19' as [25],'PRB20' as [26],'PRB21' as [27],'PRB22' as [28],'PRB23' as [29],
'PRB24' as [30],'PRB25' as [31],'PRB26' as [32],'PRB27' as [33],'PRB28' as [34],'PRB29' as [35],'PRB30' as [36],'PRB31' as [37],
'PRB32' as [38],'PRB33' as [39],'PRB34' as [40],'PRB35' as [41],'PRB36' as [42],'PRB37' as [43],'PRB38' as [44],'PRB39' as [45],
'PRB40' as [46],'PRB41' as [47],'PRB42' as [48],'PRB43' as [49],'PRB44' as [50],'PRB45' as [51],'PRB46' as [52],'PRB47' as [53],
'PRB48' as [54],'PRB49' as [55],'PRB50' as [56],'PRB51' as [57],'PRB52' as [58],'PRB53' as [59],'PRB54' as [60],'PRB55' as [61],
'PRB56' as [62],'PRB57' as [63],'PRB58' as [64],'PRB59' as [65],'PRB60' as [66],'PRB61' as [67],'PRB62' as [68],'PRB63' as [69],
'PRB64' as [70],'PRB65' as [71],'PRB66' as [72],'PRB67' as [73],'PRB68' as [74],'PRB69' as [75],'PRB70' as [76],'PRB71' as [77],
'PRB72' as [78],'PRB73' as [79],'PRB74' as [80],'PRB75' as [81],'PRB76' as [82],'PRB77' as [83],'PRB78' as [84],'PRB79' as [85],
'PRB80' as [86],'PRB81' as [87],'PRB82' as [88],'PRB83' as [89],'PRB84' as [90],'PRB85' as [91],'PRB86' as [92],'PRB87' as [93],
'PRB88' as [94],'PRB89' as [95],'PRB90' as [96],'PRB91' as [97],'PRB92' as [98],'PRB93' as [99],'PRB94' as [100],'PRB95' as [101],
'PRB96' as [102],'PRB97' as [103],'PRB98' as [104],'PRB100' as [105]
union all
select convert(nvarchar(50),startTime), convert(nvarchar(50),turnround),name,cell,cell_name,convert(nvarchar(50),PRB0),convert(nvarchar(50),PRB1),convert(nvarchar(50),PRB2),
convert(nvarchar(50),PRB3),convert(nvarchar(50),PRB4),convert(nvarchar(50),PRB5),convert(nvarchar(50),PRB6), convert(nvarchar(50),PRB7),convert(nvarchar(50),PRB8),convert(nvarchar(50),PRB9),convert(nvarchar(50),PRB10),
convert(nvarchar(50),PRB11),convert(nvarchar(50),PRB12),convert(nvarchar(50),PRB13),convert(nvarchar(50),PRB14),convert(nvarchar(50),PRB15),convert(nvarchar(50),PRB16),convert(nvarchar(50),PRB17),convert(nvarchar(50),PRB18),
convert(nvarchar(50),PRB19),convert(nvarchar(50),PRB20),convert(nvarchar(50),PRB21),convert(nvarchar(50),PRB22), convert(nvarchar(50),PRB23),convert(nvarchar(50),PRB24),convert(nvarchar(50),PRB25),convert(nvarchar(50),PRB26),
convert(nvarchar(50),PRB27),convert(nvarchar(50),PRB28),convert(nvarchar(50),PRB29),convert(nvarchar(50),PRB30),convert(nvarchar(50),PRB31),convert(nvarchar(50),PRB32),convert(nvarchar(50),PRB33),convert(nvarchar(50),PRB34),
convert(nvarchar(50),PRB35),convert(nvarchar(50),PRB36),convert(nvarchar(50),PRB37),convert(nvarchar(50),PRB38), convert(nvarchar(50),PRB39),convert(nvarchar(50),PRB40),convert(nvarchar(50),PRB41),convert(nvarchar(50),PRB42),
convert(nvarchar(50),PRB43),convert(nvarchar(50),PRB44),convert(nvarchar(50),PRB45),convert(nvarchar(50),PRB46),convert(nvarchar(50),PRB47),convert(nvarchar(50),PRB48),convert(nvarchar(50),PRB49),convert(nvarchar(50),PRB50),
convert(nvarchar(50),PRB51),convert(nvarchar(50),PRB52),convert(nvarchar(50),PRB53),convert(nvarchar(50),PRB54), convert(nvarchar(50),PRB55),convert(nvarchar(50),PRB56),convert(nvarchar(50),PRB57),convert(nvarchar(50),PRB58),
convert(nvarchar(50),PRB59),convert(nvarchar(50),PRB60),convert(nvarchar(50),PRB61),convert(nvarchar(50),PRB62),convert(nvarchar(50),PRB63),convert(nvarchar(50),PRB64),convert(nvarchar(50),PRB65),convert(nvarchar(50),PRB66),
convert(nvarchar(50),PRB67),convert(nvarchar(50),PRB68),convert(nvarchar(50),PRB69),convert(nvarchar(50),PRB70), convert(nvarchar(50),PRB71),convert(nvarchar(50),PRB72),convert(nvarchar(50),PRB73),convert(nvarchar(50),PRB74),
convert(nvarchar(50),PRB75),convert(nvarchar(50),PRB76),convert(nvarchar(50),PRB77),convert(nvarchar(50),PRB78),convert(nvarchar(50),PRB79),convert(nvarchar(50),PRB80),convert(nvarchar(50),PRB81),convert(nvarchar(50),PRB82),
convert(nvarchar(50),PRB83),convert(nvarchar(50),PRB84),convert(nvarchar(50),PRB85),convert(nvarchar(50),PRB86), convert(nvarchar(50),PRB87),convert(nvarchar(50),PRB88),convert(nvarchar(50),PRB89),convert(nvarchar(50),PRB90),
convert(nvarchar(50),PRB91),convert(nvarchar(50),PRB92),convert(nvarchar(50),PRB93),convert(nvarchar(50),PRB94),convert(nvarchar(50),PRB95),convert(nvarchar(50),PRB96),convert(nvarchar(50),PRB97),convert(nvarchar(50),PRB98),convert(nvarchar(50),PRB99)
from tbPRBNew )as temptable
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable" queryout "E:\sql-log\data\test4.txt" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable  --ɾ����ʱ��


--��ѯ��Ԫĳ��ʱ��Σ�Сʱ����ĳ������ֵ�ı仯���
select *
from tbPRBNew
where startTime>='2016-07-17 00:00' and starttime <= '2016-07-17 04:00' and name='����Ͽ����������ٶ�-HLHF'

select* from tbC2INew
--3.4����С��C2I���ŷ���
--�Ȳ���ǰ�ĸ����Խ���tbC2INew
--�洢���̼����ֵ�ͱ�׼��
go

create proc create_C2INew as
begin
insert into tbC2INew(SCEll,NCELL,C2I_mean,std)
select ServingSector,InterferingSector,avg((LteScRSRP-LteNcRSRP)*1.000) 
as C2I_mean,round(stdev(LteScRSRP-LteNcRSRP),6) as std
from tbMROData
group by ServingSector,InterferingSector
having count(ServingSector)>100
end

select * from tbMROData
--������̨����С��ID�Լ�mean��std
select ServingSector,InterferingSector,avg((LteScRSRP-LteNcRSRP)*1.000) 
as C2I_mean,round(stdev(LteScRSRP-LteNcRSRP),6) as  std
from tbMROData
group by ServingSector,InterferingSector
having count(ServingSector)>200
--��̨��ֵ����������tbC2INew����������
update tbC2INew set PrbC2I9=0.0001,PrbABS6=9.9 where SCELL='xxx' and NCELL='yyyy'

--Ԥ��tbC2INewǰ100��
select top 100* from tbC2INew

--����tbC2INew
if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable'))
drop table TD_LTE..TempTable
go
select * into TD_LTE..temptable from(
select 'SCELL	'as [1],'NCELL	'as [2],'C2I_mean ' as [3],'std	' as [4],'PrbC2I9	' as [5],'PrbABS6' as [6]
union all
select convert(char(20),SCELL),convert(char(20),NCELl), convert(char(20),C2I_mean),convert(char(20),std), convert(char(20),PrbC2I9),  convert(char(15),PrbABS6)from tbC2INew )as temptable
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable" queryout "E:\sql-log\data\test.txt" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable 

-----------------

select* from tbC2INew
--3.5��ѯ�ص����Ǹ�����Ԫ��
--�洢��������tbC2I3 ��x��ѡ
if (object_id('proc_C2I3', 'P') is not null)
    drop proc proc_C2I3
go
create proc proc_C2I3(@x float)
as
truncate table tbC2I3
insert into tbC2I3
select  S.SCELL as S_SCELL,S.NCELL as R_SCELL,T.SCELL as T_SCELL
from tbC2INew as T,tbC2INew as S,tbC2INew as R
where ((T.Scell=R.NCELL and R.SCELL=S.NCELL and S.SCELL=T.NCELL)or (s.scell=t.ncell and s.ncell=r.ncell and t.scell=r.scell)or 
(s.scell=r.scell and s.ncell=t.ncell and t.scell=r.ncell) or (s.scell=r.ncell and s.ncell=t.ncell and t.scell=r.scell)) 
and T.PrbABS6>=@x and R.PrbABS6>=@x and S.PrbABS6>=@x
union 
select  S.SCELL as S_SCELL,S.NCELL as R_SCELL,T.NCELL as T_SCELL
from tbC2INew as T,tbC2INew as S,tbC2INew as R
where ((T.SCELL=S.NCELL and R.NCELL=S.SCELL and R.Scell=T.Ncell) or(s.scell=T.scell and s.ncell=r.scell and t.NCELL=r.ncell) or
(s.scell=t.scell and s.ncell=r.ncell and t.ncell=r.scell)or(s.scell=r.scell and s.ncell=t.scell and t.ncell=r.ncell))and
 T.PrbABS6>=@x and R.PrbABS6>=@x and S.PrbABS6>=@x
go

exec proc_C2I3 @x=0.22

select* from tbC2I3
select * from tbATUC2I
truncate table  tbMROData
select * from tbPRBNew

--ɾ���ظ���Ԫ�鴥����
if exists (select * from sysobjects where name = 'tri_C2I3')
drop trigger tri_C2I3
go
create trigger tri_C2I3 on tbC2I3 instead of insert as
declare @S_SCELL nvarchar(255)
declare @R_SCELL nvarchar(255)
declare @T_SCELL nvarchar(255)
declare  cur_new insensitive cursor
for select*from inserted
open cur_new
fetch next from cur_new into @S_SCELL,@R_SCELL,@T_SCELL
while @@fetch_status <> -1
begin
delete tbC2I3 where (A_sector_id=@S_SCELL and B_sector_id=@T_SCELL and C_sector_id=@R_SCELL)or 
(A_sector_id=@T_SCELL and B_sector_id=@R_SCELL and C_sector_id=@S_SCELL) or
(A_sector_id=@R_SCELL and B_sector_id=@S_SCELL and C_sector_id=@T_SCELL) or
(A_sector_id=@T_SCELL and B_sector_id=@S_SCELL and C_sector_id=@R_SCELL) or
(A_sector_id=@S_SCELL and B_sector_id=@R_SCELL and C_sector_id=@T_SCELL) or
(A_sector_id=@R_SCELL and B_sector_id=@T_SCELL and C_sector_id=@S_SCELL) 
insert into tbC2I3 values(@S_SCELL,@R_SCELL,@T_SCELL)
fetch next from cur_new into @S_SCELL,@R_SCELL,@T_SCELL
end
close cur_new
deallocate cur_new
go

select* from tbKPI


--����tbC2I3
if exists(select * from TD_LTE..sysobjects where id = object_id('TD_LTE..TempTable'))
drop table TD_LTE..TempTable
go
select * into TD_LTE..temptable from(
select 'A_SECTOR_ID'as [1],'B_SECTOR_ID' as [2],'B_SECTOR_ID' as [3]
union all
select convert(char(20),A_SECTOR_ID),convert(char(20),B_SECTOR_ID),convert(char(20),C_SECTOR_ID)  from tbC2I3 )as temptable
EXEC master..xp_cmdshell 'BCP "SELECT  * FROM TD_LTE..temptable" queryout "E:\sql-log\data\test6.txt" -c -q -S"DESKTOP-5M6JKFJ" -U"sa" -P"ly520741"'
drop table TD_LTE..TempTable  --ɾ����ʱ��


--�������ܱȽ�

select * from tbC2INew
delete from tbCell
truncate table tbC2INew


alter table tbC2Inew add primary key(Scell,ncell)

select* from tbKPI

if exists (select * from sysobjects where name = 'tri_MROData')
drop trigger tri_MROData
go
create trigger tri_MROData on tbMROData instead of insert as
declare @TimeStamp nvarchar(30)
declare @servingsector nvarchar(255)
declare @interferingsector nvarchar(50)
declare @LteScRSRP int
declare @LteNcRSRP int
declare @count int 
select @TimeStamp=TimeStamp,@servingsector=servingsector ,@interferingsector=interferingsector,@LteScRSRP=LteScRSRP,@LteNcRSRP=LteNcRSRP from inserted
begin
select @count=count(*) from tbMROData where TimeStamp=@TimeStamp and servingsector=@servingsector and interferingsector=@interferingsector and LteScRSRP=@LteScRSRP and LteNcRSRP=@LteNcRSRP
if(@count=0)
	begin
		insert into tbMROData select* from inserted
	end
else
	begin
		delete tbMROData where TimeStamp=@TimeStamp and servingsector=@servingsector and interferingsector=@interferingsector and LteScRSRP=@LteScRSRP and LteNcRSRP=@LteNcRSRP
		insert into tbMROData select* from inserted
	end
end
go


--��������ʱ��
sp_configure 'show advanced options', 1
GO
RECONFIGURE
GO
sp_configure 'remote query timeout', 2147483647
GO
RECONFIGURE
GO
--�鿴������ʱ��
SELECT * FROM sys.configurations WHERE configuration_id IN (1519,1520,1541);