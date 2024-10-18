from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Rule
from .serializers import RuleSerializer
from .utils import create_rule, evaluate_rule  # Import your AST functions here
from django.shortcuts import render

class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def create(self, request, *args, **kwargs):
        rule_string = request.data.get('rule_string')
        # Save rule to the database
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def evaluate(self, request, *args, **kwargs):
        rule_id = request.data.get('rule_id')
        data = request.data.get('data')
        try:
            rule = Rule.objects.get(id=rule_id)
            rule_ast = create_rule(rule.rule_string)  # Convert rule string to AST
            result = evaluate_rule(rule_ast, data)  # Evaluate the rule
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Rule.DoesNotExist:
            return Response({"error": "Rule not found"}, status=status.HTTP_404_NOT_FOUND)



    def index(request):
        return render(request, 'index.html')
