import re


class PlayerView:
    # Function: gets attributes of class and returns a dict of inputs of user.
    @classmethod
    def get_inputs(cls):
        dict_inputs = {}
        list_attributes = ["first_name", "last_name", "date_birth", "id_player"]
        for element in list_attributes:
            while True:
                data = input(f"{element} : ")
                if cls.validate_input(element, data) == True:
                    dict_inputs[element] = data
                    break
        return dict_inputs

    # Validate inputs user
    @classmethod
    def validate_input(cls, element, data):
        if data:
            if element == "id_player":
                match = re.search(r"[A-Z]{2}[0-9]{5}", data)
                if match:
                    return True
                else:
                    print("\nInvalid id")
                    return False
            elif element == "date_birth":
                match = re.search(
                    r"(0[1-9]|[12][0-9]|3[01])(\/|-)(0[1-9]|1[1,2])(\/|-)(19|20)\d{2}",
                    data,
                )
                if match:
                    return True
                else:
                    print("\nInvalid date")
                    return False
            else:
                return True
        else:
            print("\nMissing input")
            return False

    @classmethod
    def get_id(cls):
        id = input("Type the id player = ")
        return id
