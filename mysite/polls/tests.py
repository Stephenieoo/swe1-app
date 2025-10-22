from django.test import TestCase
from django.urls import reverse


class PollsViewTests(TestCase):
    """测试 polls 应用的视图"""
    
    def test_index_view(self):
        """测试首页是否可以正常访问"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_contains_welcome_message(self):
        """测试首页是否包含欢迎信息"""
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'polls')


class HealthCheckTests(TestCase):
    """健康检查测试"""
    
    def test_health_check(self):
        """测试健康检查端点"""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
# Create your tests here.
