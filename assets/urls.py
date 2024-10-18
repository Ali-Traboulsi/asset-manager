from django.urls import path
from .views import AssetView, LendingView

urlpatterns = [
    path('', AssetView.GetAllAssetsView.as_view(), name='assets_list'),
    path('add/', AssetView.AddAssetView.as_view(), name='add_asset'),
    path('edit/<uuid:asset_id>/', AssetView.EditAssetView.as_view(), name='edit_asset'),
    path('delete/<uuid:asset_id>/', AssetView.DeleteAssetView.as_view(), name='delete_asset'),
    path('lend/', LendingView.LendAssetView.as_view(), name='lend_asset'),
    path('return/', LendingView.ReturnAsset.as_view(), name='return_asset')
]