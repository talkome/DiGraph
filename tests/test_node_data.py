from unittest import TestCase

from src.node_data import node_data


class test_node_data(TestCase):
    def setUp(self) -> None:
        self.nodes_list = [node_data(i) for i in range(8)]

    def test_get_key(self):
        node1 = self.nodes_list.__getitem__(4)
        node2 = self.nodes_list.__getitem__(5)
        self.assertNotEqual(node1.key, node2.key)

    def test_get_tag(self):
        node1 = self.nodes_list.__getitem__(3)
        node1.set_tag(1)
        node2 = self.nodes_list.__getitem__(6)
        self.assertNotEqual(node1.tag, node2.tag)

    def test_get_info(self):
        node1 = self.nodes_list.__getitem__(2)
        node1.set_info("hello")
        node2 = self.nodes_list.__getitem__(7)
        node2.set_info("bye")
        self.assertNotEqual(node1.info, node2.info)
