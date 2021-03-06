import constants
from action import Action
from point import Point
import random

last_key = ''

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        
        self._keyboard_service = keyboard_service
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")
        head = snake.get_head()
        points = food.get_points()
        global last_key
        # snake.grow_tail(points)
        # snake2.grow_tail(points)
        number = 1
        
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            if last_key != 'a':
                grow = random.randint(0,3)
                if grow == 2:
                    snake.grow_tail(points)
                    last_key = 'a'
            
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)

            if last_key != 'd':
                grow = random.randint(0,3)
                if grow == 2:
                    snake.grow_tail(points)
                    last_key = 'd'
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)

            if last_key != 'w':
                grow = random.randint(0,4)
                if grow == 2:
                    snake.grow_tail(points)
                    last_key = 'w'
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

            if last_key != 's':
                grow = random.randint(0,4)
                if grow == 2:
                    snake.grow_tail(points)
                    last_key = 's'

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)

            if last_key != 'j':
                grow = random.randint(0,3)
                if grow == 2:
                    snake2.grow_tail2(points)
                    last_key = 'j'
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            if last_key != 'l':
                grow = random.randint(0,3)
                if grow == 2:
                    snake2.grow_tail2(points)
                    last_key = 'l'
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)

            if last_key != 'i':
                grow = random.randint(0,4)
                if grow == 2:
                    snake2.grow_tail2(points)
                    last_key = 'i'
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

            if last_key != 'k':
                grow = random.randint(0,4)
                if grow == 2:
                    snake2.grow_tail2(points)
                    last_key = 'k'
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        snake2 = cast.get_second_actor("snakes")
        snake2.turn_head(self._direction2)
