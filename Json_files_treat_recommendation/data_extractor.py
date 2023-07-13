def extract_data(json_object): 

    frailty=json_object["content"][0]["data"]["events"][0]["data"]["items"][2]["value"]["symbol"]["value"].upper()
    heart_failure=json_object["content"][0]["data"]["events"][0]["data"]["items"][3]["value"]["symbol"]["value"].upper()
    established_cvd=json_object["content"][0]["data"]["events"][0]["data"]["items"][4]["value"]["symbol"]["value"].upper()
    hepatic_steatosis=json_object["content"][0]["data"]["events"][0]["data"]["items"][5]["value"]["symbol"]["value"].upper()
    strokes=json_object["content"][0]["data"]["events"][0]["data"]["items"][6]["value"]["symbol"]["value"].upper()

    symptoms=json_object["content"][1]["data"]["events"][0]["data"]["items"][0]["value"]["symbol"]["value"].upper()

    current_eGFR=float(json_object["content"][2]["data"]["events"][3]["data"]["items"][1]["items"][0]["value"]["value"])
    current_UACR=float(json_object["content"][2]["data"]["events"][4]["data"]["items"][1]["items"][0]["value"]["value"])   
    
    current_BMI=json_object["content"][4]["data"]["events"][0]["data"]["items"][0]["value"]["magnitude"]

    hba1c_records=[]
    for number in range(3):
        if(json_object["content"][2]["data"]["events"][number]["data"]["items"][0]["value"]["value"]!= "Lorem ipsum"):
            hba1c_records.append(float(json_object["content"][2]["data"]["events"][number]["data"]["items"][1]["items"][0]["value"]["value"]))

    medication_dict={}
    for number in range(10):
        if(json_object["content"][3]["data"]["events"][number]["data"]["items"][0]["value"]["value"]!= "Lorem ipsum"):
            medication_dict[json_object["content"][3]["data"]["events"][number]["data"]["items"][0]["value"]["value"]]=json_object["content"][3]["data"]["events"][number]["data"]["items"][1]["value"]["value"]

    CVRFs=[]
    for number in range(6):
        if(json_object["content"][5]["data"]["events"][number]["data"]["items"][0]["value"]["value"]!= "Lorem ipsum"):
            CVRFs.append(json_object["content"][5]["data"]["events"][number]["data"]["items"][0]["value"]["value"])

    return(frailty,heart_failure,established_cvd,hepatic_steatosis,strokes,symptoms,current_UACR,current_eGFR,current_BMI,medication_dict,hba1c_records,CVRFs)
