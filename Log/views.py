from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse,HttpResponsePermanentRedirect
#from Log.models import userinfo
from Log.models import Tbsecadjcell
from Log.models import Tbkpi
from Log.models import Tboptcell
from Log.models import Tbprb
from Log.models import Tbmrodata
from Log.models import Userlist2
from Log.models import Tbatuhandover
from Log.models import Tbadjcell
import time
import datetime
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from django import forms
from Log.models import Tbcell
import os
from xlrd import xldate_as_tuple
import csv
from io import StringIO
import json
from django.db import connection, transaction
# Create your views here.


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class ChooseForm(forms.Form):
    table_choose = forms.CharField(max_length=10)


class ChooseForm1(forms.Form):
    table_choose1 = forms.CharField(max_length=10)


class RegUserForm(forms.Form):
    Regusername = forms.CharField(max_length=50)
    Regpassword = forms.CharField(max_length=50)
    user_type = forms.CharField(max_length=10)


class DownloadForm(forms.Form):
    down_file = forms.CharField(max_length=255)


class SearchTbCellForm(forms.Form):
    index = forms.CharField(max_length = 50)


print("开始了")

global bar_value
bar_value = 0.0

##gengxinchangshi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def upload_tbCell(request):
    global bar_value
    if request.method == "POST":
        file_obj = request.FILES["up_file"]
        type_excel = file_obj.name.split('.')[1]
        print(type_excel)
        name_excel = file_obj.name.split('.')[0]
        print(file_obj.name)
        bar_value = 0.0
        if 'xlsx' == type_excel:
            data = xlrd.open_workbook(filename=None, file_contents=file_obj.read())
            print("读取文件结束，准备导入！")
            table = data.sheet_by_index(0)
            successLines = 1
            workList = []
            failLines = 0
            if 'tbOptCell' == name_excel:
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if type(row[0]) == str and type(row[1]) == float and row[1] % 1 == 0 and type(row[2]) == str:
                            workList.append(Tboptcell(sector_id=row[0], earfcn=row[1], cell_type=row[2]))
                        else:
                            failLines = failLines + 1
                            print(successLines + failLines)
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 500 == 0:  # 每五行进行一次插入
                        bar_value = successLines/(successLines+failLines)
                        print("上传进度：")
                        print(bar_value)
                        print("已插入到")
                        print(successLines)
                        print(type(row[1]))
                        # print("已插入到第n行")
                        Tboptcell.objects.bulk_create(workList)
                        workList = []
                Tboptcell.objects.bulk_create(workList)
            elif 'tbKPI' == name_excel:
                print(table.nrows)
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if (type(row[1]) == float and row[1] % 1 == 0
                                and type(row[2]) == str
                                and type(row[3]) == str
                                and type(row[4]) == str
                                and type(row[5]) == float and row[6] % 1 == 0
                                and type(row[6]) == float and row[6] % 1 == 0
                                and type(row[7]) == float
                                and type(row[8]) == float and row[8] % 1 == 0
                                and type(row[9]) == float and row[9] % 1 == 0
                                and type(row[10]) == float
                                and type(row[11]) == float and row[11] % 1 == 0
                                and type(row[12]) == float and row[12] % 1 == 0
                                and type(row[13]) == float
                                and type(row[14]) == float
                                and type(row[15]) == float and row[15] % 1 == 0
                                and type(row[16]) == float and row[16] % 1 == 0
                                and type(row[17]) == float and row[17] % 1 == 0
                                and type(row[18]) == float
                                and type(row[19]) == float and row[19] % 1 == 0
                                and type(row[20]) == float and row[20] % 1 == 0
                                and type(row[21]) == float and row[21] % 1 == 0
                                and type(row[22]) == float and row[22] % 1 == 0
                                and type(row[23]) == float and row[23] % 1 == 0
                                and type(row[24]) == float and row[24] % 1 == 0
                                and type(row[25]) == float and row[25] % 1 == 0
                                and type(row[26]) == float and row[26] % 1 == 0
                                and type(row[27]) == float
                                and type(row[28]) == float
                                and type(row[29]) == float
                                and type(row[30]) == float
                                and type(row[31]) == float
                                and type(row[32]) == float and row[32] % 1 == 0
                                and type(row[33]) == float and row[33] % 1 == 0
                                and type(row[34]) == float and row[34] % 1 == 0
                                and type(row[35]) == float
                                and type(row[36]) == float and row[36] % 1 == 0
                                and type(row[37]) == float and row[37] % 1 == 0
                                and type(row[38]) == float and row[38] % 1 == 0
                                and type(row[39]) == float and row[39] % 1 == 0
                                and type(row[40]) == float and row[40] % 1 == 0
                                and type(row[41]) == float and row[41] % 1 == 0
                        ):
                            # date = d
                            print(type(row[0]))
                            print(row[0])
                            date = date_transform(row[0])
                            workList.append(Tbkpi(starttime=date, turnround=row[1], name=row[2], cell_multi=row[3],
                                                  cell=row[4], suc_time=row[5], req_time=row[6], rrc_suc_rate=row[7],
                                                  suc_total=row[8], try_total=row[9], e_rab_suc_rate=row[10],
                                                  enodeb_exception=row[11],
                                                  cell_exception=row[12], e_rab_offline=row[13], ay=row[14],
                                                  enodeb_release_time=row[15],
                                                  ue_context_exception_time=row[16], ue_context_suc_time=row[17],
                                                  wifi_offline_rate=row[18], t_field=row[19],
                                                  u_field=row[20], v_field=row[21], w_field=row[22], x_field=row[23],
                                                  y_field=row[24], z_field=row[25], aa_field=row[26], ab_field=row[27],
                                                  ac_field=row[28], ad_field=row[29], ae_field=row[30],
                                                  af_field=row[31], ag_field=row[32], ah_field=row[33],
                                                  ai_field=row[34], aj_field=row[35],
                                                  ak_field=row[36], al_field=row[37],
                                                  am_field=row[38], an_field=row[39],
                                                  ao_field=row[40], ap_field=row[41],
                                                  ))
                            successLines = successLines + 1
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")

                    if successLines % 500 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        bar_value = successLines / (successLines + failLines)
                        print("已插入到")
                        print(successLines)
                        print("fail")
                        print(failLines)
                        print(type(row[1]))
                        # print("已插入到第n行")
                        Tbkpi.objects.bulk_create(workList)
                        workList = []
            elif 'tbCell' == name_excel:
                time1 = time.time()
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if (type(row[0]) == str and type(row[1]) == str and type(row[2]) == str
                                and type(row[3]) == float and row[3] % 1 == 0 and type(row[4]) == str
                                and type(row[5]) == float and row[5] % 1 == 0
                                and type(row[6]) == float and row[6] % 1 == 0 and type(row[7]) == float and row[
                                    7] % 1 == 0
                                and type(row[8]) == float and row[8] % 1 == 0
                                and type(row[9]) == float and row[9] % 1 == 0 and type(row[10]) == str
                                and type(row[11]) == float
                                and type(row[12]) == float and type(row[13]) == str and type(row[14]) == float
                                and type(row[15]) == float and type(row[16]) == float and type(row[17]) == float
                                and type(row[18]) == float):  # 判断用户名是否为字符串
                            workList.append(Tbcell(city=row[0],
                                                   sector_id=row[1],
                                                   sector_name=row[2],
                                                   enodebid=row[3],
                                                   enodeb_name=row[4],
                                                   earfcn=row[5],
                                                   pci=row[6],
                                                   pss=row[7],
                                                   sss=row[8],
                                                   tac=row[9],
                                                   vendor=row[10],
                                                   longitude=row[11],
                                                   latitude=row[12],
                                                   style=row[13],
                                                   azimuth=row[14],
                                                   height=row[15],
                                                   electtilt=row[16],
                                                   mechtilt=row[17],
                                                   totletilt=row[18]))
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 1000 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        bar_value = successLines / table.nrows
                        print("上传进度：")
                        print(bar_value)
                        time2 = time.time()
                        print("success:")
                        print(successLines)
                        print("fail:")
                        print(failLines)
                        print(type(row[0]))
                        # print("已插入到第n行")
                        bulk_re = Tbcell.objects.bulk_create(workList)
                        print(bulk_re)
                        workList = []
            elif 'tbPRB' == name_excel:
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if (type(row[1]) == float and row[1] % 1 == 0
                            and type(row[2]) == str
                            and type(row[3]) == str
                            and type(row[4]) == str
                            and type(row[5]) == float and type(row[6]) == float and type(row[7]) == float
                            and type(row[8]) == float and type(row[9]) == float and type(row[10]) == float
                            and type(row[11]) == float and type(row[12]) == float and type(row[13]) == float
                            and type(row[14]) == float and type(row[15]) == float and type(row[16]) == float
                            and type(row[17]) == float and type(row[18]) == float and type(row[19]) == float
                            and type(row[20]) == float and type(row[21]) == float and type(row[22]) == float
                            and type(row[23]) == float and type(row[24]) == float and type(row[25]) == float
                            and type(row[26]) == float and type(row[27]) == float and type(row[28]) == float
                            and type(row[29]) == float and type(row[30]) == float and type(row[31]) == float
                            and type(row[32]) == float and type(row[33]) == float and type(row[34]) == float
                            and type(row[35]) == float and type(row[36]) == float and type(row[37]) == float
                            and type(row[38]) == float and type(row[39]) == float and type(row[40]) == float
                            and type(row[41]) == float and type(row[42]) == float and type(row[43]) == float
                            and type(row[44]) == float and type(row[45]) == float and type(row[46]) == float
                            and type(row[47]) == float and type(row[48]) == float and type(row[49]) == float
                            and type(row[50]) == float
                            and type(row[51]) == float and type(row[52]) == float and type(row[53]) == float
                            and type(row[54]) == float and type(row[55]) == float and type(row[56]) == float
                            and type(row[57]) == float and type(row[58]) == float and type(row[59]) == float
                            and type(row[60]) == float
                            and type(row[61]) == float and type(row[62]) == float and type(row[63]) == float
                            and type(row[64]) == float and type(row[65]) == float and type(row[66]) == float
                            and type(row[67]) == float and type(row[68]) == float and type(row[69]) == float
                            and type(row[70]) == float
                            and type(row[71]) == float and type(row[72]) == float and type(row[73]) == float
                            and type(row[74]) == float and type(row[75]) == float and type(row[76]) == float
                            and type(row[77]) == float and type(row[78]) == float and type(row[79]) == float
                            and type(row[80]) == float
                            and type(row[81]) == float and type(row[82]) == float and type(row[83]) == float
                            and type(row[84]) == float and type(row[85]) == float and type(row[86]) == float
                            and type(row[87]) == float and type(row[88]) == float and type(row[89]) == float
                            and type(row[90]) == float
                            and type(row[91]) == float and type(row[92]) == float and type(row[93]) == float
                            and type(row[94]) == float and type(row[95]) == float and type(row[96]) == float
                            and type(row[97]) == float and type(row[98]) == float and type(row[99]) == float
                            and type(row[100]) == float
                            and type(row[101]) == float and type(row[102]) == float and type(row[103]) == float
                            and type(row[104]) == float
                        ):
                            #date = d
                            #print(type(row[0]))
                            #print(row[0])
                            #date = datetime_transform(row[0])
                            date = datetime.strptime(row[0], "%m/%d/%Y %X")
                            print(date)
                            workList.append(Tbprb(starttime=date, turnround=row[1],  name=row[2], cell=row[3],
                                                  cell_name=row[4],
                                                  prb0=row[5], prb1=row[6], prb2=row[7], prb3=row[8],
                                                  prb4=row[9], prb5=row[10], prb6=row[11], prb7=row[12],
                                                  prb8=row[13], prb9=row[14], prb10=row[15], prb11=row[16],
                                                  prb12=row[17], prb13=row[18], prb14=row[19], prb15=row[20],
                                                  prb16=row[21], prb17=row[22], prb18=row[23], prb19=row[24],
                                                  prb20=row[25], prb21=row[26], prb22=row[27], prb23=row[28],
                                                  prb24=row[29], prb25=row[30], prb26=row[31], prb27=row[32],
                                                  prb28=row[33], prb29=row[34], prb30=row[35], prb31=row[36],
                                                  prb32=row[37], prb33=row[38], prb34=row[39], prb35=row[40],
                                                  prb36=row[41], prb37=row[42], prb38=row[43], prb39=row[44],
                                                  prb40=row[45], prb41=row[46], prb42=row[47], prb43=row[48],
                                                  prb44=row[49], prb45=row[50], prb46=row[51], prb47=row[52],
                                                  prb48=row[53], prb49=row[54], prb50=row[55], prb51=row[56],
                                                  prb52=row[57], prb53=row[58], prb54=row[59], prb55=row[60],
                                                  prb56=row[61], prb57=row[62], prb58=row[63], prb59=row[64],
                                                  prb60=row[65], prb61=row[66], prb62=row[67], prb63=row[68],
                                                  prb64=row[69], prb65=row[70], prb66=row[71], prb67=row[72],
                                                  prb68=row[73], prb69=row[74], prb70=row[75], prb71=row[76],
                                                  prb72=row[77], prb73=row[78], prb74=row[79], prb75=row[80],
                                                  prb76=row[81], prb77=row[82], prb78=row[83], prb79=row[84],
                                                  prb80=row[85], prb81=row[86], prb82=row[87], prb83=row[88],
                                                  prb84=row[89], prb85=row[90], prb86=row[91], prb87=row[92],
                                                  prb88=row[93], prb89=row[94], prb90=row[95], prb91=row[96],
                                                  prb92=row[97], prb93=row[98], prb94=row[99], prb95=row[100],
                                                  prb96=row[101], prb97=row[102], prb98=row[103], prb99=row[104],
                                                  ))
                            successLines = successLines + 1
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")

                    if successLines % 10000 == 0:  # 每五行进行一次插入
                        bar_value = successLines / (successLines + failLines)
                        time2 = time.time()
                        print("绑定列属性用时")
                        print(time2 - time1)
                        print("已插入到")
                        print(successLines)
                        # print("已插入到第n行")
                        Tbprb.objects.bulk_create(workList)
                        time3 = time.time()
                        print("写入数据库用时")
                        print(time3 - time2)
                        workList = []
                Tbprb.objects.bulk_create(workList)
            elif 'tbSecAdjcell' == name_excel:
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if type(row[0]) == str and type(row[1]) == str:
                            workList.append(Tbsecadjcell(s_sector_id=row[0], n_sector_id=row[1]))
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 500 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        bar_value = successLines / (successLines + failLines)
                        print("已插入到")
                        print(successLines)
                        print(type(row[0]))
                        # print("已插入到第n行")
                        Tbsecadjcell.objects.bulk_create(workList)
                        workList = []
        elif 'csv' == type_excel:
            print("csv")
            if 'tbMROData' == name_excel:
                print("打开了MRO")
                temp_data = file_obj.read().decode('ascii', 'ignore')
                print(temp_data)
                print(type(temp_data))
                dataFile = StringIO(temp_data)
                table = csv.reader(dataFile)
                print("读取文件结束，准备导入！")
                print(type(table))
                print(table)
                successLines = 1
                workList = []
                next(table)
                failLines = 0
                time1 = time.time()
                for row in table:
                    #print(line)
                    #print(type(line ))
                    #row = line.split(",")
                    row[3:7] = list(map(eval, row[3:7]))  # 使用map和eval函数批量将字符串转化成整型或浮点型
                    workList.append(Tbmrodata(timestamp=row[0], servingsector=row[1], interferingsector=row[2],
                                              ltescrsrp=row[3], ltencrsrp=row[4], ltencearfcn=row[5],
                                              ltencpci=row[6])
                                    )
                    successLines = successLines + 1
                    if successLines % 50000 == 0:  # 每五行进行一次插入
                        bar_value = successLines / (successLines + failLines)
                        time2 = time.time()
                        print("绑定列属性用时")
                        print(time2 - time1)
                        print("已插入到")
                        print(successLines)
                        Tbmrodata.objects.bulk_create(workList)
                        time3 = time.time()
                        print("写入数据库用时")
                        print(time3 - time2)
                        workList = []
                        time1 = time.time()
                Tbmrodata.objects.bulk_create(workList)
        else:
            return render_to_response("uploadtbCell.html")
        bar_value = 1.0
        return render_to_response("uploadtbCell.html")
    return render_to_response("uploadtbCell.html")


