class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = ""
        for (let s of strs) {
            res += s.length + "?" + s
        }
        return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = []
        let j = 0
        while ( j < str.length) {
            let num = ""
            while (str[j] !== "?") {
                num += str[j]
                j++
            }
            j++
            num = Number(num)
            let word = ""
            while (num > 0) {
                word += str[j]
                num--
                j++
            }
            res.push(word)
        }
        return res
    }
}
