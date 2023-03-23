from typing import List, Dict, Optional
import re

def readPatientsFromFile(fileName):
    patients = {}
    patientsData=[]

    try:
        with open(fileName) as f:
            patientsData = f.read().splitlines() 
    except:
        print('The file '+fileName+' could not be found.')
        exit()

    for patientData in patientsData:
        try:
            data = patientData.split(',')

            if(len(data)!=8):
                print('Invalid number of fields ('+str(len(data))+') in line: '+patientData)
                continue
            if(float(data[2])<35 or float(data[2])>42):
                print('Invalid temperature value ('+data[2]+') in line: '+patientData)
            if(int(data[3])<30 or int(data[3])>180):
                print('Invalid heart rate value ('+data[3]+') in line: '+patientData)
            if(int(data[4])<5 or int(data[4])>40):
                print('Invalid respiratory rate value ('+data[4]+') in line: '+patientData)
            if(int(data[5])<70 or int(data[5])>200):
                print('Invalid systolic blood pressure value ('+data[5]+') in line: '+patientData)
            if(int(data[6])<40 or int(data[6])>120):
                print('Invalid diastolic blood pressure value ('+data[6]+') in line: '+patientData)
            if(int(data[7])<70 or int(data[7])>100):
                print('Invalid oxygen saturation value ('+data[7]+') in line: '+patientData)
            
            dataset = data[1:]
            if(patients.get(data[0]) is None):
                patients[data[0]] = [dataset]
            else:
                patients[data[0]].append(dataset)

        except:
            print('An unexpected error occurred while reading the file.')
    return patients


def displayPatientData(patients, patientId=0):
    
    if(patientId==0):
        ids = list(patients.keys())
        for id in ids:
            displayPatientData(patients,id)
    else:
        print('Patient ID:',patientId)
        dataset = patients[patientId]
        for data in dataset:
            print(" Visit Date:", data[0])
            print("  Temperature:", "%.2f" % float(data[1]), "C")
            print("  Heart Rate: "+data[2]+" bpm")
            print("  Respiratory Rate: "+data[3]+" bpm")
            print("  Systolic Blood Pressure: "+data[4]+" mmHg")
            print("  Diastolic Blood Pressure: "+data[5]+" mmHg")
            print("  Oxygen Saturation: "+data[6]+" %")

