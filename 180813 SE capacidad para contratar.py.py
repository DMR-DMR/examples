# 180813 SE capacidad para contratar.py: Este es un ejemplo básico de un Sistema legal Experto desarrolado en modo IF Statement
# El propósito de este archivo es de servir como guía para la comprensión de sistemas expertos basados en reglas.
# Python 3.6.5
# 18 de Agosto de 2018

__author__      = "Diego Maldonado Rosas"
# diegomaldonadorosas@gmail.com

__copyright__   = "GNU General Public License"
# copyright information available at https://en.wikipedia.org/wiki/GNU_General_Public_License#Version_3



# ---------------------------------------------------------------------
# No piece of this document nor any of the conclusions hereby expressed
# create any attorney-client relationship between you and Diego Maldonado Rosas
#
# This material is intended  for general information purposes only
# and does not constitute legal advice.  For legal issues that arise,
# the reader should consult legal counsel.
# ---------------------------------------------------------------------



#INDICE
#1. Banco de mensajes de bienvenida y preguntas
#2. Banco de respuestas posibles
#3. Motor en base a IF statements


#1. Banco de mensajes de bienvenida y preguntas

Welcome = "\n \n    Bienvenido(a) a este ejemplo básico de un sistema experto legal.\n \n    Le haremos un par de preguntas. \n    En base a sus respuestas y a la legislación\n    chilena vigente, le diremos si usted tiene\n    capacidad legal para contratar. "
dotted_line = "    --------------------------------------------\n"
line_break =" \n "

print (line_break)

print (Welcome)

print (line_break)

esc = input("    Presione ENTER para continuar \n \n")

print (line_break)
print(dotted_line)
print (line_break)

edad = int(input ("    PREGUNTAS:\n \n    EDAD:\n    ¿qué edad tiene usted? (escríba en números):   "))

print (line_break)

sexo = input ("    SEXO:\n    ¿cual es su género? Escriba 1 si usted es mujer, 2 si usted es hombre:   ")

print (line_break)
print(dotted_line)
print (line_break)

print ("    RESPUESTAS:\n\n")

#2. Banco de respuestas posibles
niña = "    Usted es una niña. No tiene capacidad para contratar. "
niño = "    Usted es un niño. No tiene capacidad para contratar."
na = "    Si usted contrata, dicho acto adolecerá de nulidad absoluta."
NR = "    Si usted contrata sin la autorización de su representante legal, dicho acto adolecerá de nulidad relativa."
varon_impuber = "    Usted es un varón impuber. No tiene capacidad para contratar"
mujer_impuber ="    Usted es una mujer impuber. No tiene capacidad para contratar"
representante_NA = "    Usted deberá actuar legalmente a través de su representante legal: \n    padre, madre, adoptante y su tutor o curador.\n"
representante_NR = "    Usted deberá actuar representado o debidamente autorizado por su representante legal: \n    padre, madre, adoptante y su tutor o curador.\n"
mayor_de_edad ="    Usted es mayor de edad y por lo tanto tiene PLENA capacidad para contratar."
menor_de_edad ="    Usted es una persona menor de edad. Usted no puede contratar por si sólo."

#3. Motor en base a IF statements

if (edad < 7 and sexo == "1"):
    print(niña)
    print(na)
    print(representante_NA)
elif (edad < 7 and sexo == "2"):
    print(niño)
    print(na)
    print(representante_NA)

elif (edad < 12 and sexo == "1"):
    print (mujer_impuber)
    print(na)
    print(representante_NA)

elif (edad < 14 and sexo == "2"):
    print (varon_impuber)
    print(na)
    print(representante_NA)

elif (edad < 18 and sexo == "1"):
    print (menor_de_edad)
    print(NR)
    print(representante_NR)

elif (edad < 18 and sexo == "2"):
    print (menor_de_edad)
    print(NR)
    print(representante_NR)

else:
    print(mayor_de_edad)

esc = input("\n    presione ENTER para salir \n \n \n ")
