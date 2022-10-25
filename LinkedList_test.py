from LinkedList import LinkedList

def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty()

def test_is_not_empty():
    ll = LinkedList()
    ll.add(5)
    assert not ll.is_empty()

def test_add_head():
    ll = LinkedList()
    ll.add(5)
    assert ll.get_head() == 5

def test_search_head():
    ll = LinkedList()
    ll.add(5)
    assert ll.search(5)

def test_search_none():
    ll = LinkedList()
    ll.add(5)
    assert not ll.search(7)

def test_search_empty():
    ll = LinkedList()
    assert not ll.search(-1)

def test_delete():
    ll = LinkedList()
    ll.add(5)
    assert ll.delete(5) == 5

def test_delete_empty():
    ll = LinkedList()
    ll.add(5)
    ll.delete(5)
    assert ll.is_empty()

def test_add_many_empty():
    ll = LinkedList()
    ll.add(15)
    ll.add(16)
    ll.add(17)
    assert not ll.is_empty()

def test_add_many_search():
    ll = LinkedList()
    ll.add(15)
    ll.add(16)
    ll.add(17)
    assert ll.search(15)
    assert ll.search(16)
    assert ll.search(17)

def test_add_many_delete_end():
    ll = LinkedList()
    ll.add(15)
    ll.add(16)
    ll.add(17)
    ll.delete(17)
    assert ll.search(15)
    assert ll.search(16)
    assert not ll.search(17)

def test_add_many_delete_front():
    ll = LinkedList()
    ll.add(15)
    ll.add(16)
    ll.add(17)
    ll.delete(15)
    assert ll.search(17)
    assert ll.search(16)
    assert not ll.search(15)

def test_add_many_delete_middle():
    ll = LinkedList()
    ll.add(15)
    ll.add(16)
    ll.add(17)
    ll.delete(16)
    assert ll.search(15)
    assert not ll.search(16)
    assert ll.search(17)

def test_delete_empty1():
    ll = LinkedList()
    assert ll.delete(1) is None

def test_clear_empty():
    ll = LinkedList()
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.clear()
    assert ll.is_empty()

def test_clear_search():
    ll = LinkedList()
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.clear()
    assert not ll.search(7)

def test_add_delete_many():
    ll = LinkedList()
    le = []
    la = []
    for i in range(20,201,10):
        ll.add(i)
        le.append(i)
    for i in range(20,201,10):
        la.append(ll.delete(i))
    assert le == la
    assert ll.is_empty()
