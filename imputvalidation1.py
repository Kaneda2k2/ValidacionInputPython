
import pyinputplus as pyip


response=pyip.inputNum(limit=2, default="N/A")



response=pyip.inputInt(prompt="Entra un numero: ")
#Filtrar edad 18 años.
response=pyip.inputNum("Enter num:", min=18 , max=40)

response=pyip.inputNum("Enter num:",greaterThan=20)
