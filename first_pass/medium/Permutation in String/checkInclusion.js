/** Given two strings s1 and s2, 
 *      return true if s2 contains a permutation of s1, 
 *      or false otherwise.
 * 
 * In other words, return true if one of s1's permutations is the substring of s2. 
 * */

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const n = s1.length;
    const m = s2.length;

    // Basic length check
    if (m < n) return false;

    // Getting counts and unique letters of s1
    const s1LetterMap = [];
    const s2LetterMap = [];
    for (let i = 0; i < 26; ++i) {
        s1LetterMap[i] = 0;
        s2LetterMap[i] = 0;
    }

    for (let i = 0; i < n; ++i) {
        const letter = s1[i];
        const letterIndex = getLetterIndex(letter);
        s1LetterMap[letterIndex] += 1;
    }

    // Fixed sliding window
    let left = 0;
    let right = n - 1;

    // Initial window counts
    for (let i = left; i <= right; ++i) {
        const letter = s2[i];
        const letterIndex = getLetterIndex(letter);
        s2LetterMap[letterIndex] += 1;
    }

    // Now we move the fixed sliding window
    while (right < m) {
        // Time to check for the condition
        if (compareLetterMaps(s1LetterMap, s2LetterMap)) return true;

        // Move the sliding window one step from the right
        right += 1;

        // Sanity Check
        if (right >= m) break;

        let letter = s2[right];
        let letterIndex = getLetterIndex(letter);
        s2LetterMap[letterIndex] += 1;

        // Move the sliding window one step from the left
        letter = s2[left];
        letterIndex = getLetterIndex(letter);
        s2LetterMap[letterIndex] -= 1;
        left += 1;
    }

    return false;
};

const getLetterIndex = (letter) => {
    return letter.charCodeAt(0) - "a".charCodeAt(0);
}

const compareLetterMaps = (l1, l2) => {
    if (l1.length !== l2.length) return false;
    
    for (let i = 0; i < l1.length; ++i) {
        if (l1[i] !== l2[i]) return false;
    }

    return true;
}

const testCheckInclusion = (s1, s2, output) => {
    const result = checkInclusion(s1, s2);
    
    if (result == output) console.log("Test Case Passed!");
    else console.log(`Test Case Failed: s1: ${s1} s2: ${s2} result: ${result} output: ${output}`); 
}

testCheckInclusion("ab", "eidbaooo", true);
testCheckInclusion("ab", "eidboaoo", false);