class LivingBeings:
    # class attributes
    var1 = 'Human'
    var2 = 'Animal'
    var3 = 'Vertebrate'

    # Sample Method
    def fun(self):
        print(self.var1)
        print(self.var2)


# Object instantiation
classObj = LivingBeings()

# accessing class attributes using object
print(classObj.var3)
classObj.fun()
