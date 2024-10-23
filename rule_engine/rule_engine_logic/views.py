from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Rule, UserProfile
from .serializers import RuleSerializer, UserProfileSerializer
from .utils import create_rule, evaluate_rule  # Import your AST functions here
from django.shortcuts import render
from rest_framework.decorators import action

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def create(self, request, *args, **kwargs):
        rule_string = request.data.get('rule_string')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'], url_path='evaluate')
    def evaluate(self, request, *args, **kwargs):
        rule_id = request.data.get('rule_id')
        user_id = request.data.get('data').get('id')

        try:
            # Fetch the rule
            rule = Rule.objects.get(id=rule_id)
            rule_function = create_rule(rule.rule_string)  # Convert rule string to AST function

            # Fetch the user's profile data using the user ID
            user_profile = UserProfile.objects.get(id=user_id)

            # Create the context with user profile details
            user_data = {
                'age': user_profile.age,
                'income': user_profile.income,
                'department': user_profile.department,
            }

            # Log rule and context for debugging purposes
            print("Evaluating rule:", rule.rule_string)
            print("Data for evaluation:", user_data)

            # Evaluate the rule using the user's profile data
            result = evaluate_rule(rule_function, user_data)
            return Response({"result": result}, status=status.HTTP_200_OK)

        except Rule.DoesNotExist:
            return Response({"error": "Rule not found"}, status=status.HTTP_404_NOT_FOUND)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Log the exception for debugging purposes
            print("Error during evaluation:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

def index(request):
    rules = Rule.objects.all()  # Fetch all rules from the database
    user_profiles = UserProfile.objects.all()  # Fetch all user profiles from the database
    context = {
        'rules': rules,
        'user_profiles': user_profiles
    }
    return render(request, 'rule_engine_logic/index.html', context)
