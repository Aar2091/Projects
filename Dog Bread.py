class dog:
    
    species = "dog"

    def __init__(self, bread):
        self.bread = bread

bella = dog("German Shepher")
Lucy = dog("Golden Retriever")

print("Bella is a {}".format (bella.species))
print("Lucy is a {}".format (Lucy.species))
print("Bella is a {}".format (bella.bread))
print("Lucy is a {}".format (Lucy.bread))