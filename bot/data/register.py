import json
def registration(ism, familiya, phone, kurs, photo, long, lat):
    with open('applicants.json', 'r') as f:
        applicants = json.load(f)
    new_applicant ={
        'ism' : ism,
        'familiya': familiya,
        'phone': phone,
        'kurs': kurs,
        'photo': photo,
        'long': long,
        'lat': lat
    }
    applicants.append(new_applicant)
    with open('applicants.json','w') as f:
        json.dump(applicants, f)
