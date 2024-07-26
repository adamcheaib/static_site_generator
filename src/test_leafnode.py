from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test__eq__(self):
        node = LeafNode("p", "This is a paragraph", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_uneq(self):
        node = LeafNode("p", "This is a paragraph", None)
        node2 = LeafNode("b", "This is a bold", None)
        self.assertNotEqual(node.to_html(), node2.to_html())


if __name__ == "__main__":
    unittest.main()