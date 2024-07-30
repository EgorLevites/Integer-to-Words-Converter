from enum import Enum

class Digit(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

class Teens(Enum):
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14
    FIFTEEN = 15
    SIXTEEN = 16
    SEVENTEEN = 17
    EIGHTEEN = 18
    NINETEEN = 19
    TWENTY = 20

class Tens(Enum):
    TWENTY_ = 20
    THIRTY_ = 30
    FORTY_ = 40
    FIFTY_ = 50
    SIXTY_ = 60
    SEVENTY_ = 70
    EIGHTY_ = 80
    NINETY_ = 90

class Hundreds(Enum):
    ONE_HUNDRED_ = 100
    TWO_HUNDRED_ = 200
    THREE_HUNDRED_ = 300
    FOUR_HUNDRED_ = 400
    FIVE_HUNDRED_ = 500
    SIX_HUNDRED_ = 600
    SEVEN_HUNDRED_ = 700
    EIGHT_HUNDRED_ = 800
    NINE_HUNDRED_ = 900


def intToStr(userNum):
    strNum = ''
    if userNum == 1000: return 'ONE_THOUSAND'
    if userNum == 0: return 'ZERO'
    if userNum >= 100:
        strNum += Hundreds(userNum // 100 * 100).name
        userNum %= 100

    if (userNum // 10 > 1):
        strNum += Tens(userNum // 10 * 10).name
        userNum %= 10

    if (9 < userNum < 20):
        strNum += Teens(userNum).name
        return strNum
    
    if (0 < userNum < 10): strNum += Digit(userNum).name

    return strNum

def main():
    userNum = int(input('Enter a number from 1 to 1000: '))
    print(intToStr(userNum))

if __name__ == "__main__":
    main()