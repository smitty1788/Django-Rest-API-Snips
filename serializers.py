from projects.models import Projects
from rest_framework import serializers


# Add Serializers here
# ---------------------

# Project Serilializer
class ProjectsSerializer(serializers.ModelSerializer):
    
    state = serializers.StringRelatedField()
    account = serializers.StringRelatedField()
    
    class Meta:
        model = Projects
        fields = (
            "id",
            "name",
            "deltek",
            "account",
            "city",
            "state",
        )
        

class ProjectDetailsSerializer(serializers.ModelSerializer):
    
    novo_office = serializers.StringRelatedField()
    partner = serializers.StringRelatedField()
    principal = serializers.StringRelatedField()
    manager = serializers.StringRelatedField()
    biller = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    county = serializers.StringRelatedField()
    account = serializers.StringRelatedField()
    account_address_line = serializers.CharField(source='account.billing_address.address_line', read_only=True)
    account_street = serializers.CharField(source='account.billing_address.street', read_only=True)
    account_city = serializers.CharField(source='account.billing_address.city', read_only=True)
    account_state = serializers.CharField(source='account.billing_address.state.state_name', read_only=True)
    account_postcode = serializers.CharField(source='account.billing_address.postcode', read_only=True)
    contact = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField(many=True)
    eng_type = serializers.StringRelatedField(many=True)
    eng_desc = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Projects
        fields = (
            "id",
            "name",
            "deltek",
            "novo_office",
            "partner",
            "principal",
            "manager",
            "biller",
            "assigned_to",
            "address",
            "city",
            "state",
            "postcode",
            "county",
            "account",
            "account_address_line",
            "account_street",
            "account_city",
            "account_state",
            "account_postcode",
            "contact",
            "fee",
            "exspense",
            "retainer",
            "stage",
            "start_date",
            "manager_due_date",
            "client_due_date",
            "description",
            "eng_type",
            "eng_desc",
            "folder_path",
        )
