'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd
import turtle


class TurtleCommand(object):
    def __init__(self, my_turtle):
        self.my_turtle = my_turtle

    def execute(self, arg):
        raise NotImplementedError


class ForwardCommand(TurtleCommand):
    def __init__(self, my_turtle, distance):
        super().__init__(my_turtle)
        self.value = distance

    def execute(self):
        turtle.forward(int(self.value))


class RightCommand(TurtleCommand):
    'Turn turtle right by given number of degrees:  RIGHT 20'

    def __init__(self, turtle, degree):
        super().__init__(turtle)
        self.value = degree

    def execute(self):
        turtle.right(int(self.value))


class LeftCommand(TurtleCommand):
    'Turn turtle right by given number of degrees:  LEFT 20'

    def __init__(self, turtle, degree):
        super().__init__(turtle)
        self.value = degree

    def execute(self):
        turtle.left(int(self.value))


class HomeCommand(TurtleCommand):
    'Return turtle to the home position:  HOME'

    def __init__(self, turtle):
        super().__init__(turtle)

    def execute(self):
        turtle.home()


class CircleCommand(TurtleCommand):
    'Draw circle with given radius an options extent and steps:  CIRCLE 50'

    def __init__(self, turtle, radius):
        super().__init__(turtle)
        self.value = radius

    def execute(self):
        turtle.circle(int(self.value))


class PositionCommand(TurtleCommand):
    'Print the current turtle position:  POSITION'

    def __init__(self, turtle):
        super().__init__(turtle)

    def execute(self):
        print('Current position is %d %d\n' % turtle.position())


class HeadingCommand(TurtleCommand):
    'Print the current turtle heading in degrees:  HEADING'

    def __init__(self, turtle):
        super().__init__(turtle)

    def execute(self):
        print('Current heading is %d\n' % (turtle.heading(),))


class ResetCommand(TurtleCommand):
    'Clear the screen and return turtle to center:  RESET'

    def __init__(self, turtle):
        super().__init__(turtle)

    def execute(self):
        turtle.reset()


class ByeCommand(TurtleCommand):
    'Close the turtle window, and exit:  BYE'
    def __init__(self, turtle):
        super().__init__(turtle)

    def execute(self):
        print('Thank you for using Turtle')
        turtle.bye()


class TurtleCommandInvoker(object):
    def __init__(self):
        self.commands = []
        self.is_recorded = False

    def start_recording(self):
        self.reset_commands()
        self.is_recorded = True

    def stop_recording(self):
        self.is_recorded = False

    def add_command(self, commad):
        self.commands.append(commad)

    def reset_commands(self):
        self.commands = []

    def run_all(self):
        for command in self.commands:
            command.execute()

    def run(self, command):
        if self.is_recorded is True:
            self.add_command(command)
        command.execute()


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    my_turtle = turtle
    client = TurtleCommandInvoker()

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        command = ForwardCommand(self.my_turtle, int(arg))
        self.client.run(command)

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        # turtle.right(int(arg))
        command = RightCommand(self.my_turtle, int(arg))
        self.client.run(command)

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        command = LeftCommand(self.my_turtle, int(arg))
        self.client.run(command)

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        command = HomeCommand(self.my_turtle)
        self.client.run(command)

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        command = CircleCommand(self.my_turtle, int(arg))
        self.client.run(command)

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        command = PositionCommand(self.my_turtle)
        self.client.run(command)

    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        command = HeadingCommand(self.my_turtle)
        self.client.run(command)

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        command = ResetCommand(self.my_turtle)
        self.client.run(command)

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        command = ByeCommand(self.my_turtle)
        self.client.run(command)
        return True

    def do_record(self, arg):
        self.client.start_recording()

    def do_stop(self, arg):
        self.client.stop_recording()

    def do_playback(self, arg):
        self.client.run_all()


if __name__ == '__main__':
    TurtleShell().cmdloop()
 
