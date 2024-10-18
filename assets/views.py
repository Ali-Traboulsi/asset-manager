from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .assestMixins import AdminRequiredMixin
from .forms import AssetForm
from .models import Asset


class AssetView(View):

    class GetAllAssetsView(AdminRequiredMixin, View):
        @staticmethod
        def get_all_assets(request):
            assets = Asset.objects.all()
            template_name = 'assets/asset_list.html'
            return render(request, template_name, {'assets': assets})

    class AddAssetView(AdminRequiredMixin, View):
        template_name = 'assets/add_asset.html'

        def get(self, request):
            form = AssetForm()
            return render(request, self.template_name, {'form': form})

        def post(self, request):
            form = AssetForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('assets/asset_list')  # Redirect after saving
            return render(request, self.template_name, {'form': form})

    class DeleteAssetView(AdminRequiredMixin, View):
        template_name = 'assets/delete_asset.html'

        @staticmethod
        def get_object(asset_id):
            """
            Custom method to get the asset object or raise 404.
            """
            return get_object_or_404(Asset, id=asset_id)

        def get(self, request, asset_id):
            asset = self.get_object(asset_id)
            return render(request, self.template_name, {'asset': asset})

        def post(self, request, asset_id):
            asset = self.get_object(asset_id)
            asset.delete()
            return redirect('assets/asset_list')

    class EditAssetView(AdminRequiredMixin, View):
        template_name = 'assets/edit_asset.html'

        @staticmethod
        def get_object(asset_id):
            """
            Custom method to get the asset object or raise 404.
            """
            return get_object_or_404(Asset, id=asset_id)

        def get(self, request, asset_id):
            asset = self.get_object(asset_id)  # Use the custom get_object method
            form = AssetForm(instance=asset)
            return render(request, self.template_name, {'form': form})

        def post(self, request, asset_id):
            asset = self.get_object(asset_id)
            form = AssetForm(request.POST, instance=asset)
            if form.is_valid():
                form.save()
                return redirect('assets/asset_list')  # Redirect after editing
            return render(request, self.template_name, {'form': form})
