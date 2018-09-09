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
from Log.models import Tbprbnew
from Log.models import Tbc2Inew
from Log.models import Tbatuc2I
from Log.models import Tbc2I3
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


class SearchKPIForm(forms.Form):
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)
    name = forms.CharField(max_length = 255)
    attr = forms.CharField(max_length = 255)


class SearchPRBForm(forms.Form):
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)
    name = forms.CharField(max_length = 255)
    attr = forms.CharField(max_length = 255)

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
            print("正在读取文件")
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
                            #print(date)
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
                        bar_value = successLines / table.nrows
                        time2 = time.time()
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
                file = file_obj.read()
                temp_data = file.decode('ascii', 'ignore')
                print(temp_data)
                print(type(temp_data))
                dataFile = StringIO(temp_data)
                tb = csv.reader(dataFile)
                count = 0
                for i in tb:
                    count += 1
                print(count)
                temp_data = file.decode('ascii', 'ignore')
                print(temp_data)
                print(type(temp_data))
                dataFile = StringIO(temp_data)
                tb = csv.reader(dataFile)
                table = csv.reader(dataFile)
                print("读取文件结束，准备导入！")
                print(type(table))
                print(table)
                successLines = 1
                workList = []
                next(table)
                failLines = 0
                time1 = time.time()

                print(count)
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
                        bar_value = successLines / count
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

def download_preview(request):
    cursor = connection.cursor()
    if request.method == "POST":
        df = DownloadForm(request.POST)
        if df.is_valid():
            down_file = df.cleaned_data["down_file"]
            print("预览")
            if down_file == 'tbOptCell':
                cursor.execute('select top 100* from tbOptCell')
                tb_Opt = cursor.fetchall()
                # print(tbC2I3)
                result = []
                row = {'sector_id': '', 'earfcn': '', 'cell_type': ''}
                count = 0
                for x in tb_Opt:
                    row['sector_id'] = x[0]
                    row['earfcn'] = x[1]
                    row['cell_type'] = x[2]
                    result.append(row)
                    print(row)
                    row = {'sector_id': '', 'earfcn': '', 'cell_type': ''}
                    count = count + 1
                print(result)
                return render_to_response("download.html",
                                          {"Opt_table": result, 'tb_Name': 'tbOptCell', 'tb_length': count})
            elif down_file == 'tbATUHandOver':
                cursor.execute('select top 100* from tbATUHandover')
                tb_ATU = cursor.fetchall()
                # print(tbC2I3)
                result = []
                row = {'ssector_id': '', 'nsector_id': '', 'hoatt': ''}
                count = 0
                for x in tb_ATU:
                    row['ssector_id'] = x[0]
                    row['nsector_id'] = x[1]
                    row['hoatt'] = x[2]
                    result.append(row)
                    row = {'ssector_id': '', 'nsector_id': '', 'hoatt': ''}
                    count = count + 1
                return render_to_response("download.html",
                                          {"ATU_table": result, 'tb_Name': 'tbATUHandOver', 'tb_length': count})
            elif down_file == 'tbATUC2I':
                cursor.execute('select top 100* from tbATUC2I')
                tb_Adj = cursor.fetchall()
                # print(tbC2I3)
                result = []
                row = {'sector_id': '', 'ncell_id': '', 'ratio_all': '', 'cosite': '','rank': ''}
                count = 0
                for x in tb_Adj:
                    row['sector_id'] = x[0]
                    row['ncell_id'] = x[1]
                    row['ratio_all'] = x[2]
                    row['cosite'] = x[3]
                    row['rank'] = x[4]
                    result.append(row)
                    row = {'sector_id': '', 'ncell_id': '', 'ratio_all': '', 'cosite': '', 'rank': ''}
                    count = count + 1
                return render_to_response("download.html",
                                          {"ATUC2I_table": result, 'tb_Name': 'tbATUC2I', 'tb_length': count})

    return render_to_response("download.html")


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
                return render_to_response("download.html", {"Opt_table": tb_Opt, 'tb_Name': 'tbOptCell', 'tb_length':Opt_lenth})
            elif down_file == 'tbATUHandOver':
                tb_ATU = Tbatuhandover.objects.all()
                print(tb_ATU)
                ATU_lenth = len(tb_ATU)
                return render_to_response("download.html", {"ATU_table": tb_ATU, 'tb_Name': 'tbATUHandOver','tb_length':ATU_lenth})
            elif down_file == 'tbATUC2I':
                tb_Adj = Tbatuc2I.objects.all()
                print(tb_Adj)
                Adj_lenth=len(tb_Adj)
                return render_to_response("download.html", {"ATUC2I_table": tb_Adj, 'tb_Name': 'tbATUC2I', 'tb_length':Adj_lenth})

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