###############
    return render_to_response("uploadtbCell.html")


def import_table_from_excel(request):
    if request.method == "POST":
        c = ChooseForm(request.POST)
        print(c)
        if c.is_valid():
            table_choose = c.cleaned_data["table_choose"]
            if table_choose == '1':
                data = xlrd.open_workbook(r'C:\Users\wansh\Desktop\tbCell.xlsx')
                print("读取文件结束，准备导入！")
                table = data.sheet_by_index(0)
                successLines= 1
                workList = []
                failLines = 0
                time1 = time.time()
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:     #检查是否为空行
                        if (type(row[0]) == str and type(row[1]) == str and type(row[2]) == str
                            and type(row[3]) == float and row[3] % 1 == 0 and type(row[4]) == str
                            and type(row[5]) == float and row[5] % 1 == 0
                            and type(row[6]) == float and row[6] % 1 == 0 and type(row[7]) == float and row[7] % 1 == 0
                            and type(row[8]) == float and row[8] % 1 == 0
                            and type(row[9]) == float and row[9] % 1 == 0 and type(row[10]) == str
                            and type(row[11]) == float
                            and type(row[12]) == float and type(row[13]) == str and type(row[14]) == float
                            and type(row[15]) == float and type(row[16]) == float and type(row[17]) == float
                            and type(row[18]) == float):     #判断用户名是否为字符串
                            workList.append(Tbcell(city=row[0],
                                                   sector_id=row[1],
                                                   sector_name=row[2],
                                                   enodebid=row[3],
                                                   enodeb_name=row[4],
                                                   earfcn=row[5],
                                                   pci=row[6],
                                                   pss=row[7],
                                                   sss=row[8],
                                                   tac=row[9],
                                                   vendor=row[10],
                                                   longitude=row[11],
                                                   latitude=row[12],
                                                   style=row[13],
                                                   azimuth=row[14],
                                                   height=row[15],
                                                   electtilt=row[16],
                                                   mechtilt=row[17],
                                                   totletilt=row[18]))
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 1000 == 0 or successLines + failLines >= table.nrows:      #每五行进行一次插入
                        time2 = time.time()
                        print("success:")
                        print(successLines)
                        print("fail:")
                        print(failLines)
                        print(type(row[0]))
                        #print("已插入到第n行")
                        Tbcell.objects.bulk_create(workList)
                        workList = []
                return HttpResponse("tbCell Upload Success!")

            elif table_choose == '2':
                data = xlrd.open_workbook(r'C:\Users\wansh\Desktop\tbSecAdjCell.xlsx')
                print("读取文件结束，准备导入！")
                table = data.sheet_by_index(0)
                successLines = 1
                workList = []
                failLines = 0
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if type(row[0]) == str and type(row[1]) == str:
                            workList.append(Tbsecadjcell(s_sector_id=row[0], n_sector_id=row[1]))
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 500 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        print("已插入到")
                        print(successLines)
                        print(type(row[0]))
                        # print("已插入到第n行")
                        Tbsecadjcell.objects.bulk_create(workList)
                        workList = []
                return HttpResponse("tbSecAdjCell Upload Success!")
            elif table_choose == '3':
                data = xlrd.open_workbook(r'C:\Users\wansh\Desktop\tbOptCell.xlsx')
                print("读取文件结束，准备导入！")
                table = data.sheet_by_index(0)
                successLines = 1
                workList = []
                failLines = 0
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if type(row[0]) == str and type(row[1]) == float and row[1] % 1 == 0 and type(row[2]) == str:
                            workList.append(Tboptcell(sector_id=row[0], earfcn=row[1], cell_type=row[2]))
                        else:
                            failLines = failLines + 1
                            print(successLines+failLines)
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")
                    successLines = successLines + 1
                    if successLines % 500 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        print("已插入到")
                        print(successLines)
                        print(type(row[1]))
                        # print("已插入到第n行")
                        Tboptcell.objects.bulk_create(workList)
                        workList = []
                return HttpResponse("tbOptCell Upload Success!")
            elif table_choose == '4':
                data = xlrd.open_workbook(r'C:\Users\wansh\Desktop\tbKpi.xlsx')
                print("读取文件结束，准备导入！")
                table = data.sheet_by_index(0)
                successLines = 1
                workList = []
                failLines = 0
                print(table.nrows)
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if (type(row[1]) == float and row[1] % 1 == 0
                            and type(row[2]) == str
                            and type(row[3]) == str
                            and type(row[4]) == str
                            and type(row[5]) == float and row[6] % 1 == 0
                            and type(row[6]) == float and row[6] % 1 == 0
                            and type(row[7]) == float
                            and type(row[8]) == float and row[8] % 1 == 0
                            and type(row[9]) == float and row[9] % 1 == 0
                            and type(row[10]) == float
                            and type(row[11]) == float and row[11] % 1 == 0
                            and type(row[12]) == float and row[12] % 1 == 0
                            and type(row[13]) == float
                            and type(row[14]) == float
                            and type(row[15]) == float and row[15] % 1 == 0
                            and type(row[16]) == float and row[16] % 1 == 0
                            and type(row[17]) == float and row[17] % 1 == 0
                            and type(row[18]) == float
                            and type(row[19]) == float and row[19] % 1 == 0
                            and type(row[20]) == float and row[20] % 1 == 0
                            and type(row[21]) == float and row[21] % 1 == 0
                            and type(row[22]) == float and row[22] % 1 == 0
                            and type(row[23]) == float and row[23] % 1 == 0
                            and type(row[24]) == float and row[24] % 1 == 0
                            and type(row[25]) == float and row[25] % 1 == 0
                            and type(row[26]) == float and row[26] % 1 == 0
                            and type(row[27]) == float
                            and type(row[28]) == float
                            and type(row[29]) == float
                            and type(row[30]) == float
                            and type(row[31]) == float
                            and type(row[32]) == float and row[32] % 1 == 0
                            and type(row[33]) == float and row[33] % 1 == 0
                            and type(row[34]) == float and row[34] % 1 == 0
                            and type(row[35]) == float
                            and type(row[36]) == float and row[36] % 1 == 0
                            and type(row[37]) == float and row[37] % 1 == 0
                            and type(row[38]) == float and row[38] % 1 == 0
                            and type(row[39]) == float and row[39] % 1 == 0
                            and type(row[40]) == float and row[40] % 1 == 0
                            and type(row[41]) == float and row[41] % 1 == 0
                        ):
                            #date = d
                            print(type(row[0]))
                            print(row[0])
                            date = date_transform(row[0])
                            workList.append(Tbkpi(starttime=date, turnround=row[1],  name=row[2], cell_multi=row[3],
                                                  cell=row[4], suc_time=row[5], req_time=row[6], rrc_suc_rate=row[7],
                                                  suc_total=row[8], try_total=row[9], e_rab_suc_rate=row[10],
                                                  enodeb_exception=row[11],
                                                  cell_exception=row[12], e_rab_offline=row[13], ay=row[14],
                                                  enodeb_release_time=row[15],
                                                  ue_context_exception_time=row[16], ue_context_suc_time=row[17],
                                                  wifi_offline_rate=row[18], t_field=row[19],
                                                  u_field=row[20], v_field=row[21], w_field=row[22], x_field=row[23],
                                                  y_field=row[24], z_field=row[25], aa_field=row[26], ab_field=row[27],
                                                  ac_field=row[28], ad_field=row[29], ae_field=row[30],
                                                  af_field=row[31], ag_field=row[32], ah_field=row[33],
                                                  ai_field=row[34], aj_field=row[35],
                                                  ak_field=row[36], al_field=row[37],
                                                  am_field=row[38], an_field=row[39],
                                                  ao_field=row[40], ap_field=row[41],
                                                  ))
                            successLines = successLines + 1
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")

                    if successLines % 500 == 0 or successLines + failLines >= table.nrows:  # 每五行进行一次插入
                        print("已插入到")
                        print(successLines)
                        print("fail")
                        print(failLines)
                        print(type(row[1]))
                        # print("已插入到第n行")
                        Tbkpi.objects.bulk_create(workList)
                        workList = []
                return HttpResponse("tbKpi Upload Success!")
            elif table_choose == '5':
                print("准备打开PRB")
                time_ofs = time.time()
                data = xlrd.open_workbook(r'C:\Users\wansh\Desktop\tbPRB.xlsx')
                time_ofe = time.time()
                print("读取文件结束，用时")
                print(time_ofe-time_ofs)
                print("开始导入数据库")
                table = data.sheet_by_index(0)
                successLines = 1
                workList = []
                failLines = 0
                print(table.nrows)
                time1 = time.time()
                for line in range(1, table.nrows):
                    row = table.row_values(line)
                    if row:  # 检查是否为空行
                        if (type(row[1]) == float and row[1] % 1 == 0
                            and type(row[2]) == str
                            and type(row[3]) == str
                            and type(row[4]) == str
                            and type(row[5]) == float and type(row[6]) == float and type(row[7]) == float
                            and type(row[8]) == float and type(row[9]) == float and type(row[10]) == float
                            and type(row[11]) == float and type(row[12]) == float and type(row[13]) == float
                            and type(row[14]) == float and type(row[15]) == float and type(row[16]) == float
                            and type(row[17]) == float and type(row[18]) == float and type(row[19]) == float
                            and type(row[20]) == float and type(row[21]) == float and type(row[22]) == float
                            and type(row[23]) == float and type(row[24]) == float and type(row[25]) == float
                            and type(row[26]) == float and type(row[27]) == float and type(row[28]) == float
                            and type(row[29]) == float and type(row[30]) == float and type(row[31]) == float
                            and type(row[32]) == float and type(row[33]) == float and type(row[34]) == float
                            and type(row[35]) == float and type(row[36]) == float and type(row[37]) == float
                            and type(row[38]) == float and type(row[39]) == float and type(row[40]) == float
                            and type(row[41]) == float and type(row[42]) == float and type(row[43]) == float
                            and type(row[44]) == float and type(row[45]) == float and type(row[46]) == float
                            and type(row[47]) == float and type(row[48]) == float and type(row[49]) == float
                            and type(row[50]) == float
                            and type(row[51]) == float and type(row[52]) == float and type(row[53]) == float
                            and type(row[54]) == float and type(row[55]) == float and type(row[56]) == float
                            and type(row[57]) == float and type(row[58]) == float and type(row[59]) == float
                            and type(row[60]) == float
                            and type(row[61]) == float and type(row[62]) == float and type(row[63]) == float
                            and type(row[64]) == float and type(row[65]) == float and type(row[66]) == float
                            and type(row[67]) == float and type(row[68]) == float and type(row[69]) == float
                            and type(row[70]) == float
                            and type(row[71]) == float and type(row[72]) == float and type(row[73]) == float
                            and type(row[74]) == float and type(row[75]) == float and type(row[76]) == float
                            and type(row[77]) == float and type(row[78]) == float and type(row[79]) == float
                            and type(row[80]) == float
                            and type(row[81]) == float and type(row[82]) == float and type(row[83]) == float
                            and type(row[84]) == float and type(row[85]) == float and type(row[86]) == float
                            and type(row[87]) == float and type(row[88]) == float and type(row[89]) == float
                            and type(row[90]) == float
                            and type(row[91]) == float and type(row[92]) == float and type(row[93]) == float
                            and type(row[94]) == float and type(row[95]) == float and type(row[96]) == float
                            and type(row[97]) == float and type(row[98]) == float and type(row[99]) == float
                            and type(row[100]) == float
                            and type(row[101]) == float and type(row[102]) == float and type(row[103]) == float
                            and type(row[104]) == float
                        ):
                            #date = d
                            #print(type(row[0]))
                            #print(row[0])
                            #date = datetime_transform(row[0])
                            date = datetime.strptime(row[0], "%m/%d/%Y %X")
                            print(date)
                            workList.append(Tbprb(starttime=date, turnround=row[1],  name=row[2], cell=row[3],
                                                  cell_name=row[4],
                                                  prb0=row[5], prb1=row[6], prb2=row[7], prb3=row[8],
                                                  prb4=row[9], prb5=row[10], prb6=row[11], prb7=row[12],
                                                  prb8=row[13], prb9=row[14], prb10=row[15], prb11=row[16],
                                                  prb12=row[17], prb13=row[18], prb14=row[19], prb15=row[20],
                                                  prb16=row[21], prb17=row[22], prb18=row[23], prb19=row[24],
                                                  prb20=row[25], prb21=row[26], prb22=row[27], prb23=row[28],
                                                  prb24=row[29], prb25=row[30], prb26=row[31], prb27=row[32],
                                                  prb28=row[33], prb29=row[34], prb30=row[35], prb31=row[36],
                                                  prb32=row[37], prb33=row[38], prb34=row[39], prb35=row[40],
                                                  prb36=row[41], prb37=row[42], prb38=row[43], prb39=row[44],
                                                  prb40=row[45], prb41=row[46], prb42=row[47], prb43=row[48],
                                                  prb44=row[49], prb45=row[50], prb46=row[51], prb47=row[52],
                                                  prb48=row[53], prb49=row[54], prb50=row[55], prb51=row[56],
                                                  prb52=row[57], prb53=row[58], prb54=row[59], prb55=row[60],
                                                  prb56=row[61], prb57=row[62], prb58=row[63], prb59=row[64],
                                                  prb60=row[65], prb61=row[66], prb62=row[67], prb63=row[68],
                                                  prb64=row[69], prb65=row[70], prb66=row[71], prb67=row[72],
                                                  prb68=row[73], prb69=row[74], prb70=row[75], prb71=row[76],
                                                  prb72=row[77], prb73=row[78], prb74=row[79], prb75=row[80],
                                                  prb76=row[81], prb77=row[82], prb78=row[83], prb79=row[84],
                                                  prb80=row[85], prb81=row[86], prb82=row[87], prb83=row[88],
                                                  prb84=row[89], prb85=row[90], prb86=row[91], prb87=row[92],
                                                  prb88=row[93], prb89=row[94], prb90=row[95], prb91=row[96],
                                                  prb92=row[97], prb93=row[98], prb94=row[99], prb95=row[100],
                                                  prb96=row[101], prb97=row[102], prb98=row[103], prb99=row[104],
                                                  ))
                            successLines = successLines + 1
                        else:
                            failLines = failLines + 1
                            print("有数据类型不对")
                    else:
                        failLines = failLines + 1
                        print("出现空行！")

                    if successLines % 10000 == 0:  # 每五行进行一次插入
                        time2 = time.time()
                        print("绑定列属性用时")
                        print(time2 - time1)
                        print("已插入到")
                        print(successLines)
                        # print("已插入到第n行")
                        Tbprb.objects.bulk_create(workList)
                        time3 = time.time()
                        print("写入数据库用时")
                        print(time3 - time2)
                        workList = []
                Tbprb.objects.bulk_create(workList)
                return HttpResponse("tbPRB Upload Success!")
            elif table_choose == '6':
                table = open(r'C:\Users\wansh\Desktop\tbMROData.csv')
                print("读取文件结束，准备导入！")
                successLines = 1
                workList = []
                next(table)
                failLines = 0
                time1 = time.time()
                for line in table:
                    row = line.split(",")
                    row[3:7] = list(map(eval, row[3:7]))    #使用map和eval函数批量将字符串转化成整型或浮点型
                    workList.append(Tbmrodata(timestamp=row[0], servingsector=row[1], interferingsector=row[2],
                                              ltescrsrp=row[3], ltencrsrp=row[4], ltencearfcn=row[5],
                                              ltencpci=row[6])
                                    )
                    successLines = successLines + 1
                    if successLines % 50000 == 0:  # 每五行进行一次插入
                        time2 = time.time()
                        print("绑定列属性用时")
                        print(time2-time1)
                        print("已插入到")
                        print(successLines)
                        Tbmrodata.objects.bulk_create(workList)
                        time3 = time.time()
                        print("写入数据库用时")
                        print(time3-time2)
                        workList = []
                        time1 = time.time()
                Tbmrodata.objects.bulk_create(workList)
                return HttpResponse("tbMROData Upload Success!")
            elif table_choose == '7':       #导入txt格式的PRB表格
                time_ofs = time.time()
                table = open(r'C:\Users\wansh\Desktop\tbPRB.txt')
                time_ofe = time.time()
                print("读物文件用时：")
                print(time_ofe-time_ofs)
                print("读取文件结束，准备导入！")
                successLines = 1
                workList = []
                next(table)
                failLines = 0
                time1 = time.time()
                for line in table:
                    row = line.split("\t")
                    date = datetime.strptime(row[0], "%m/%d/%Y %X")
                    row[5:105] = list(map(eval, row[5:105]))
                    workList.append(Tbprb(starttime=date, turnround=row[1], name=row[2], cell=row[3],
                                          cell_name=row[4],
                                          prb0=row[5], prb1=row[6], prb2=row[7], prb3=row[8],
                                          prb4=row[9], prb5=row[10], prb6=row[11], prb7=row[12],
                                          prb8=row[13], prb9=row[14], prb10=row[15], prb11=row[16],
                                          prb12=row[17], prb13=row[18], prb14=row[19], prb15=row[20],
                                          prb16=row[21], prb17=row[22], prb18=row[23], prb19=row[24],
                                          prb20=row[25], prb21=row[26], prb22=row[27], prb23=row[28],
                                          prb24=row[29], prb25=row[30], prb26=row[31], prb27=row[32],
                                          prb28=row[33], prb29=row[34], prb30=row[35], prb31=row[36],
                                          prb32=row[37], prb33=row[38], prb34=row[39], prb35=row[40],
                                          prb36=row[41], prb37=row[42], prb38=row[43], prb39=row[44],
                                          prb40=row[45], prb41=row[46], prb42=row[47], prb43=row[48],
                                          prb44=row[49], prb45=row[50], prb46=row[51], prb47=row[52],
                                          prb48=row[53], prb49=row[54], prb50=row[55], prb51=row[56],
                                          prb52=row[57], prb53=row[58], prb54=row[59], prb55=row[60],
                                          prb56=row[61], prb57=row[62], prb58=row[63], prb59=row[64],
                                          prb60=row[65], prb61=row[66], prb62=row[67], prb63=row[68],
                                          prb64=row[69], prb65=row[70], prb66=row[71], prb67=row[72],
                                          prb68=row[73], prb69=row[74], prb70=row[75], prb71=row[76],
                                          prb72=row[77], prb73=row[78], prb74=row[79], prb75=row[80],
                                          prb76=row[81], prb77=row[82], prb78=row[83], prb79=row[84],
                                          prb80=row[85], prb81=row[86], prb82=row[87], prb83=row[88],
                                          prb84=row[89], prb85=row[90], prb86=row[91], prb87=row[92],
                                          prb88=row[93], prb89=row[94], prb90=row[95], prb91=row[96],
                                          prb92=row[97], prb93=row[98], prb94=row[99], prb95=row[100],
                                          prb96=row[101], prb97=row[102], prb98=row[103], prb99=row[104],
                                          ))
                    successLines = successLines + 1
                    if successLines % 10000 == 0:  # 每五行进行一次插入
                        time2 = time.time()
                        print("绑定列属性用时")
                        print(time2-time1)
                        print("已插入到")
                        print(successLines)
                        Tbprb.objects.bulk_create(workList)
                        time3 = time.time()
                        print("写入数据库用时")
                        print(time3-time2)
                        workList = []
                        time1 = time.time()
                Tbprb.objects.bulk_create(workList)
                return HttpResponse("tbPRB.txt Upload Success!")
            elif table_choose == 'a':
                tb_opt = Tboptcell.objects.all()
                print(type(tb_opt))
                print(tb_opt)
                return render_to_response("stest.html", {"table": tb_opt})
            else:
                return render(request, "test.html", )
        else:
            return render(request, "test.html", )
    else:
        return render(request, "test.html",)



