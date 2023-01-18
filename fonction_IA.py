# coding: utf-8
import argparse
import random
import client
import const
import plateau
import case
import joueur


def mur_autour_joueur(plan, ma_couleur, les_joueurs):
    """ Cette fonction permet de savoir dans quelle direction le joueurs peut aller en fonction des murs
    Args:
        plan (str): le plan du plateau comme comme indiqué dans le sujet
    Returns:
        list: une liste de direction où le joueur peut aller
    """
    liste_couleur = []
    for i in les_joueurs.keys():
        if i == ["couleur"]:
            liste_couleur.append(i.lower)
    liste_couleur.append("#")
    
    pos = joueur.get_pos(ma_couleur)
    direction_possible = [plan[pos[0]-1][pos[1]], plan[pos[0]+1][pos[1]], plan[pos[0]][pos[1]+1], plan[pos[0]][pos[1]-1]]
    for direction in ["N","S","E","O"]:
        if direction == "N":
            if plan[pos[0]-1][pos[1]] in liste_couleur:
                direction_possible.remove(direction)
        elif direction == "S":
            if plan[pos[0]+1][pos[1]] in liste_couleur:
                direction_possible.remove(direction)
        elif direction == "E":
            if plan[pos[0]][pos[1]+1] in liste_couleur:
                direction_possible.remove(direction)
        elif direction == "O":
            if plan[pos[0]][pos[1]-1] in liste_couleur:
                direction_possible.remove(direction)
    return direction_possible


def case_vide_direction(plan,pos,direction):
    """ Cette fonction permet d'obtenir la liste d'index des positions des cases vides
    Args:
        plan (str): le plan du plateau comme indiqué dans le sujet
        pos (tuple): la position du joueur
        direction (str): la direction où on veut regarder
    Returns:
        list: une liste d'index des cases étant incolore
    """
    distance_max = 5
    case_vides = []
    pos2 = pos
    INC_DIRECTION = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'O': (0, -1), 'X': (0, 0)}
    for index in range(distance_max):
        if plateau.est_sur_plateau(plan,pos2) and not plan["cases"][pos2]["mur"]:
            if plan["cases"][pos2]['couleur'] == ' ':
                case_vides.append(index+1)
        pos2 = (pos2[0] + INC_DIRECTION[direction][0], pos2[1] + INC_DIRECTION[direction][1])
    return case_vides

def case_peinte_autre_joueurs_direction(plan,pos,direction,ma_couleur):
    """ Cette fonction permet d'obtenir la liste d'index des positions des cases peintes par des autres joueur)
    Args:n
        plan (str): le plan du plateau comme indiqué dans le sujet
        pos (tuple): la position du joueur
        direction (str): la direction où on veut regarder
    Returns:
        list: une liste d'index des cases étant peintes par des joueurs autres que nous même
    """
    distance_max = 5
    case_joueurs = []
    pos2 = pos
    INC_DIRECTION = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'O': (0, -1), 'X': (0, 0)}
    for index in range(distance_max):
        if plateau.est_sur_plateau(plan,pos2) and not plan["cases"][pos2]["mur"]:
            if plan["cases"][pos2]['couleur'] != ' ':
                if plan["cases"][pos2]['couleur'] != ma_couleur:
                    case_joueurs.append(index+1)
        pos2 = (pos2[0] + INC_DIRECTION[direction][0], pos2[1] + INC_DIRECTION[direction][1])
    return case_joueurs

def nb_cases_possibles_a_peindre_direction(plan,pos,reserve,direction,ma_couleur):
    """ Cette fonction permet d'obtenir le nombre de cases possibles à peindre dans une direction et un nombre de reserve donné
    Args:
        plan (str): le plan du plateau comme indiqué dans le sujet
        pos (tuple): la position du joueur
        reserve (int): le nombre de reserve du joueur
        direction (str): la direction où on veut regarder
    Returns:
        int: le nombre de cases possibles à peindre dans une direction et un nombre de reserve donné
    """
    nombre_case = 0
    case_vide = case_peinte_autre_joueurs_direction(plan,pos,direction,ma_couleur)
    case_peinte_autre_joueurs = case_peinte_autre_joueurs_direction(plan,pos,direction,ma_couleur)
    for i in range(1,6):
        if i in case_vide:
            if reserve >= 1:
                reserve -= 1
                nombre_case = i
        elif i in case_peinte_autre_joueurs:
            if reserve >= 2:
                reserve -= 2
                nombre_case = i
    return nombre_case

def dico_reserve(plan,les_joueurs):
    pass

def joueurs_plus_proche():
    pass

def direction():
    pass

def get_coords_objets():
    pass

def case_vide_plus_proche():
    pass