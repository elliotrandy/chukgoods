from django.test import TestCase, Client
from .models import Shop

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    # def test_shop_creation(self):
    #     shop = Shop.objects.create(
    #       name="BURHAN FC MENANG",
    #       description="BURHAN FC 1-0 PANDA BC",
    #       category="apparel",
    #       is_featured=True
    #     )
    #     self.assertEqual(shop.category, "apparel")
    #     self.assertTrue(shop.is_featured)
        
    # def test_shop_default_values(self):
    #     shop = Shop.objects.create(
    #       name="Test Shop",
    #       description="Test description"
    #     )
    #     self.assertEqual(shop.category, "footwear")
    #     self.assertFalse(shop.is_featured)
        
    # def test_increment_views(self):
    #     shop = Shop.objects.create(
    #       name="Test Shop",
    #       description="Test description"
    #     )
    #     initial_views = shop.shop_views
    #     shop.increment_views()
    #     self.assertEqual(shop.shop_views, initial_views + 1)
        
    # def test_is_shop_hot_threshold(self):
    #     # Test shop with exactly 20 views (should not be hot)
    #     shop_20 = Shop.objects.create(
    #       name="Shop with 20 views",
    #       description="Test description",
    #       shop_views=20
    #     )
    #     self.assertFalse(shop_20.is_shop_hot)
        
    #     # Test shop with 21 views (should be hot)
    #     shop_21 = Shop.objects.create(
    #       name="Shop with 21 views", 
    #       description="Test description",
    #       shop_views=21
    #     )
    #     self.assertTrue(shop_21.is_shop_hot)