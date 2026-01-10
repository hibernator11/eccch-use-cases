#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 10:08:00 2026

@author: gustavo
"""

fichero = "metadata-bne.txt"

import csv

with open('metadata-bne.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["title", "type", "author", "date", "subject", "description", "id"]
    writer.writerow(field)

    title = id = author = date = subject = description = ''
    type = 'map'
    
    with open(fichero) as file:
        for line in file:
            print(line.rstrip())
            if "Identificador corto" in line:
                id = line.split(": ")[1]
                print("id:" + id)
            elif "Título:" in line:
                title = line.split(": ")[1]
                print("title:" + title)
            elif "Autoría" in line:
                author = line.split(": ")[1]
                print("author:" + author)
            elif "Descripción física" in line:
                description = line[line.index(":"):]
                print("description:" + description)
            elif "Materia:" in line:
                subject = line.split(": ")[1]
                print("subject:" + subject)
            elif "Fecha:" in line:
                date = line.split(": ")[1]
                print("date:" + date)
                break

            writer.writerow([author,date,subject,description,id])
            title = id = author = date = subject = description = ''
