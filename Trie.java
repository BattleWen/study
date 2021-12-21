class Trie{

    class Node{
        int count;
        Node[] child;
        Node(){
            count = 0;
            child = new Node[26];
        }
    }

    public Trie(){
        root = new Node();
    }

    public void insert(String word){
        find(word, true, false);
    }

    public boolean search(String word){
        return find(word, false, false);
    }

    public boolean startsWith(String prefix){
        return find(prefix, false, true);
    }

    private boolean find(String word,boolean isInsert, boolean isPrefix){
        Node curr = root;
        for (char ch : s.toCharArray()){
            if (curr.child[ch - 'a'] == null){
                if (isInsert){
                    curr.child[ch - 'a'] = new Node();
                }else {
                    return false;
                }
            }
            curr = curr.child[ch - 'a'];
        }
        if (isInsert) curr.count++;
        if (isPerfix) return true;
        return curr.count > 0;
    }
}