def analyse_C2I(request):
    cursor = connection.cursor()
    print("准备分析")
    compute_C2Inew()
    cursor.execute('select prbc2i9 from tbC2INew')
    data = cursor.fetchone()
    print(data[0])
    if data[0] == None:
        print("C2Inew为空")

        print("计算完成")
        cursor.execute('select * from tbC2INew')
        data = cursor.fetchall()
        print(data)
        for x in data:
            dict = tuple_to_c2i_dict(x)
            prbc2i9 = norm(dict['c2i_mean'], dict['std'], 9)
            prbc2i6 = norm(dict['c2i_mean'], dict['std'], 6)
            if prbc2i9>1:
                print("prbc2i9")
                print(prbc2i9)
            if prbc2i6>1:
                print("prbc2i6")
                print(prbc2i6)
            if dict['scell'] == '253934-0' and dict['ncell'] == '253898-1':
                print("出错行？？？")
                print("prbc2i9")
                print(prbc2i9)
                print("prbc2i6")
                print(prbc2i6)

            cursor.execute('update tbC2INew set prbc2i9 = %s,prbabs6 = %s '
                           'where SCELL= %s and NCELL= %s', (prbc2i9, prbc2i6, dict['scell'], dict['ncell']))

    cursor.execute('select * from tbC2INew')
    data = cursor.fetchall()
    print(data)
    result = []
    for x in data:
        dict = tuple_to_c2i_dict(x)
        result.append(dict)
    #print(results)
    return render_to_response("analyC2I.html", {'tbC2Inew': result})



def tuple_to_c2i_dict(data):
    result = {}
    result['scell'] = data[0]
    result['ncell'] = data[1]
    result['c2i_mean'] = data[2]
    result['std'] = data[3]
    result['prbc2i9'] = data[4]
    result['prbabs6'] = data[5]
    return result


def compute_C2Inew():
    cursor = connection.cursor()
    print("准备调用存储过程")
    cursor.execute("exec create_C2INew")
    #data = cursor.fetchall()
    print("执行完存储过程了")


class AnalyseForm(forms.Form):
    x = forms.FloatField()


"""
控制用户输入的x
"""
def analyse_3cell(request):
    cursor = connection.cursor()
    if request.method == "POST":
        af = AnalyseForm(request.POST)
        if af.is_valid():
            x = af.cleaned_data["x"]
            print(x)
            if x <= 1:
                cursor.execute('exec proc_C2I3 %s', (x,))
                print("完成三元组分析")
                #data = Tbc2I3.objects.all()
                #print(data)
                cursor.execute('select * from tbC2I3')
                tbC2I3 = cursor.fetchall()
                # print(tbC2I3)
                result = []
                row = {'a_id': '', 'b_id': '', 'c_id': ''}
                count = 0
                print(tbC2I3)
                for x in tbC2I3:
                    row['a_id'] = x[0]
                    row['b_id'] = x[1]
                    row['c_id'] = x[2]
                    print("x")
                    print(x)
                    result.append(row)
                    count = count + 1

                print(result)
                print("共有三元组")
                print(count)
                return render_to_response("analy3cell.html", {"triTuple:": result, "count": count})
            else:
                return render_to_response("analy3cell.html")
    return render_to_response("analy3cell.html")


