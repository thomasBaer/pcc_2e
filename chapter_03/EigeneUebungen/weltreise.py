orte=['rom', 'paris', 'new york', 'ottawa', 'los angeles', 'ankara']

print("1) Liste der Orte (Original): " + str(orte))

print("2) Liste der Orte, aber sortiert: " + str(sorted(orte)))

print("3) Liste der Orte (Original): " + str(orte))

print("4) Liste der Orte, aber umgekehrt sortiert: " +  str(sorted(orte, reverse=True)))

print("5) Liste der Orte (Original): " + str(orte))

orte.reverse()
print("6) Liste der Orte, aber umgekehrt: " + str(orte))

orte.reverse()
print("7) Liste der Orte, aber umgekehrt: " + str(orte))

orte.sort()

print("8) Liste der Orte, aber dauerhaft sortiert: " + str(orte))

orte.sort(reverse=True)

print("9) Liste der Orte, aber dauerhaft umgekehrt sortiert: " + str(orte))

print("A) Liste der Orte (Original): " + str(orte))

print(len(orte))
print(orte[5])




