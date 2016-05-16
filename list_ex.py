'''
Created on 2012-12-14

@author: dnikolic
'''

empty_list = []
full_list = ['WINDOWS', 'LINUX', 'MAC']

class MyClass():
    pass

def combine_lists():
    return [1, 2, 'three'] + [4, 'five']

def delete_from_list():
    mylist = [1, 2, 3]
    print mylist
    mylist.remove(1)
    print mylist

    a = MyClass()
    b = MyClass()
    mylist = [a, b]
    print mylist
    mylist.remove(a)
    print mylist
    
def sort_list():
    mylist = [1, 20, 7, 15, 3]
    
    print 'unsorted list %s' % mylist
    mylist.sort()
    print 'sorted list %s' % mylist
    
    print 'print using iterator...'
    ix = 1
    for item in mylist:
        print ix, item
        ix += 1
        
    print 'print using index...'
    for ix in range(0, len(mylist)):
        print ix+1, mylist[ix]
    
    
class MyItem():
    def __init__(self, amount):
        self.amount = amount
        
class MyListClass(list):
    def __init__(self, *args, **kwargs):
        super(MyListClass, self).__init__(*args, **kwargs)
        self.total = 0
        
    def append(self, item):
        super(MyListClass, self).append(item)
        #list.append(item)
        self.total += item.amount
        
    def remove(self, item):
        super(MyListClass, self).remove(item)
        #list.remove(item)
        self.total -= item.amount
        
    def remove_by_amount(self, amount):
        for item in self:
            if item.amount == amount:
                self.remove(item)
        
        
def test_my_list_class():
    mylist = MyListClass()
    
    item1 = MyItem(3)
    item2 = MyItem(5)
    item3 = MyItem(9)
    
    mylist.append(item1)
    print mylist.total
    mylist.append(item2)
    print mylist.total
    mylist.append(item3)
    print mylist.total
    mylist.remove(item2)
    print mylist.total
    mylist.remove_by_amount(9)
    print mylist.total
    mylist.remove_by_amount(7)
    print mylist.total
    
    
    


if __name__ == '__main__':
    #print combine_lists()
    #delete_from_list()
    #test_my_list_class()
    sort_list()
