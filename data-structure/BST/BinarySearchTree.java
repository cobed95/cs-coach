public class BinarySearchTree {
    public Node root;

    public BinarySearchTree(int rootData) {
        this.root = new Node(rootData);
    }

    public void insert(int data) {
        root.insert(data);
    }

    public Node get(int data) {
        return root.get(data);
    }

    public void delete(int data) {
        root.delete(data);
    }
}
