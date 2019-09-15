public class Node {
    public int data;
    public Node left;
    public Node right;

    public Node(int data) {
        this(data, null, null);
    }

    public Node(int data, Node left, Node right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    public void insert(int data) {
        if (data == this.data) {
            return;
        } else if (data > this.data) {
            if (this.right != null) {
                this.right.insert(data);
            } else {
                this.right = new Node(data);
            }
        } else {
            if (this.left != null) {
                this.left.insert(data);
            } else {
                this.left = new Node(data);
            }
        }
    }

    public Node get(int data) {
        if (data == this.data) {
            return this;
        } else if (data > this.data) {
            if (this.right != null) {
                return this.right.get(data);
            } else {
                return null;
            }
        } else {
            if (this.left != null) {
                return this.left.get(data);
            } else {
                return null;
            }
        }
    }

    public Node delete(int data) {
        // TODO: implement delete.
        return null;
    }
}
