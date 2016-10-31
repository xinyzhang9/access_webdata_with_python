/**
 * @constructor
 * Initialize your data structure here.
 */
var TrieNode = function() {
    this.children = []
    this.char = ''
    this.isEnd = false
};

TrieNode.prototype.indexOf = function(char) {
    for(var i = 0;i<this.children.length;i++) {
        if(this.children[i].char === char) {
            return i
        }
    }
    return -1
}
TrieNode.prototype.insert = function(char) {
    var newNode = new TrieNode()
    newNode.char = char
    this.children.push(newNode)
    return newNode
}

/**
 * @constructor
 */
var WordDictionary = function() {
    this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 * Adds a word into the data structure.
 */
WordDictionary.prototype.addWord = function(word) {
    var char, index = 0,
        node = this.root
    for(var i = 0; i < word.length; i++) {
        char = word.charAt(i)
        index = node.indexOf(char)
        if(index >= 0) {
            node = node.children[index]
        } else {
            node = node.insert(char)
        }
    }
    node.isEnd = true
};

/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the data structure. A word could
 * contain the dot character '.' to represent any one letter.
 */
WordDictionary.prototype.search = function(word) {
    return (function search(root,word) {
        var char,index = 0,
            node = root,result = false
        for(var i = 0; i < word.length; i++) {
            char = word.charAt(i)
            if(char === '.') {
                for(var j = 0;j<node.children.length;j++) {
                    result = result || search(node.children[j],word.slice(i+1))
                }
                return result
            } else {
                index = node.indexOf(char) 
                if(index >= 0) {
                    node = node.children[index]
                } else {
                    return false
                }
            }
        }
        return node.isEnd === true
    })(this.root,word);
};