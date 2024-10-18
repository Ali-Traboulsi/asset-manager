from django.urls import path
from .views import AssetView

urlpatterns = [
    path('', AssetView.GetAllAssetsView.as_view(), name='asset_list'),
    path('/add/', AssetView.AddAssetView.as_view(), name='add_asset'),
    path('/edit/<int:asset_id>', AssetView.EditAssetView.as_view(), name='edit_asset'),
    path('/delete/<int:asset_id>', AssetView.DeleteAssetView.as_view(), name='delete_asset')
]