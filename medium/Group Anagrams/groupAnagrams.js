var isAnagram = function (s, t) {
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
        return false;
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

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const words = strs.map((word) => {
    return [word, true];
  });

  const groups = [];
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (!word[1]) {
      continue;
    }
    const group = [word[0]];

    for (let j = i + 1; j < words.length; j++) {
      const otherWord = words[j];
      if (!otherWord[1]) {
        continue;
      }
      if (isAnagram(word[0], otherWord[0])) {
        group.push(otherWord[0]);
        words[j][1] = false;
      }
    }

    groups.push(group);
  }

  return groups;
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
