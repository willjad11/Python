const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

function join(arr, separator) {
    newStr = "";
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == arr.length) {
            newStr += arr[i];
        }
        else {
            newStr += arr[i] + separator;
        }
    }
    console.log(newStr)
}

join(arr1, separator1)
join(arr2, separator2)
join(arr3, separator3)
join(arr4, separator4)
join(arr5, separator5)