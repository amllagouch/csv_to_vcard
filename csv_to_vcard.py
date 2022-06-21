#!/usr/bin/python3.9
import csv

with open("students_book.csv", encoding='utf-8-sig') as csv_file:
    my_contacts = csv.reader(csv_file, delimiter=';')
    with open("students_book.vcf", "a") as my_file:
        for row in my_contacts:
            last_name, first_name, number = row
            my_file.write("BEGIN:VCARD\n")
            my_file.write("VERSION:2.1\n")
            my_file.write(f"N:{last_name};{first_name};;;\n")
            my_file.write(f"FN:{first_name} {last_name}\n")
            my_file.write(f"TEL;CELL:{number}\n")
            my_file.write("END:VCARD\n")

