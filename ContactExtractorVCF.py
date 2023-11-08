import vobject


def extract_phone_numbers(vcf_file):
    phone_numbers = []
    with open(vcf_file, 'r', encoding='utf-8') as vcf:
        vcf_data = vcf.read()
        vcf_parsed = vobject.readOne(vcf_data)

        if vcf_parsed is not None:
            for tel in vcf_parsed.tel_list:
                phone_numbers.append(tel.value)

    return phone_numbers


vcf_file = 'path/to/your/contacts.vcf'  # Replace with the path to your VCF file
phone_numbers = extract_phone_numbers(vcf_file)

if phone_numbers:
    for i, number in enumerate(phone_numbers, start=1):
        print(f"{i}. {number}")
else:
    print("No phone numbers found in the VCF file.")
