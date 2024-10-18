from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Check if the user is the owner of the object or an admin
        return self.request.user.is_superuser

    def handle_no_permission(self):
      return redirect('fetch_assets_list')