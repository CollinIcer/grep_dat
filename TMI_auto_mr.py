#!/usr/bin/python3
#coding=utf-8


import time
import os
import subprocess
import shutil

ConfFile = "TestCase.txt"
ExecuteFile = "plc_dl_links_MR_Rx201216.exe"
NewCreateName = "Downlinklog"
 
case_id=1000
root=os.getcwd()

OPTION=[0,1,2]
PHR_TMI_ORI=[
#[0]:Name
#[1]:MCS
#[2]:Block size
["GDW",0],
["GDW",1],
["GDW",2],
["GDW",3],
["GDW",4],
["GDW",5],
["GDW",6]
]

PHR_TMI_SIM=[
#[0]:Name
#[1]:MCS
#[2]:Block size
["GDW",0],
["GDW",6]
]

PHR_TMI_SIM1=[
#[0]:Name
#[1]:MCS
#[2]:Block size
["GDW",1],
["GDW",2],
["GDW",3],
["GDW",4],
["GDW",5]
]


PSDU_TMI=[
#[0]:Name
#[1]:MCS
#[2]:BLock size
["GDW",0,16   ], 
["GDW",1,40   ],
["GDW",2,72   ],
["GDW",3,136  ],
["GDW",4,264  ],
["GDW",5,520  ],
["GDW",6,16   ]
]


PSDU_TMI_ORI=[
#[0]:Name
#[1]:MCS
#[2]:BLock size
["GDW",0,16   ], 
["GDW",1,16   ],
["GDW",2,16   ],
["GDW",3,16   ],
["GDW",4,16   ],
["GDW",5,16   ],
["GDW",6,16   ],
["GDW",0,40   ],
["GDW",1,40   ],
["GDW",2,40   ],
["GDW",3,40   ],
["GDW",4,40   ],
["GDW",5,40   ],
["GDW",6,40   ],
["GDW",0,72   ],
["GDW",1,72   ],
["GDW",2,72   ],
["GDW",3,72   ],
["GDW",4,72   ],
["GDW",5,72   ],
["GDW",6,72   ],
["GDW",0,136  ],  
["GDW",1,136  ],
["GDW",2,136  ],
["GDW",3,136  ],
["GDW",4,136  ],
["GDW",5,136  ],
["GDW",6,136  ],
["GDW",0,264  ],
["GDW",1,264  ],
["GDW",2,264  ],
["GDW",3,264  ],
["GDW",4,264  ],
["GDW",5,264  ],
["GDW",6,264  ],
["GDW",0,520  ],
["GDW",1,520  ],
["GDW",2,520  ],
["GDW",3,520  ],
["GDW",4,520  ],
["GDW",5,520  ],
["GDW",6,520  ]
]


def OneCnf(case_id,i,TMIx,TMIy):
    fi=0
	#read original file
    lines = []
    ConfFilePath=root+'\\'+ConfFile
    f=open(ConfFilePath,'r')
    for line in f:
        lines.append(line)

    #print(lines)
    f.close()
    
    #modify line
    lines[50] = str(i) + '\n'         #OPTION
    lines[56] = str(TMIx[1]) + '\n'   #PHRMCS
    lines[64] = str(TMIy[2]) + '\n'   #PSDUblock size
    lines[68] = str(TMIy[1]) + '\n'   #PSDUMCS
    if(i==0):
        zeropad = 15
    elif(i==1):
        zeropad = 22
    else:
        zeropad =26
    lines[78] = str(zeropad) + '\n' 
    lines[262] = "OPTION"+str(i)+"PHR"+str(TMIx[1])+"PSDU"+str(TMIy[1])+"SIZE"+str(TMIy[2])+'\n'
    
    # save file
    f=open(ConfFilePath,'w+')
    f.writelines(lines)
    f.close()
    ExecutePath  = root+'\\'+ExecuteFile
    print(ExecutePath)
    TargetName = "mr_rx_top_case"+str(case_id)
    try:
        subprocess.call(ExecuteFile,timeout = 540 )
        dir_list = os.listdir()
        #[fi for fi,x in enumerate(dir_list) if x.find("Downlinklog")!=-1]
        #NewCreateName=dir_list[fi]
        newf_idx = [fi for fi,x in enumerate(dir_list) if x.find("Downlinklog")!=-1]
        NewCreateName=dir_list[newf_idx[0]]
        
    except subprocess.TimeoutExpired:
        print("OPTION"+str(i)+" TMI phr:"+str(TMIx[1])+" psdu :"+str(TMIy[1])+".Failed!"+'\n')
        
    NewCreateName_mv=root+'\\'+NewCreateName+'\\'+ConfFile
    shutil.copy(ConfFilePath,NewCreateName)
    
    print("OPTION"+str(i)+" TMI phr:"+str(TMIx[1])+" psdu :"+str(TMIy[1])+"OK\n")
    os.rename(NewCreateName,TargetName)
	# time.sleep(1)


if __name__ == '__main__':
	
    for i in OPTION:
        for x in PHR_TMI_ORI:
            for y in PSDU_TMI_ORI:
                if(case_id==1006):
                    print("DO------------\n")
                    OneCnf(case_id,i,x,y)
                case_id = case_id + 1
                

	

