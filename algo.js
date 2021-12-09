const str = "Hello World";
const rotateAmnt1 = 0;
const expected1 = "Hello World";
const rotateAmnt2 = 1;
const expected2 = "dHello Worl";
const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";
const rotateAmnt4 = 4;
const expected4 = "orldHello W";
const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
const strA1 = "ABCD";
const strB1 = "CDAB";
const expected12 = true;
const strA2 = "ABCD";
const strB2 = "CDBA";
const expected22 = false;

function rotateStr(str, amnt) {
    slice = "";
    newStr = "";
    if (str.length < amnt) {
        amnt = amnt - str.length;
    }
    for (var i = str.length - 1; i >= str.length - amnt; i--) {
        slice = str[i] + slice;
    }
    newStr += slice + str.slice(0, str.length - amnt);
    console.log(newStr)
    return newStr;
}

rotateStr(str, rotateAmnt1)
rotateStr(str, rotateAmnt2)
rotateStr(str, rotateAmnt3)
rotateStr(str, rotateAmnt4)
rotateStr(str, rotateAmnt5)

function isRotation(s1, s2) {
    for (i = 0; i < s2.length; i++) {
        if (rotateStr(s2, i) == s1) {
            return console.log(true)
        }
    }
    return console.log(false);
}

isRotation(strA1, strB1)
isRotation(strA2, strB2)