
const str1 = "aaaabbcddddooopppvvvvvfffddwwwww";

function encodeStr(str){

    let count = 1;
    let newstring = "";

    for (let i = 0; i < str.length; i++) {
        if (str[i] == str[i - 1]) {
            count ++;
        }
        if (i == str.length - 1) {
            newstring += str[i] + count;
        }
        else if (str[i] !== str[i - 1] && i - 1 > 0) {
            newstring += str[i - 1] + count
            count = 1;
        }
        else if (str[i] !== str[i - 1] && str[i] !== str[i + 1]) {
            newstring += str[i] + "1";
        }
    }
    console.log(newstring)
}

encodeStr(str1)