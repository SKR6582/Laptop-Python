#CosPro2_6_4Q

def solution(cards):
    if cards[0][0] == cards[1][0] :
        if cards[0][0] == cards[2][0]:
            print("case_1")
            return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 3)
        else :
            print("case_2")
            return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 2)
    
    elif cards[1][0] == cards[2][0] :
        if cards[1][0] == cards[0][0]:
            print("case_3")
            return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 3)
        else :
            print("case_4")
            return ((int(cards[0][1]) + int(cards[1][3]) + int(cards[2][1])) * 2 )
        
    elif cards[2][0] == cards[0][0] :
        if cards[2][0] == cards[1][0]:
            print("case_5")
            return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 3)
        else :
            print("case_6")
            return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 2)
    else :
        print("case_7")
        return ((int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1])) * 1)


card1 = [["blue","2"],["red","5"],["black","3"]]
ret1 = solution(card1)
print("return value is {}.".format(ret1))

card2 = [["blue","2"],["blue","5"],["black","3"]]
ret2 = solution(card2)
print("return value is {}.".format(ret2))
