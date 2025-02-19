if __name__ == "__main__":
    # Write your solution here
    # Базовый класс: Геометрическая фигура
    class Shape:
        """
        Класс, представляющий базовую геометрическую фигуру
        """

        def __init__(self, color: str):
            """
            Инициализация объекта Shape

            :param color: Цвет фигуры (str)
            """
            self._color = color  # Защищенный атрибут, так как цвет может быть изменен только через методы

        def get_color(self) -> str:
            """
            Возвращает цвет фигуры

            :return: Цвет фигуры (str)
            """
            return self._color

        def set_color(self, new_color: str):
            """
            Устанавливает новый цвет фигуры

            :param new_color: Новый цвет (str)
            """
            self._color = new_color

        def area(self) -> float:
            """
            Вычисляет площадь фигуры.
            В базовом классе метод не имеет реализации и возвращает 0

            :return: Площадь фигуры (float)
            """
            return 0.0

        def perimeter(self) -> float:
            """
            Вычисляет периметр фигуры.
            В базовом классе метод не имеет реализации и возвращает 0

            :return: Периметр фигуры (float)
            """
            return 0.0

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта для пользователей

            :return: Строковое представление (str)
            """
            return f"Shape with color {self._color}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта для разработчиков

            :return: Строковое представление (str)
            """
            return f"Shape(color={self._color})"


    # Дочерний класс: Прямоугольник
    class Rectangle(Shape):
        """
        Класс, представляющий прямоугольник, наследующийся от базового класса Shape
        """

        def __init__(self, color: str, width: float, height: float):
            """
            Инициализация объекта Rectangle

            :param color: Цвет прямоугольника (str)
            :param width: Ширина прямоугольника (float)
            :param height: Высота прямоугольника (float)
            """
            super().__init__(color)  # Вызываем конструктор родительского класса
            self._width = width  # Защищенные атрибуты для ширины и высоты
            self._height = height

        def area(self) -> float:
            """
            Переопределяем метод area() для вычисления площади прямоугольника
            Так как формула площади для прямоугольника отличается от базовой реализации

            :return: Площадь прямоугольника (float)
            """
            return self._width * self._height

        def perimeter(self) -> float:
            """
            Переопределяем метод perimeter() для вычисления периметра прямоугольника
            Формула периметра для прямоугольника отличается от базовой реализации

            :return: Периметр прямоугольника (float)
            """
            return 2 * (self._width + self._height)

        def __str__(self) -> str:
            """
            Переопределяем метод __str__() для более подробного представления прямоугольника

            :return: Строковое представление (str)
            """
            return f"Rectangle with color {self.get_color()}, width {self._width} and height {self._height}"

        def __repr__(self) -> str:
            """
            Переопределяем метод __repr__() для более подробного представления прямоугольника

            :return: Строковое представление (str)
            """
            return f"Rectangle(color={self.get_color()}, width={self._width}, height={self._height})"
    pass
