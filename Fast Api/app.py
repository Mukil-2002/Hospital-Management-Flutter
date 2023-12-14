from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import uvicorn
from flask import Flask, jsonify
import json
class DataType(BaseModel):
    Symptoms1: str
    Symptoms2: str
    Symptoms3: str
    Symptoms4: str
    Symptoms5: str

app = FastAPI()
l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
'Migraine','Cervical spondylosis',
'Paralysis','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']


"""
Sample JSON Input:- 
{
    "NPPM": 1,
    "LoanStatus": "no loans taken/all loans paid back duly",
    "Objective": "New Car Purchase",
    "Amount": 50000,
    "Guarantee": "co-applicant",
    "Experience": "between 1 and 4 years",
    "M_Status": "male and divorced/seperated",
    "ExistingLoan": 0,
    "Age": 35,
    "CA_Balance": "no current account",
    "SA_Balance": "greater than 1000",
    "PI_Balance": 15000,
    "WorkAB": "Yes",
    "PhNum": 0,
    "Tenure": 3,
    "prop": "Real Estate",
    "JobTyp": "skilled employee / official",
    "HouseT": "own",
    "NOE": 2
}
"""

medicines_list = {'Fungal infection': ['clotrimazole', 'econazole', 'miconazole'],
'Allergy': ['Cetirizine', 'Desloratadine', 'Fexofenadine'],
'GERD': ['esomeprazole', 'lansoprazole', 'omeprazole'],
'Chronic cholestasis': ['Ursodeoxycholic acid', 'Cholestyramine', 'Rifampicin'],
'Drug Reaction': ['antihistamine', 'loratadine', 'Bronchodilators'],
'Peptic ulcer diseae': ['Omeprazole', 'pantoprazole', 'lansoprazole'],
'AIDS': ['Abacavir', 'Didanosine', 'Emtricitabine'],
'Diabetes': ['Metformin', 'glimepiride', 'gliclazide'],
'Gastroenteritis': ['Imodium', 'Pepto-Bismol', 'Kaopectate'],
'Bronchial Asthma': ['ProAir HFA', 'Ventolin HFA', 'Xopenex'],
'Hypertension': ['lisinopril (Prinivil, Zestril)', 'benazepril (Lotensin)', 'captopril'],
'Migraine': ['Imitrex', 'Tosymra', 'rizatriptan'],
'Cervical spondylosis': ['Advil', 'Motrin IB', 'Aleve'],
'Paralysis': ['Succinylcholine', 'Rocuronium', 'Vecuronium'],
'Jaundice': ['cholestyramine', 'colestipol'],
'Malaria': ['Atovaquone', 'Proguanil', 'Chloroquine', 'Doxycycline', 'Mefloquine'],
'Chicken pox': 'Acyclovir',
'Dengue': 'DENVAXIA',
'Typhoid': ['Fluoroquinolones', 'Cephalosporins'],
'hepatitis A': ['Acetaminophen', 'paracetamol'],
'Hepatitis B': ['Entecavir', 'Tenofovir', 'Lamivudine', 'Adefovir'],
'Hepatitis C': ['Elbasvir', 'Grazoprevir'],
'Hepatitis D': ['Pegylated interferon alpha'],
'Hepatitis E': 'Ribavirin',
'Alcoholic hepatitis': ['Corticosteroids', 'Pentoxifylline'],
'Tuberculosis': ['Rifampin', 'Isoniazid', 'Pyrazinamide', 'Ethambutol'],
'Common Cold': ['Acetaminophen', 'Advil', 'Sudafed'],
'Pneumonia': ['Azithromycin', 'Erythromycin', 'Amoxicillin'],
'Dimorphic hemmorhoids(piles)': 'Dabur Pilochek Tablets',
'Heartattack': ['Aspirin', 'Beta blockers', 'ACE inhibitors'],
'Varicoseveins': ['Asclera', 'Sodium tetradecyl sulfate'],
'Hypothyroidism': ['levothyroxine', 'Tirosine'],
'Hyperthyroidism': ['Carbimazole and Propylthiouracil', 'Methimazole'],
'Hypoglycemia': ['Metformin', 'Glipizide', 'Methimazole'],
'Osteoarthristis': ['Ibuprofen','Acetaminophen'],
'Arthritis': [' Naproxen',' Aspirin',' Ibuprofen'],
'(vertigo) Paroymsal  Positional Vertigo': ['Diphenhydramine', 'Ondansetron'],
'Acne': ['Tetracycline'  , ' Macrolide'],
'Urinary tract infection': ['Sulfamethoxazole', 'Ciprofloxacin' ],
'Psoriasis': ['Methotrexate', 'Cyclosporine'],
'Impetigo' : ['mupirocin antibiotic ointment' , 'cephalexin' ]}

