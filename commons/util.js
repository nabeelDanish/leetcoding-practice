module.exports.compareArrays = function (arr1, arr2) {
    if (arr1.length !== arr2.length)
        return false
    arr1.forEach((element, index) => {
        if (element !== arr2[index])
            return false
    })
    return true
}