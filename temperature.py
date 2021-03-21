tempincelsius = input("Please enter a temperature in Celsius...")

tempinfarhenheit = float(tempincelsius) * 1.8 + 32

roundedF = round(tempinfarhenheit, 2)

print(tempincelsius + " degrees celsius is " + str(roundedF) + " degrees farhenheit.")