tests = {
    'Fungal infection': ['Fungal Culture Test', 'KOH (Potassium Hydroxide) Preparation', 'Blood Tests for Systemic Fungal Infections', 'https://medlineplus.gov/lab-tests/fungal-culture-test/#:~:text=A%20fungal%20culture%20test%20is,see%20if%20treatment%20is%20working'],
    'Allergy': ['Prick and Intradermal Allergy Skin Tests', 'Blood Tests for Allergies', 'Food and Drug Challenge Tests', 'https://www.mayoclinic.org/diseases-conditions/allergies/symptoms-causes/syc-20351497#:~:text=Allergies%20occur%20when%20your%20immune,produces%20substances%20known%20as%20antibodies.'],
    'GERD': ['Upper endoscopy', 'Esophageal pH monitoring', 'Esophageal manometry', 'https://www.mayoclinic.org/diseases-conditions/gerd/diagnosis-treatment/drc-20361959'],
    'Chronic cholestasis': ['Magnetic Resonance Cholangiopancreatography (MRCP)', 'Ultrasound', 'Endoscopic Retrograde Cholangiopancreatography (ERCP)', 'https://my.clevelandclinic.org/health/diseases/24554-cholestasis#:~:text=Cholestasis%20is%20the%20slowing%20or,into%20your%20organs%2C%20causing%20inflammation.'],
    'Drug Reaction': ['Complete Blood Count (CBC)', 'Liver Function Tests (LFTs)', 'Renal Function Tests', 'Skin or Allergy Testing', 'https://acaai.org/allergies/allergic-conditions/drug-allergies/'],
    'Peptic ulcer diseae': ['H. pylori Antibody Test', 'H. pylori Stool Antigen Test', 'Upper Endoscopy (Esophagogastroduodenoscopy or EGD)', 'https://www.mayoclinic.org/diseases-conditions/peptic-ulcer/symptoms-causes/syc-20354223#:~:text=Peptic%20ulcers%20occur%20when%20acid,that%20normally%20protects%20against%20acid.'],
    'AIDS': ['HIV Antibody Tests', 'HIV Antigen Test', 'HIV Nucleic Acid Tests', 'https://www.mayoclinic.org/diseases-conditions/hiv-aids/symptoms-causes/syc-20373524#:~:text=Acquired%20immunodeficiency%20syndrome%20(AIDS)%20is,to%20fight%20infection%20and%20disease.'],
    'Diabetes': ['Fasting Plasma Glucose (FPG) Test', 'Oral Glucose Tolerance Test (OGTT)', 'Glycated Hemoglobin (HbA1c) Test', 'https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes#:~:text=Diabetes%20is%20a%20disease%20that,to%20be%20used%20for%20energy.'],
    'Gastroenteritis': ['Stool Culture', 'Stool Ova and Parasite (O&P) Examination', 'Polymerase Chain Reaction (PCR) Test', 'https://medlineplus.gov/gastroenteritis.html#:~:text=What%20is%20gastroenteritis%3F,dehydration%20or%20cause%20severe%20symptoms.' ], 
    'Bronchial Asthma': ['Pulmonary Function Tests (PFTs)', 'Methacholine Challenge Test', 'Fractional Exhaled Nitric Oxide (FeNO) Test', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2696883/#:~:text=Recurrent%20episodes%20of%20acute%20shortness,often%20arise%20after%20physical%20exercise.'],
    'Hypertension': ['Blood Pressure Measurement', 'Lipid Profile', 'Renal Function Tests', 'https://www.cdc.gov/bloodpressure/about.htm#:~:text=High%20blood%20pressure%2C%20also%20called,blood%20pressure%20(or%20hypertension).'],
    'Migraine': ["There's no specific test to diagnose migraines", 'https://www.mayoclinic.org/diseases-conditions/migraine-headache/symptoms-causes/syc-20360201#:~:text=A%20migraine%20is%20a%20headache,sensitivity%20to%20light%20and%20sound.'],
    'Cervical spondylosis': ['X-ray of the Cervical Spine', 'Magnetic Resonance Imaging (MRI) of the Cervical Spine', 'Electromyography (EMG)', 'https://www.ncbi.nlm.nih.gov/books/NBK551557/#:~:text=Cervical%20spondylosis%20is%20a%20natural,disability%20and%20rising%20healthcare%20costs.'],
    'Paralysis': ['Computed Tomography (CT) Scan or Magnetic Resonance Imaging (MRI) of the brain', 'Complete Blood Count (CBC)', 'Coagulation Tests (Prothrombin Time, Activated Partial Thromboplastin Time)', 'https://www.nhs.uk/conditions/paralysis/#:~:text=Paralysis%20is%20the%20loss%20of,may%20be%20temporary%20or%20permanent.'],
    'Jaundice': ['Liver Function Tests (LFTs)', 'Hepatitis A, B, C, D, and E Tests', 'Abdominal Ultrasound', 'https://www.mountsinai.org/health-library/diseases-conditions/jaundice#:~:text=Jaundice%20is%20a%20condition%20produced,the%20whites%20of%20the%20eyes.'],
    'Malaria': ['Blood Smear', 'Rapid Diagnostic Tests (RDTs)', 'Polymerase Chain Reaction (PCR) Test', 'https://www.who.int/news-room/fact-sheets/detail/malaria#:~:text=Malaria%20is%20a%20life%2Dthreatening,be%20mild%20or%20life%2Dthreatening.'],
    'Chicken pox': ['polymerase chain reaction (PCR) to detect VZV in skin lesions (vesicles, scabs, maculopapular lesions)', 'https://www.cdc.gov/chickenpox/index.html#:~:text=Chickenpox%20is%20a%20highly%20contagious,spreads%20over%20the%20entire%20body.'],
    'Dengue': ['Dengue Virus Antibody Tests', 'Dengue Virus NS1 Antigen Test', 'Complete Blood Count (CBC)', 'https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue#:~:text=Dengue%20(break%2Dbone%20fever),body%20aches%2C%20nausea%20and%20rash.'],
    'Typhoid': ['Blood Culture', 'Stool Culture', 'Widal Test', 'https://www.who.int/news-room/fact-sheets/detail/typhoid#:~:text=Typhoid%20fever%20is%20a%20life,and%20spread%20into%20the%20bloodstream.'],
    'hepatitis A': ['Hepatitis A IgM Antibody Test', 'Liver Function Tests (LFTs)', 'Total Bilirubin Test', 'https://www.who.int/news-room/fact-sheets/detail/hepatitis-a'],
    'Hepatitis B': ['Hepatitis B Surface Antigen (HBsAg) Test', 'Hepatitis B Core Antibody (anti-HBc) Test', 'Hepatitis B DNA Test', 'https://www.mayoclinic.org/diseases-conditions/hepatitis-b/symptoms-causes/syc-20366802'],
    'Hepatitis C': ['Hepatitis C Antibody Test', 'Hepatitis C RNA Test', 'Liver Function Tests (LFTs)', 'https://www.mayoclinic.org/diseases-conditions/hepatitis-c/symptoms-causes/syc-20354278'],
    'Hepatitis D': ['Hepatitis D Antibody Test', 'Hepatitis D RNA Test', 'Liver Function Tests (LFTs)', 'https://www.cdc.gov/hepatitis/hdv/index.htm#:~:text=Hepatitis%20D%20only%20occurs%20in,long%2Dterm%2C%20chronic%20infection.'],
    'Hepatitis E': ['Hepatitis E Antibody Test', 'Hepatitis E RNA Test', 'Liver Function Tests (LFTs)', 'https://www.who.int/news-room/fact-sheets/detail/hepatitis-e#:~:text=Hepatitis%20E%20is%20an%20inflammation,symptomatic%20cases%20of%20hepatitis%20E.'],
    'Alcoholic hepatitis': ['Liver Function Tests (LFTs)', 'Complete Blood Count (CBC)', 'Abdominal Ultrasound', 'https://www.ncbi.nlm.nih.gov/books/NBK470217/#:~:text=Alcoholic%20hepatitis%20is%20a%20severe,features%20of%20systemic%20inflammatory%20response.'],
    'Tuberculosis': ['Tuberculin Skin Test (TST) or Interferon-Gamma Release Assay (IGRA)', 'Sputum Smear Microscopy', 'Chest X-ray', 'https://www.who.int/news-room/fact-sheets/detail/tuberculosis#:~:text=Tuberculosis%20(TB)%20is%20an%20infectious,been%20infected%20with%20TB%20bacteria.'],
    'Common Cold': ['Nasal Swab or Nasopharyngeal Swab', 'https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605#:~:text=The%20common%20cold%20is%20a,have%20even%20more%20frequent%20colds.'],
    'Pneumonia': ['Chest X-ray', 'Complete Blood Count (CBC)', 'Sputum Culture and Gram Stain', 'https://www.mayoclinic.org/diseases-conditions/pneumonia/symptoms-causes/syc-20354204'],
    'Dimorphic hemmorhoids(piles)': ['Digital Rectal Examination (DRE)', 'Proctoscopy or Colonoscopy', 'Stool Occult Blood Test', 'https://my.clevelandclinic.org/health/diseases/15120-hemorrhoids'],
    'Heartattack': ['Troponin Test', 'Electrocardiogram (ECG)', 'Cardiac Enzyme Tests (CK-MB, LDH, and AST)', 'https://www.mayoclinic.org/diseases-conditions/heart-attack/symptoms-causes/syc-20373106'],
    'Varicoseveins': ['Duplex Ultrasound', 'Venogram', 'Magnetic Resonance Venography (MRV)', 'https://www.nhlbi.nih.gov/health/varicose-veins#:~:text=Varicose%20veins%20are%20swollen%2C%20twisted,that%20develops%20in%20the%20rectum.'],
    'Hypothyroidism': ['Thyroid-Stimulating Hormone (TSH) Test', 'Thyroid Hormone (T3 and T4) Tests', 'Antithyroid Antibody Tests', 'https://www.niddk.nih.gov/health-information/endocrine-diseases/hypothyroidism#:~:text=Trials%20for%20Hypothyroidism-,What%20is%20hypothyroidism%3F,the%20front%20of%20your%20neck.'],
    'Hyperthyroidism': ['Thyroid-Stimulating Hormone (TSH) Test', 'Thyroid Hormone (T3 and T4) Tests', 'Radioactive Iodine Uptake (RAIU) Test', 'https://www.mayoclinic.org/diseases-conditions/hyperthyroidism/symptoms-causes/syc-20373659#:~:text=Hyperthyroidism%20happens%20when%20the%20thyroid,and%20rapid%20or%20irregular%20heartbeat.'],
    'Hypoglycemia': ['Fasting Plasma Glucose Test', 'Oral Glucose Tolerance Test (OGTT)', 'Insulin and C-peptide Levels', 'https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/low-blood-glucose-hypoglycemia#:~:text=Low%20blood%20glucose%2C%20also%20called,deciliter%20(mg%2FdL).'],
    'Osteoarthristis': ['X-rays', 'Joint Fluid Analysis', 'Blood Tests', 'https://www.cdc.gov/arthritis/basics/osteoarthritis.htm#:~:text=Osteoarthritis%20(OA)%20is%20the%20most,underlying%20bone%20begins%20to%20change.'],
    'Arthritis': ['Rheumatoid Factor (RF) Test', 'Anti-Cyclic Citrullinated Peptide (anti-CCP) Test', 'Complete Blood Count (CBC)', 'https://www.mayoclinic.org/diseases-conditions/arthritis/symptoms-causes/syc-20350772#:~:text=Arthritis%20is%20the%20swelling%20and,are%20osteoarthritis%20and%20rheumatoid%20arthritis.'],
    '(vertigo) Paroymsal  Positional Vertigo': ['Dix-Hallpike Test', 'Electronystagmography (ENG) or Videonystagmography (VNG)', 'Head Impulse Test (HIT)', 'https://www.mayoclinic.org/diseases-conditions/vertigo/symptoms-causes/syc-20370055#:~:text=Benign%20paroxysmal%20positional%20vertigo%20(BPPV)%20is%20one%20of%20the%20most,changes%20in%20your%20head\'s%20position.'],
    'Acne': ['No specific lab tests are typically required for the diagnosis of acne', 'https://www.mayoclinic.org/diseases-conditions/acne/symptoms-causes/syc-20368047#:~:text=Overview,but%20acne%20can%20be%20persistent.'],
    'Urinary tract infection': ['Urine Culture and Sensitivity', 'Urinalysis', 'C-reactive Protein (CRP) Test', 'https://www.mayoclinic.org/diseases-conditions/urinary-tract-infection/symptoms-causes/syc-20353447#:~:text=A%20urinary%20tract%20infection%20(UTI,a%20UTI%20than%20are%20men.'],
    'Psoriasis': ['Skin Biopsy', 'https://www.mayoclinic.org/diseases-conditions/psoriasis/symptoms-causes/syc-20355840#:~:text=Psoriasis%20is%20a%20skin%20disease,make%20it%20hard%20to%20concentrate.'],
    'Impetigo': ['Bacterial Culture', 'Gram Stain', 'Antimicrobial Susceptibility Testing', 'https://www.cdc.gov/groupastrep/diseases-public/impetigo.html#:~:text=Impetigo%20starts%20as%20a%20red,Around%20the%20nose%20and%20mouth']
}

print(medicines_list["hepatitis A"])
# {'disease': hepatitis b, 
# 'test': [array of tests], 
# 'medicines ' :[array of medicines ] 
# }
def Preprocessing(tr):
    t2 = []
    for idx in range(0,95):
        t2.append(0)
    
    for i in range(0,len(l1)):
        for j in tr:
            if l1[i]==j:
                t2[i]=1
    return t2

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
async def predict(item: DataType):
    print("hi")
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    # df = Preprocessing(df)
    temp_li = []
    temp_li = list(df.iloc[0].values)
    # print(temp_li)
    input_m = Preprocessing(temp_li)
    ans = model.predict([input_m])
    ans = ans[0]

    h='no'
    ans_vl = ""
    for a in range(0,len(disease)):
        if(ans == a):
            # h='yes'
            ans_vl = disease[ans]
            test=tests[ans_vl]
            medicines=medicines_list[ans_vl]
            my_dict={"disease":ans_vl,"test":test,"medicines":medicines}
            # print(ans_vl)
            break
        else:
            ans_vl = "Sorry Couldn't Detect Any Diseace"
    #return  my_dict
    return my_dict
    # return ans_vl


@app.get("/")
async def root():
    return {"message": "This API Only Has Get Method as of now"}



"""
{
    "Symptoms1" : "knee_pain",
    "Symptoms2" : "mild_fever",
    "Symptoms3" : "muscle_pain",
    "Symptoms4" : "internal_itching",
    "Symptoms5" : "malaise"
}
"""
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

