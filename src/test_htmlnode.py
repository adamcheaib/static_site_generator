import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("b", "Amazing text!", None, {"name": "adam"})
        node2 = HTMLNode("b", "Amazing text!", None, {"name": "adam"})
        self.assertEqual(node1, node2)

    def test_different(self):
        node1 = HTMLNode("b", "Amazing text!", None, {"name": "adamssss"})
        node2 = HTMLNode("b", "Amazing text!", None, {"name": "adam"})
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()