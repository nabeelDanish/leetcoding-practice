/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const letterMap = {};
    if (s.length !== t.length) {
        return false;
    }

    for (let i = 0; i < s.length; i++) {
        const letter = s[i];
        if (letterMap[letter] != null) {
            letterMap[letter] += 1;
        } else {
            letterMap[letter] = 1;
        }
    }

    for (let i = 0; i < t.length; i++) {
        const letter = t[i];
        if (letterMap[letter] != null) {
            letterMap[letter] -= 1;
            if (letterMap[letter] < 0) {
                return false
            }
        } else {
            return false;
        }
    }

    for (key in Object.keys(letterMap)) {
        if (letterMap[key] > 0) {
            return false;
        }
    }

    return true;
};

const testIsAnagram = function(s, t, output) {
    const result = isAnagram(s, t);
    if (result == output) {
        console.log("Test Case Passed!");
    } else {
        console.log(
          `Test Case Failed: s: ${s} t: ${t} output: ${output} result: ${result}`
        );
    }
}

testIsAnagram("anagram", "nagaram", true);
testIsAnagram("rat", "car", false);
testIsAnagram("", "", true);