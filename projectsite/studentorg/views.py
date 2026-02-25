from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

# ---------------------------
# Home Page
# ---------------------------
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Total students
        context["total_students"] = Student.objects.count()
        
        # Students who joined this year
        today = timezone.now().date()
        count = (
            OrgMember.objects
            .filter(date_joined__year=today.year)
            .values("student")
            .distinct()
            .count()
        )
        context["students_joined_this_year"] = count

        # Total organizations
        context["total_organizations"] = Organization.objects.count()

        # Total programs
        context["total_programs"] = Program.objects.count()

        return context

# ---------------------------
# Organization Views
# ---------------------------
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        allowed = ["college__college_name", "name"]
        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("college__college_name", "name")
            
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


# ---------------------------
# OrgMember Views
# ---------------------------
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')

        if query:
            qs = qs.filter(
                Q(student__firstname__icontains=query) |
                Q(student__lastname__icontains=query) |
                Q(student__middlename__icontains=query) |
                Q(organization__name__icontains=query) |
                Q(student__program__prog_name__icontains=query)
            )

        allowed = [
            "student__firstname",
            "student__program__prog_name",
            "organization__name",
            "date_joined"
        ]

        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("student__firstname")

        return qs

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')


# ---------------------------
# Student Views
# ---------------------------
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')

        if query:
            qs = qs.filter(
                Q(student_id__icontains=query) |
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(middlename__icontains=query) |
                Q(program__prog_name__icontains=query)
            )

        allowed = [
            "student_id",
            "lastname",
            "firstname",
            "middlename",
            "program__prog_name"
        ]

        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("student_id")  # default ordering

        return qs

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')


# ---------------------------
# College Views
# ---------------------------
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')

        if query:
            qs = qs.filter(
                Q(college_name__icontains=query)
            )

        allowed = ["college_name", "created_at", "updated_at"]
        if sort_by in allowed:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by("college_name")  # default

        return qs

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')


# ---------------------------
# Program Views
# ---------------------------
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5
    ordering = ["prog_name"]

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')
        sort_by = self.request.GET.get("sort_by")

        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )

        allowed = ["prog_name", "college__college_name"]
        if sort_by in allowed:
            qs = qs.order_by(sort_by)

        return qs
    
class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')