class NameError(Exception):
    def __init__(self, text):
        self.txt = text


def check_name(name):
    if any(element.isdigit() for element in name):
        raise NameError('Имя не может содержать в себе цифры')
    else:
        print(name)