def search_sql_PRB(request):
    nameList = Tbprb.objects.values("name").all().distinct()
    if request.method == "POST":
        print("POST")
        spf = SearchPRBForm(request.POST)
        print(spf)
        if spf.is_valid():
            start = spf.cleaned_data["startTime"]
            print(start)
            end = spf.cleaned_data["endTime"]
            name = spf.cleaned_data["name"]
            attr = spf.cleaned_data["attr"]
            print(attr)


            results = Tbprbnew.objects.raw('select * from tbPRBNew where startTime '
                                           'between %s and %s and name = %s', [start, end, name])

            #results = Tbprbnew.objects.raw('select * from tbPRBNew where name = %s', [name])
            for x in results:
                print("结果")
                print(x.prb0)
            print(results)
            result = []
            dateList = []
            for x in results:
                print(x.starttime)
                dateList.append(str(x.starttime))
            for j in range(0, 99):
                i = str(j)
                if i in attr:
                    print("OK")
                    if 0 == j:
                        for x in results:
                            result.append(x.prb0)
                    elif 1 == j:
                        for x in results:
                            result.append(x.prb1)
                    elif 2 == j:
                        for x in results:
                            result.append(x.prb2)
                    elif 3 == j:
                        for x in results:
                            result.append(x.prb3)
                    elif 4 == j:
                        for x in results:
                            result.append(x.prb4)
                    elif 5 == j:
                        for x in results:
                            result.append(x.prb5)
                    elif 6 == j:
                        for x in results:
                            result.append(x.prb6)
                    elif 7 == j:
                        for x in results:
                            result.append(x.prb7)
                    elif 8 == j:
                        for x in results:
                            result.append(x.prb8)
                    elif 9 == j:
                        for x in results:
                            result.append(x.prb9)
                    elif 10 == j:
                        for x in results:
                            result.append(x.prb10)
                    elif 11 == j:
                        for x in results:
                            result.append(x.prb11)
                    elif 12 == j:
                        for x in results:
                            result.append(x.prb12)
                    elif 13 == j:
                        for x in results:
                            result.append(x.prb13)
                    elif 14 == j:
                        for x in results:
                            result.append(x.prb14)
                    elif 15 == j:
                        for x in results:
                            result.append(x.prb15)
                    elif 16 == j:
                        for x in results:
                            result.append(x.prb16)
                    elif 17 == j:
                        for x in results:
                            result.append(x.prb17)
                    elif 18 == j:
                        for x in results:
                            result.append(x.prb18)
                    elif 19 == j:
                        for x in results:
                            result.append(x.prb19)
                    elif 20 == j:
                        for x in results:
                            result.append(x.prb20)
                    elif 21 == j:
                        for x in results:
                            result.append(x.prb21)
                    elif 22 == j:
                        for x in results:
                            result.append(x.prb22)
                    elif 23 == j:
                        for x in results:
                            result.append(x.prb23)
                    elif 24 == j:
                        for x in results:
                            result.append(x.prb24)
                    elif 25 == j:
                        for x in results:
                            result.append(x.prb25)
                    elif 26 == j:
                        for x in results:
                            result.append(x.prb26)
                    elif 27 == j:
                        for x in results:
                            result.append(x.prb27)
                    elif 28 == j:
                        for x in results:
                            result.append(x.prb28)
                    elif 29 == j:
                        for x in results:
                            result.append(x.prb29)
                    elif 30 == j:
                        for x in results:
                            result.append(x.prb30)
                    elif 31 == j:
                        for x in results:
                            result.append(x.prb31)
                    elif 32 == j:
                        for x in results:
                            result.append(x.prb32)
                    elif 33 == j:
                        for x in results:
                            result.append(x.prb33)
                    elif 34 == j:
                        for x in results:
                            result.append(x.prb34)
                    elif 35 == j:
                        for x in results:
                            result.append(x.prb35)
                    elif 36 == j:
                        for x in results:
                            result.append(x.prb36)
                    elif 37 == j:
                        for x in results:
                            result.append(x.prb37)
                    elif 38 == j:
                        for x in results:
                            result.append(x.prb38)
                    elif 39 == j:
                        for x in results:
                            result.append(x.prb39)
                    elif 40 == j:
                        for x in results:
                            result.append(x.prb40)
                    elif 41 == j:
                        for x in results:
                            result.append(x.prb41)
                    elif 42 == j:
                        for x in results:
                            result.append(x.prb42)
                    elif 43 == j:
                        for x in results:
                            result.append(x.prb43)
                    elif 44 == j:
                        for x in results:
                            result.append(x.prb44)
                    elif 45 == j:
                        for x in results:
                            result.append(x.prb45)
                    elif 46 == j:
                        for x in results:
                            result.append(x.prb46)
                    elif 47 == j:
                        for x in results:
                            result.append(x.prb47)
                    elif 48 == j:
                        for x in results:
                            result.append(x.prb48)
                    elif 49 == j:
                        for x in results:
                            result.append(x.prb49)
                    elif 50 == j:
                        for x in results:
                            result.append(x.prb50)
                    elif 51 == j:
                        for x in results:
                            result.append(x.prb51)
                    elif 52 == j:
                        for x in results:
                            result.append(x.prb52)
                    elif 53 == j:
                        for x in results:
                            result.append(x.prb53)
                    elif 54 == j:
                        for x in results:
                            result.append(x.prb54)
                    elif 55 == j:
                        for x in results:
                            result.append(x.prb55)
                    elif 56 == j:
                        for x in results:
                            result.append(x.prb56)
                    elif 57 == j:
                        for x in results:
                            result.append(x.prb57)
                    elif 58 == j:
                        for x in results:
                            result.append(x.prb58)
                    elif 59 == j:
                        for x in results:
                            result.append(x.prb59)
                    elif 60 == j:
                        for x in results:
                            result.append(x.prb60)
                    elif 61 == j:
                        for x in results:
                            result.append(x.prb61)
                    elif 62 == j:
                        for x in results:
                            result.append(x.prb62)
                    elif 63 == j:
                        for x in results:
                            result.append(x.prb63)
                    elif 64 == j:
                        for x in results:
                            result.append(x.prb64)
                    elif 65 == j:
                        for x in results:
                            result.append(x.prb65)
                    elif 66 == j:
                        for x in results:
                            result.append(x.prb66)
                    elif 67 == j:
                        for x in results:
                            result.append(x.prb67)
                    elif 68 == j:
                        for x in results:
                            result.append(x.prb68)
                    elif 69 == j:
                        for x in results:
                            result.append(x.prb69)
                    elif 70 == j:
                        for x in results:
                            result.append(x.prb70)
                    elif 71 == j:
                        for x in results:
                            result.append(x.prb71)
                    elif 72 == j:
                        for x in results:
                            result.append(x.prb72)
                    elif 73 == j:
                        for x in results:
                            result.append(x.prb73)
                    elif 74 == j:
                        for x in results:
                            result.append(x.prb74)
                    elif 75 == j:
                        for x in results:
                            result.append(x.prb75)
                    elif 76 == j:
                        for x in results:
                            result.append(x.prb76)
                    elif 77 == j:
                        for x in results:
                            result.append(x.prb77)
                    elif 78 == j:
                        for x in results:
                            result.append(x.prb78)
                    elif 79 == j:
                        for x in results:
                            result.append(x.prb79)
                    elif 80 == j:
                        for x in results:
                            result.append(x.prb80)
                    elif 81 == j:
                        for x in results:
                            result.append(x.prb81)
                    elif 82 == j:
                        for x in results:
                            result.append(x.prb82)
                    elif 83 == j:
                        for x in results:
                            result.append(x.prb83)
                    elif 84 == j:
                        for x in results:
                            result.append(x.prb84)
                    elif 85 == j:
                        for x in results:
                            result.append(x.prb85)
                    elif 86 == j:
                        for x in results:
                            result.append(x.prb86)
                    elif 87 == j:
                        for x in results:
                            result.append(x.prb87)
                    elif 88 == j:
                        for x in results:
                            result.append(x.prb88)
                    elif 89 == j:
                        for x in results:
                            result.append(x.prb89)
                    elif 90 == j:
                        for x in results:
                            result.append(x.prb90)
                    elif 91 == j:
                        for x in results:
                            result.append(x.prb91)
                    elif 92 == j:
                        for x in results:
                            result.append(x.prb92)
                    elif 93 == j:
                        for x in results:
                            result.append(x.prb93)
                    elif 94 == j:
                        for x in results:
                            result.append(x.prb94)
                    elif 95 == j:
                        for x in results:
                            result.append(x.prb95)
                    elif 96 == j:
                        for x in results:
                            result.append(x.prb96)
                    elif 97 == j:
                        for x in results:
                            result.append(x.prb97)
                    elif 98 == j:
                        for x in results:
                            result.append(x.prb98)
                    elif 99 == j:
                        for x in results:
                            result.append(x.prb99)
                    break


            return render_to_response("searchPRB.html", {"result": json.dumps(result), "attr": json.dumps(attr),
                                       "Name_List": nameList,
                                       "dateList": json.dumps(dateList),"name":json.dumps(name)})

    return render_to_response("searchPRB.html", {"Name_List": nameList})


