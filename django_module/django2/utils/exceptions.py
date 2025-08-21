
class ApplicationError(Exception):
    def __init__(self, message, extra = None, *args):
        super().__init__(message, *args)
        self.message = message
        self.extra = extra or {}



# docker image = докер образ
# docker container = докер контейнер

# class
# object

# docker image "python11":
# -- base: "debian"
# -- python11
# -- выппилены не нужные зависимости
# -- установлены нужные

# docker image "django-app":
# -- base: "python11"
# -- создать папку app
# -- в этот app скопировать наш проект
# -- запустить наш проект




