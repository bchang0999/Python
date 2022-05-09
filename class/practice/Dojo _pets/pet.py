

from tkinter import N


class Pet:
    def __init__( name , type , tricks, health, energy ):
        name =name
        type = type
        tricks = tricks
        health = health
        energy= energy
    
    def sleep(name):
        energy =+ 25
        name = name
        print (f'{name} went to sleep!')
        return (f'energy - {energy}')
    
    def eat(name):
        energy =+ 5
        health =+ 10
        print(f'{name} ate some food!')
        return (f'energy - {energy}')
        return (f'health - {health}')


    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
    
