# -*- coding: utf-8 -*-
"""
Creates Histograms from polling data

@author: pyakovlev
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# Import data and rename long columns
AllData = pandas.read_csv('201711CAH_edited.csv')

# Slice data for plots
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
NotHungry = AllData[AllData.iloc[:,20] == "Not Hungry"]
LittleHungry = AllData[AllData.iloc[:,20] == "A Little Hungry"]
VeryHungry = AllData[AllData.iloc[:,20] == "Very Hungry"]
NotHungryMen = AllData[(AllData.iloc[:,20] == "Not Hungry")&(AllData['Gender']=='Male')]
LittleHungryMen = AllData[(AllData.iloc[:,20] == "A Little Hungry")&(AllData['Gender']=='Male')]
VeryHungryMen = AllData[(AllData.iloc[:,20] == "Very Hungry")&(AllData['Gender']=='Male')]
NotHungryWomen = AllData[(AllData.iloc[:,20] == "Not Hungry")&(AllData['Gender']=='Female')]
LittleHungryWomen = AllData[(AllData.iloc[:,20] == "A Little Hungry")&(AllData['Gender']=='Female')]
VeryHungryWomen = AllData[(AllData.iloc[:,20] == "Very Hungry")&(AllData['Gender']=='Female')]

# Fights
MenYes = len(Men[Men.iloc[:,21]=="Yes"]) / (len(Men[Men.iloc[:,21]=="Yes"])+len(Men[Men.iloc[:,21]=="No"]))
WomenYes = len(Women[Women.iloc[:,21]=="Yes"]) / (len(Women[Women.iloc[:,21]=="Yes"])+len(Women[Women.iloc[:,21]=="No"]))
DemocratsYes = len(Democrats[Democrats.iloc[:,21]=="Yes"]) / (len(Democrats[Democrats.iloc[:,21]=="Yes"])+len(Democrats[Democrats.iloc[:,21]=="No"]))
RepublicansYes = len(Republicans[Republicans.iloc[:,21]=="Yes"]) / (len(Republicans[Republicans.iloc[:,21]=="Yes"])+len(Republicans[Republicans.iloc[:,21]=="No"]))
IncLt25Yes = len(IncLt25[IncLt25.iloc[:,21]=="Yes"]) / (len(IncLt25[IncLt25.iloc[:,21]=="Yes"])+len(IncLt25[IncLt25.iloc[:,21]=="No"]))
Inc25t50Yes = len(Inc25t50[Inc25t50.iloc[:,21]=="Yes"]) / (len(Inc25t50[Inc25t50.iloc[:,21]=="Yes"])+len(Inc25t50[Inc25t50.iloc[:,21]=="No"]))
Inc50t75Yes = len(Inc50t75[Inc50t75.iloc[:,21]=="Yes"]) / (len(Inc50t75[Inc50t75.iloc[:,21]=="Yes"])+len(Inc50t75[Inc50t75.iloc[:,21]=="No"]))
Inc75t100Yes = len(Inc75t100[Inc75t100.iloc[:,21]=="Yes"]) / (len(Inc75t100[Inc75t100.iloc[:,21]=="Yes"])+len(Inc75t100[Inc75t100.iloc[:,21]=="No"]))
Incgt100Yes = len(Incgt100[Incgt100.iloc[:,21]=="Yes"]) / (len(Incgt100[Incgt100.iloc[:,21]=="Yes"])+len(Incgt100[Incgt100.iloc[:,21]=="No"]))
AgeLt30Yes = len(AgeLt30[AgeLt30.iloc[:,21]=="Yes"]) / (len(AgeLt30[AgeLt30.iloc[:,21]=="Yes"])+len(AgeLt30[AgeLt30.iloc[:,21]=="No"]))
Age30t60Yes = len(Age30t60[Age30t60.iloc[:,21]=="Yes"]) / (len(Age30t60[Age30t60.iloc[:,21]=="Yes"])+len(Age30t60[Age30t60.iloc[:,21]=="No"]))
AgeGt60Yes = len(AgeGt60[AgeGt60.iloc[:,21]=="Yes"]) / (len(AgeGt60[AgeGt60.iloc[:,21]=="Yes"])+len(AgeGt60[AgeGt60.iloc[:,21]=="No"]))
MenDemsYes = len(MenDems[MenDems.iloc[:,21]=="Yes"]) / (len(MenDems[MenDems.iloc[:,21]=="Yes"])+len(MenDems[MenDems.iloc[:,21]=="No"]))
WomenDemsYes = len(WomenDems[WomenDems.iloc[:,21]=="Yes"]) / (len(WomenDems[WomenDems.iloc[:,21]=="Yes"])+len(WomenDems[WomenDems.iloc[:,21]=="No"]))
MenRepsYes = len(MenReps[MenReps.iloc[:,21]=="Yes"]) / (len(MenReps[MenReps.iloc[:,21]=="Yes"])+len(MenReps[MenReps.iloc[:,21]=="No"]))
WomenRepsYes = len(WomenReps[WomenReps.iloc[:,21]=="Yes"]) / (len(WomenReps[WomenReps.iloc[:,21]=="Yes"])+len(WomenReps[WomenReps.iloc[:,21]=="No"]))
IncLt25MenYesPct = len(IncLt25Men[IncLt25Men.iloc[:,21]=="Yes"]) / (len(IncLt25Men[IncLt25Men.iloc[:,21]=="Yes"])+len(IncLt25Men[IncLt25Men.iloc[:,21]=="No"]))
Inc25t50MenYesPct = len(Inc25t50Men[Inc25t50Men.iloc[:,21]=="Yes"]) / (len(Inc25t50Men[Inc25t50Men.iloc[:,21]=="Yes"])+len(Inc25t50Men[Inc25t50Men.iloc[:,21]=="No"]))
Inc50t75MenYesPct = len(Inc50t75Men[Inc50t75Men.iloc[:,21]=="Yes"]) / (len(Inc50t75Men[Inc50t75Men.iloc[:,21]=="Yes"])+len(Inc50t75Men[Inc50t75Men.iloc[:,21]=="No"]))
Inc75t100MenYesPct = len(Inc75t100Men[Inc75t100Men.iloc[:,21]=="Yes"]) / (len(Inc75t100Men[Inc75t100Men.iloc[:,21]=="Yes"])+len(Inc75t100Men[Inc75t100Men.iloc[:,21]=="No"]))
Incgt100MenYesPct = len(Incgt100Men[Incgt100Men.iloc[:,21]=="Yes"]) / (len(Incgt100Men[Incgt100Men.iloc[:,21]=="Yes"])+len(Incgt100Men[Incgt100Men.iloc[:,21]=="No"]))
IncLt25WomenYesPct = len(IncLt25Women[IncLt25Women.iloc[:,21]=="Yes"]) / (len(IncLt25Women[IncLt25Women.iloc[:,21]=="Yes"])+len(IncLt25Women[IncLt25Women.iloc[:,21]=="No"]))
Inc25t50WomenYesPct = len(Inc25t50Women[Inc25t50Women.iloc[:,21]=="Yes"]) / (len(Inc25t50Women[Inc25t50Women.iloc[:,21]=="Yes"])+len(Inc25t50Women[Inc25t50Women.iloc[:,21]=="No"]))
Inc50t75WomenYesPct = len(Inc50t75Women[Inc50t75Women.iloc[:,21]=="Yes"]) / (len(Inc50t75Women[Inc50t75Women.iloc[:,21]=="Yes"])+len(Inc50t75Women[Inc50t75Women.iloc[:,21]=="No"]))
Inc75t100WomenYesPct = len(Inc75t100Women[Inc75t100Women.iloc[:,21]=="Yes"]) / (len(Inc75t100Women[Inc75t100Women.iloc[:,21]=="Yes"])+len(Inc75t100Women[Inc75t100Women.iloc[:,21]=="No"]))
Incgt100WomenYesPct = len(Incgt100Women[Incgt100Women.iloc[:,21]=="Yes"]) / (len(Incgt100Women[Incgt100Women.iloc[:,21]=="Yes"])+len(Incgt100Women[Incgt100Women.iloc[:,21]=="No"]))
NotHungryYes = len(NotHungry[NotHungry.iloc[:,21]=="Yes"]) / (len(NotHungry[NotHungry.iloc[:,21]=="Yes"])+len(NotHungry[NotHungry.iloc[:,21]=="No"]))
LittleHungryYes = len(NotHungry[NotHungry.iloc[:,21]=="Yes"]) / (len(NotHungry[NotHungry.iloc[:,21]=="Yes"])+len(NotHungry[NotHungry.iloc[:,21]=="No"]))
VeryHungryYes = len(VeryHungry[VeryHungry.iloc[:,21]=="Yes"]) / (len(VeryHungry[VeryHungry.iloc[:,21]=="Yes"])+len(VeryHungry[VeryHungry.iloc[:,21]=="No"]))
NotHungryMenYesPct = len(NotHungryMen[NotHungryMen.iloc[:,21]=="Yes"]) / (len(NotHungryMen[NotHungryMen.iloc[:,21]=="Yes"])+len(NotHungryMen[NotHungryMen.iloc[:,21]=="No"]))
LittleHungryMenYesPct = len(LittleHungryMen[LittleHungryMen.iloc[:,21]=="Yes"]) / (len(LittleHungryMen[LittleHungryMen.iloc[:,21]=="Yes"])+len(LittleHungryMen[LittleHungryMen.iloc[:,21]=="No"]))
VeryHungryMenYesPct = len(VeryHungryMen[VeryHungryMen.iloc[:,21]=="Yes"]) / (len(VeryHungryMen[VeryHungryMen.iloc[:,21]=="Yes"])+len(VeryHungryMen[VeryHungryMen.iloc[:,21]=="No"]))
NotHungryWomenYesPct = len(NotHungryWomen[NotHungryWomen.iloc[:,21]=="Yes"]) / (len(NotHungryWomen[NotHungryWomen.iloc[:,21]=="Yes"])+len(NotHungryWomen[NotHungryWomen.iloc[:,21]=="No"]))
LittleHungryWomenYesPct = len(LittleHungryWomen[LittleHungryWomen.iloc[:,21]=="Yes"]) / (len(LittleHungryWomen[LittleHungryWomen.iloc[:,21]=="Yes"])+len(LittleHungryWomen[LittleHungryWomen.iloc[:,21]=="No"]))
VeryHungryWomenYesPct = len(VeryHungryWomen[VeryHungryWomen.iloc[:,21]=="Yes"]) / (len(VeryHungryWomen[VeryHungryWomen.iloc[:,21]=="Yes"])+len(VeryHungryWomen[VeryHungryWomen.iloc[:,21]=="No"]))


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
NotHungryMenPct = NotHungry.iloc[:,1].value_counts()[1] / (NotHungry.iloc[:,1].value_counts()[0]+NotHungry.iloc[:,1].value_counts()[1])
LittleHungryMenPct = LittleHungry.iloc[:,1].value_counts()[1] / (LittleHungry.iloc[:,1].value_counts()[0]+LittleHungry.iloc[:,1].value_counts()[1])
VeryHungryMenPct = VeryHungry.iloc[:,1].value_counts()[1] / (VeryHungry.iloc[:,1].value_counts()[0]+VeryHungry.iloc[:,1].value_counts()[1])

# Equality
MenMEqual = len(Men[Men.iloc[:,15]=="More Equal Society"]) / (len(Men[Men.iloc[:,15]=="More Equal Society"])+len(Men[Men.iloc[:,15]=="More Unequal Society"]))
WomenMEqual = len(Women[Women.iloc[:,15]=="More Equal Society"]) / (len(Women[Women.iloc[:,15]=="More Equal Society"])+len(Women[Women.iloc[:,15]=="More Unequal Society"]))
DemocratsMEqual = len(Democrats[Democrats.iloc[:,15]=="More Equal Society"]) / (len(Democrats[Democrats.iloc[:,15]=="More Equal Society"])+len(Democrats[Democrats.iloc[:,15]=="More Unequal Society"]))
RepublicansMEqual = len(Republicans[Republicans.iloc[:,15]=="More Equal Society"]) / (len(Republicans[Republicans.iloc[:,15]=="More Equal Society"])+len(Republicans[Republicans.iloc[:,15]=="More Unequal Society"]))
AgeLt30MEqual = len(AgeLt30[AgeLt30.iloc[:,15]=="More Equal Society"]) / (len(AgeLt30[AgeLt30.iloc[:,15]=="More Equal Society"])+len(AgeLt30[AgeLt30.iloc[:,15]=="More Unequal Society"]))
Age30t60MEqual = len(Age30t60[Age30t60.iloc[:,15]=="More Equal Society"]) / (len(Age30t60[Age30t60.iloc[:,15]=="More Equal Society"])+len(Age30t60[Age30t60.iloc[:,15]=="More Unequal Society"]))
AgeGt60MEqual = len(AgeGt60[AgeGt60.iloc[:,15]=="More Equal Society"]) / (len(AgeGt60[AgeGt60.iloc[:,15]=="More Equal Society"])+len(AgeGt60[AgeGt60.iloc[:,15]=="More Unequal Society"]))
IncLt25MEqual = len(IncLt25[IncLt25.iloc[:,15]=="More Equal Society"]) / (len(IncLt25[IncLt25.iloc[:,15]=="More Equal Society"])+len(IncLt25[IncLt25.iloc[:,15]=="More Unequal Society"]))
Inc25t50MEqual = len(Inc25t50[Inc25t50.iloc[:,15]=="More Equal Society"]) / (len(Inc25t50[Inc25t50.iloc[:,15]=="More Equal Society"])+len(Inc25t50[Inc25t50.iloc[:,15]=="More Unequal Society"]))
Inc50t75MEqual = len(Inc50t75[Inc50t75.iloc[:,15]=="More Equal Society"]) / (len(Inc50t75[Inc50t75.iloc[:,15]=="More Equal Society"])+len(Inc50t75[Inc50t75.iloc[:,15]=="More Unequal Society"]))
Incgt100MEqual = len(Incgt100[Incgt100.iloc[:,15]=="More Equal Society"]) / (len(Incgt100[Incgt100.iloc[:,15]=="More Equal Society"])+len(Incgt100[Incgt100.iloc[:,15]=="More Unequal Society"]))
NotHungryMEqual = len(NotHungry[NotHungry.iloc[:,15]=="More Equal Society"]) / (len(NotHungry[NotHungry.iloc[:,15]=="More Equal Society"])+len(NotHungry[NotHungry.iloc[:,15]=="More Unequal Society"]))
LittleHungryMEqual = len(LittleHungry[LittleHungry.iloc[:,15]=="More Equal Society"]) / (len(LittleHungry[LittleHungry.iloc[:,15]=="More Equal Society"])+len(LittleHungry[LittleHungry.iloc[:,15]=="More Unequal Society"]))
VeryHungryMEqual = len(VeryHungry[VeryHungry.iloc[:,15]=="More Equal Society"]) / (len(VeryHungry[VeryHungry.iloc[:,15]=="More Equal Society"])+len(VeryHungry[VeryHungry.iloc[:,15]=="More Unequal Society"]))
NotHungryMenMEqual = len(NotHungryMen[NotHungryMen.iloc[:,15]=="More Equal Society"]) / (len(NotHungryMen[NotHungryMen.iloc[:,15]=="More Equal Society"])+len(NotHungryMen[NotHungryMen.iloc[:,15]=="More Unequal Society"]))
LittleHungryMenMEqual = len(LittleHungryMen[LittleHungryMen.iloc[:,15]=="More Equal Society"]) / (len(LittleHungryMen[LittleHungryMen.iloc[:,15]=="More Equal Society"])+len(LittleHungryMen[LittleHungryMen.iloc[:,15]=="More Unequal Society"]))
VeryHungryMenMEqual = len(VeryHungryMen[VeryHungryMen.iloc[:,15]=="More Equal Society"]) / (len(VeryHungryMen[VeryHungryMen.iloc[:,15]=="More Equal Society"])+len(VeryHungryMen[VeryHungryMen.iloc[:,15]=="More Unequal Society"]))
NotHungryWomenMEqual = len(NotHungryWomen[NotHungryWomen.iloc[:,15]=="More Equal Society"]) / (len(NotHungryWomen[NotHungryWomen.iloc[:,15]=="More Equal Society"])+len(NotHungryWomen[NotHungryWomen.iloc[:,15]=="More Unequal Society"]))
LittleHungryWomenMEqual = len(LittleHungryWomen[LittleHungryWomen.iloc[:,15]=="More Equal Society"]) / (len(LittleHungryWomen[LittleHungryWomen.iloc[:,15]=="More Equal Society"])+len(LittleHungryWomen[LittleHungryWomen.iloc[:,15]=="More Unequal Society"]))
VeryHungryWomenMEqual = len(VeryHungryWomen[VeryHungryWomen.iloc[:,15]=="More Equal Society"]) / (len(VeryHungryWomen[VeryHungryWomen.iloc[:,15]=="More Equal Society"])+len(VeryHungryWomen[VeryHungryWomen.iloc[:,15]=="More Unequal Society"]))

# Welfare
NotHungryMenWelfare = len(NotHungryMen[NotHungryMen.iloc[:,12] == "Decreased"]) / (len(NotHungryMen[NotHungryMen.iloc[:,12] == "Decreased"]) + len(NotHungryMen[NotHungryMen.iloc[:,12] == "Increased"]) + len(NotHungryMen[NotHungryMen.iloc[:,12] == "Kept the Same"]))
LittleHungryMenWelfare = len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Decreased"]) / (len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Decreased"]) + len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Increased"]) + len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Kept the Same"]))
VeryHungryMenWelfare = len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Decreased"]) / (len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Decreased"]) + len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Increased"]) + len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Kept the Same"]))
NotHungryWomenWelfare = len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Decreased"]) / (len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Decreased"]) + len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Increased"]) + len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Kept the Same"]))
LittleHungryWomenWelfare = len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Decreased"]) / (len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Decreased"]) + len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Increased"]) + len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Kept the Same"]))
VeryHungryWomenWelfare = len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Decreased"]) / (len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Decreased"]) + len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Increased"]) + len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Kept the Same"]))
NotHungryMenWelfareInc = len(NotHungryMen[NotHungryMen.iloc[:,12] == "Increased"]) / (len(NotHungryMen[NotHungryMen.iloc[:,12] == "Decreased"]) + len(NotHungryMen[NotHungryMen.iloc[:,12] == "Increased"]) + len(NotHungryMen[NotHungryMen.iloc[:,12] == "Kept the Same"]))
LittleHungryMenWelfareInc = len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Increased"]) / (len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Decreased"]) + len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Increased"]) + len(LittleHungryMen[LittleHungryMen.iloc[:,12] == "Kept the Same"]))
VeryHungryMenWelfareInc = len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Increased"]) / (len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Decreased"]) + len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Increased"]) + len(VeryHungryMen[VeryHungryMen.iloc[:,12] == "Kept the Same"]))
NotHungryWomenWelfareInc = len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Increased"]) / (len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Decreased"]) + len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Increased"]) + len(NotHungryWomen[NotHungryWomen.iloc[:,12] == "Kept the Same"]))
LittleHungryWomenWelfareInc = len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Increased"]) / (len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Decreased"]) + len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Increased"]) + len(LittleHungryWomen[LittleHungryWomen.iloc[:,12] == "Kept the Same"]))
VeryHungryWomenWelfareInc = len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Increased"]) / (len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Decreased"]) + len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Increased"]) + len(VeryHungryWomen[VeryHungryWomen.iloc[:,12] == "Kept the Same"]))

# Rich to Poor
NotHungryMenRobin = len(NotHungryMen[NotHungryMen.iloc[:,17].str.contains('Yes')]) / (len(NotHungryMen[NotHungryMen.iloc[:,17].str.contains('Yes')]) + len(NotHungryMen[NotHungryMen.iloc[:,17].str.contains('No')]))
LittleHungryMenRobin = len(LittleHungryMen[LittleHungryMen.iloc[:,17].str.contains('Yes')]) / (len(LittleHungryMen[LittleHungryMen.iloc[:,17].str.contains('Yes')]) + len(LittleHungryMen[LittleHungryMen.iloc[:,17].str.contains('No')]))
VeryHungryMenRobin = len(VeryHungryMen[VeryHungryMen.iloc[:,17].str.contains('Yes')]) / (len(VeryHungryMen[VeryHungryMen.iloc[:,17].str.contains('Yes')]) + len(VeryHungryMen[VeryHungryMen.iloc[:,17].str.contains('No')]))
NotHungryWomenRobin = len(NotHungryWomen[NotHungryWomen.iloc[:,17].str.contains('Yes')]) / (len(NotHungryWomen[NotHungryWomen.iloc[:,17].str.contains('Yes')]) + len(NotHungryWomen[NotHungryWomen.iloc[:,17].str.contains('No')]))
LittleHungryWomenRobin = len(LittleHungryWomen[LittleHungryWomen.iloc[:,17].str.contains('Yes')]) / (len(LittleHungryWomen[LittleHungryWomen.iloc[:,17].str.contains('Yes')]) + len(LittleHungryWomen[LittleHungryWomen.iloc[:,17].str.contains('No')]))
VeryHungryWomenRobin = len(VeryHungryWomen[VeryHungryWomen.iloc[:,17].str.contains('Yes')]) / (len(VeryHungryWomen[VeryHungryWomen.iloc[:,17].str.contains('Yes')]) + len(VeryHungryWomen[VeryHungryWomen.iloc[:,17].str.contains('No')]))

# Hunger
IncLt25Full = len(IncLt25[IncLt25.iloc[:,20] == "Not Hungry"]) / (len(IncLt25[IncLt25.iloc[:,20] == "Not Hungry"]) + len(IncLt25[IncLt25.iloc[:,20] == "A Little Hungry"])  + len(IncLt25[IncLt25.iloc[:,20] == "Very Hungry"]))
IncLt25Little = len(IncLt25[IncLt25.iloc[:,20] == "A Little Hungry"]) / (len(IncLt25[IncLt25.iloc[:,20] == "Not Hungry"]) + len(IncLt25[IncLt25.iloc[:,20] == "A Little Hungry"])  + len(IncLt25[IncLt25.iloc[:,20] == "Very Hungry"]))
IncLt25Very = len(IncLt25[IncLt25.iloc[:,20] == "Very Hungry"]) / (len(IncLt25[IncLt25.iloc[:,20] == "Not Hungry"]) + len(IncLt25[IncLt25.iloc[:,20] == "A Little Hungry"])  + len(IncLt25[IncLt25.iloc[:,20] == "Very Hungry"]))
Inc25t50Full = len(Inc25t50[Inc25t50.iloc[:,20] == "Not Hungry"]) / (len(Inc25t50[Inc25t50.iloc[:,20] == "Not Hungry"]) + len(Inc25t50[Inc25t50.iloc[:,20] == "A Little Hungry"])  + len(Inc25t50[Inc25t50.iloc[:,20] == "Very Hungry"]))
Inc25t50Little = len(Inc25t50[Inc25t50.iloc[:,20] == "A Little Hungry"]) / (len(Inc25t50[Inc25t50.iloc[:,20] == "Not Hungry"]) + len(Inc25t50[Inc25t50.iloc[:,20] == "A Little Hungry"])  + len(Inc25t50[Inc25t50.iloc[:,20] == "Very Hungry"]))
Inc25t50Very = len(Inc25t50[Inc25t50.iloc[:,20] == "Very Hungry"]) / (len(Inc25t50[Inc25t50.iloc[:,20] == "Not Hungry"]) + len(Inc25t50[Inc25t50.iloc[:,20] == "A Little Hungry"])  + len(Inc25t50[Inc25t50.iloc[:,20] == "Very Hungry"]))
Inc50t75Full = len(Inc50t75[Inc50t75.iloc[:,20] == "Not Hungry"]) / (len(Inc50t75[Inc50t75.iloc[:,20] == "Not Hungry"]) + len(Inc50t75[Inc50t75.iloc[:,20] == "A Little Hungry"])  + len(Inc50t75[Inc50t75.iloc[:,20] == "Very Hungry"]))
Inc50t75Little = len(Inc50t75[Inc50t75.iloc[:,20] == "A Little Hungry"]) / (len(Inc50t75[Inc50t75.iloc[:,20] == "Not Hungry"]) + len(Inc50t75[Inc50t75.iloc[:,20] == "A Little Hungry"])  + len(Inc50t75[Inc50t75.iloc[:,20] == "Very Hungry"]))
Inc50t75Very = len(Inc50t75[Inc50t75.iloc[:,20] == "Very Hungry"]) / (len(Inc50t75[Inc50t75.iloc[:,20] == "Not Hungry"]) + len(Inc50t75[Inc50t75.iloc[:,20] == "A Little Hungry"])  + len(Inc50t75[Inc50t75.iloc[:,20] == "Very Hungry"]))
Inc75t100Full = len(Inc75t100[Inc75t100.iloc[:,20] == "Not Hungry"]) / (len(Inc75t100[Inc75t100.iloc[:,20] == "Not Hungry"]) + len(Inc75t100[Inc75t100.iloc[:,20] == "A Little Hungry"])  + len(Inc75t100[Inc75t100.iloc[:,20] == "Very Hungry"]))
Inc75t100Little = len(Inc75t100[Inc75t100.iloc[:,20] == "A Little Hungry"]) / (len(Inc75t100[Inc75t100.iloc[:,20] == "Not Hungry"]) + len(Inc75t100[Inc75t100.iloc[:,20] == "A Little Hungry"])  + len(Inc75t100[Inc75t100.iloc[:,20] == "Very Hungry"]))
Inc75t100Very = len(Inc75t100[Inc75t100.iloc[:,20] == "Very Hungry"]) / (len(Inc75t100[Inc75t100.iloc[:,20] == "Not Hungry"]) + len(Inc75t100[Inc75t100.iloc[:,20] == "A Little Hungry"])  + len(Inc75t100[Inc75t100.iloc[:,20] == "Very Hungry"]))
Incgt100Full = len(Incgt100[Incgt100.iloc[:,20] == "Not Hungry"]) / (len(Incgt100[Incgt100.iloc[:,20] == "Not Hungry"]) + len(Incgt100[Incgt100.iloc[:,20] == "A Little Hungry"])  + len(Incgt100[Incgt100.iloc[:,20] == "Very Hungry"]))
Incgt100Little = len(Incgt100[Incgt100.iloc[:,20] == "A Little Hungry"]) / (len(Incgt100[Incgt100.iloc[:,20] == "Not Hungry"]) + len(Incgt100[Incgt100.iloc[:,20] == "A Little Hungry"])  + len(Incgt100[Incgt100.iloc[:,20] == "Very Hungry"]))
Incgt100Very = len(Incgt100[Incgt100.iloc[:,20] == "Very Hungry"]) / (len(Incgt100[Incgt100.iloc[:,20] == "Not Hungry"]) + len(Incgt100[Incgt100.iloc[:,20] == "A Little Hungry"])  + len(Incgt100[Incgt100.iloc[:,20] == "Very Hungry"]))

#Make Plots
pp = PdfPages('CAPlots.pdf')

plt.figure(1)
plt.bar(np.arange(2),(MenYes,WomenYes))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(2),('Men','Women'))
plt.ylabel('Percentage Yes')
pp.savefig()

plt.figure(2)
plt.bar(np.arange(2),(DemocratsYes,RepublicansYes))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(2),('Democrats','Republicans'))
plt.ylabel('Percentage Yes')
pp.savefig()

plt.figure(3)
plt.bar(np.arange(3),(AgeLt30Yes,Age30t60Yes,AgeGt60Yes))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(3),('Age <30','Age 30-60', 'Age >60'))
plt.ylabel('Percentage Yes')
pp.savefig()

plt.figure(4)
plt.bar(np.arange(5),(IncLt25Yes,Inc25t50Yes,Inc50t75Yes,Inc75t100Yes,Incgt100Yes))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
plt.ylabel('Percentage Yes')
plt.tight_layout()
pp.savefig()

plt.figure(5)
plt.bar(np.arange(5),(IncLt25MenPct,Inc25t50MenPct,Inc50t75MenPct,Inc75t100MenPct,Incgt100MenPct))
plt.title('Gender')
plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
plt.ylabel('Percentage Men')
plt.tight_layout()
pp.savefig()

plt.figure(6)
plt.bar(np.arange(3),(NotHungryYes,LittleHungryYes,VeryHungryYes))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Yes')
pp.savefig()

plt.figure(7)
plt.bar(np.arange(3),(NotHungryMenPct,LittleHungryMenPct,VeryHungryMenPct))
plt.title('Gender')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Men')
pp.savefig()

plt.figure(8)
plt.bar(np.arange(2),(DemocratsMEqual,RepublicansMEqual))
plt.title('Would you perfer a more or less equal society?')
plt.xticks(np.arange(2),('Republicans', 'Democrats'))
plt.ylabel('Percentage More Equal')
pp.savefig()

plt.figure(9)
plt.bar(np.arange(2),(MenMEqual,WomenMEqual))
plt.title('Would you perfer a more or less equal society?')
plt.xticks(np.arange(2),('Men', 'Women'))
plt.ylabel('Percentage More Equal')
pp.savefig()

plt.figure(10)
width = .35
fig10, ax10 = plt.subplots()
rects1 = ax10.bar(np.arange(5), (IncLt25MenYesPct,Inc25t50MenYesPct,Inc50t75MenYesPct,Inc75t100MenYesPct,Incgt100MenYesPct), width, color='r')
rects2 = ax10.bar(np.arange(5)+width, (IncLt25WomenYesPct,Inc25t50WomenYesPct,Inc50t75WomenYesPct,Inc75t100WomenYesPct,Incgt100WomenYesPct), width, color='b')
ax10.legend((rects1[0], rects2[0]), ('Men', 'Women'))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
plt.ylabel('Percentage Yes')
plt.tight_layout()
pp.savefig()

plt.figure(11)
width = .35
fig11, ax11 = plt.subplots()
rects1 = ax11.bar(np.arange(3),(NotHungryMenYesPct,LittleHungryMenYesPct,VeryHungryMenYesPct), width, color='r')
rects2 = ax11.bar(np.arange(3)+width,(NotHungryWomenYesPct,LittleHungryWomenYesPct,VeryHungryWomenYesPct), width, color='b')
ax11.legend((rects1[0], rects2[0]), ('Men', 'Women'))
plt.title('Could you beat most people in a fist fight?')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Yes')
pp.savefig()

plt.figure(12)
width = .35
fig12, ax12 = plt.subplots()
rects1 = ax12.bar(np.arange(3),(NotHungryMenMEqual,LittleHungryMenMEqual,VeryHungryMenMEqual), width, color='r')
rects2 = ax12.bar(np.arange(3)+width,(NotHungryWomenMEqual,LittleHungryWomenMEqual,VeryHungryWomenMEqual), width, color='b')
ax12.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
plt.title('Would you perfer a more or less equal society?')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage More Equal')
pp.savefig()

plt.figure(13)
width = .2
fig13, ax13 = plt.subplots()
rects1 = ax13.bar(np.arange(5),(IncLt25Full,Inc25t50Full,Inc50t75Full,Inc75t100Full,Incgt100Full), width, color='r')
rects2 = ax13.bar(np.arange(5)+width,(IncLt25Little,Inc25t50Little,Inc50t75Little,Inc75t100Little,Incgt100Little), width, color='g')
rects3 = ax13.bar(np.arange(5)+2*width,(IncLt25Very,Inc25t50Very,Inc50t75Very,Inc75t100Very,Incgt100Very), width, color='b')
ax13.legend((rects1[0], rects2[0], rects3[0]), ('Not Hungry', 'A Little Hungry', 'Very Hungry'), loc=5)
plt.title('Hunger by Income')
plt.xticks(np.arange(5),('< $25k/yr','$25-50 k/yr', '$50-75 k/yr','$75-100 k/yr','$>100 k/yr'), rotation='vertical')
plt.ylabel('Percentage')
plt.tight_layout()
pp.savefig()

plt.figure(14)
width = .35
fig14, ax14 = plt.subplots()
rects1 = ax14.bar(np.arange(3),(NotHungryMenWelfare,LittleHungryMenWelfare,VeryHungryMenWelfare), width, color='r')
rects2 = ax14.bar(np.arange(3)+width,(NotHungryWomenWelfare,LittleHungryWomenWelfare,VeryHungryWomenWelfare), width, color='b')
ax14.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
plt.title('Do you think federal funding for welfare programs in America \n should be increased, decreased, or kept the same? ')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Saying Decrease')
pp.savefig()

plt.figure(15)
width = .35
fig15, ax15 = plt.subplots()
rects1 = ax15.bar(np.arange(3),(NotHungryMenWelfareInc,LittleHungryMenWelfareInc,VeryHungryMenWelfareInc), width, color='r')
rects2 = ax15.bar(np.arange(3)+width,(NotHungryWomenWelfareInc,LittleHungryWomenWelfare,VeryHungryWomenWelfareInc), width, color='b')
ax15.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
plt.title('Do you think federal funding for welfare programs in America \n should be increased, decreased, or kept the same? ')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Saying Increase')
pp.savefig()

plt.figure(16)
width = .35
fig16, ax16 = plt.subplots()
rects1 = ax16.bar(np.arange(3),(NotHungryMenRobin,LittleHungryMenRobin,VeryHungryMenRobin), width, color='r')
rects2 = ax16.bar(np.arange(3)+width,(NotHungryWomenRobin,LittleHungryWomenRobin,VeryHungryWomenRobin), width, color='b')
ax16.legend((rects1[0], rects2[0]), ('Men', 'Women'), loc=3)
plt.title('Do you think our government should take money \n from the rich and give it to the poor? ')
plt.xticks(np.arange(3),('Not Hungry', 'A Little Hungry', 'Very Hungry'))
plt.ylabel('Percentage Saying Yes')
pp.savefig()

pp.close()