def search_sql_KPI(request):
    nameList = Tbkpi.objects.values("cell").all().distinct()
    #nameList = {'1'}
    print("namelist:")
    #print(idList)
    print(type(nameList))
    print(nameList)
    print("名字？？？")
    if request.method == "POST":
        print("POST")
        skf = SearchKPIForm(request.POST)
        print(skf)
        if skf.is_valid():
            start = skf.cleaned_data["startTime"]
            print(start)
            end = skf.cleaned_data["endTime"]
            name = skf.cleaned_data["name"]
            attr = skf.cleaned_data["attr"]
            results = Tbkpi.objects.raw('select * from tbKPI where startTime'
                                       ' between %s and %s '
                                       'and cell = %s', [start, end, name])
            # result = Tbkpi.objects.filter(starttime__gt=start,
            #                              starttime__lt=end, name=name).values("cell_multi").all()
            dateList = []
            for x in results:
                print(x.starttime)
                dateList.append(str(x.starttime))
            print(results)
            #attr_str=str(attr)
            result=[]
            #result_list = []
            #result_list=list(results.objects.all())
           # result_list=[]

            #print(type(result_list))

            if attr == 'RRC连接建立完成次数（无）':
                for x in results:
                    result.append(x.suc_time)
                    print(type(x))
            elif attr == 'RRC连接建立完成次数（包括重发）':
                for x in results:
                    result.append(x.req_time)
            elif attr == 'RRC建立成功率qf(%)':
                for x in results:
                    result.append(x.rrc_suc_rate)
            elif attr == 'E-RAB建立成功总次数（无）':
                for x in results:
                    result.append(x.suc_total)
            elif attr == 'E-RAB建立尝试总次数（无）':
                for x in results:
                    result.append(x.try_total)
            elif attr == 'E-RAB建立成功率2(%)':
                for x in results:
                    result.append(x.e_rab_suc_rate)
            elif attr == 'eNodeB触发的E-RAB异常释放总次数（无）':
                for x in results:
                    result.append(x.enodeb_exception)
            elif attr == '小区切换出E-RAB异常释放总次数（无）':
                for x in results:
                    result.append(x.cell_exception)
            elif attr == 'E-RAB掉线率（新）（%）':
                for x in results:
                    result.append(x.e_rab_offline)
            elif attr == '无线接通率ay（%）':
                for x in results:
                    result.append(x.ay)
            elif attr == 'eNodeB发起的S1 RESET导致的UE Context释放次数 (无)':
                for x in results:
                    result.append(x.enodeb_release_time)
            elif attr == 'UE Context异常释放次数 (无)':
                for x in results:
                    result.append(x.ue_context_exception_time)
            elif attr == 'UE Context建立成功总次数 (无)':
                for x in results:
                    result.append(x.ue_context_suc_time)
            elif attr == '无线掉线率（%）':
                for x in results:
                    result.append(x.wifi_offline_rate)
            elif attr == 'eNodeB内异频切换出成功次数 (无)':
                for x in results:
                    result.append(x.t_field)
            elif attr == 'eNodeB内异频切换出尝试次数 (无)':
                for x in results:
                    result.append(x.u_field)
            elif attr == 'eNodeB内同频切换出成功次数 (无)':
                for x in results:
                    result.append(x.v_field)
            elif attr == 'eNodeB内异频切换出尝试次数 (无)':
                for x in results:
                    result.append(x.w_field)
            elif attr == 'eNodeB间异频切换出成功次数 (无)':
                for x in results:
                    result.append(x.x_field)
            elif attr == 'eNodeB间异频切换出尝试次数 (无)':
                for x in results:
                    result.append(x.y_field)
            elif attr == 'eNodeB间同频切换出成功次数 (无)':
                for x in results:
                    result.append(x.z_field)
            elif attr == 'eNodeB间同频切换出尝试次数 (无)':
                for x in results:
                    result.append(x.aa_field)
            elif attr == 'eNB内切换成功率（%）':
                for x in results:
                    result.append(x.ab_field)
            elif attr == 'eNB间切换成功率（%）':
                for x in results:
                    result.append(x.ac_field)
            elif attr == '同频切换成功率zsp（%）':
                for x in results:
                    result.append(x.ad_field)
            elif attr == '异频切换成功率zsp（%）':
                for x in results:
                    result.append(x.ae_field)
            elif attr == '切换成功率（%）':
                for x in results:
                    result.append(x.ae_field)
            elif attr == '小区PDCP层所接收到的上行数据的总吞吐量 (比特)':
                for x in results:
                    result.append(x.af_field)
            elif attr == '小区PDCP层所发送到的下行数据的总吞吐量':
                for x in results:
                    result.append(x.ag_field)
            elif attr == 'RRC重建请求次数（无）':
                for x in results:
                    result.append(x.ah_field)
            elif attr == 'RRC连接重建比率（%）':
                for x in results:
                    result.append(x.ai_field)
            elif attr == '通过重建回源小区的eNodeB间同频切换出执行成功次数 (无)':
                for x in results:
                    result.append(x.aj_field)
            elif attr == '通过重建回源小区的eNodeB间异频切换出执行成功次数 (无)':
                for x in results:
                    result.append(x.ak_field)
            elif attr == '通过重建回源小区的eNodeB内同频切换出执行成功次数 (无)':
                for x in results:
                    result.append(x.al_field)
            elif attr == '通过重建回源小区的eNodeB内同频切换出执行成功次数 (无)':
                for x in results:
                    result.append(x.am_field)
            elif attr == '通过重建回源小区的eNodeB内异频切换出执行成功次数 (无)':
                for x in results:
                    result.append(x.an_field)
            elif attr == 'eNB内切换出成功次数（次）':
                for x in results:
                    result.append(x.ao_field)
            elif attr == 'eNB内切换出请求次数（次）':
                for x in results:
                    result.append(x.ap_field)
            result_count=len(result)
            return render_to_response("searchKPI.html",
                                      {"result": json.dumps(result), "attr": json.dumps(attr),
                                       "length":json.dumps(result_count), "Name_List": nameList,
                                       "dateList": json.dumps(dateList)})
        else:
            return render_to_response("searchKPI.html", {"Name_List": nameList})
    return render_to_response("searchKPI.html", {"Name_List": nameList})


