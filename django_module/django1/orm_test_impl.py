from unicodedata import lookup


class ORM:


    def __init__(self):
        self.table_name = "post"

    def all(self):

        qs = f"SELECT * FROM {self.table_name};"

        # Отправили запрос в базу psycopg.execute(qs)

        return qs

    def filter(self, **kwargs):
        qs = f"SELECT * FROM {self.table_name}"

        for key, value in kwargs.items():
            if "WHERE" not in qs:
                qs += f"\nWHERE "
            if not qs.strip(' \n').endswith("WHERE"):
                qs += " AND "

            parts = key.split("__")

            op = "="
            if len(parts) > 1:
                lookup = parts[1]
                if lookup == "contains":
                    op = "LIKE"
                    value = f"'%{value}%'"
                elif lookup == "in":
                    op = "IN"
                    value = f"({', '.join([str(e) for e in value])})"

            qs += f"{parts[0]} {op} {value}"

        qs += ";"
        # Отправили запрос в базу psycopg.execute(qs)
        return qs


class Post:
    # other columns
    # table_name = None

    # def __init__(self):
    #     Post.table_name = self.__class__.__name__

    # objects = ORM(model_name=table_name)
    objects = ORM()




# qs = Post.objects.all()
qs = Post.objects.filter(id__in=['2', '4', '5'], content__contains="xxx")

print(qs)


