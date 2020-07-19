from collections import MutableMapping


class MapBase(MutableMapping):
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class Tree:
    class Position:

        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0


class BinaryTree(Tree):

    def left(self, p):

        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Postion Type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_postion(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_postion(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_postion(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_postion(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_postion(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_postion(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_postion(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_postion(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be leaf ")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


class TreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def _subtree_search(self, p: Position, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_acess(p)
            return p

    def find_min(self):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_acess(p)
            if k != p.key():
                raise KeyError("Key Error: " + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_acess(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
                self._rebalance_insert(leaf)

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p
            p = self.after(p)

    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError("Key Error: " + repr(k))

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        x = p._node
        y = self.parent(p)
        z = self.parent(y)
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._node._left)
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


class RedBlackTreeMap(TreeMap):

    class _Node(TreeMap._Node):
        __slots__ = "_red"

        def __init__(self,element,parent=None,left=None,right=None):
            super().__init__(element,parent,left,right)
            self._red = True #new node red by default

    def _set_red(self,p):p._node._red = True
    def _set_black(self,p):p._node._red = False
    def _set_color(self,p,make_red):p._node._red = make_red
    def _is_red(self,p):return p is not None and p._node._red
    def _is_red_leaf(self,p):return self._is_red(p) and self.is_leaf(p) #TODO finish _Node class function is_leaf()

    def _get_red_child(self,p):
        for child in (self.left(p),self.right(p)):
            if self._is_red(child):
                return child
        return None

    def _rebalance_insert(self,p):
        self._resolve_red(p)

    def _resolve_red(self,p):
        if self.is_root(p):
            self._set_black(p)
        else:
            parent = self.parent(p)
            if self._is_red(parent):
                uncle = self.sibling(parent)
                if not self._is_red(uncle):
                    middle = self._restructure(p)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self._set_red(grand)
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand) #recursion at red grandparent

    def _rebalance_delete(self, p):
        if len(self) == 1:
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p,c)
            elif n ==2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self,z,y):
        if not self._is_red(y):
            x =self._get_red_child(y)
            if x is not None:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle,old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)
                elif not self.is_root(z):
                    self._fix_deficit((self.parent(z),self.sibling(z)))
        else:
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z,self.left(z))
            else:
                self._fix_deficit(z,self.right(z))
    
