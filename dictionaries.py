""" doc string
        This module is used as an example on how to rank pets

        This is 100% true
    """

# Inline comments give context - like how much love the pet has? or how much I love the pet?
#The amount Joel loves his pets
pets_love = {
    "pet1": {
        "cuteness": 10,
        "smarts": 5
        
    }

}

print("Pet1's smartness is", pets_love["pet1"]["smarts"])

pets_love["pet2"] = 11
pets_love["pet3"] = 8

pets_love["pet3"] = 2

print(pets_love)
