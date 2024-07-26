import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text", None)
            ], None)
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text", None)
            ], None)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", None),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text", None)
            ], None)

        node2 = ParentNode(
        "p",
        [
            LeafNode("b", "Boldsss text", None),
            LeafNode(None, "Normal text", None),
            LeafNode("i", "italic text", None),
            LeafNode(None, "Normal text", None)
        ], None)
        self.assertNotEqual(node, node2)
