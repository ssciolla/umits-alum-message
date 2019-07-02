import django_filters
from alum_message.models import Message, Alum


class MessageFilter(django_filters.FilterSet):
    sender_alum = django_filters.CharFilter(
        field_name='sender_alum__uniqname',
        label='Sender',
        lookup_expr='exact'
    )

    recipients = django_filters.CharFilter(
        field_name='receipts__alum__uniqname',
        label='Recipient',
        lookup_expr='exact'
    )

    class Meta:
        model = Message
        # form = SearchForm
        # fields [] is required, even if empty.
        fields = []
