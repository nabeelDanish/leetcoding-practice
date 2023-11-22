/**
 * Given two strings s and t of lengths m and n respectively, 
 * return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
 * If there is no such substring, return the empty string "".
 * 
 * The testcases will be generated such that the answer is unique.
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    const n = s.length;
    const m = t.length;

    // Basic Length Check
    if (n < m) return "";

    let minWindowString = "";

    // Initializing s and t empty count arrays
    const tLetterMap = [];
    const sLetterMap = [];
    for (let i = 0; i < 52; ++i) {
        tLetterMap[i] = 0;
        sLetterMap[i] = 0;
    }

    // Getting the counts of the T string
    for (let i = 0; i < m; ++i) {
        const letter = t[i];
        const letterIndex = getLetterIndex(letter);
        tLetterMap[letterIndex] += 1;
    }

    // Sliding window (Starting with the size of t)
    let left = 0;
    let right = m - 1;

    // Initial Window Counts
    for (let i = left; i <= right; ++i) {
        const letter = s[i];
        const letterIndex = getLetterIndex(letter);
        sLetterMap[letterIndex] += 1;
    }

    // Now we move the fix sliding window
    while (right < n) {
        if (!includesLetterMap(tLetterMap, sLetterMap)) {
            // If the window does not contain T letters
            // We expand it towards the right until it does
            right += 1;
            if (right >= n) return minWindowString;

            const letter = s[right];
            const letterIndex = getLetterIndex(letter);
            sLetterMap[letterIndex] += 1;
        } else {
            // Otherwise we try and shrink it from the left
            // First we store the minimum that we have right now
            const currentWindowLength = right - left + 1;
            if (currentWindowLength < minWindowString.length || minWindowString === "") {
                minWindowString = s.slice(left, right + 1);
            }

            // Move the left and remove it from the counts
            const letter = s[left];
            const letterIndex = getLetterIndex(letter);
            sLetterMap[letterIndex] -= 1;

            left += 1;
            if (left >= n) return minWindowString;
        }
    }

    return minWindowString;
};

const getLetterIndex = (letter) => {
    const isLowerCase = (letter === letter.toLowerCase());
    if (isLowerCase) return letter.charCodeAt(0) - "a".charCodeAt(0);
    else return (letter.charCodeAt(0) - "A".charCodeAt(0)) + 26;
}

const includesLetterMap = (l1, l2) => {    
    for (let i = 0; i < l1.length; ++i) {
        if (l1[i] > 0 && l2[i] < l1[i]) return false;
    }

    return true;
}

const testMinWindow = (s, t, output) => {
    const result = minWindow(s, t);
    if (result === output) {
        console.log("Test Case Passed!");
    } else {
        console.log(`Test Case Failed! s: ${s} t: ${t} result: ${result} output: ${output}`);
    }
}

testMinWindow("ADOBECODEBANC", "ABC", "BANC");
testMinWindow("a", "a", "a");
testMinWindow("a", "aa", "");
testMinWindow("ab", "A", "");