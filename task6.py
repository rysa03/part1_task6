def bigger_guy(f_guy, s_guy):
    if f_guy>s_guy:
        return f_guy
    else:
        return s_guy

def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20
    assert bigger_guy(10, 10) == 10
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
print("YOUR CODE IS CORRECT!")
test_bigger_guy()