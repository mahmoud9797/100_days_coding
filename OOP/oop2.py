class Square:
    def __init__(self, size=0, position=(0, 0)):
       self.__size = size
       self.__position = position

    @property
    def size(self):
        """ to get the value of size"""
        return self.__size
    @size.setter
    def size(self, value):
        """ to set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        """to get postion value"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """to set valie of position"""
        if (not isinstance(value, tuple) or 
            len(value) != 2 or
            not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
            ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def area(self):
        """calculate the area of square"""
        return self.__size ** 2

    def my_print(self):
        """ to print square with x and y coordinate"""
        if self.__size == 0:
            print("")
        else:
            lines = ["" * self.__position[1]]
            row = [" " * self.__position[0] + "#" * self.__size for i in range(self.__size)]
            print("\n".join(lines + row))
    