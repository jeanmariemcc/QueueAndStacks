from StackLL import StackLL

def test_is_empty():
    s = StackLL()
    assert s.is_empty()

def test_enq_empty():
    s = StackLL()
    s.push(5)
    assert not s.is_empty()

def test_enq_peek():
    s = StackLL()
    s.push(5)
    assert s.peek() == 5

def test_pop():
    s = StackLL()
    s.push(5)
    assert s.pop() == 5

def test_pop_empty():
    s = StackLL()
    s.push(5)
    s.pop()
    assert s.is_empty()

def test_enq_many_empty():
    s = StackLL()
    s.push(15)
    s.push(16)
    s.push(17)
    assert not s.is_empty()

def test_enq_many_peek():
    s = StackLL()
    s.push(15)
    s.push(16)
    s.push(17)
    assert s.peek() == 17

def test_enq_many_pop():
    s = StackLL()
    s.push(15)
    s.push(16)
    s.push(17)
    assert s.pop() == 17

def test_pop_empty():
    s = StackLL()
    assert s.pop() is None

def test_clear_empty():
    s = StackLL()
    s.push(5)
    s.clear()
    assert s.is_empty()

def test_enq_pop_many():
    s = StackLL()
    le = []
    la = []
    for i in range(20,201,10):
        s.push(i)
        le.insert(0,i)
    while not s.is_empty():
        la.append(s.pop())
    assert le == la