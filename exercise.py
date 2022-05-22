def check_type(amount):
    print("data type of amount is "+str(type(amount)))


def check(amount):
    if amount > 90:
        value="too much"
    elif amount > 40 and amount < 90:
        value="enough"
    else:
        value="too low"
    return value


def ptr():
    for a in range(0,5):
        print("noob")


def cal_avg(m_list):
    avg=sum(m_list)/len(m_list)
    return round(avg,1)


def user_input():
    m_list=[]
    str_input=input()
    str_list=str_input.split(",")
    for a in str_list:
        m_list.append(int(a))
    return m_list


def main():
    print("Please enter a number")
    m_list=user_input()
    print(m_list)
    print("Average amount is ",cal_avg(m_list))
    ptr()
    print(check(80))
    amount=23
    check_type(amount)


if __name__ == '__main__':
    main()