def search_sql_eNodeb(request):
    cursor = connection.cursor()
    """
    # Data modifying operation - commit required
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()
    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()
    """
    idList = list(Tbcell.objects.values("enodebid").all().distinct())
    # ursor.execute("select distinct SECTOR_ID from TbCell ",)
    nameList = list(Tbcell.objects.values("enodeb_name").all().distinct())

    print("namelist:")
    print(idList)
    print(type(nameList))
    print(nameList)
    print("名字？？？")
    if request.method == "POST":
        print("POST")
        stf = SearchTbCellForm(request.POST)
        if stf.is_valid():
            search = stf.cleaned_data["index"]
            index = {'enodeb_name': search}
            if index in nameList:
                print("按名字查询")
                name = str(index.get('enodeb_name'))

                name = [name]
                cursor.execute("select * from TbCell where enodeb_name = %s", name)
                data = cursor.fetchone()
                # transaction.commit_unless_managed()

                # dataFilter = Tbcell.objects.filter(sector_id=id)
                # print(dataFilter)
                result = tuple_to_cell_dict(data)
                result = [result]
                print(result)
                result_len=len(result)
                return render_to_response("searchEnodeb.html", {"result": result,"length":result_len,"EnodebID_List": idList, "EnodebName_List": nameList})
            else:
                search = eval(search)
                index = {'enodebid': search}
                print(index)
                if index in idList:
                    # 按照ID查询
                    print("按ID查询")
                    id = index.get('enodebid')
                    dataFilter = Tbcell.objects.filter(enodebid=id)
                    print(dataFilter)
                    result_len=len(dataFilter)
                    return render_to_response("searchEnodeb.html", {"result": dataFilter, "length": result_len,"EnodebID_List": idList, "EnodebName_List": nameList})

                else:
                    print("?????????????????????????????????????????????")
                    return render_to_response("searchEnodeb.html", {"EnodebID_List": idList, "EnodebName_List": nameList})
    return render_to_response("searchEnodeb.html", {"EnodebID_List": idList, "EnodebName_List": nameList})


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
    #ursor.execute("select distinct SECTOR_ID from TbCell ",)
    nameList = Tbcell.objects.values("sector_name").all().distinct()

    print("namelist:")
    print(idList)
    print(type(nameList))
    print(nameList)
    print("名字？？？")
    if request.method == "POST":
        print("POST")
        stf = SearchTbCellForm(request.POST)
        if stf.is_valid():
            search = stf.cleaned_data["index"]
            index = {'sector_id': search}
            if index in idList:  # 按照ID查询
                print("按ID查询")
                id = str(index.get('sector_id'))
                # Data modifying operation - commit required
                id = [id]
                cursor.execute("select * from TbCell where SECTOR_ID = %s", id)
                data = cursor.fetchone()
                #transaction.commit_unless_managed()

                #dataFilter = Tbcell.objects.filter(sector_id=id)
                #print(dataFilter)
                result = tuple_to_cell_dict(data)
                result = [result]
                result_len=len(result)
                return render_to_response("searchCell.html", {"result": result, "length": result_len,"CellID_List": idList, "CellName_List":nameList})
            else:
                index = {'sector_name': search}
                if index in nameList:
                    print("按名字查询")
                    name = str(index.get('sector_name'))

                    name = [name]
                    cursor.execute("select * from TbCell where SECTOR_NAME = %s", name)
                    data = cursor.fetchone()
                    # transaction.commit_unless_managed()

                    # dataFilter = Tbcell.objects.filter(sector_id=id)
                    # print(dataFilter)
                    result = tuple_to_cell_dict(data)
                    print(data)
                    result = [result]
                    print(result)
                    result_len=len(result)
                    return render_to_response("searchCell.html", {"result": result,"length":result_len,"CellID_List": idList, "CellName_List":nameList})
                else:
                    print("?????????????????????????????????????????????")
                    return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})
    return render_to_response("searchCell.html", {"CellID_List": idList, "CellName_List": nameList})


