import tkinter as tk
from tkinter import ttk
import csv

def read_csv(filename):
    '''Retorna as linhas do arquivo csv passado por parâmetro.'''
    rows = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)
    
    return rows

def prepare_tree_data(rows, icon_male, icon_female):
    '''Retorna um dicionário com os dados agrupados por cidade'''
    grouped_data = {}

    for row in rows:
        if row['Gender'] == 'Male':
            row['Icon'] = icon_male
        else:
            row['Icon'] = icon_female
    
        city = row['City']
        if city not in grouped_data:
            grouped_data[city] = []
        grouped_data[city].append(row)
    
    return grouped_data

def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value

def create_tree_view(root, employees, icons):
    
    frame = ttk.Frame(root)

    treeview = ttk.Treeview(frame, columns=("Salary", "Bonus"))

    treeview.heading('#0', text="Employee")
    treeview.heading('Salary', text='Salary')
    treeview.heading('Bonus', text='Bonus')

    employees_data = prepare_tree_data(employees, icons['female'], icons['male'])

    for city in employees_data.keys():
        #Adicionar cidade
        city_id = treeview.insert('', tk.END, text=city, image=icons['city'])

        #Adicionar os empregados da cidade
        for employee in employees_data[city]:
            treeview.insert(
                city_id,
                tk.END,
                text=employee['Fisrt Name'] + ' ' + employee['Last Name'],
                values=(format_currency(employee['Salary']), format_currency(employee['Bonus'])),
                image=employee['Icon']
            )