def login(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        #print(uf)
        if uf.is_valid():   #登录
            username = uf.cleaned_data["username"]
            password = uf.cleaned_data["password"]
            userFilter = Userlist2.objects.filter(username=username, password=password)
            if len(userFilter) > 0:
                print("登陆成功")
                return render_to_response("User.html", {"logResult": "YES"})
            else:
                print("登陆失败")
                result = False
                return render_to_response("first.html", {"logResult": "NO"})
            #print("获得POST")
        else:       #注册
            uf = RegUserForm(request.POST)
            #print(uf)
            #print(type(uf))
            if uf.is_valid():
                Regusername = uf.cleaned_data["Regusername"]
                Regpassword = uf.cleaned_data["Regpassword"]
                user_type = uf.cleaned_data["user_type"]
                userFilter = Userlist2.objects.filter(username=Regusername)
                if len(userFilter) > 0:
                    return render_to_response("first.html", {"regResult": "用户名已存在"})
                else:
                    if user_type == 'VIP':
                        Userlist2.objects.create(username=Regusername, password=Regpassword, type=1, state=0)
                    else:
                        Userlist2.objects.create(username=Regusername, password=Regpassword, type=0, state=0)
                    return render_to_response("first.html", {"regResult": "注册成功"})
    return render_to_response("first.html")




    return render_to_response("first.html")


def user(request):
    return render_to_response("User.html")

def uploadTbCell(request):
    return render_to_response("uploadtbCell.html")


def date_transform(raw_date):
    temp1 = raw_date.split()
    #print(temp1)
    temp2 = temp1[0].split('/')
    temp3 = '-'
    temp4 = ['', '', '']
    temp4[0] = temp2[2]
    temp4[2] = temp2[1]
    temp4[1] = temp2[0]
    date = temp3.join(temp4)
    #print(date)
    return date

def datetime_transform(raw_datetime):
    temp1 = raw_datetime.split()
    #print(temp1)
    temp2 = temp1[0].split('/')
    temp3 = '/'
    temp4 = ['', '', '']
    temp4[0] = temp2[2]
    temp4[2] = temp2[1]
    temp4[1] = temp2[0]
    date = temp3.join(temp4)
    temp5 = [' ', ' ']
    temp5[0] = date
    temp5[1] = temp1[1]
    temp6 = ' '
    datetime = temp6.join(temp5)
    print(datetime)
    #print(date)
    return datetime


#数据导出



def download_table(request):
    if request.method == "POST":
        df = DownloadForm(request.POST)
        if df.is_valid():
            down_file = df.cleaned_data["down_file"]
            if down_file == 'tbOptCell':
                tb_Opt = Tboptcell.objects.all()
                Opt_lenth = len(tb_Opt)
                print(len(tb_Opt))
                print(type(tb_Opt))
                return render_to_response("download.html", {"Opt_table": tb_Opt, 'tb_Name': 'tbOptCell'})
            elif down_file == 'tbATUHandOver':
                tb_ATU = Tbatuhandover.objects.all()
                print(tb_ATU)
                return render_to_response("download.html", {"ATU_table": tb_ATU, 'tb_Name': 'tbATUHandover'})
            elif down_file == 'tbAdjCell':
                tb_Adj = Tbadjcell.objects.all()
                print(tb_Adj)
                return render_to_response("download.html", {"Adj_table": tb_Adj, 'tb_Name': 'tbAdjCell'})

    return render_to_response("download.html")


def download_data(request):
    if request.method == "POST":
        c = ChooseForm(request.POST)
        #if c.is_valid():
        download_choose = c.cleaned_data["table_choose"]
        print("????")
        if download_choose == '1':
            tb_opt = Tboptcell.objects.all()
            print(type(tb_opt))
            return render_to_response("stest.html", {"table": tb_opt})
       # else:
       #     return HttpResponse("表格没有数据")
    else:
        return render(request, "dtest.html",)


def search_sql_cell(request):
    cursor = connection.cursor()
    """
    # Data modifying operation - commit required
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()
    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()
    """
    idList = list(Tbcell.objects.values("sector_id").all().distinct())
    cursor.execute("select distinct SECTOR_ID from TbCell ",)
    nameList = cursor.fetchall()

    print("namelist:")
    print(idList)
    print(type(nameList))
    print(nameList)
    print("名字？？？")
    if request.method == "POST":
        print("POST")
        stf = SearchTbCellForm(request.POST)
        if stf.is_valid():
            index = stf.cleaned_data["index"]
            print(type(index))
            print(index)
            print(type(idList[0]))
            index = {'sector_id': index}
            print(type(index))
            print(index)
            if index in idList:  # 按照ID查询
                print("按ID查询")
                id = str(index.get('sector_id'))
                # Data modifying operation - commit required
                print(type(id))
                print(id)
                id = [id]
                print(type(id))
                print(id)
                cursor.execute("select * from TbCell where SECTOR_ID = %s", id)
                data = cursor.fetchone()
                print(type(data))
                print(data)
                #transaction.commit_unless_managed()

                #dataFilter = Tbcell.objects.filter(sector_id=id)
                #print(dataFilter)
                return render_to_response("searchCell.html", {"result": data})
            elif index in nameList:
                print("按名字查询")
                dataFilter = Tbcell.objects.filter(sector_name=index)
                print(dataFilter)
                return render_to_response("searchCell.html", {"result": dataFilter})
            else:
                print("?????????????????????????????????????????????")
                return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})
    return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})


