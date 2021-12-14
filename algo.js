const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

function binarySearch(sortedNums, searchNum) {
    let divide = Math.ceil(sortedNums.length / 2);
    let part1 = sortedNums.slice(0, divide)
    let part2 = sortedNums.slice(-divide + 1)
    if (searchNum < part2[0]) {
        for (let i = 0; i < part1.length; i++) {
            if (part1[i] == searchNum) {
                console.log(true);
                return true;
            }
        }
        console.log(false);
        return false;
    }
    else if (searchNum > part1[part1.length - 1]) {
        for (let i = 0; i < part2.length; i++) {
            if (part2[i] == searchNum) {
                console.log(true);
                return true;
            }
        }
        console.log(false);
        return false;
    }
}

binarySearch(nums3, searchNum3)