def tuple_to_cell_dict(data):
    result = {'sector_id': '',
              'city': '',
              'sector_name': '',
                'enodebid': '',
                'enodeb_name': '',
                'earfcn': '',
                'pci': '',
                'pss': '',
                'sss': '',
                'tac': '',
                'vendor': '',
                'longitude': '',
                'latitude': '',
                'style': '',
                'azimuth': '',
                'height': '',
                'electtilt': '',
                'mechtilt': '',
                'totletilt': ''}

    result['city'] = data[0]
    result['sector_id'] = data[1]
    result['sector_name'] = data[2]
    result['enodebid'] = data[13]
    result['enodeb_name'] = data[14]
    result['earfcn'] = data[3]
    result['pci'] = data[4]
    result['pss'] = data[5]
    result['sss'] = data[6]
    result['tac'] = data[7]
    result['vendor'] = data[15]
    result['longitude'] = data[16]
    result['latitude'] = data[17]
    result['style'] = data[18]
    result['azimuth'] = data[8]
    result['height'] = data[9]
    result['electtilt'] = data[10]
    result['mechtilt'] = data[11]
    result['totletilt'] = data[12]

    return result


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
                return render_to_response("searchCell.html", {"result": dataFilter,
                                                              "CellID_List": idList, "CellName_List": nameList})
            elif index in nameList:
                print("按名字查询")
                dataFilter = Tbcell.objects.filter(sector_name=index)
                print(dataFilter)
                return render_to_response("searchCell.html", {"result": dataFilter,
                                                              "CellID_List": idList, "CellName_List": nameList})
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
    return st_norm(u)


def progress_bar(request):
    global bar_value
    print("收到请求")
    return HttpResponse(bar_value)