def tuple_to_cell_dict(data):
    result = {'sector_id': '',}

def search_cell(request):
    idList = list(Tbcell.objects.values("sector_id").all().distinct())
    nameList = Tbcell.objects.values("sector_name").all().distinct()

    print(idList)
    print(nameList)
    if request.method == "POST":
        stf = SearchTbCellForm(request.POST)
        if stf.is_valid():
            index = stf.cleaned_data["index"]
            print(type(index))
            print(index)
            print(type(idList[0]))
            index = {'sector_id': index}
            print(type(index))
            print(index)
            if index in idList:     #按照ID查询
                print("按ID查询")
                id = index.get('sector_id')
                dataFilter = Tbcell.objects.filter(sector_id=id)
                print(dataFilter)
                return render_to_response("searchCell.html", {"result": dataFilter})
            elif index in nameList:
                print("按名字查询")
                dataFilter = Tbcell.objects.filter(sector_name=index)
                print(dataFilter)
                return render_to_response("searchCell.html", {"result": dataFilter})
            else:
                print("?????????????????????????????????????????????")
                return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})
    return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})


def st_norm(u):
    '''标准正态分布'''
    import math
    x = abs(u) / math.sqrt(2)
    T = (0.0705230784, 0.0422820123, 0.0092705272,
         0.0001520143, 0.0002765672, 0.0000430638)
    E = 1 - pow((1 + sum([a * pow(x, (i + 1))
                          for i, a in enumerate(T)])), -16)
    p = 0.5 - 0.5 * E if u < 0 else 0.5 + 0.5 * E
    return (p)


def norm(a, sigma, x):
    '''一般正态分布'''
    u = (x - a) / sigma
    return (st_norm(u))

def progress_bar(request):
    global bar_value
    print("收到请求")
    return HttpResponse(bar_value)

