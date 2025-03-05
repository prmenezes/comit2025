"""Module containing code related to contacting a person"""


class ContactMixin:
    """Class representing an entity that can be reached at an address, email, etc"""

    def __init__(
        self,
        identifier: str,
        email: str | None = None,
        street: str | None = None,
        city: str | None = None,
        postal_code: str | None = None,
        province: str | None = None,
        # The below parameters should be in the end and in this order - positional arguments tuple and keyword arguments
        *args,
        **kwargs
    ):
        """Initializes a new instance of Contact

        Args:
            identifier (str): The identifier for the entity that has a method of contact
            email (str | None, optional): email. Defaults to None.
            street (str | None, optional): street address. Defaults to None.
            city (str | None, optional): _description_. Defaults to None.
            postal_code (str | None, optional): _description_. Defaults to None.
            province (str | None, optional): _description_. Defaults to None.
        """
        self.identifier = identifier
        self.email = email
        self.street  = street
        self.city = city
        self.postal_code = postal_code
        self.province = province

        #Mixin class doe not inherit, but could inherit or be inherited from. 
        super().__init__(*args, **kwargs)