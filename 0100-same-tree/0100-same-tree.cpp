
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Both empty → same
        if (!p && !q) return true;

        // One empty, other not → different
        if (!p || !q) return false;

        // Values different → different
        if (p->val != q->val) return false;

        // Check left and right subtrees recursively
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};