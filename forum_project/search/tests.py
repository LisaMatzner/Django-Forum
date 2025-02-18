from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from forum.models import Thread, Comment
from django.db.models import Count


class SearchResultsViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create users for testing
        cls.user1 = get_user_model().objects.create_user(
            username="user1", password="password123", display_name="User One")
        cls.user2 = get_user_model().objects.create_user(
            username="user2", password="password123", display_name="User Two")

        # Create threads for testing
        cls.thread1 = Thread.objects.create(
            author=cls.user1,
            title="Test Thread 1",
            description="Description for Test Thread 1"
        )
        cls.thread2 = Thread.objects.create(
            author=cls.user2,
            title="Test Thread 2",
            description="Description for Test Thread 2"
        )
        cls.thread3 = Thread.objects.create(
            author=cls.user2,
            title="Test Thread 3",
            description="Description for Test Thread 3"
        )

        # Add comments to some threads
        cls.comment1 = Comment.objects.create(
            author=cls.user1,
            thread=cls.thread1,
            text="First comment on thread 1"
        )
        cls.comment2 = Comment.objects.create(
            author=cls.user2,
            thread=cls.thread1,
            text="Second comment on thread 1"
        )

    def test_search_for_threads_by_title(self):
        """Test if threads can be searched by title."""
        response = self.client.get(reverse('search-results'), {'q': 'Test Thread 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thread 1')
        self.assertNotContains(response, 'Test Thread 2')

    def test_search_for_threads_by_description(self):
        """Test if threads can be searched by description."""
        response = self.client.get(reverse('search-results'), {'q': 'Description for Test Thread 2'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thread 2')
        self.assertNotContains(response, 'Test Thread 1')

    def test_search_for_users_by_username(self):
        """Test if users can be searched by username."""
        response = self.client.get(reverse('search-results'), {'q': 'user1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User One')
        self.assertNotContains(response, 'User Two')

    def test_search_for_users_by_display_name(self):
        """Test if users can be searched by display name."""
        response = self.client.get(reverse('search-results'), {'q': 'User Two'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Two')
        self.assertNotContains(response, 'User One')

    def test_search_with_no_results(self):
        """Test searching for a term with no results."""
        response = self.client.get(reverse('search-results'), {'q': 'nonexistent term'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No threads found')

    def test_filter_threads_by_newest(self):
        """Test sorting threads by newest."""
        response = self.client.get(reverse('search-results'), {'q': 'Test', 'filter': 'newest'})
        self.assertEqual(response.status_code, 200)
        # Check if the threads are ordered by newest (most recent first)
        self.assertTrue(response.context['results'][0].date_opened_at >= response.context['results'][1].date_opened_at)

    def test_filter_threads_by_oldest(self):
        """Test sorting threads by oldest."""
        response = self.client.get(reverse('search-results'), {'q': 'Test', 'filter': 'oldest'})
        self.assertEqual(response.status_code, 200)
        # Check if the threads are ordered by oldest (earliest first)
        self.assertTrue(response.context['results'][0].date_opened_at <= response.context['results'][1].date_opened_at)

    def test_filter_threads_by_most_comments(self):
        """Test sorting threads by most comments."""
        response = self.client.get(reverse('search-results'), {'q': 'Test', 'filter': 'most_comments'})
        self.assertEqual(response.status_code, 200)
        # Check if the threads are ordered by most comments
        thread_with_most_comments = response.context['results'][0]
        self.assertEqual(thread_with_most_comments.comment_count, 2)

    def test_filter_threads_by_least_comments(self):
        """Test sorting threads by least comments."""
        response = self.client.get(reverse('search-results'), {'q': 'Test', 'filter': 'least_comments'})
        self.assertEqual(response.status_code, 200)
        # Check if the threads are ordered by least comments
        thread_with_least_comments = response.context['results'][0]
        self.assertEqual(thread_with_least_comments.comment_count, 0)

    def test_search_filter_options_displayed(self):
        """Test if filter options are displayed on the search results page."""
        response = self.client.get(reverse('search-results'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        # Check if filter buttons are rendered
        self.assertContains(response, 'Newest')
        self.assertContains(response, 'Oldest')
        self.assertContains(response, 'Most Comments')
        self.assertContains(response, 'Least Comments')
