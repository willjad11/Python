const queue1 = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;
const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

function socialDistancingEnforcer(queue) {
    spaceCount = 0;
    started = false;
    for (var i = 0; i < queue.length; i++) {
        if (queue[i] != 0 && started == false) {
            started = true;
        }
        else if (started == true) {
            if (queue[i] == 0) {
                spaceCount += 1;
            }
            if (queue[i] == 1) {
                if (spaceCount == 6) {
                    spaceCount = 0;
                }
                else {
                    console.log(false)
                    return false
                }
            }
        }
    }
    console.log(true)
    return true
}

socialDistancingEnforcer(queue1)
socialDistancingEnforcer(queue2)