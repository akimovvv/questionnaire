from django.db import models
from django.contrib.auth.models import User

departments = (('OTP ServiceDesk', 'ОТП ServiceDesk'),
               ('IT Department', 'IT-Департамент'),
               ('Administrative and Economic Department', 'Административно хозяйственный отдел'),
               ('MR and KO Department', 'Департамент МР и КО'),
               ('Customer Support Department', 'Департамент Поддержки Клиентов'),
               ('Sales Department', 'Департамент Продаж'),
               ('Digital Services Department', 'Департамент Цифровых Услуг'),
               ('Credit Specialists', 'Кредитные Специалисты'),
               ('General Department', 'Общий отдел'),
               ('AUR Department', 'Отдел АУР'),
               ('Product Development Department', 'Отдел Разработки Продуктов'),
               ('Retail Underwriting Department', 'Отдел розничного Андеррайтинга'),
               ('Project Management Department', 'Отдел управления проектами'),
               ('Supervisors', 'Руководство'),
               ('Secretary of the Board of Directors', 'Секретарь Совета Директоров'),
               ('Security Service', 'Служба Безопасности'),
               ('Credit Administration Department', 'Управление Администрирования Кредитов'),
               ('Collateral Management', 'Управление Залогового Обеспечения'),
               ('Information Security Department', 'Управление Информационной Безопасности'),
               ('Marketing Department', 'Управление Маркетинга'),
               ('Reporting Department (RD)', 'Управление Отчётности (УО)'),
               ('Management of Payment Systems (MPS)', 'Управление Платёжных Систем (УПС)'),
               ('Personnel Development Management', 'Управление Развитие Персонала'),
               ('Department of Settlements (DS)', 'Управление Расчётов (УР)'),
               ('Fraud Service', 'Фрод Служба'),
               ('Economic Management', 'Экономическое Управление'),
               ('Legal Management', 'Юридическое Управление'),
               ('All Savings Banks', 'Все Сберегательные Кассы'),
               ('All Branches', 'Все Филиалы'))


class Test(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название теста')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='Дата и время начала тестирования')
    duration = models.TimeField(verbose_name='Продолжительность тестирования')
    department = models.CharField(verbose_name='Тестирование для', choices=departments, max_length=300)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer_option(models.Model):
    text = models.TextField(verbose_name='Вариант ответа')
    is_correct = models.BooleanField(verbose_name='Правильный ответ')
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class User_answer_history(models.Model):
    score = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Процент правильно отвеченных вопросов')
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Uncorrect_answer_analytic(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)