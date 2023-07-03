import os
# 定义文件路径
GSX_ROOT=input('Please enter the root of your GSX:')
# Texture_ROOT=input('Please enter the root of your own Livery:')
# 定义添加行
code_to_add_to_catering = '''[BACL]
couatl.icaoprefixes = ZBAA
couatl.atc_parking_codes = Beijing Air Catering(Full Vechile)
couatl.basecolor = white

[BACL2]
couatl.icaoprefixes = ZBAA
couatl.atc_parking_codes = Beijing Air Catering Co.,LTD(Normal Vechile)
couatl.basecolor = white

[BAIK]
couatl.icaoprefixes = ZBAA
couatl.atc_parking_codes = Beijing Airport Inflight Kitchen
couatl.basecolor = white

[BJXHHNA]
couatl.icaoprefixes = ZBAA
couatl.atc_parking_codes = Beijing Xinhua Airport Catering
couatl.basecolor = white

[CGO]
couatl.icaoprefixes = ZHCC ZYTL
couatl.atc_parking_codes = China Southern CGO Catering(Use at ZHCC and ZYTL)
couatl.basecolor = white

[CKG]
couatl.atc_parking_codes = ZUCK
couatl.icaoprefixes = Sichuan Airlines Chongqing Airport Catering
couatl.basecolor = white

[CSNAC]
couatl.icaoprefixes = ZYCC ZHHH ZWWW ZYTX
couatl.atc_parking_codes = China Southern Airlines Air Catering(Use at ZYCC ZHHH ZWWW ZYTX)
couatl.basecolor = white

[CTU]
couatl.icaoprefixes = ZUUU
couatl.atc_parking_codes = Sichuan Airlines LSG Catering
couatl.basecolor = white

[CXA]
couatl.icaoprefixes = ZSAM ZSFZ ZSHC
couatl.atc_parking_codes = Xiamen Air Catering(Use at ZSAM ZSFZ ZSHC)
couatl.basecolor = cyan

[CZJC]
couatl.icaoprefixes = ZSCG
couatl.atc_parking_codes = Changzhou Benniu Airport
couatl.basecolor = white

[DKH]
couatl.icaoprefixes = ZSSS ZSPD
couatl.atc_parking_codes = Juneyao Air Catering(Use at ZSSS ZSPD)
couatl.basecolor = white

[DLAAC]
couatl.icaoprefixes = ZYTL
couatl.atc_parking_codes = Dalian Air Catering
couatl.basecolor = white

[DLAAC2]
couatl.icaoprefixes = ZYTL
couatl.atc_parking_codes = China Southern Airlines Dalian Air Catering 
couatl.basecolor = white

[EAC]
couatl.icaoprefixes = ZSPD ZSSS ZSNJ
couatl.atc_parking_codes = Eastern Air Catering(Old Logo)
couatl.basecolor = white

[EAC2]
couatl.icaoprefixes = ZSPD ZSSS ZSNJ ZBAD
couatl.atc_parking_codes = Eastern Air Catering(New Logo)
couatl.basecolor = white

[EAC3]
couatl.icaoprefixes = ZSPD ZSSS ZSNJ
couatl.atc_parking_codes = Eastern Air Catering
couatl.basecolor = white

[FJFLIPORT]
couatl.icaoprefixes = ZSFZ ZSWY
couatl.atc_parking_codes = Fujian Fliport Food Co.,LTD(Use at ZSFZ ZSWY)
couatl.basecolor = white

[FLIPORT]
couatl.icaoprefixes = ZSAM
couatl.atc_parking_codes = Xiamen Fliport Catering
couatl.basecolor = white

[GAC]
couatl.icaoprefixes = ZUGY ZUYI ZUTR ZUNP ZUAS ZUZY ZULB ZUBJ ZUKJ
couatl.atc_parking_codes = Guizhou Air Catering
couatl.basecolor = white

[GBIALSG]
couatl.icaoprefixes = ZGGG
couatl.atc_parking_codes = Guangzhou Airport LSG Sky Chefs
couatl.basecolor = white

[GXAC]
couatl.icaoprefixes = ZGNN ZGKL ZGBH ZGZH ZGBS ZGWZ ZGHC
couatl.atc_parking_codes = Guangxi Xiangfei Air Catering
couatl.basecolor = white

[HCAF]
couatl.icaoprefixes = ZHCC
couatl.atc_parking_codes = Henan Civil Aviation Food
couatl.basecolor = white

[HTIA]
couatl.icaoprefixes = ZSTX
couatl.atc_parking_codes = Huangshan Airport Air Catering
couatl.basecolor = white

[HXIA]
couatl.icaoprefixes = ZSOF
couatl.atc_parking_codes = Hefei Xinqiao Airport Air Catering
couatl.basecolor = white

[KAC]
couatl.icaoprefixes = ZWSH
couatl.atc_parking_codes = Kashi Air Catering
couatl.basecolor = white

[KTAF]
couatl.icaoprefixes = ZWKL
couatl.atc_parking_codes = Korla Tianyuan Aviation Food
couatl.basecolor = white

[KMG]
couatl.atc_parking_codes = Yunnan International Airport Huazhuo Air Catering
couatl.icaoprefixes = ZPPP ZPLJ ZPJH ZPMS ZPSM ZPTC ZPBS ZPWS ZPZT ZPLC ZPDL ZPDQ
couatl.basecolor = white

[NANLAND]
couatl.icaoprefixes = ZGGG ZBAD ZGSD
couatl.atc_parking_codes = Nanland Air Catering
couatl.basecolor = white

[NBHS]
couatl.icaoprefixes = ZSNB
couatl.atc_parking_codes = Ningbo Lishe Airport Air Catering
couatl.basecolor = white

[NTJC]
couatl.icaoprefixes = ZSNT
couatl.atc_parking_codes = Nantong Airport Air Catering
couatl.basecolor = white

[NTJC2]
couatl.icaoprefixes = ZSNT
couatl.atc_parking_codes = Nantong Airport Air Catering
couatl.basecolor = white

[PEK]
couatl.icaoprefixes = ZBAA
couatl.atc_parking_codes = Beijing Air Catering
couatl.basecolor = white

[SACL]
couatl.icaoprefixes = ZGSZ
couatl.atc_parking_codes = Shenzhen Air Catering
couatl.basecolor = white

[SAIC]
couatl.icaoprefixes = ZSSS
couatl.atc_parking_codes = Shanghai Airport International Catering(Left Logo)
couatl.basecolor = white

[SAIC2]
couatl.icaoprefixes = ZSSS
couatl.atc_parking_codes = Shanghai Airport International Catering(Right Logo)
couatl.basecolor = white

[SALSG]
couatl.icaoprefixes = ZUUU
couatl.atc_parking_codes = Sichuan Airlines LSG Catering
couatl.basecolor = white

[SCCQ]
couatl.icaoprefixes = ZUCK
couatl.atc_parking_codes = Sichuan Airlines Chongqing Airport Catering Co,.Ltd.
couatl.basecolor = white

[SDA]
couatl.atc_parking_codes = Shandong Jinping Catering
couatl.icaoprefixes = ZSJN ZSQD ZSYT ZSWH 
couatl.basecolor = white

[SHA]
couatl.atc_parking_codes = Eastern Air Catering(Old logo with waist line)
couatl.icaoprefixes = ZSSS ZSPD ZSNJ
couatl.basecolor = white

[SWAC]
couatl.icaoprefixes = ZUUU
couatl.atc_parking_codes = Southwest Airport Air Catering
couatl.basecolor = white

[SZSH]
couatl.icaoprefixes = ZGSZ
couatl.atc_parking_codes = Shenzhen Airlines Air Catering
couatl.basecolor = white

[TIBETFLIPORT]
couatl.icaoprefixes = ZULS ZUNZ ZUAL ZUDR ZUSH ZUBD ZURK
couatl.atc_parking_codes = Tibet Fliport Food Co.,LTD
couatl.basecolor = white

[TJCCA]
couatl.icaoprefixes = ZBTJ
couatl.atc_parking_codes = Air China Air Catering(Tianjin)
couatl.basecolor = white

[TJKG]
couatl.icaoprefixes = ZBTJ
couatl.atc_parking_codes = Tianjin Airport Kitchen Ltd.(Bold Fonts)
couatl.basecolor = white

[TSN]
couatl.icaoprefixes = ZBTJ
couatl.atc_parking_codes = Tianjin Airport Kitchen Ltd.(Regular Fonts)
couatl.basecolor = white

[WZSP]
couatl.icaoprefixes = ZSWZ
couatl.atc_parking_codes = Wenzhou Airport Air Catering
couatl.basecolor = white

[XBJC]
couatl.icaoprefixes = ZLXY ZLIC ZLXN ZLTS ZLYL ZLGY ZLGM ZLXH ZLYA ZLZW ZLYS ZLLN ZLHZ ZLGL ZLDL ZLHX
couatl.atc_parking_codes = China West Airport Group International Airport Catering Co,.LTD.
couatl.basecolor = white

[XIY]
couatl.icaoprefixes = ZLXY
couatl.atc_parking_codes = CHINA WEST AIRPORT GROUP(Only used at ZLXY)
couatl.basecolor = white

[XJHNALSG]
couatl.icaoprefixes = ZWWW
couatl.atc_parking_codes = Xinjiang HNA LSG Sky Chefs
couatl.basecolor = white

[XZKG]
couatl.icaoprefixes = ZULS
couatl.atc_parking_codes = Tibet In-flight Meal Company
couatl.basecolor = white

[YAC]
couatl.icaoprefixes = ZPPP
couatl.atc_parking_codes = Yunnan International Airport Air Catering
couatl.basecolor = white

[YAC2]
couatl.icaoprefixes = ZPPP
couatl.atc_parking_codes = Yunnan International Airport Air Catering
couatl.basecolor = white

[YZ]
couatl.icaoprefixes = ZSYA
couatl.atc_parking_codes = Yangzhou Airport Air Catering
couatl.basecolor = white

[ZHKG]
couatl.icaoprefixes = ZGSD
couatl.atc_parking_codes = Zhuhai Airport Food Co.,LTD
couatl.basecolor = white

[ZJZY]
couatl.icaoprefixes = ZSHC
couatl.atc_parking_codes = Zhejiang Zhongyu Aiation Development
couatl.basecolor = white

[CKCA]
couatl.icaoprefixes = ZUCK
couatl.atc_parking_codes = Chongqing Air Catering CO.,LTD.
couatl.basecolor = white

[COMAC]
couatl.icaoprefixes = ZSPD
couatl.atc_parking_codes = COMAC Catering support ARJ21 "Electoric Car"
couatl.basecolor = white

[DAIK]
couatl.icaoprefixes = ZBAD
couatl.atc_parking_codes = Beijing Daxing International Airport Inflight Catering Ltd.
couatl.basecolor = white

[GGourmet_CN]
couatl.icaoprefixes = ZSPD
couatl.atc_parking_codes = GateGourmet China
couatl.basecolor = white

[GZAC]
couatl.icaoprefixes = ZSGZ
couatl.atc_parking_codes = GZ Air-Catering
couatl.basecolor = white

[HNA]
couatl.icaoprefixes = ZJ ZJSY ZJHK ZJQH ZJYX
couatl.atc_parking_codes = Hainan Air Catering CO.,LTD
couatl.basecolor = white

[IMA]
couatl.icaoprefixes = ZBHH ZBDS ZBOW ZBLA ZBMZ ZBCF ZBTL ZBUL ZBXH ZBUH
couatl.atc_parking_codes = Hainan Air Catering CO.,LTD
couatl.basecolor = white

[NNAP]
couatl.icaoprefixes = ZGNN
couatl.atc_parking_codes = Nanning Wuxu International Airport Company
couatl.basecolor = white

[YCAP]
couatl.icaoprefixes = ZSYN
couatl.atc_parking_codes = Yancheng Nanyang International Airport
couatl.basecolor = white
'''
code_to_add_to_handling='''
[3U]
couatl.atc_parking_codes = Sichuan Airlines Ground Service
couatl.icaoprefixes = ZUCK ZUUU
couatl.basecolor = red

[AMU]
couatl.atc_parking_codes = Air Macau Ground Service
couatl.icaoprefixes = VMMC
couatl.basecolor = blue

[CA]
couatl.atc_parking_codes = Air China Airlines Ground Service
couatl.icaoprefixes = Z ZHHH ZUCK ZUUU 
couatl.basecolor = red

[CAH]
couatl.atc_parking_codes = Beijing Airport Ground Service Co.Ltd.
couatl.icaoprefixes = ZBAA ZBAD
couatl.basecolor = blue

[CAN]
couatl.atc_parking_codes = Guangzhou Baiyun Airport Ground Service
couatl.icaoprefixes = ZGGG
couatl.basecolor = green

[CDC]
couatl.atc_parking_codes = LOONG Air Ground Service
couatl.icaoprefixes = ZSHC
couatl.basecolor = cyan

[CDG]
couatl.atc_parking_codes = Shandong Airlines Ground Service
couatl.icaoprefixes = ZSQD ZSJN ZSYT
couatl.basecolor = blue

[CKG]
couatl.atc_parking_codes = Chongqing Jiangbei Airport Ground Service
couatl.icaoprefixes = ZUCK
couatl.basecolor = blue

[CQH]
couatl.atc_parking_codes = Spring Airlines Ground Service
couatl.icaoprefixes = ZSSS ZSPD
couatl.basecolor = green

[CQN]
couatl.atc_parking_codes = Chongqing Airlines Ground Service
couatl.icaoprefixes = ZUCK
couatl.basecolor = Blue

[CRK]
couatl.atc_parking_codes = Hong Kong International Airport Gronud Service
couatl.icaoprefixes = VHHH VHHX
couatl.basecolor = red

[CSC]
couatl.atc_parking_codes = Sichuan Airlines Ground Service
couatl.icaoprefixes = Z ZU ZUUU ZUTF
couatl.basecolor = white

[CSX]
couatl.atc_parking_codes = Changsha Huanghua Airport Ground Service
couatl.icaoprefixes = ZGHA
couatl.basecolor = blue

[CSZ]
couatl.atc_parking_codes = Shenzhen Airlines Ground Service
couatl.icaoprefixes = ZGSZ
couatl.basecolor = red

[CTU]
couatl.atc_parking_codes = Chengdu Shuangliu Airport Ground Service
couatl.icaoprefixes = ZUUU
couatl.basecolor = blue

[CXA]
couatl.atc_parking_codes = Xiamen Airlines Ground Service
couatl.icaoprefixes = Z ZSAM ZSFZ ZSHC ZSQZ
couatl.basecolor = blue

[CZ]
couatl.atc_parking_codes = China Southern Airlines Ground Service
couatl.icaoprefixes = Z ZSPD ZYTL ZYTX ZHCC ZGSZ ZGGG ZWWW ZHHH ZYTL ZJSY ZJHK
couatl.basecolor = blue

[DLC]
couatl.atc_parking_codes = Dalian Airport Ground Service
couatl.icaoprefixes = ZYTL
couatl.basecolor = blue

[FOC]
couatl.atc_parking_codes = Fuzhou Changele Airport Ground Service
couatl.icaoprefixes = ZSFZ
couatl.basecolor = blue

[HAK]
couatl.atc_parking_codes = Haikou Meilan Airport Ground Service
couatl.icaoprefixes = ZJHK
couatl.basecolor = blue

[HDA]
couatl.atc_parking_codes = Dragon Air
couatl.icaoprefixes = VH VHHH VHHX
couatl.basecolor = red

[HFE]
couatl.atc_parking_codes = Hefei Xinqiao Airport Ground Service
couatl.icaoprefixes = ZSOF
couatl.basecolor = blue

[HGH]
couatl.atc_parking_codes = Hangzhou Xiaoshan Airport Ground Service
couatl.icaoprefixes = ZSHC
couatl.basecolor = blue

[HKG]
couatl.atc_parking_codes = Hongkong Airport Ground Service
couatl.icaoprefixes = VHHH
couatl.basecolor = blue

[HNAC]
couatl.atc_parking_codes = Henan Airport Ground Service
couatl.icaoprefixes = ZHCC
couatl.basecolor = blue

[HU]
couatl.atc_parking_codes = Hainan Airlines Ground Service
couatl.icaoprefixes = Z ZJSY ZJHK
couatl.basecolor = red

[KHN]
couatl.atc_parking_codes = Nanchang Changbei Airport Ground Service
couatl.icaoprefixes = ZSCN
couatl.basecolor = blue

[KMG]
couatl.atc_parking_codes = Yunnan Airport Group Ground Service
couatl.icaoprefixes = ZPPP ZPLJ ZPJH ZPMS ZPSM ZPTC ZPBS ZPZT ZPLC ZPDL ZPDQ
couatl.basecolor = blue

[KNA]
couatl.atc_parking_codes = Kunming Airlines Ground Service
couatl.icaoprefixes = ZPPP
couatl.basecolor = red

[KWE]
couatl.atc_parking_codes = Guizhou Longdongbao Airport Ground Service
couatl.icaoprefixes = ZUGY
couatl.basecolor = blue

[LAMG]
couatl.atc_parking_codes = Liaoning Airport Ground Service
couatl.icaoprefixes = ZYTX ZYDD ZYJZ ZYCY ZYAS
couatl.basecolor = yellow

[LKE]
couatl.atc_parking_codes = Lucky Air Ground Service
couatl.icaoprefixes = ZPPP
couatl.basecolor = red

[LONGYAN]
couatl.atc_parking_codes = Longyan Guanzhaishan Airport Ground Service
couatl.icaoprefixes = ZSLO
couatl.basecolor = blue

[MU]
couatl.atc_parking_codes = China Eastern Airlines Ground Service
couatl.icaoprefixes = Z ZS ZP ZB ZG ZY ZW ZSPD ZSSS ZSNJ ZPPP ZHCC ZBAD ZBAA
couatl.basecolor = red

[NGB]
couatl.atc_parking_codes = Ningbo Lishe Airport Ground Service
couatl.icaoprefixes = ZSNB
couatl.basecolor = blue

[NKG]
couatl.atc_parking_codes = Nanjing Lukou Airport Ground Service
couatl.icaoprefixes = ZSNJ
couatl.basecolor = blue

[SIAS]
couatl.atc_parking_codes = Shanghai Airports Ground Service
couatl.icaoprefixes = ZSPD ZSSS
couatl.basecolor = blue

[SJW]
couatl.atc_parking_codes = Shijiazhuang Zhengding Airport Ground Service
couatl.icaoprefixes = ZBSJ
couatl.basecolor = blue

[SYX]
couatl.atc_parking_codes = Sanya Phoenix Airport Ground Service
couatl.icaoprefixes = ZJSY
couatl.basecolor = blue

[SZX]
couatl.atc_parking_codes = Shenzhen Baoan Airport Group Ground Service
couatl.icaoprefixes = ZGSZ
couatl.basecolor = blue

[TAO]
couatl.atc_parking_codes = Qingdao Jiaodong Airport Ground Service
couatl.icaoprefixes = ZSQD
couatl.basecolor = blue

[UEA]
couatl.atc_parking_codes = Chengdu Airlines
couatl.icaoprefixes = ZUUU
couatl.basecolor = red

[URC]
couatl.atc_parking_codes = Xinjiang Airport Group Ground Service
couatl.icaoprefixes = ZW
couatl.basecolor = blue

[WUH]
couatl.atc_parking_codes = Wuhan Tianhe Airport Ground Service
couatl.icaoprefixes = ZHHH
couatl.basecolor = blue

[WYS]
couatl.atc_parking_codes = Wuyishan Airport Gronud Service
couatl.icaoprefixes = ZSWY
couatl.basecolor = blue

[XIY]
couatl.atc_parking_codes = Xi’an Xianyang Airport Ground Service
couatl.icaoprefixes = ZLXY
couatl.basecolor = yellow

[XMN]
couatl.atc_parking_codes = Xiamen Airport Ground Service
couatl.icaoprefixes = ZSAM
couatl.basecolor = blue

[ZH]
couatl.atc_parking_codes = Shenzhen Airlines Ground Service
couatl.icaoprefixes = Z ZGSZ
couatl.basecolor = red

[ZUH]
couatl.atc_parking_codes = Zhuhai Jinwan Airport Ground Service
couatl.icaoprefixes = ZGSD
couatl.basecolor = blue
'''

code_to_add_to_jetwaylogo='''[BOC]
couatl.icaoprefixes = Z ZSJN
couatl.atc_parking_codes = BOC

[CCB]
couatl.icaoprefixes = Z ZS ZSAM
couatl.atc_parking_codes = CCB

[CGB]
couatl.icaoprefixes = Z ZG ZGGG
couatl.atc_parking_codes = CGB
'''

# 打开文件并在末尾添加代码
with open(os.path.join(GSX_ROOT, "texture", "rules_catering.cfg"), mode="a") as f:
    f.write('\n' + code_to_add_to_catering)
with open(os.path.join(GSX_ROOT, "texture", "rules_handling.cfg"), mode="a") as f:
    f.write('\n' + code_to_add_to_handling)
with open(os.path.join(GSX_ROOT, "texture", "rules_jetwaylogo.cfg"), mode="a") as f:
    f.write('\n' + code_to_add_to_jetwaylogo)
input('Mission Complete, press "Enter" to exit the Script.')