#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>

struct BstNode
{
    int data;
    struct BstNode* left;
    struct BstNode* right;
};


struct BstNode* GetNewNode(int data){
    struct BstNode* newNode = (struct BstNode*)malloc(sizeof(struct BstNode));
    newNode -> data = data;
    newNode -> left = newNode ->right = NULL;
    return newNode;
}


struct BstNode* Insert(struct BstNode* root,int data){
    if(root == NULL){   //tree is empty
        root = GetNewNode(data);
    }
    else if (data <= (root -> data))
    {
        root -> left = Insert(root -> left, data);
    }
    else{
        root -> right = Insert(root -> right, data);
    }    
    return root;
}

bool Search(struct BstNode* root,int data){
    if(root == NULL) return false;
    else if(data == root -> data) return true;
    else if(data <= root -> data) return Search(root -> left, data);
    else return Search(root -> right, data);
}


//Function to find some data in the tree
struct BstNode* Find(struct BstNode* root, int data) {
	if(root == NULL) return NULL;
	else if(root->data == data) return root;
	else if(root->data < data) return Find(root->right,data);
	else return Find(root->left,data);
}


int FindMin(struct BstNode* root){  // root is a local variable acopy of actual reference stored here
    if (root == NULL)
    {
        printf("Error: Empty tree\n");
        return -1;
    }
    
    while(root -> left != NULL){
        root = root -> left;
    }
    return root -> data;
}

struct BstNode* FindMinPtr(struct BstNode* root){
    if (root == NULL) return NULL;
    while(root -> left != NULL){
        root = root -> left;
    }
    return root;
}

// Altenative algo

// int FindMin(struct BstNode* root){
//     if (root == NULL)
//     {
//         printf("Error: Empty tree\n");
//         return -1;
//     }
//     else if (root -> left == NULL)
//     {
//         return root -> data;
//     }
//     return FindMin(root -> left);
// }


int FindMax(struct BstNode* root){
    if (root == NULL)
    {
        printf("Error: Empty tree\n");
        return -1;
    }
    
    while(root -> right != NULL){
        root = root -> right;
    }
    return root -> data;
}

// Alternative algo

// int FindMax(struct BstNode* root){
//     if (root == NULL)
//     {
//         printf("Error: Empty tree\n");
//         return -1;
//     }
//     else if (root -> right == NULL)
//     {
//         return root -> data;
//     }
//     return FindMax(root -> right);
// }

int FindHeight(struct BstNode* root){
    if(root == NULL){
        return -1;
    }
    int leftHeight = FindHeight(root -> left);
    int rightHeight = FindHeight(root -> right);
    return fmax(leftHeight,rightHeight)+1;
}


//preorder: space complexity O(height of tree)  ie n(worse case) or log n(balanced) function stack due to recursion; 
// time complexity O(n)
void Preorder(struct BstNode* root){ 
    if(root == NULL) return;
    printf(" %d",root -> data);
    Preorder(root -> left);
    Preorder(root -> right);
}

void Inorder(struct BstNode* root){ 
    if(root == NULL) return;
    Inorder(root -> left);
    printf(" %d",root -> data);    
    Inorder(root -> right);
}

void Postorder(struct BstNode* root){ 
    if(root == NULL) return;
    Postorder(root -> left);
    Postorder(root -> right);
    printf(" %d",root -> data);
}

void ReverseInorder(struct BstNode* root){ 
    if(root == NULL) return;
    ReverseInorder(root -> right);
    printf(" %d",root -> data);    
    ReverseInorder(root -> left);
}



bool IsSubtreeLesser(struct BstNode* root,int value){
    if(root == NULL) return true;
    if(root->data <= value && IsSubtreeLesser(root->left,value) && IsSubtreeLesser(root->right,value))
        return true;
    else
        return false;
}


bool IsSubtreeGreater(struct BstNode* root,int value){
    if(root == NULL) return true;
    if(root->data >= value && IsSubtreeGreater(root->left,value) && IsSubtreeGreater(root->right,value))
        return true;
    else
        return false;
}

bool IsBinarySearchTree(struct BstNode* root)
{
    if(root == NULL) return true;
    if(IsSubtreeLesser(root -> left,root -> data)
    && IsSubtreeGreater(root -> right,root -> data)
    && IsBinarySearchTree(root -> left)
    && IsBinarySearchTree(root -> right))
        return true;
    else return false;
}

struct BstNode* Delete(struct BstNode* root, int data){
    if(root == NULL) return root;
    else if(root -> data < data) return root -> left = Delete(root -> left, data);
    else if(root -> data > data) return root -> right = Delete(root -> right, data);
    else{
        // Case 1:No Child
        if(root -> left == NULL && root -> right == NULL){
            free(root);
            root == NULL;
        }
        // Case 2: one child
        else if(root->left ==NULL){
            struct BstNode* temp = root;
            root = root -> right;
            free(temp);
        }
        else if(root->right ==NULL){
            struct BstNode* temp = root;
            root = root -> left;
            free(temp);
        }
        // Case 3: two children
        else{
            struct BstNode* temp = FindMinPtr(root->right);
            root -> data = temp -> data;
            root -> right = Delete(root -> right,temp -> data);
        }
    }
    return root;
}

struct BstNode* GetSuccessor(struct BstNode* root, int data){
    //Search the node 
    struct BstNode* current = Find(root,data);
    if(current == NULL) return NULL;
    // Case 1: Node has right subtree 
    if (current -> right != NULL)
    {
        return FindMinPtr(current -> right);
    }
    // Case 2: No right Subtree 
    else{
        struct BstNode* successor = NULL;
        struct BstNode* ancestor = NULL;
        while (ancestor != current)
        {
            if (current -> data < ancestor -> data)
            {
                successor = ancestor;
                ancestor = ancestor -> left;
            }
            else{
                ancestor = ancestor -> right;
            }            
        }
        return successor;    
    }       
}

int main(){
    struct BstNode* root=NULL;
    root = Insert(root,15);
    root = Insert(root,10);
    root = Insert(root,20);
    root = Insert(root,25);
    root = Insert(root,8);
    root = Insert(root,12);

    printf(" \nInorder:");
    Inorder(root);

    printf(" \nReverseInorder:");
    ReverseInorder(root);

    bool x = Search(root,11);
    printf("\nSearch result: %d",x);

    int y = FindHeight(root);
    printf("\nHeight Of tree is: %d",y);

    int z = IsBinarySearchTree(root);
    printf("\nIS it a BST ? : %d",z);

    int w = 10;
    struct BstNode* s = GetSuccessor(root,w);
    printf("\nSucessor of %d is : %d",w,s->data);


}


