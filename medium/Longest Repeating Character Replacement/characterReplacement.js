/**
 * You are given a string s and an integer k. 
 * You can choose any character of the string and change it to any other uppercase English character. 
 * You can perform this operation at most k times.
 * 
 * Return the length of the longest substring containing the same letter you can get after performing the above operations.
 */

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    const n = s.length;

    let left = 0;
    let right = 0;
    let maxLength = 0;

    // Initialize the letter map
    const alphabetCount = [];
    for (let i = 0; i < 26; ++i) {
        alphabetCount.push(0);
    }

    // Getting the window to the first element
    const letter = s[left];
    const letterIndex = letter.charCodeAt(0) - "A".charCodeAt(0);
    
    alphabetCount[letterIndex] += 1;
    right += 1;
    maxLength = 1;

    // Move the right pointer towards the end
    while (right < n) {
        // Compute the most frequent element
        const letter = s[right];
        const letterIndex = letter.charCodeAt(0) - "A".charCodeAt(0);
        alphabetCount[letterIndex] += 1;

        // Get the max from the alphabetCount
        let mostFrequent = Math.max(...alphabetCount);

        // Compute window length
        let windowLen = right - left + 1;

        // Check for condition
        if (windowLen - mostFrequent <= k) {
            // All is good. compute the max length
            maxLength = Math.max(maxLength, windowLen);
        } else {
            // Now we shrink the window from the left
            while (windowLen - mostFrequent > k && left < n) {
                const leftLetter = s[left];
                const letterIndex = leftLetter.charCodeAt(0) - "A".charCodeAt(0);
                alphabetCount[letterIndex] -= 1;

                left += 1;

                // Get the max from the alphabetCount
                mostFrequent = Math.max(...alphabetCount);

                // Compute window length
                windowLen = right - left + 1;
            }
            
        }

        // Move the right pointer
        right += 1;
    }

    return maxLength;
};

const testCharacterReplacement = (s, k, output) => {
    const result = characterReplacement(s, k);

    if (result === output) console.log("Test Case Passed!");
    else console.log(`Test Case Failed: s: ${s} k: ${k} output: ${output} result: ${result}`);
}

testCharacterReplacement("ABAB", 2, 4);
testCharacterReplacement("AABABBA", 1, 4);
testCharacterReplacement("AAAB", 0, 3);
testCharacterReplacement("ABAA", 0, 2);