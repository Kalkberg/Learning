# -*- coding: utf-8 -*-
"""
Creates Histograms from polling data

@author: pyakovlev
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

# Import data and rename long columns
AllData = pandas.read_csv('201709CAH_edited.csv')

## Slice data for plots
Men = AllData[AllData['Gender']=='Male']
Women = AllData[AllData['Gender']=='Female']
IncLt25 = AllData[AllData['Income'] < 25000]
Inc25t50 = AllData[(AllData['Income'] > 25000) & (AllData['Income'] < 50000)]
Inc50t75 = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)]
Inc75t100  = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)]
Incgt100 = AllData[AllData['Income'] > 100000]
Democrats = AllData[AllData.iloc[:,4].str.contains('Democrat')]
Republicans = AllData[AllData.iloc[:,4].str.contains('Republican')]
AgeLt30 = AllData[AllData['Age']<30]
Age30t60 = AllData[(AllData['Age']<60) & (AllData['Age']>30)]
AgeGt60 = AllData[AllData['Age']>30]
MenDems = AllData[(AllData['Gender']=='Male')&(AllData.iloc[:,4].str.contains('Democrat'))]
WomenDems = AllData[(AllData['Gender']=='Female')&(AllData.iloc[:,4].str.contains('Democrat'))]
MenReps = AllData[(AllData['Gender']=='Male')&(AllData.iloc[:,4].str.contains('Republican'))]
WomenReps = AllData[(AllData['Gender']=='Female')&(AllData.iloc[:,4].str.contains('Republican'))]
IncLt25Men = AllData[(AllData['Income'] < 25000)&(AllData['Gender']=='Male')]
Inc25t50Men = AllData[(AllData['Income'] > 25000) & (AllData['Income'] < 50000)&(AllData['Gender']=='Male')]
Inc50t75Men = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)&(AllData['Gender']=='Male')]
Inc75t100Men  = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)&(AllData['Gender']=='Male')]
Incgt100Men = AllData[(AllData['Income'] > 100000)&(AllData['Gender']=='Male')]
IncLt25Women = AllData[(AllData['Income'] < 25000)&(AllData['Gender']=='Female')]
Inc25t50Women = AllData[(AllData['Income'] > 25000) & (AllData['Income'] < 50000)&(AllData['Gender']=='Female')]
Inc50t75Women = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)&(AllData['Gender']=='Female')]
Inc75t100Women = AllData[(AllData['Income'] > 50000) & (AllData['Income'] < 75000)&(AllData['Gender']=='Female')]
Incgt100Women = AllData[(AllData['Income'] > 100000)&(AllData['Gender']=='Female')]
GradHS = AllData[AllData.iloc[:,6]=="High school"]
GradSColl = AllData[AllData.iloc[:,6]=="Some college"]
GradColl = AllData[AllData.iloc[:,6]=="College degree"]
GradGrad = AllData[AllData.iloc[:,6]=="Graduate degree"]
ScienceSA = AllData[AllData.iloc[:,17]=="Strongly Agree"]
ScienceMA = AllData[AllData.iloc[:,17]=="Somewhat Agree"]
ScienceMeh = AllData[AllData.iloc[:,17]=="Niether Agree nor Disagree"]
ScienceMD = AllData[AllData.iloc[:,17]=="Somewhat Disagree"]
ScienceSD = AllData[AllData.iloc[:,17]=="Strongly Disagree"]
VaccinesSA = AllData[AllData.iloc[:,18]=="Strongly Agree"]
VaccinesMA = AllData[AllData.iloc[:,18]=="Somewhat Agree"]
VaccinesMeh = AllData[AllData.iloc[:,18]=="Niether Agree nor Disagree"]
VaccinesMD = AllData[AllData.iloc[:,18]=="Somewhat Disagree"]
VaccinesSD = AllData[AllData.iloc[:,18]=="Strongly Disagree"]
ScifundLow = AllData[AllData.iloc[:,24]=="Too Low"]
ScifundMed = AllData[AllData.iloc[:,24]=="About Right"]
ScifundHigh = AllData[AllData.iloc[:,24]=="Too High"]
#NotHungry = AllData[AllData.iloc[:,20] == "Not Hungry"]
#LittleHungry = AllData[AllData.iloc[:,20] == "A Little Hungry"]
#VeryHungry = AllData[AllData.iloc[:,20] == "Very Hungry"]
#NotHungryMen = AllData[(AllData.iloc[:,20] == "Not Hungry")&(AllData['Gender']=='Male')]
#LittleHungryMen = AllData[(AllData.iloc[:,20] == "A Little Hungry")&(AllData['Gender']=='Male')]
#VeryHungryMen = AllData[(AllData.iloc[:,20] == "Very Hungry")&(AllData['Gender']=='Male')]
#NotHungryWomen = AllData[(AllData.iloc[:,20] == "Not Hungry")&(AllData['Gender']=='Female')]
#LittleHungryWomen = AllData[(AllData.iloc[:,20] == "A Little Hungry")&(AllData['Gender']=='Female')]
#VeryHungryWomen = AllData[(AllData.iloc[:,20] == "Very Hungry")&(AllData['Gender']=='Female')]
#
# Gender
DemocratsMenPct = Democrats.iloc[:,1].value_counts()[1] / (Democrats.iloc[:,1].value_counts()[0]+Democrats.iloc[:,1].value_counts()[1])
RepublicansMenPct = Republicans.iloc[:,1].value_counts()[1] / (Republicans.iloc[:,1].value_counts()[0]+Republicans.iloc[:,1].value_counts()[1])
IncLt25MenPct = IncLt25.iloc[:,1].value_counts()[1] / (IncLt25.iloc[:,1].value_counts()[0]+IncLt25.iloc[:,1].value_counts()[1])
Inc25t50MenPct = Inc25t50.iloc[:,1].value_counts()[1] / (Inc25t50.iloc[:,1].value_counts()[0]+Inc25t50.iloc[:,1].value_counts()[1])
Inc50t75MenPct = Inc50t75.iloc[:,1].value_counts()[1] / (Inc50t75.iloc[:,1].value_counts()[0]+Inc50t75.iloc[:,1].value_counts()[1])
Inc75t100MenPct = Inc75t100.iloc[:,1].value_counts()[1] / (Inc75t100.iloc[:,1].value_counts()[0]+Inc75t100.iloc[:,1].value_counts()[1])
Incgt100MenPct = Incgt100.iloc[:,1].value_counts()[1] / (Incgt100.iloc[:,1].value_counts()[0]+Incgt100.iloc[:,1].value_counts()[1])
AgeLt30MenPct = AgeLt30.iloc[:,1].value_counts()[1] / (AgeLt30.iloc[:,1].value_counts()[0]+AgeLt30.iloc[:,1].value_counts()[1])
Age30t60MenPct = Age30t60.iloc[:,1].value_counts()[1] / (Age30t60.iloc[:,1].value_counts()[0]+Age30t60.iloc[:,1].value_counts()[1])
AgeGt60MenPct = AgeGt60.iloc[:,1].value_counts()[1] / (AgeGt60.iloc[:,1].value_counts()[0]+AgeGt60.iloc[:,1].value_counts()[1])
#NotHungryMenPct = NotHungry.iloc[:,1].value_counts()[1] / (NotHungry.iloc[:,1].value_counts()[0]+NotHungry.iloc[:,1].value_counts()[1])
#LittleHungryMenPct = LittleHungry.iloc[:,1].value_counts()[1] / (LittleHungry.iloc[:,1].value_counts()[0]+LittleHungry.iloc[:,1].value_counts()[1])
#VeryHungryMenPct = VeryHungry.iloc[:,1].value_counts()[1] / (VeryHungry.iloc[:,1].value_counts()[0]+VeryHungry.iloc[:,1].value_counts()[1])

# Science
ScienceSAVaccinesSA = len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Agree"]) / (len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Disagree"]))
ScienceSAVaccinesMA = len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Agree"])  / (len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Disagree"]))
ScienceSAVaccinesMD = len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Disagree"])  / (len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Disagree"]))
ScienceSAVaccinesSD = len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Disagree"])  / (len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSA[ScienceSA.iloc[:,18]=="Strongly Disagree"]) )
ScienceMAVaccinesSA = len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Agree"])  / (len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Disagree"]))
ScienceMAVaccinesMA = len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Agree"])  / (len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Disagree"]))
ScienceMAVaccinesMD = len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Disagree"])  / (len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Disagree"]))
ScienceMAVaccinesSD = len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Disagree"])  / (len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMA[ScienceMA.iloc[:,18]=="Strongly Disagree"]))
ScienceMDVaccinesSA = len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Agree"]) / (len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Disagree"]))
ScienceMDVaccinesMA = len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Agree"])  / (len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Disagree"]))
ScienceMDVaccinesMD = len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Disagree"])  / (len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Disagree"]))
ScienceMDVaccinesSD = len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Disagree"])  / (len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceMD[ScienceMD.iloc[:,18]=="Strongly Disagree"]))
ScienceSDVaccinesSA = len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Agree"]) / (len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Disagree"]))
ScienceSDVaccinesMA = len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Agree"])  / (len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Disagree"]))
ScienceSDVaccinesMD = len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Disagree"]) / (len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Disagree"]))
ScienceSDVaccinesSD = len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Disagree"]) / (len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Agree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Somewhat Disagree"]) + len(ScienceSD[ScienceSD.iloc[:,18]=="Strongly Disagree"]))

MenDemsScienceSA = len(MenDems[MenDems.iloc[:,17]=="Strongly Agree"]) / (len(MenDems[MenDems.iloc[:,17]=="Strongly Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Disagree"]) + len(MenDems[MenDems.iloc[:,17]=="Strongly Disagree"]))
MenDemsScienceMA = len(MenDems[MenDems.iloc[:,17]=="Somewhat Agree"]) / (len(MenDems[MenDems.iloc[:,17]=="Strongly Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Disagree"]) + len(MenDems[MenDems.iloc[:,17]=="Strongly Disagree"]))
MenDemsScienceMD = len(MenDems[MenDems.iloc[:,17]=="Somewhat Disagree"]) / (len(MenDems[MenDems.iloc[:,17]=="Strongly Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Disagree"]) + len(MenDems[MenDems.iloc[:,17]=="Strongly Disagree"]))
MenDemsScienceSD = len(MenDems[MenDems.iloc[:,17]=="Strongly Disagree"]) / (len(MenDems[MenDems.iloc[:,17]=="Strongly Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Agree"]) + len(MenDems[MenDems.iloc[:,17]=="Somewhat Disagree"]) + len(MenDems[MenDems.iloc[:,17]=="Strongly Disagree"]))
WomenDemsScienceSA = len(WomenDems[WomenDems.iloc[:,17]=="Strongly Agree"]) / (len(WomenDems[WomenDems.iloc[:,17]=="Strongly Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Disagree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Strongly Disagree"]))
WomenDemsScienceMA = len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Agree"]) / (len(WomenDems[WomenDems.iloc[:,17]=="Strongly Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Disagree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Strongly Disagree"]))
WomenDemsScienceMD = len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Disagree"]) / (len(WomenDems[WomenDems.iloc[:,17]=="Strongly Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Disagree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Strongly Disagree"]))
WomenDemsScienceSD = len(WomenDems[WomenDems.iloc[:,17]=="Strongly Disagree"]) / (len(WomenDems[WomenDems.iloc[:,17]=="Strongly Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Agree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Somewhat Disagree"]) + len(WomenDems[WomenDems.iloc[:,17]=="Strongly Disagree"]))
MenRepsScienceSA = len(MenReps[MenReps.iloc[:,17]=="Strongly Agree"]) / (len(MenReps[MenReps.iloc[:,17]=="Strongly Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Disagree"]) + len(MenReps[MenReps.iloc[:,17]=="Strongly Disagree"]))
MenRepsScienceMA = len(MenReps[MenReps.iloc[:,17]=="Somewhat Agree"]) / (len(MenReps[MenReps.iloc[:,17]=="Strongly Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Disagree"]) + len(MenReps[MenReps.iloc[:,17]=="Strongly Disagree"]))
MenRepsScienceMD = len(MenReps[MenReps.iloc[:,17]=="Somewhat Disagree"]) / (len(MenReps[MenReps.iloc[:,17]=="Strongly Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Disagree"]) + len(MenReps[MenReps.iloc[:,17]=="Strongly Disagree"]))
MenRepsScienceSD = len(MenReps[MenReps.iloc[:,17]=="Strongly Disagree"]) / (len(MenReps[MenReps.iloc[:,17]=="Strongly Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Agree"]) + len(MenReps[MenReps.iloc[:,17]=="Somewhat Disagree"]) + len(MenReps[MenReps.iloc[:,17]=="Strongly Disagree"]))
WomenRepsScienceSA = len(WomenReps[WomenReps.iloc[:,17]=="Strongly Agree"]) / (len(WomenReps[WomenReps.iloc[:,17]=="Strongly Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Disagree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Strongly Disagree"]))
WomenRepsScienceMA = len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Agree"]) / (len(WomenReps[WomenReps.iloc[:,17]=="Strongly Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Disagree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Strongly Disagree"]))
WomenRepsScienceMD = len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Disagree"]) / (len(WomenReps[WomenReps.iloc[:,17]=="Strongly Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Disagree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Strongly Disagree"]))
WomenRepsScienceSD = len(WomenReps[WomenReps.iloc[:,17]=="Strongly Disagree"]) / (len(WomenReps[WomenReps.iloc[:,17]=="Strongly Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Agree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Somewhat Disagree"]) + len(WomenReps[WomenReps.iloc[:,17]=="Strongly Disagree"]))

# Science Funding
ScifundLowVal = ScifundLow.iloc[:,22]
ScifundMedVal = ScifundMed.iloc[:,22]
ScifundHighVal = ScifundHigh.iloc[:,22]

#Make Plots
pp = PdfPages('CAPlots2.pdf')

#plt.figure(1)
#plt.bar(np.arange(2),(MenYes,WomenYes))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(2),('Men','Women'))
#plt.ylabel('Percentage Yes')
#pp.savefig()
#
#plt.figure(2)
#plt.bar(np.arange(2),(DemocratsYes,RepublicansYes))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(2),('Democrats','Republicans'))
#plt.ylabel('Percentage Yes')
#pp.savefig()
#
#plt.figure(3)
#plt.bar(np.arange(3),(AgeLt30Yes,Age30t60Yes,AgeGt60Yes))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(3),('Age <30','Age 30-60', 'Age >60'))
#plt.ylabel('Percentage Yes')
#pp.savefig()
#
#plt.figure(4)
#plt.bar(np.arange(5),(IncLt25Yes,Inc25t50Yes,Inc50t75Yes,Inc75t100Yes,Incgt100Yes))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
#plt.ylabel('Percentage Yes')
#plt.tight_layout()
#pp.savefig()
#
plt.figure(5)
plt.bar(np.arange(5),(IncLt25MenPct,Inc25t50MenPct,Inc50t75MenPct,Inc75t100MenPct,Incgt100MenPct))
plt.title('Gender')
plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
plt.ylabel('Percentage Men')
plt.tight_layout()
pp.savefig()
#
#plt.figure(6)
#plt.bar(np.arange(3),(NotHungryYes,LittleHungryYes,VeryHungryYes))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Yes')
#pp.savefig()
#
#plt.figure(7)
#plt.bar(np.arange(3),(NotHungryMenPct,LittleHungryMenPct,VeryHungryMenPct))
#plt.title('Gender')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Men')
#pp.savefig()
#
#plt.figure(8)
#plt.bar(np.arange(2),(DemocratsMEqual,RepublicansMEqual))
#plt.title('Would you perfer a more or less equal society?')
#plt.xticks(np.arange(2),('Republicans', 'Democrats'))
#plt.ylabel('Percentage More Equal')
#pp.savefig()
#
#plt.figure(9)
#plt.bar(np.arange(2),(MenMEqual,WomenMEqual))
#plt.title('Would you perfer a more or less equal society?')
#plt.xticks(np.arange(2),('Men', 'Women'))
#plt.ylabel('Percentage More Equal')
#pp.savefig()
#
#plt.figure(10)
#width = .35
#fig10, ax10 = plt.subplots()
#rects1 = ax10.bar(np.arange(5), (IncLt25MenYesPct,Inc25t50MenYesPct,Inc50t75MenYesPct,Inc75t100MenYesPct,Incgt100MenYesPct), width, color='r')
#rects2 = ax10.bar(np.arange(5)+width, (IncLt25WomenYesPct,Inc25t50WomenYesPct,Inc50t75WomenYesPct,Inc75t100WomenYesPct,Incgt100WomenYesPct), width, color='b')
#ax10.legend((rects1[0], rects2[0]), ('Men', 'Women'))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
#plt.ylabel('Percentage Yes')
#plt.tight_layout()
#pp.savefig()
#
#plt.figure(11)
#width = .35
#fig11, ax11 = plt.subplots()
#rects1 = ax11.bar(np.arange(3),(NotHungryMenYesPct,LittleHungryMenYesPct,VeryHungryMenYesPct), width, color='r')
#rects2 = ax11.bar(np.arange(3)+width,(NotHungryWomenYesPct,LittleHungryWomenYesPct,VeryHungryWomenYesPct), width, color='b')
#ax11.legend((rects1[0], rects2[0]), ('Men', 'Women'))
#plt.title('Could you beat most people in a fist fight?')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Yes')
#pp.savefig()
#
#plt.figure(12)
#width = .35
#fig12, ax12 = plt.subplots()
#rects1 = ax12.bar(np.arange(3),(NotHungryMenMEqual,LittleHungryMenMEqual,VeryHungryMenMEqual), width, color='r')
#rects2 = ax12.bar(np.arange(3)+width,(NotHungryWomenMEqual,LittleHungryWomenMEqual,VeryHungryWomenMEqual), width, color='b')
#ax12.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
#plt.title('Would you perfer a more or less equal society?')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage More Equal')
#pp.savefig()
#
#plt.figure(13)
#width = .2
#fig13, ax13 = plt.subplots()
#rects1 = ax13.bar(np.arange(5),(IncLt25Full,Inc25t50Full,Inc50t75Full,Inc75t100Full,Incgt100Full), width, color='r')
#rects2 = ax13.bar(np.arange(5)+width,(IncLt25Little,Inc25t50Little,Inc50t75Little,Inc75t100Little,Incgt100Little), width, color='g')
#rects3 = ax13.bar(np.arange(5)+2*width,(IncLt25Very,Inc25t50Very,Inc50t75Very,Inc75t100Very,Incgt100Very), width, color='b')
#ax13.legend((rects1[0], rects2[0], rects3[0]), ('Not Hungry', 'A Little Hungry', 'Very Hungry'), loc=5)
#plt.title('Hunger by Income')
#plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
#plt.ylabel('Percentage')
#plt.tight_layout()
#pp.savefig()
#
#plt.figure(14)
#width = .35
#fig14, ax14 = plt.subplots()
#rects1 = ax14.bar(np.arange(3),(NotHungryMenWelfare,LittleHungryMenWelfare,VeryHungryMenWelfare), width, color='r')
#rects2 = ax14.bar(np.arange(3)+width,(NotHungryWomenWelfare,LittleHungryWomenWelfare,VeryHungryWomenWelfare), width, color='b')
#ax14.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
#plt.title('Do you think federal funding for welfare programs in America \n should be increased, decreased, or kept the same? ')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Saying Decrease')
#pp.savefig()
#
#plt.figure(15)
#width = .35
#fig15, ax15 = plt.subplots()
#rects1 = ax15.bar(np.arange(3),(NotHungryMenWelfareInc,LittleHungryMenWelfareInc,VeryHungryMenWelfareInc), width, color='r')
#rects2 = ax15.bar(np.arange(3)+width,(NotHungryWomenWelfareInc,LittleHungryWomenWelfare,VeryHungryWomenWelfareInc), width, color='b')
#ax15.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
#plt.title('Do you think federal funding for welfare programs in America \n should be increased, decreased, or kept the same? ')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Saying Increase')
#pp.savefig()
#
#plt.figure(16)
#width = .35
#fig16, ax16 = plt.subplots()
#rects1 = ax16.bar(np.arange(3),(NotHungryMenRobin,LittleHungryMenRobin,VeryHungryMenRobin), width, color='r')
#rects2 = ax16.bar(np.arange(3)+width,(NotHungryWomenRobin,LittleHungryWomenRobin,VeryHungryWomenRobin), width, color='b')
#ax16.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
#plt.title('Do you think our government should take money \n from the rich and give it to the poor? ')
#plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
#plt.ylabel('Percentage Saying Yes')
#pp.savefig()
#

plt.figure(17)
width = .15
fig17, ax17 = plt.subplots()
rects1 = ax17.bar(np.arange(4)-1*width,(ScienceSAVaccinesSA,ScienceSAVaccinesMA,ScienceSAVaccinesMD,ScienceSAVaccinesSD), width, color='r')
rects2 = ax17.bar(np.arange(4),(ScienceMAVaccinesSA,ScienceMAVaccinesMA,ScienceMAVaccinesMD,ScienceMAVaccinesSD), width, color='g')
rects4 = ax17.bar(np.arange(4)+1*width,(ScienceSDVaccinesSA,ScienceSDVaccinesMA,ScienceSDVaccinesMD,ScienceSDVaccinesSD), width, color='b')
rects5 = ax17.bar(np.arange(4)+2*width,(ScienceSAVaccinesSA,ScienceSAVaccinesMA,ScienceSAVaccinesMD,ScienceSAVaccinesSD), width, color='m')

ax17.legend((rects1[0], rects2[0], rects4[0], rects5[0]), ('Strongly Agree', 'Somewhat Agree', 'Somewhat Disagree','Strongly Disagree'), loc=0, title="Vaccines are safe")
plt.title('Scientists are generally honest and are serving the public good. ')
plt.xticks(np.arange(4),('Stongly\nAgree', 'Somewhat\nAgree', 'Somewhat\nDisagree', 'Strongly\nDisagree'))
plt.ylabel('Percentage')
pp.savefig()

plt.figure(18)
width = .15
fig18, ax18 = plt.subplots()
rects1 = ax18.bar(np.arange(4)-1*width,(MenDemsScienceSA,MenDemsScienceMA,MenDemsScienceMD,MenDemsScienceSD), width, color='r')
rects2 = ax18.bar(np.arange(4),(WomenDemsScienceSA,WomenDemsScienceMA,WomenDemsScienceMD,WomenDemsScienceSD), width, color='g')
rects3 = ax18.bar(np.arange(4)+1*width,(MenRepsScienceSA,MenRepsScienceMA,MenRepsScienceMD,MenRepsScienceSD), width, color='b')
rects4 = ax18.bar(np.arange(4)+2*width,(WomenRepsScienceSA,WomenRepsScienceMA,WomenRepsScienceMD,WomenRepsScienceSD), width, color='m')

ax18.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Strongly Agree', 'Somewhat Agree', 'Somewhat Disagree','Strongly Disagree'), loc=0)
plt.title('Scientists are generally honest and are serving the public good. ')
plt.xticks(np.arange(4),('Democratic\nMen', 'Democratic\nWomen', 'Republican\nMen', 'Republican\nWomen'))
plt.ylabel('Percentage')
pp.savefig()

plt.figure(19)
fig19, ax19 = plt.subplots()
sns.kdeplot(ScifundHigh.iloc[:,22],legend=False,ax=ax19,color='r')
sns.kdeplot(ScifundMed.iloc[:,22],legend=False,ax=ax19,color='k')
sns.kdeplot(ScifundLow.iloc[:,22],legend=False,ax=ax19,color='b')
red_line = mlines.Line2D([],[],color='r', label='Too High')
black_line = mlines.Line2D([],[],color='k', label='Just Right')
blue_line = mlines.Line2D([],[],color='b', label='Too Low')
ax19.set_xlim(0,100)
plt.xlabel('Percentage of Federal Budget Spent on Science')
ax19.legend(handles=[red_line,black_line,blue_line], loc=0, title="Federal funding for science is:")
pp.savefig()

plt.figure(20)
sns.factorplot(x="Gender",col="Political Affiliation", data=AllData, kind="count")
pp.savefig()

plt.figure(21)
sns.factorplot(x=AllData.columns[3],col="Political Affiliation", data=AllData, kind="count")
pp.savefig()

plt.figure(22)
sns.factorplot(x=AllData.columns[22],y=AllData.columns[24],hue="Gender", data=AllData,kind='violin', size=8)
pp.savefig()

plt.figure(23)
sns.factorplot(x=AllData.columns[22],y=AllData.columns[24],hue="Political Affiliation", data=AllData,kind='violin', size=8)
pp.savefig()

plt.figure(24)
sns.factorplot(x="Books Read",y="Political Affiliation", hue="Gender", data=AllData, kind="bar",size=5)
pp.savefig()

pp.close()