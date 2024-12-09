'''
Created on 2012-12-14

@author: dnikolic
'''

empty_list = []
full_list = ['WINDOWS', 'LINUX', 'MAC']


def access_list_elements():
    mylist = ['a', 'b', 'c', 'd', 'e']

    print('list is {}'.format(mylist))
    print('len(mylist) = {}'.format(len(mylist)))
    print('last element mylist[-1] = {}'.format(mylist[-1]))

def combine_lists():
    l1 = [1, 2, 'three']
    print(f'l1 = {l1}')
    l2 = [4, 'five']
    print(f'l2 = {l2}')
    print(f'l1+l2 = {l1 + l2}')

def add_list_to_list():
    l1 = ['-a', '-b', '-c']
    print(f'original l1 = {l1}')
    lstr = '-d -f -g'
    print(lstr)
    l1.extend(lstr.split())
    print(f'extended l1 = {l1}')

def delete_from_list():
    mylist = [1, 2, 3]
    print(mylist)
    mylist.remove(2)
    print(mylist)

    a = MyClass()
    b = MyClass()
    mylist = [a, b]
    print(mylist)
    mylist.remove(a)
    print(mylist)
    
def sort_list():
    mylist = [1, 20, 7, 15, 3]
    
    print('unsorted list %s' % mylist)
    mylist.sort()
    print('sorted list %s' % mylist)
    
    print('print using iterator...')
    ix = 1
    for item in mylist:
        print(ix, item)
        ix += 1
        
    print('print using index...')
    for ix in range(0, len(mylist)):
        print(ix+1, mylist[ix])
    
    
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
    print(mylist.total)
    mylist.append(item2)
    print(mylist.total)
    mylist.append(item3)
    print(mylist.total)
    mylist.remove(item2)
    print(mylist.total)
    mylist.remove_by_amount(9)
    print(mylist.total)
    mylist.remove_by_amount(7)
    print(mylist.total)


if __name__ == '__main__':
    combine_lists()
    add_list_to_list()
    # delete_from_list()
    # test_my_list_class()
    # sort_list()
    # access_list_elements()
