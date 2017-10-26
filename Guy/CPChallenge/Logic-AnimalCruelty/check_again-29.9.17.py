'''
נראה לי שמצאתי פיתרון
כל פעם שיש לחלק מספר כלשהו יוצא לנו מספר עשרוני שאיי אפשר לעשות עליו קסור
מה שכן אפשר לעשות זה להפוך אותו למספר שלם, הבעיה עם זה שאנחנו מפסידים חלק מהערכים של המספר האמיתי אחרי ה-"." והחוסר שלהם ישפיע על התוצאה הססופית
על כן יש דרך לעקוף את זה זה להכפיל את המספר העשרוני במספר מבוסס עשיריות ואז להעביר את הנקודה קדימה
לדוגמא
1/2 = 1.5
1.5 * 10 = 15

עם ה"15" אפשר לעשות עליו קסור
ולכן יתכן שבפונקציה עשו את הדבר הזה כדי לא לאבד ערכים

אבל הבעיה היא שאנחנו לא נדע כמה מספרים באים אחרי הנקודה
ולכן צריך לעשות פונקציה שהופכת את המספר למחרוזת ועושה לופ על האורך של המספר שלאחר הנקודה וכל פעם מכפילה ב10
מה שאומר שלאחר הפונקציה הזאת נקבל מספר שלם שאפשר לעשות עליו קסור
שים לב: שצריך לקבל מהפונקציה גם את הערך של כמה מספרים היו אחרי הנקודה כדי שלאחר הקסור נוכל להחזיר את המספר לעשרוני
זה נראה לי יביא נקודה חשובה לפיתרון

נ.ב.
ראיתי אם עושים את הפונקציה כרגיל מפסידים מספרים
הפסד המספרים יושב בין 0 לבין 32
כלומר בפונקציה הרגילה חישוב מספר כל שהוא מ 0 עד 31 כולל תמיד יביא את אותה תוצאה
וזה לא טוב כי אז צריך לנחש את התוצאה
ויותר גרוע יתכן שבמספרים גבוהים יותר הפער הזה רק עולה
ולכן נראה לי נכון לעשות מה שציינתי למעלה




def func(x):
        x = x / 2
        x = xor(x, 951335252)

        if (x & 255) > 83:
            x = x + 256
        x = x / 39

        do 3 times:
            x = x * 33
            x = x - 1
            x = x / 4
            x = xor(x, 89)

        return x
//end of func(x)

func()



def func(x):

    x = x/2
    x = x ^ 951335252
    if (x and 255) > 83:
        x = x + 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4
        x = x ^ 89
    return x
'''
def check_dechimal(x):
    string = str(x)
    if 0 == int(string[string.find('.')+1:]):
        return(int(x), 1)
    float_num = x
    len_of_num_after_point = len(string[string.find('.')+1:]) # this will bring the len after ".'
    newString = string.replace(".", '')
    division_num_after_func = '1' + ('0' * len_of_num_after_point) # divition num to for futer use (make to Decimal)
    return (int(newString), int(division_num_after_func))

def func(x):

    x = x/2
    if type(x) == float:
        x = check_dechimal(x)[0]
        division = check_dechimal(x)[1]

    x = x ^ 951335252
    x = x / division
    print(x)
    if (x and 255) > 83:
        x = x + 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4

        if type(x) == float:
            x = check_dechimal(x)[0]
            division = check_dechimal(x)[1]

        x = x ^ 89

        x = x / division

    return x




print(func(2))

