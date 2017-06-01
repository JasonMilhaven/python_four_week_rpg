import time
import threading
import sys
import os

import pygame

from Entity import *
from Player import *
from UIComponent import *
from UITextComponent import *
from Input import *
from Tile import *
from utilities import *
from Game import *

"""
    ******************************************************************************

    Class: Program
    
    Description: A single instance (but not Singleton) class representing the program,
    with a window, draw loop, and game loop to handle logic.
    
    Author: Jason Milhaven
    
    History: No longer using "Daemon" thread as draw loop,
    draw loop should be terminated first, not last.
    
    ******************************************************************************
"""

class Program():

    """
        ==============================================================================
        
        Method: init
        
        Description: Constructor for the Program class, creates the window given
        a title, w and h constants, sets window icon.
        
        The game logic and event handling is in event_loop, on the main thread.
        The drawing is handled exclusively in draw_loop, on a seperate thread.
        
        UI is created upon instantiation.
        
        Author: Jason Milhaven
        
        History: Disabled draw thread as a hotfix to prevent load crashing.
        A single thread seems to make walking smooth?
        
        ==============================================================================
    """

    def __init__(self):
        
        # constants
        self.WIN_TITLE = "Pythonica"
        #self.WIN_WIDTH = 1024
        #self.WIN_HEIGHT = 576
        self.WIN_WIDTH = 1280
        self.WIN_HEIGHT = 720
        self.WIN_ICON_FILENAME = "Icon.png"
        self.FILL_COLOR = (0, 0, 0)
        
        # core variables
        self.isRunning = True
        self.uiComponents = []
        self.hoveredUI = None
        self.input = Input()
        self.updateDelay = 1
        self.delayedUpdateAccumulator = 0
        self.lastEventTime = time.time()
        self.lastDrawTime = time.time()
        self.pyClock = pygame.time.Clock()
        
        # if activeGame is None, then use is in menu
        # if activeGame points to a Game, then in game
        self.activeGame = None
        
        # get rid of this line?
        self.activeGame = Game(self.WIN_WIDTH, self.WIN_HEIGHT)
        
        # pygame initialization
        pygame.init()
        self.pySurface = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        pygame.display.set_caption(self.WIN_TITLE)
        pygame.display.set_icon(load_img(self.WIN_ICON_FILENAME))
        
        # make the ui
        u = UITextComponent()
        u.set_size(self.WIN_WIDTH, self.WIN_HEIGHT / 6)
        u.set_pos(self.WIN_WIDTH * 0.5, self.WIN_HEIGHT - u.get_size_y() / 2)
        u.set_visible(True)
        u.name = "UI 1"
        u.text = "test text here test text here test text here "
        u.borderSize = 1
        self.uiComponents.append(u)
        
        u2 = UIComponent(400, 400, 100, 100)
        u2.set_visible(False)
        u2.name = "UI 2"
        self.uiComponents.append(u2)
        
        b = UIComponent(400, 100, 300, 100)
        b.set_visible(False)
        b.name = "Banner"
        b.img = load_img("TestBanner.png")
        self.uiComponents.append(b)
        
        # any sort of testing should be done here
        
        
        
        # begin the main program
        
        self.drawThread = threading.Thread(target=self.draw_loop)
        #self.drawThread.setDaemon(True)
        # threads should be killed manually
        #self.drawThread.start()
        self.event_loop()

    """
        ==============================================================================
        
        Method: close
        
        Description: Called when the user closes the window, sets isRunning to False,
        ending both the game and draw loops.  Kills the drawThread, ends pygame,
        calls sys.exit to cleanup any resources.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def close(self):
        self.isRunning = False
        
        # kill any threads here
        #self.drawThread.join()
        
        pygame.quit()
        sys.exit(0)

    """
        ==============================================================================
        
        Method: __is_in__
        
        Description: If x and y are inside transform, returns true, otherwise returns false.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __is_in__(self, x, y, transform):
        
        ret = False
        
        xCondition = x <= transform.get_pos_x() + transform.get_size_x() * 0.5 and x > transform.get_pos_x() - transform.get_size_x() * 0.5
        yCondition = y <= transform.get_pos_y() + transform.get_size_y() * 0.5 and y > transform.get_pos_y() - transform.get_size_y() * 0.5
        
        ret = xCondition and yCondition
        return ret
        
    """
        ==============================================================================
        
        Method: __colliding_x__
        
        Description: Returns true if t1 and t2 are colliding on the x axis.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """

    def __colliding_x__(self, t1, t2):
    
        ret = False
        
        len = abs(t1.get_size_x() * 0.5 + t2.get_size_x() * 0.5)
        
        if abs(t1.get_pos_x() - t2.get_pos_x()) < len:
            ret = True
        
        return ret

    """
        ==============================================================================
        
        Method: __colliding_y__
        
        Description: Returns true if t1 and t2 are colliding on the y axis.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
        
    def __colliding_y__(self, t1, t2):
        ret = False
        
        len = abs(t1.get_size_y() * 0.5 + t2.get_size_y() * 0.5)
        
        if abs(t1.get_pos_y() - t2.get_pos_y()) < len:
            ret = True
        
        return ret
        
    """
        ==============================================================================
        
        Method: event_loop
        
        Description: May be refered to as the "Game Loop" in comments as well as "Event Loop".
        
        Called on the main thread, runs while the program isRunning.
        Handles each event: user input, mouse click on ui components, and
        user closing the window.  Also handles any game-related logic and calls entity update
        functions.  Handles collision for entities and tiles.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def event_loop(self):
        while self.isRunning:
            self.draw_loop()
            mX, mY = pygame.mouse.get_pos()
            isClick = False
            
            frameDelta = time.time() - self.lastEventTime
            self.lastEventTime = time.time()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    isClick = True
                    clickedUI = None
                    
                    # REVERSE the ui click detection, very important
                    for ui in reversed(self.uiComponents):
                        if ui.get_visible():
                            if self.__is_in__(mX, mY, ui):
                                clickedUI = ui
                                ui.on_clicked()
                                break
            
            for ui in self.uiComponents:
                if ui.get_visible():
                    if self.hoveredUI:
                        if not self.__is_in__(mX, mY, self.hoveredUI):
                            self.hoveredUI.on_hover_end()
                            self.hoveredUI = None
                        break
                    else:
                        if self.__is_in__(mX, mY, ui):
                            self.hoveredUI = ui
                            ui.on_hover_begin()
                            
                elif event.type == pygame.KEYDOWN:
                
                    rawKey = event.key
                    #prettyKey = event.unicode
                    
                    # wasd down
                    if rawKey == pygame.K_w:
                        self.input.set_pos_y(-1)
                    elif rawKey == pygame.K_a:
                        self.input.set_pos_x(-1)
                    elif rawKey == pygame.K_s:
                        self.input.set_pos_y(1)
                    elif rawKey == pygame.K_d:
                        self.input.set_pos_x(1)
                    
                    # arrows down
                    if rawKey == pygame.K_UP:
                        self.input.set_pos_y(-1)
                    elif rawKey == pygame.K_LEFT:
                        self.input.set_pos_x(-1)
                    elif rawKey == pygame.K_DOWN:
                        self.input.set_pos_y(1)
                    elif rawKey == pygame.K_RIGHT:
                        self.input.set_pos_x(1)
                    
                elif event.type == pygame.KEYUP:
                
                    rawKey = event.key
                    
                    # wasd up
                    if rawKey == pygame.K_w:
                        self.input.set_pos_y(-self.input.get_pos_y() + 1)
                    elif rawKey == pygame.K_a:
                        self.input.set_pos_x(-self.input.get_pos_x() + 1)
                    elif rawKey == pygame.K_s:
                        self.input.set_pos_y(-self.input.get_pos_y() - 1)
                    elif rawKey == pygame.K_d:
                        self.input.set_pos_x(-self.input.get_pos_x() - 1)
                        
                    # arrows up
                    if rawKey == pygame.K_UP:
                        self.input.set_pos_y(-self.input.get_pos_y() + 1)
                    elif rawKey == pygame.K_LEFT:
                        self.input.set_pos_x(-self.input.get_pos_x() + 1)
                    elif rawKey == pygame.K_DOWN:
                        self.input.set_pos_y(-self.input.get_pos_y() - 1)
                    elif rawKey == pygame.K_RIGHT:
                        self.input.set_pos_x(-self.input.get_pos_x() - 1)
            
            if self.activeGame:
                self.activeGame.player.set_move(self.input.get_pos_x(), self.input.get_pos_y())
                
                # ensure entities cannot walk into tiles
                for entity in self.activeGame.currentRoom.entities:
                    entity.pre_update(frameDelta)
                    
                    if isClick:
                        if self.__is_in__(mX, mY, entity):
                            entity.on_clicked()
                    
                    for tile in self.activeGame.currentRoom.tiles:
                        if tile.isBlocking:
                        
                            a = tile.get_pos_x() - entity.get_pos_x()
                            b = tile.get_pos_y() - entity.get_pos_y()
                            
                            xDir = clamp01(a)
                            yDir = clamp01(b)
                            
                            c = abs(a)
                            d = abs(b)
                        
                            if self.__colliding_x__(entity, tile) and self.__colliding_y__(entity, tile):
                                if entity.get_move_x() == xDir and (c > d):
                                    entity.set_move_x(0)
                                if entity.get_move_y() == yDir and (d > c):
                                    entity.set_move_y(0)
                
                    self.delayedUpdateAccumulator += frameDelta
                    if self.delayedUpdateAccumulator >= self.updateDelay:
                        entity.delayed_update(self.delayedUpdateAccumulator)
                        self.delayedUpdateAccumulator = 0

                    entity.update(frameDelta)
                    
    """
        ==============================================================================
        
        Method: __draw_ui__
        
        Description: Draws a UIComponent instance using pygame rectangles.
        Draws the border as rectangles.
        
        Author: Jason Milhaven
        
        History:
        
        ==============================================================================
    """
    
    def __draw_ui__(self, ui):
        pygame.draw.rect(self.pySurface, ui.color, (
            ui.get_pos_x() - (ui.get_size_x() * 0.5),
            ui.get_pos_y() - (ui.get_size_y() * 0.5),
            ui.get_size_x(),
            ui.get_size_y()
        ))
        pygame.draw.rect(self.pySurface, ui.borderColor, (
            ui.get_pos_x() - (ui.get_size_x() * 0.5),
            ui.get_pos_y() - (ui.get_size_y() * 0.5),
            ui.get_size_x(),
            ui.borderSize
        ))
        pygame.draw.rect(self.pySurface, ui.borderColor, (
            ui.get_pos_x() - (ui.get_size_x() * 0.5),
            ui.get_pos_y() - (ui.get_size_y() * 0.5) + ui.get_size_y() - ui.borderSize,
            ui.get_size_x(),
            ui.borderSize
        ))
        pygame.draw.rect(self.pySurface, ui.borderColor, (
            ui.get_pos_x() - (ui.get_size_x() * 0.5),
            ui.get_pos_y() - (ui.get_size_y() * 0.5),
            ui.borderSize,
            ui.get_size_y()
        ))
        pygame.draw.rect(self.pySurface, ui.borderColor, (
            ui.get_pos_x() - (ui.get_size_x() * 0.5) + ui.get_size_x() - ui.borderSize,
            ui.get_pos_y() - (ui.get_size_y() * 0.5),
            ui.borderSize,
            ui.get_size_y()
        ))
    
    """
        ==============================================================================
        
        Method: draw_loop
        
        Description: Got rid of second thread.  draw_loop is now called at the end
        of the event loop.
        
        Author: Jason Milhaven
        
        History: Called on the seperate thread, runs while the program isRunning.
        Draws any visible UIComponent instances.  Draws tiles and entities,
        calls animate on entities.
        
        ==============================================================================
    """
    
    def draw_loop(self):
        #while self.isRunning:
        
        # not a very elegant fix, but there's no time left to make this prettier
        if self.isRunning:
            frameDelta = time.time() - self.lastDrawTime
            self.lastDrawTime = time.time()
            
            self.pySurface.fill(self.FILL_COLOR)
            
            if self.activeGame:
                for tile in self.activeGame.currentRoom.tiles:
                    tile.draw(self.pySurface)
                for entity in self.activeGame.currentRoom.entities:
                    entity.draw(self.pySurface)
                    entity.animate()
                
            for ui in self.uiComponents:
                if ui.get_visible():
                    self.__draw_ui__(ui)
                    ui.draw(self.pySurface);

                
            #self.pyClock.tick(60)
            pygame.display.update()
        
