/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const result = {};

  for (let j = 0; j < strs.length; ++j) {
    const str = strs[j];

    // Getting an empty count
    const count = [];
    for (let i = 0; i < 26; ++i) {
      count.push(0);
    }

    // Now we compute its character count
    for (let i = 0; i < str.length; i++) {
      const letter = str[i];
      const value = letter.charCodeAt(0) - "a".charCodeAt(0);
      count[value] += 1;
    }

    if (result[count] != null) {
      result[count].push(str);
    } else {
      result[count] = [str];
    }
  }

  return Object.values(result);
};

const testGroupAnagrams = function (strs, output) {
  const result = groupAnagrams(strs);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: strs: ${JSON.stringify(strs)} output: ${JSON.stringify(
        output
      )} result: ${JSON.stringify(result)}`
    );
  }
};

testGroupAnagrams(
  ["eat", "tea", "tan", "ate", "nat", "bat"],
  [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
);
testGroupAnagrams([""], [[""]]);
testGroupAnagrams(["a"], [["a"]]);
testGroupAnagrams(["", ""], [["", ""]]);
