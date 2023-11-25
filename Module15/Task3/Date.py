class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def parse_date(cls, date: str) -> list:
        return list(map(int, date.split('-')))

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        date_nums = cls.parse_date(date)
        if len(date_nums) != 3:
            return False
        day, month, year = date_nums
        return 0 < day <= 31 and 0 < month <= 12 and year > 0

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        if cls.is_date_valid(date):
            day, month, year = cls.parse_date(date)
            return cls(day, month, year)

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'