from allauth.account.adapter import DefaultAccountAdapter

class CustomUserAccountAdapter(DefaultAccountAdapter):
  def save_user(self, request, user, form, commit=True):
    from allauth.account.utils import user_field

    user = super().save_user(request, user, form, False)
    user_field(user, 'name', request.data.get('name'))
    user_field(user, 'age', request.data.get('age'))
    user_field(user, 'gender', request.data.get('gender'))
    user_field(user, 'asset', request.data.get('asset'))
    user_field(user, 'salary', request.data.get('salary'))
    user_field(user, 'target_period', request.data.get('target_period'))
    user_field(user, 'future_value', request.data.get('future_value'))
    user_field(user, 'purpose', request.data.get('purpose'))
    user.save()
    return user