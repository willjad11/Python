string1 = "a x a";
string2 = "racecar";
string3 = "Dud";
const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

const str4 = "a1001x20002y5677765z";
const expected4 = "5677765";

const str5 = "a1001x20002y567765z";
const expected5 = "567765";

function ispalindrome(str) {

    newString = "";
    if (str.length == 1) {
        return true;
    }
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }

    if (str == newString) {
        return true;
    }

    else {
        return false
    }
}

// console.log(ispalindrome(string1))
// console.log(ispalindrome(string2))
// console.log(ispalindrome(string3))

function ispalindrome2(str2) {

    var newString = "";
    var palindromes = [];

    for (var i = 0; i < str2.length; i++) {
        newString = str2[i]
        if (ispalindrome(newString) == true) {
            palindromes.push(newString);
        }
        for (var x = i + 1; x < str2.length; x++) {
            newString += str2[x]
            if (ispalindrome(newString) == true) {
                palindromes.push(newString);
            }
        }
        newString = "";
    }
    index = 0;
    for (var y = 0; y < palindromes.length; y++) {
        if (palindromes[y].length > palindromes[index].length) {
            index = y;
        }
    }
    console.log(palindromes[index])
    return palindromes[index];
}

ispalindrome2(str1)
ispalindrome2(str2)
ispalindrome2(str3)
ispalindrome2(str4)
ispalindrome2(str5)