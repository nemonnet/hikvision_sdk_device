﻿#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@version: 0.0.1
@author: lee
@license: Apache Licence
@contact: shida23577@hotmail.com
@software: PyCharm
@file: hikvision_types.py
@time: 2016/4/27 15:23
"""

import sys, collections
from ctypes import *

Session = collections.namedtuple('Session', 'device_id session_id ip port user pwd')

if sys.platform == 'win32':
    ExceptionCallback = WINFUNCTYPE(None, c_ulong, c_long, c_long, c_void_p)
    DataCallback = WINFUNCTYPE(None, c_long, c_ulong, POINTER(c_byte), c_ulong, c_void_p)
else:
    ExceptionCallback = CFUNCTYPE(None, c_ulong, c_long, c_long, c_void_p)
    DataCallback = CFUNCTYPE(None, c_long, c_ulong, POINTER(c_byte), c_ulong, c_void_p)

def enum(**enums):
    return type('Enum', (), enums)

EXCEPTION_EVENT_TYPE = enum(EXCEPTION_RELOGIN=0x8040, EXCEPTION_LOGIN_SUCCESS=0x8041, EXCEPTION_EXCHANGE=0x8000\
                            , EXCEPTION_RESUME_EXCHANGE=0x8017)


V_STREAM_VALUE_TYPE = enum(NET_DVR_SYSHEAD = 1, NET_DVR_STREAMDATA = 2, NET_DVR_AUDIOSTREAMDATA =3, NET_DVR_PRIVATE_DATA=112)

V_PTZ_CMD_TYPE = enum(LIGHT_PWRON=2, WIPER_PWRON=3, FAN_PWRON=4, HEATER_PWRON=5, AUX_PWRON1=6,
                      AUX_PWRON2=7, SET_PRESET=8, CLE_PRESET=9, ZOOM_IN=11, ZOOM_OUT=12, FOCUS_NEAR=13, FOCUS_FAR=14,
                      IRIS_OPEN=15, IRIS_CLOSE=16, TILT_UP=21, TILT_DOWN=22, PAN_LEFT=23,
                      PAN_RIGHT=24, LEFT_UP=25, RIGHT_UP=26, LEFT_DOWN=27, RIGHT_DOWN=28,
                      PAN_AUTO=29, GOTO_PRESET=39, TILT_DOWN_ZOOM_IN=58, TILT_DOWN_ZOOM_OUT=59, PAN_LEFT_ZOOM_IN=60,
                      PAN_LEFT_ZOOM_OUT=61, PAN_RIGHT_ZOOM_IN=62, PAN_RIGHT_ZOOM_OUT=63,
                      UP_LEFT_ZOOM_IN=64, UP_LEFT_ZOOM_OUT=65, UP_RIGHT_ZOOM_IN=66, UP_RIGHT_ZOOM_OUT=67,
                      DOWN_LEFT_ZOOM_IN=68, DOWN_LEFT_ZOOM_OUT=69, DOWN_RIGHT_ZOOM_IN=70,
                      DOWN_RIGHT_ZOOM_OUT=71, TILT_UP_ZOOM_IN=72, TILT_UP_ZOOM_OUT=73)

NET_DVR_DEV_TYPE = enum(DVR=1, ATMDVR=2, DVS=3, DEC=4, ENC_DEC=5, DVR_HC=6, DVR_HT=7,
                        DVR_HF=8, DVR_HS=9, DVR_HTS=10, DVR_HB=11, DVR_HCS=12, DVS_A=13,
                        DVR_HC_S=14, DVR_HT_S=15, DVR_HF_S=16, DVR_HS_S=17, ATMDVR_S=18,
                        DVR_7000H=19, DEC_MAT=20, DVR_MOBILE=21, DVR_HD_S=22, DVR_HD_SL=23,
                        DVR_HC_SL=24, DVR_HS_ST=25, DVS_HW=26, DS630X_D=27, DS640X_HD=28,
                        DS610X_D=29, IPCAM=30, MEGA_IPCAM=31, IPCAM_X62MF=32, ITCCAM=35,
                        IVS_IPCAM=36, ZOOMCAM=38, IPDOME=40, IPDOME_MEGA200=41, IPDOME_MEGA130=42,
                        TII_IPCAM=44, IPMOD=50, IDS6501_HF_P=60, IDS6101_HF_A=61, IDS6002_HF_B=62,
                        IDS6101_HF_B=63, IDS52XX=64, IDS90XX=65, IDS8104_AHL_S_HX=66, IDS8104_AHL_S_H=67,
                        IDS91XX=68, IIP_CAM_B=69, IIP_CAM_F=70, DS71XX_H=71, DS72XX_H_S=72, DS73XX_H_S=73,
                        DS72XX_HF_S=74, DS73XX_HFI_S=75, DS76XX_H_S=76, DS76XX_N_S=77, DS81XX_HS_S=81,
                        DS81XX_HL_S=82, DS81XX_HC_S=83, DS82XX_HD_S=84, DS82XX_HE_S=85, DS82XX_HF_S=86,
                        DS81XX_AH_S=87, DS81XX_AHF_S=88, DS90XX_HF_S=90, DS91XX_HF_S=91, DS91XX_HD_S=92,
                        IDS90XX_A=93, IDS91XX_A=94, DS95XX_N_S=95, DS96XX_N_SH=96, DS90XX_HF_SH=97,
                        DS91XX_HF_SH=98, DS_65XXHC=105, DS65XXHC_S=106, DS_65XXHF=107, DS_65XXHF_S=108,
                        DS_6500HF_B=109, IVMS_6200_C=110, IVMS_6200_B=111, DS72XXHV_ST15=112, DS72XXHV_ST20=113,
                        IVMS_6200_T=114, IVMS_6200_BP=115, DS_81XXHC_ST=116, DS_81XXHS_ST=117, DS_81XXAH_ST=118,
                        DS_81XXAHF_ST=119, DS_66XXDVS=120, DS_19AXX=142, DS_19CXX=144, DS_19DXX=145, DS_19XX=146,
                        DS_19SXX=147, DS_1HXX=148, DS_C10H=161, DS_C10N_BI=162, DS_C10N_DI=163, DS_C10N_SI=164,
                        DS_C10N_DO=165, DS_C10N_SERVER=166, IDS_8104_AHFL_S_H=171, IDS_65XX_HF_A=172, IDS90XX_HF_RH=173,
                        IDS91XX_HF_RH=174, IDS_65XX_HF_B=175, IDS_65XX_HF_P=176, IVMS_6200_F=177, IVMS_6200_F_S=179,
                        DS90XX_HF_RH=181, DS91XX_HF_RH=182, DS78XX_S=183, DS81XXHW_ST=186, DS91XXHW_ST=187,
                        DS91XX_ST=188, DS81XX_ST=189, DS81XXH_ST=190, DS73XXH_ST=191, DS81XX_SH=192, DS81XX_SN=193,
                        DS96XXN_ST=194, DS86XXN_ST=195, DS80XXHF_ST=196, DS90XXHF_ST=197, DS76XXN_ST=198,
                        DS9664N_RX=199,
                        ENCODER_SERVER=200, DECODER_SERVER=201, PCNVR_SERVER=202, CVR_SERVER=203, DS_91XXHFH_ST=204,
                        DS_66XXHFH=205, TRAFFIC_TS_SERVER=210, TRAFFIC_VAR=211, IPCALL=212, DS64XXHD_T=701,
                        DS_65XXD=703,
                        DS63XXD_T=704, DS_64XXHD_S=706, DS_68XXT=707, DS65XXD_T=708, DS_K260X=850, IPCAM_FISHEYE=1002,
                        IPCAM_BINOCULAR=1004, TRAFFIC_ECT=1400, TRAFFIC_PARKING_SERVER=1401, DS90XXHW_ST=2001,
                        DS72XXHX_SH=2002, DS_92XX_HF_ST=2003, DS_91XX_HF_XT=2004, DS_90XX_HF_XT=2005, DS_73XXHX_SH=2006,
                        DS_72XXHFH_ST=2007, DS_67XXHF_SATA=2008, DS_67XXHW=2009, DS_67XXHW_SATA=2010, DS_67XXHF=2011,
                        DS_6772XXHF_SV=2012, DS_72XXHW_SV=2013, DS_81XXHX_SH=2014, DS_71XXHX_SL=2015, DS_77XXN_ST=2201,
                        DS_95XX_N_ST=2202, DS_85XX_N_ST=2203, DS_96XX_N_XT=2204, DS_76XX_N_SE=2205, DS_86XXSN_SX=2206,
                        DS_96XX_N_RX=2207, DS_96XXX_N_E=2213, DS_76XXN_EX=2214, DS_77XXN_E4=2215, DS_86XXN_E8=2216,
                        DS_81XXTHFH_E=2217, DS_96XXN_FX=2230, DS_86XXN_FX=2231, PCNVR_IVMS_4200=2301, IVMS_6200_TP=2401,
                        IVMS_6200_TF=2402)



class NET_DVR_PROTO_TYPE(Structure):
    _fields_ = [('dwType', c_ulong),
                ('byDescribe', c_ubyte * 16)]

    def __str__(self):
        return "dwType:{0} byDescribe:{1}".format(self.dwType, self.byDescribe)


class NET_DVR_IPC_PROTO_LIST(Structure):
    _fields_ = [('dwsize', c_ulong),
                ('dwProtoNum', c_ulong),
                ('struProto', NET_DVR_PROTO_TYPE * 50),
                ('byRes', c_ubyte * 8)]

    def __str__(self):
        return "dwsize:{0} dwProtoNum:{1} struProto:{2} byRes:{3}".format(self.dwsize, self.dwProtoNum, self.struProto,
                                                                          self.byRes)


class NET_DVR_DIGITAL_CHANNEL_STATE(Structure):
    _fields_ = [
        ('dwsize', c_ulong),
        ('byDigitalAudioChanTalkState', c_ubyte * 64),
        ('byDigitalChanState', c_ubyte * 64),
        ('byDigitalAudioChanTalkStateEx', c_ubyte * 64 * 3),
        ('byDigitalChanStateEx', c_ubyte * 64 * 3),
        ('byRes', c_ubyte * 64)
    ]


class NET_DVR_IPADDR(Structure):
    _fields_ = [
        ('sIpV4', c_char * 16),
        ('sIpV6', c_char * 128)
    ];

    def __str__(self):
        return "{0}:{1}".format(self.sIpV4, self.sIpV6)


class NET_DVR_IPDEVINFO_V31(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byProType', c_ubyte),
        ('byEnableQuickAdd', c_ubyte),
        ('byRes1', c_ubyte),
        ('sUserName', c_ubyte * 32),
        ('sPassword', c_ubyte * 16),
        ('byDomain', c_ubyte * 64),
        ('struIP', NET_DVR_IPADDR),
        ('wDVRPort', c_ushort),
        ('byRes2', c_ubyte * 34)
    ];

    def __str__(self):
        return "{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}:{9}".format(self.byEnable, self.byProType, self.byEnableQuickAdd,
                                                                self.byRes1, self.sUserName, self.sPassword,
                                                                self.byDomain, self.struIP, self.wDVRPort, self.byRes2)


class NET_DVR_IPCHANINFO(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byIPID', c_ubyte),
        ('byChannel', c_ubyte),
        ('byIPIDHigh', c_ubyte),
        ('byRes', c_ubyte * 32)
    ];


class NET_DVR_STREAM_MEDIA_SERVER_CFG(Structure):
    _fields_ = [
        ('byValid', c_ubyte),
        ('byRes1', c_ubyte * 3),
        ('struDevIP', NET_DVR_IPADDR),
        ('wDevPort', c_ushort),
        ('byTransmitType', c_ubyte),
        ('byRes2', c_ubyte * 69)
    ];


class NET_DVR_DEV_CHAN_INFO(Structure):
    _fields_ = [
        ('struIP', NET_DVR_IPADDR),
        ('wDVRPort', c_ushort),
        ('byChannel', c_ubyte),
        ('byTransProtocol', c_ubyte),
        ('byTransMode', c_ubyte),
        ('byFactoryType', c_ubyte),
        ('byDeviceType', c_ubyte),
        ('byDispChan', c_ubyte),
        ('bySubDispChan', c_ubyte),
        ('byResolution', c_ubyte),
        ('byRes', c_ubyte * 2),
        ('byDomain', c_ubyte * 64),
        ('sUserName', c_ubyte * 32),
        ('sPassword', c_ubyte * 16)
    ];


class NET_DVR_PU_STREAM_CFG(Structure):
    _fields_ = [
        ('dwSize', c_ulong),
        ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG),
        ('strDevChanInfo', NET_DVR_DEV_CHAN_INFO)
    ];


class NET_DVR_IPSERVER_STREAM(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byRes', c_ubyte),
        ('struIPServer', NET_DVR_IPADDR),
        ('wPort', c_ushort),
        ('wDvrNameLen', c_ushort),
        ('byDVRName', c_ubyte * 32),
        ('wDVRSerialLen', c_ushort),
        ('byRes1', c_ushort * 2),
        ('byDVRSerialNumber', c_ubyte * 48),
        ('byUserName', c_ubyte * 32),
        ('byPassword', c_ubyte * 16),
        ('byChannel', c_ubyte),
        ('byRes2', c_ubyte * 11)
    ];


class NET_DVR_DDNS_STREAM_CFG(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byRes1', c_ubyte * 3),
        ('struStreamServer', NET_DVR_IPADDR),
        ('wStreamServerPort', c_ushort),
        ('byStreamServerTransmitType', c_ubyte),
        ('byRes2', c_ubyte),
        ('struIPServer', NET_DVR_IPADDR),
        ('wIPServerPort', c_ushort),
        ('byRes3', c_ubyte * 2),
        ('sDVRName', c_ubyte * 32),
        ('wDVRNameLen', c_ushort),
        ('wDVRSerialLen', c_ushort),
        ('sDVRSerialNumber', c_ubyte * 48),
        ('sUserName', c_ubyte * 32),
        ('sPassWord', c_ubyte * 16),
        ('wDVRPort', c_ushort),
        ('byRes4', c_ubyte * 2),
        ('byChannel', c_ubyte),
        ('byTransProtocol', c_ubyte),
        ('byTransMode', c_ubyte),
        ('byFactoryType', c_ubyte)
    ];


class NET_DVR_PU_STREAM_URL(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('strURL', c_ubyte * 240),
        ('byTransProtocol', c_ubyte),
        ('wIPID', c_ushort),
        ('byChannel', c_ubyte),
        ('byRes', c_ubyte * 7)
    ];


class NET_DVR_HKDDNS_STREAM(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byRes', c_ubyte * 3),
        ('byDDNSDomain', c_ubyte * 64),
        ('wPort', c_ushort),
        ('wAliasLen', c_ushort),
        ('byAlias', c_ubyte * 32),
        ('wDVRSerialLen', c_ushort),
        ('byRes1', c_ubyte * 2),
        ('byDVRSerialNumber', c_ubyte * 48),
        ('byUserName', c_ubyte * 32),
        ('byPassWord', c_ubyte * 16),
        ('byChannel', c_ubyte),
        ('byRes2', c_ubyte * 11)
    ];


class NET_DVR_IPCHANINFO_V40(Structure):
    _fields_ = [
        ('byEnable', c_ubyte),
        ('byRes1', c_ubyte),
        ('wIPID', c_ushort),
        ('dwChannel', c_ulong),
        ('byTransProtocol', c_ubyte),
        ('byTransMode', c_ubyte),
        ('byFactoryType', c_ubyte),
        ('byRes', c_ubyte * 241)
    ];


class NET_DVR_GET_STREAM_UNION(Union):
    _fields_ = [
        ('struChanInfo', NET_DVR_IPCHANINFO),
        ('struPUStream', NET_DVR_PU_STREAM_CFG),
        ('struIPServerStream', NET_DVR_IPSERVER_STREAM),
        ('struDDNSStream', NET_DVR_DDNS_STREAM_CFG),
        ('struStreamUrl', NET_DVR_PU_STREAM_URL),
        ('struHkDDNSStream', NET_DVR_HKDDNS_STREAM),
        ('struIPChan', NET_DVR_IPCHANINFO_V40)
    ];


class NET_DVR_STREAM_MODE(Structure):
    _fields_ = [
        ('byGetStreamType', c_ubyte),
        ('byRes', c_ubyte * 3),
        ('uGetStream', NET_DVR_GET_STREAM_UNION)
    ];


class NET_DVR_IPPARACFG_V40(Structure):
    _fields_ = [
        ('dwSize', c_ulong),
        ('dwGroupNum', c_ulong),
        ('dwAchanNum', c_ulong),
        ('dwDchanNum', c_ulong),
        ('dwStartDChan', c_ulong),
        ('byAnalogChanEnable', c_ubyte * 64),
        ('struIPDevInfo', NET_DVR_IPDEVINFO_V31 * 64),
        ('struStreamMode', NET_DVR_STREAM_MODE * 64),
        ('byRes2', c_ubyte * 20)
    ];

    def __str__(self):
        return "{0}:{1}:{2}:{3}:{4}:{5}".format(self.dwSize, self.dwGroupNum, self.dwAchanNum, self.dwDchanNum,
                                                self.dwStartDChan, self.byAnalogChanEnable)


class NET_DVR_DEVICEINFO_V30(Structure):
    _fields_ = [
        ('sSerialNumber', c_ubyte * 48),
        ('byAlarmInPortNum', c_ubyte),
        ('byAlarmOutPortNum', c_ubyte),
        ('byDiskNum', c_ubyte),
        ('byDVRType', c_ubyte),
        ('byChanNum', c_ubyte),
        ('byStartChan', c_ubyte),
        ('byAudioChanNum', c_ubyte),
        ('byIPChanNum', c_ubyte),
        ('byZeroChanNum', c_ubyte),
        ('byMainProto', c_ubyte),
        ('bySubProto', c_ubyte),
        ('bySupport', c_ubyte),
        ('bySupport1', c_ubyte),
        ('bySupport2', c_ubyte),
        ('wDevType', c_ushort),
        ('bySupport3', c_ubyte),
        ('byMultiStreamProto', c_ubyte),
        ('byStartDChan', c_ubyte),
        ('byStartDTalkChan', c_ubyte),
        ('byHighDChanNum', c_ubyte),
        ('bySupport4', c_ubyte),
        ('byLanguageType', c_ubyte),
        ('byVoiceInChanNum', c_ubyte),
        ('byStartVoiceInChanNo', c_ubyte),
        ('byRes3', c_ubyte * 2),
        ('byMirrorChanNum', c_ubyte),
        ('wStartMirrorChanNo', c_ubyte),
        ('byRes2', c_ubyte * 2)];


LOGIN_RESULT = CFUNCTYPE(c_void_p, c_long, c_ulong, POINTER(NET_DVR_DEVICEINFO_V30), c_void_p)


class NET_DVR_USER_LOGIN_INFO(Structure):
    _fields_ = [('s_DeviceAddress', c_char * 129),
                ('byRes1', c_ubyte),
                ('wPort', c_ushort),
                ('sUserName', c_char * 64),
                ('sPassword', c_char * 64),
                ('cbLoginResult', LOGIN_RESULT),
                ('pUser', c_void_p),
                ('bUseAsynLogin', c_bool),
                ('byRes2', c_char * 128)];

    def __str__(self):
        return '{0}:{1}:{2}:{3}'.format(self.s_DeviceAddress, self.wPort, self.sUserName, self.sPassword)


class NET_DVR_DEVICEINFO_V40(Structure):
    _fields_ = [('struDeviceV30', NET_DVR_DEVICEINFO_V30),
                ('bySupportLock', c_ubyte),
                ('byRetryLoginTime', c_ubyte),
                ('byPasswordLevel', c_ubyte),
                ('byRes1', c_ubyte),
                ('dwSurplusLockTime', c_ulong),
                ('byRes2', c_ubyte * 256)];

    def __str__(self):
        return '{0}{1}'.format(self.struDeviceV30.byIPChanNum, self.byRetryLoginTime)


class NET_DVR_TIME(Structure):
    _fields_ = [('dwYear', c_ulong),
                ('dwMonth', c_ulong),
                ('dwDay', c_ulong),
                ('dwHour', c_ulong),
                ('dwMinute', c_ulong),
                ('dwSecond', c_ulong)];

    def __str__(self):
        return '{0}-{1}-{2} {3}:{4}:{5}'.format(self.dwYear, self.dwMonth, self.dwDay, self.dwHour, self.dwMinute,
                                                self.dwSecond)


class NET_DVR_RTSPCFG(Structure):
    _fields_ = [('dwSize', c_ulong),
                ('wPort', c_ushort),
                ('byReserve', c_ubyte * 54)];

    def __str__(self):
        return '{0}:{1}'.format(self.dwSize, self.wPort)


class NET_DVR_PREVIEWINFO(Structure):
    _fields_ = [('lChannel', c_long),
                ('dwStreamType', c_ulong),
                ('dwLinkMode', c_ulong),
                ('hPlayWnd', c_void_p),
                ('bBlocked', c_bool),
                ('bPassbackRecord', c_bool),
                ('byPreviewMode', c_byte),
                ('byStreamID', c_byte*32),
                ('byProtoType', c_byte),
                ('byRes1', c_byte*2),
                ('dwDisplayBufNum', c_ulong),
                ('byRes', c_byte*216)];
    def __str__(self):
        return "{0}:{1}:{2}".format(str(self.lChannel), str(self.dwStreamType), str(self.dwLinkMode))