def displayStats(patients, patientId=0):
    if(isinstance(patientId,int)):
        print("Error: 'patientId' should be an integer.") 
        return
    if(not isinstance(patients,dict) ):
        print("Error: 'patients' should be a dictionary.")
        return
    if(patients.get(patientId) is None ):
        if(patientId ==str(0)):
            pass
        else:
            print("No data found for patient with ID "+str(patientId)+".") 
            return
    if(patientId == str(0)):
        temp=0
        hr = 0
        rr = 0
        sbp = 0
        dbp = 0
        spo2 = 0
        patientIds = list(patients.keys())
        for id in patientIds:
            data = patients[str(id)]
            for vitals in data:
                temp += float(vitals[1])
                hr += int(vitals[2])
                rr += int(vitals[3])
                sbp += int(vitals[4])
                dbp += int(vitals[5])
                spo2 += int(vitals[6])
        temp = temp/len(data)
        hr = hr / len(data)
        rr = rr / len(data)
        sbp = sbp / len(data)
        dbp = dbp / len(data)
        spo2 = spo2 / len(data)
        print('Vital Signs for All Patients:')
        print(" Average temperature:", "%.2f" % (temp), "C")
        print(" Average heart rate:", "%.2f" % (hr), " bpm")
        print(" Average respiratory rate: ", "%.2f" % (rr)," bpm")
        print(" Average systolic blood pressure: ", "%.2f" % (sbp)," mmHg")
        print(" Average diastolic blood pressure: ", "%.2f" % (dbp)," mmHg")
        print(" Average oxygen saturation: ", "%.2f" % (spo2)," %")

    else:
        data = patients[str(patientId)]
        temp=0
        hr = 0
        rr = 0
        sbp = 0
        dbp = 0
        spo2 = 0
        for vitals in data:
            temp += float(vitals[1])
            hr += int(vitals[2])
            rr += int(vitals[3])
            sbp += int(vitals[4])
            dbp += int(vitals[5])
            spo2 += int(vitals[6])
        temp = temp/len(data)
        hr = hr / len(data)
        rr = rr / len(data)
        sbp = sbp / len(data)
        dbp = dbp / len(data)
        spo2 = spo2 / len(data)
        print('Vital Signs for All Patient '+str(patientId)+':')
        print(" Average temperature:", "%.2f" % (temp), "C")
        print(" Average heart rate:", "%.2f" % (hr), " bpm")
        print(" Average respiratory rate: ", "%.2f" % (rr)," bpm")
        print(" Average systolic blood pressure: ", "%.2f" % (sbp)," mmHg")
        print(" Average diastolic blood pressure: ", "%.2f" % (dbp)," mmHg")
        print(" Average oxygen saturation: ", "%.2f" % (spo2)," %")



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    try:
        pattern_str = r'^\d{4}-\d{2}-\d{2}$'
        if(not re.match(pattern_str,date)):
            print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
        month = int(date[5:7])
        day = int(date[8:])
        if(month<0 or month>12 or day<0 or day>31):
            print( "Invalid date. Please enter a valid date.")
        if(float(temp)<35 or float(temp)>42):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        if(int(hr)<30 or int(hr)>180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        if(int(rr)<5 or int(rr)>40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        if(int(sbp)<70 or int(sbp)>200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        if(int(dbp)<40 or int(dbp)>120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        if(int(spo2)<70 or int(spo2)>100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        datas = str(patientId)+','+str(date)+','+str(temp)+','+str(hr)+','+str(rr)+','+str(sbp)+','+str(dbp)+','+str(spo2)
        file_object = open(fileName, 'a')
        file_object.write("\n")
        file_object.write(datas)
        file_object.close()
        print("Visit is saved successfully for Patient #"+str(patientId))
    except:
        print("An unexpected error occurred while adding new data.")
    



def findVisitsByDate(patients, year=None, month=None):
    visits = []
    if(month<=0 or month>31):
        print('No visits found for the specified year/month.')
    ids = list(patients.keys())

    for id in ids:
        for vitals in patients[id]:
            date = vitals[0]
            monthValue = int(date[5:7])
            yearValue = int(date[0:4])
            yearFlag = False
            monthFlag = False
            if(year==0):
                yearFlag = True
            if(month==0):
                monthFlag = True
            
            if(int(yearValue)==year):
                yearFlag = True
            if(int(monthValue)==month):
                monthFlag = True
            if(yearFlag and monthFlag):
                visits.append([id,visits[0],visits[1],float(visits[2]),int(visits[3]),int(visits[4]),int(visits[5]),int(visits[6])])
            
    return visits


def findPatientsWhoNeedFollowUp(patients):
    followup_patients = []
    ids = list(patients.keys())
    for id in ids:
        for vitals in patients[id]:
            if(int(vitals[2])>100 or int(vitals[2])<60):
                if(int(id) not in followup_patients):
                    followup_patients.append(int(id))
            if(int(vitals[4])>140):
                if(int(id)  not in followup_patients):
                    followup_patients.append(int(id))
            if(int(vitals[5])>90):
                if(int(id)  not in followup_patients):
                    followup_patients.append(int(id))
            if(int(vitals[6])<90):
                if(int(id)  not in followup_patients):
                    followup_patients.append(int(id))
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    if(patientId not in list(patients.keys())):
        print('No data found for patient with ID',patientId)
        return
    with open(filename, "r") as f:
        lines = f.readlines()
    with open("yourfile.txt", "w") as f:
        for line in lines:
            data = line.split(',')
            if (int(patientId)==int(data[0])):
                f.write(line)
    print('Data for patient,'str(patientId),'has been deleted.')


def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, str(patientID))
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()