class TreeNode:
    
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        if self.parent:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 4
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()




def build_product_tree():

    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thick Pad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Pixal"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("Televisions")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Samaung"))
    onida = TreeNode("Onida")
    tv.add_child(onida)

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    print(onida.get_level())

    return root


if __name__ == "__main__":
    root = build_product_tree()
  #  print(root.children)
    
    root.print_tree()
