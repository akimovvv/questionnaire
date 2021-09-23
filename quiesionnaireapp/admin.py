from django.contrib import admin
from .models import Test, Question, Answer_option, Uncorrect_answer_analytic, User_answer_history

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer_option)
admin.site.register(User_answer_history)
admin.site.register(Uncorrect_answer_analytic)