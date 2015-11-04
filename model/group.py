class Group:

    def __init__(self, name=None, header=None, footer=None):

        print("Debug I'm in Group")
        self.name = name
        print ("Debug self.name" , self.name)

        self.header = header

        self.footer = footer
        print ("Debug self.footer" , self.footer)
