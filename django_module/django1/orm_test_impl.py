
class Q:

    def __init__(self, statement="", **kwargs):
        self.table_name = "post"
        self.statement = statement
        for key, value in kwargs.items():
            if not self.statement == "":
                self.statement += " AND "

            parts = key.split("__")

            op = "="
            if len(parts) > 1:
                lookup = parts[1]

                if isinstance(value, F):
                    value = f"{self.table_name}.{value.column_name}"

                if lookup == "contains":
                    op = "LIKE"
                    value = f"'%{value}%'"
                elif lookup == "in":
                    op = "IN"
                    value = f"({', '.join([str(e) for e in value])})"
                elif lookup == "gt":
                    op = ">"
                elif lookup == "gte":
                    op = ">="
                elif lookup == "lt":
                    op = "<"
                elif lookup == "lte":
                    op = "<="

            self.statement += f"{self.table_name}.{parts[0]} {op} {value}"

    def __or__(self, other):
        if not isinstance(other, Q):
            raise TypeError(f"Оператор | невозможна между <class 'Q'> и {type(other)}")

        return Q(statement=f"{self.statement} OR {other.statement}")

    def __and__(self, other):
        if not isinstance(other, Q):
            raise TypeError(f"Оператор & невозможна между <class 'Q'> и {type(other)}")

        return Q(statement=f"{self.statement} AND {other.statement}")


class F:

    def __init__(self, column_name):
        self.column_name = column_name



class ORM:


    def __init__(self):
        self.table_name = "post"

    def all(self):

        qs = f"SELECT * FROM {self.table_name};"

        # Отправили запрос в базу psycopg.execute(qs)

        return qs

    def filter(self, *args, **kwargs):
        qs = f"SELECT * FROM {self.table_name}"

        if args:
            if "WHERE" not in qs:
                qs += f"\nWHERE "

            for q_obj in args:
                qs += q_obj.statement
                qs += " AND "
            qs = qs[:-5]

        for key, value in kwargs.items():
            if "WHERE" not in qs:
                qs += f"\nWHERE "
            if not qs.strip(' \n').endswith("WHERE"):
                qs += " AND "

            parts = key.split("__")

            op = "="
            if len(parts) > 1:
                lookup = parts[1]

                if isinstance(value, F):
                    value = f"{self.table_name}.{value.column_name}"

                if lookup == "contains":
                    op = "LIKE"
                    value = f"'%{value}%'"
                elif lookup == "in":
                    op = "IN"
                    value = f"({', '.join([str(e) for e in value])})"
                elif lookup == "gt":
                    op = ">"
                elif lookup == "gte":
                    op = ">="
                elif lookup == "lt":
                    op = "<"
                elif lookup == "lte":
                    op = "<="

            qs += f"{self.table_name}.{parts[0]} {op} {value}"

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
# qs = Post.objects.filter(id__in=['2', '4', '5'], content__contains="xxx")
# qs = Post.objects.filter(created_at__gt=F("updated_at"))
qs = Post.objects.filter(
    Q(id__in=(2, 3)) | Q(content__contains="ц") &
    Q(title="xxx") | Q(id=2)
)

print(qs)



# q1 = Q(id__in=(2, 3))
# q2 = Q(content__contains="ц")

# print(q1.statement)
# print(q2.statement)
#
# print(q1 | q2)

# print(Q(id__in=(2, 3)) | Q(content__contains="ц"))


