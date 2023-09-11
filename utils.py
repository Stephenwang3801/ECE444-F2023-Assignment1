class Utils:
    def reversed(number):
        if not number.isdigit():
            return "invalid"
        return int(str(number)[::-1])
    def formatter(number):
        if not number.isdigit():
            return "invalid"
        return [bin(number), oct(number)]
