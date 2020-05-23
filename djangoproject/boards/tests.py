from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, board_topics
from .models import Board


class HomeTests(TestCase):
    # setUp creates a board instance to test
    def setUp(self):
        self.board = Board.objects.create(
                                        name='Django',
                                        description='Django board'
                                        )
        url = reverse('home')
        self.response = self.client.get(url)

    # Tests if the response of home page == 200
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    # Test if / (root url) returns home view
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse(
                                'board_topics',
                                kwargs={'pk': self.board.pk}
                                )
        self.assertContains(
                            self.response,
                            'href="{0}"'.format(board_topics_url)
                            )


class BoardTopicTests(TestCase):
    # setUp: Create a Board instance to test
    def setUp(self):
        Board.objects.create(name='Django', description='Django board')

    def test_board_topics_view_success_status_code(self):
        # Tests if django is returning 200
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        # Tests if django is returning 404
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        # Tests if django is using the correct view to render the topics
        view = resolve('/board/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_home(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
