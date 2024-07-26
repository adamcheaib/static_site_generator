# import unittest
# from textnode import TextNode
#
# class TestTextNode(unittest.TestCase):
#     def test_eq(self):
#         node = TextNode("adam", "text")
#         node2 = TextNode("adam", "text")
#         self.assertEqual(node, node2)
#
#     def test_uneq(self):
#         node = TextNode("Ali", "link")
#         node2 = TextNode("Adam", "img", "www.google.com")
#         self.assertNotEqual(node, node2)
#
# if __name__ == "__main__":
#     unittest.main()