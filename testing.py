import exercise

def test_check_amount():
    amount=80
    value=exercise.check(amount)
    assert(value=="enough")

def test_check_type():
    amount=23
    a=exercise.check_type(amount)
    assert(a== None)

def test_calc_avg():
    test_list=[10,20,30]
    result=exercise.cal_avg(test_list)
    assert(result==20)

