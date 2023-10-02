from win32api import GetSystemMetrics

Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)

#configurações Gerais
WIDTH = Width
HEIGHT = Height

PRIMARY_COLOR = [255,255,255]
SECONDARY_COLOR = [51,51,51]
BG_COLOR = [12, 149, 225]

TILE_SIZE = 64

# x -- bloquinho que o personagem vai pisar
# p -- vai ser o personagem
# "  " -- vai ser o espaço que representa o nada
# c -- vai ser uma plaquinha

TILE_SIZE = 64
MAP0 = [
'                            ',
'                            ',
'                            ',
'       XXXX           XX    ',
'   P                        ',
'XXXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX C',
'XXXXXXXX  XXXXXX  XX  XXXXXX']

MAP1 = [
'                            ',
'                            ',
'                            ',
'       XXXX           XX    ',
'                            ',
'                        XX ',
'                            ',
'            XX    XX  XX    ',
'          XXXX    XX  XXX   ',
'P         XXXXXX  XX  XXXX C',
'XXXXXXXX  XXXXXX  XX  XXXXXX']

MAP2 = [
'                            ',
'                            ',
'                            ',
'       XXXX           XX    ',
'                            ',
'                        XX ',
'                            ',
'            XX    XX  XX    ',
'          XXXX    XX  XXX   ',
'P         XXXXXX  XX  XXXX C',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']