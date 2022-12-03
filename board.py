from constants import *
from cell import Cell
import pygame

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

    