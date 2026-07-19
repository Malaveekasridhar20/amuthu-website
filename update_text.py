import os

base_dir = r'c:\Users\malav\Downloads\Amuthu Dental Website'
intra_path = os.path.join(base_dir, 'intra-oral-scanners.html')
raja_path = os.path.join(base_dir, 'doctor-raja-rajeswari.html')
doctors_path = os.path.join(base_dir, 'doctors.html')

# 1. Update intra-oral-scanners.html
with open(intra_path, 'r', encoding='utf-8') as f:
    intra = f.read()

intra = intra.replace('assets/images/intraoral_scanner_comfort.webp', 'assets/images/intraoral_scanner_comfort_new.jpeg')

with open(intra_path, 'w', encoding='utf-8') as f:
    f.write(intra)

# 2. Update doctor-raja-rajeswari.html
with open(raja_path, 'r', encoding='utf-8') as f:
    raja = f.read()

raja = raja.replace('Microsurgical Rootcanal Specialist, Conservative and Cosmetic Biomimetic Dentist', 'Microsurgical Rootcanal Specialist, Conservative,Cosmetic and Biomimetic Dentist')
raja = raja.replace('Proprietor & Microsurgical Rootcanal', 'Proprietor & Microsurgical Rootcanal specialist')
raja = raja.replace('2. Microsurgical treatment', '2. Microsurgical root canal treatment')

with open(raja_path, 'w', encoding='utf-8') as f:
    f.write(raja)

# 3. Update doctors.html
with open(doctors_path, 'r', encoding='utf-8') as f:
    doctors = f.read()

doctors = doctors.replace('B.Sc., D.H., D.M.', 'D.H., D.M.')

with open(doctors_path, 'w', encoding='utf-8') as f:
    f.write(doctors)

print("Updates applied successfully.")
