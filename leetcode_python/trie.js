/**
 * @constructor
 * Initialize your data structure here.
 */
var TrieNode = function() {
    this.childs = new Map();
    this.isWord = false;
};

var Trie = function() {
    this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 * Inserts a word into the trie.
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for(let i = 0; i < word.length; i++){
        let c = word[i];
        let child = node.childs.get(c);
        if(!child){
            child = new TrieNode();
            node.childs.set(c,child);
        }
        node = child; //propagate node
    }
    node.isWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the trie.
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for(let i = 0; i < word.length; i++){
        let c = word[i];
        node = node.childs.get(c);
        if(!node) return false;
    }
    return node.isWord;
    
};

/**
 * @param {string} prefix
 * @return {boolean}
 * Returns if there is any word in the trie
 * that starts with the given prefix.
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for(let i = 0; i < prefix.length; i++){
        let c = prefix[i];
        node = node.childs.get(c);
        if(!node) return false;
    }
    return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var trie = new Trie();
 * trie.insert("somestring");
 * trie.search("key");
 */