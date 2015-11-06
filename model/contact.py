__author__ = 'popov.sn'
from sys import maxsize

class Contact:

        def __index__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None ):
            self.firstame = firstname
            self.lastname = lastname
            self.homephone = homephone
            self.workphone = workphone
            self.secondaryphone = secondaryphone
            self.id = id

        def __repr__(self):
            return  "%s:%s %s" % (self.id, self.firstame, self.lastname)

        def __eq__(self, other):
            return (self.id is None or other.id is None or self.id == other.id)\
                    and self.firstame == other.firstame and self.lastname == other.lastname

        def id_or_max(self):
            if self.id:
                return int(self.id)
            else:
                return maxsize
