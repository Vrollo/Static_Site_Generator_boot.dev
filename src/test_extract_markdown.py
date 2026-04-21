import unittest
from extract_markdown_url import *

class TestExtractMarkdown(unittest.TestCase):
    def test_get_url(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = "[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]"
        self.assertEqual(repr(result), expected)

    def test_get_url_missing_closure(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"
        result = extract_markdown_links(text)
        expected = "[('to boot dev', 'https://www.boot.dev')]"
        self.assertEqual(repr(result), expected)

    def test_get_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = "[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]"
        self.assertEqual(repr(result), expected)

    def test_get_image_missing_exclamation(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = "[('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]"
        self.assertEqual(repr(result), expected)

    def test_get_empty(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan(https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = "[]"

