import pytest
from character import *
from settings_lvl1 import *
from utils import *
import pygame

def test_player():
    Usuario = Player()
    Usuario.go_left()
    Usuario.update()
    assert Usuario.rect.x == -6
    Usuario.jump()
    Usuario.update()
    assert Usuario.change_x == 0
    assert Usuario.change_y == 0

# REFACTORING
# state -> exponer diapos, responder preguntas e implementar el patron en algún lenguaje
def test_enemigos():
    ai_settings = Settings_lvl1()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht, ai_settings.screen_height))
    valor = ai_settings.assasin_speed_factor
    # Make a  Assasin
    character_A = Assasin(ai_settings, screen)
    character_A.moving_right = True
    character_A.rect.right = 100
    character_A.update()
    assert character_A.rect.centerx == 300+valor
    character_A.moving_left = True
    character_A.rect.left = True
    assert character_A.rect.centerx == 300
    character_A.update()


def test_conexionBD():
    assert conexion_DB("127.0.0.1","jtorres","12345","Berserk") != None
    assert conexion_DB("127.0.0.1", "admin", "admin", "Berserk") != None


def test_autentication_user():
    Valores = [("jtorres", "12345"), ("user A", "user A"), ("user B", "user B")]
    # Los primeros 3 seran aceptados ya que pertenecen a la BD

    for val in Valores:
        assert autenticate(val[0],val[1]) == True
        print("Aceptado: "+str(val));