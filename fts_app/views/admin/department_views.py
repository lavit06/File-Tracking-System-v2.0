from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from fts_app.models import StoreDocument, Role, User, Message, UserDetail, UserRoleMap, Department, SubDepartment, DepartmentRoleMap, Noting, NotingUserMap 
from django.contrib import messages
from django.db.models import Prefetch
from django.utils.text import slugify
from ..decorators import check_session_exists
from django.db.models import F 
import os

@check_session_exists 
def list_department(request):
  departments = Department.objects.select_related('created_user').all()

  data = {'section' : 'list_department', 'departments' : departments}
  return render(request,'admin/department.html',data) 



@check_session_exists 
def create_department(request):   
  if request.method == 'POST':
        name = request.POST.get('department_name')
        slug_name = slugify(request.POST.get('department_name'))
        created_user_id = request.session.get('user_id')
        status = request.POST.get('department_status')
        department = Department(name = name,slug_name = slug_name, created_user_id = created_user_id, status = status)
        department.save() 
        messages.success(request,"New Department Added")  
  
  data = {'section' : 'create_department'}
  return render(request,'admin/department.html',data)



@check_session_exists 
def update_department(request,department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
          department = Department.objects.get(id=department_id)
          # department = get_object_or_404(Department, pk = department_id)
          department.name = request.POST.get('department_name')  
          department.slug_name = slugify(request.POST.get('department_name'))
          department.status = request.POST.get('department_status')
          department.save() 
          messages.success(request,"Department Updated") 
    
    data = {'section' : 'update_department','department' : department}
    return render(request,'admin/department.html',data) 



@check_session_exists 
def delete_department(request,department_id): 
  department = Department.objects.get(id=department_id) 
  department.delete()
  return redirect('admin-list-department') 



# ----------- Sub Department -----------    


@check_session_exists 
def list_sub_department(request):
  sub_department = SubDepartment.objects.select_related('created_user','department_id').all() 
  data = {'section' : 'list_sub_department', 'sub_department' : sub_department}
  return render(request,'admin/department.html',data) 



@check_session_exists 
def create_sub_department(request):
    if request.method == 'POST':
        sub_department_name = request.POST.get('sub_department_name')
        slug_sub_department_name = slugify(request.POST.get('sub_department_name'))  
        department_id = request.POST.get('parent_department_id')
        created_user_id = request.session.get('user_id') 
        status = request.POST.get('sub_department_status')
        department_roles = request.POST.getlist('department_roles[]') 
        
        sub_department = SubDepartment(
            name=sub_department_name,
            slug_name=slug_sub_department_name,
            department_id_id=department_id,
            created_user_id=created_user_id,
            status=status
        )
        sub_department.save()

        sub_department_insert_id = sub_department.id

        for role in department_roles:
              DepartmentRoleMap.objects.create(
                  department_id = department_id,
                  sub_department_id = sub_department_insert_id,
                  role_id = role
              ) 
          
        messages.success(request, "New Sub Department Added")
        return redirect('admin-list-sub-department')  # Redirect to a suitable URL after creation
    
    roles = Role.objects.all()
    departments = Department.objects.select_related('created_user').all() 
    data = {'section': 'create_sub_department', 'departments': departments,'roles' : roles}
    return render(request, 'admin/department.html', data)



@check_session_exists 
def update_sub_department(request,sub_department_id):
    sub_department = SubDepartment.objects.get(id=sub_department_id)  
    sub_department_roles = DepartmentRoleMap.objects.filter(sub_department_id=sub_department_id)
    role_ids = []
    for r in sub_department_roles:
        role_ids.append(r.role_id)

    if request.method == 'POST':
        # department = get_object_or_404(Department, pk = department_id)
        sub_department.name = request.POST.get('sub_department_name') 
        sub_department.slug_name = slugify(request.POST.get('sub_department_name'))
        sub_department.department_id_id = request.POST.get('parent_department_id')
        sub_department.status = request.POST.get('sub_department_status')
        department_roles = request.POST.getlist('department_roles[]')    
        sub_department.save()  
  
        # DepartmentRoleMap.objects.filter(sub_department_id=sub_department_id, role_id__in=roles_to_delete).delete()

        for role in department_roles:
              defaults = {'role_id': role}
              DepartmentRoleMap.objects.update_or_create( 
                  department_id = sub_department.department_id_id,
                  sub_department_id = sub_department_id,
                  role_id=role,
                  defaults=defaults
              ) 

        messages.success(request,"Sub Department Updated")
        return redirect('admin-update-sub-department',sub_department_id)
    
    roles = Role.objects.all()
    departments = Department.objects.select_related('created_user').all() 
    data = {'section' : 'update_sub_department','sub_department' : sub_department,'roles' : roles, 'departments': departments,'sub_department_roles' : role_ids}   
    return render(request,'admin/department.html',data)   



@check_session_exists 
def delete_sub_department(request,sub_department_id):  
  sub_department = Department.objects.get(id=sub_department_id)
  sub_department.delete()  

  return redirect('admin-list-sub-department')


@check_session_exists
def search_noting(request): 
    uid = request.session.get('user_id')
    if request.method == 'POST':
        search_by_noting_no = request.POST.get('search_by_noting_no', '')
        if search_by_noting_no:
            notings = NotingUserMap.objects \
                .filter(noting__noting_no=search_by_noting_no) \
                .select_related('noting', 'from_user', 'to_user') \
                .values(
                    'id', 'is_opened', 'message', 'is_forwarded', 'status',
                    'noting__id', 'noting__noting_no', 'noting__filename_doc', 'noting__filename_dak_doc',
                    'noting__comment', 'noting__digital_signature', 'noting__status', 'noting__title', 
                    'noting__user_id', 'noting__selected_user_id', 'noting__role_id',
                    from_user_name=F('from_user__username'),
                    to_user_name=F('to_user__username')
                )
        else:
            notings = NotingUserMap.objects.none()  # Return empty queryset for NotingUserMap
    else:
        notings = NotingUserMap.objects.none()  # Return empty queryset for NotingUserMap
   
    data = {'section': "search_noting", 'notings': notings }
    return render(request, 'admin/noting.html', data) 


@check_session_exists
def monitoring_noting(request):
    notings = Noting.objects.filter().order_by('-pk')

    for noting in notings:
        # Initialize the array for users
        users_array = []
        noting_detail_array = []

        notings_map = NotingUserMap.objects \
            .filter(noting_id=noting.id, from_user_id=noting.user_id) \
            .select_related('noting', 'from_user', 'to_user') \
            .values(
                'id', 'is_opened', 'message', 'is_forwarded', 'status',
                'noting__id', 'noting__noting_no', 'noting__filename_doc', 'noting__filename_dak_doc',
                'noting__comment', 'noting__digital_signature', 'noting__status', 'noting__title',
                'noting__user_id', 'noting__selected_user_id', 'noting__role_id',
                from_user_name=F('from_user__username'),
                to_user_name=F('to_user__username')
            )

        # Collect the usernames
        for map_item in notings_map:
            users_array.append(map_item['to_user_name'])
            noting_detail_array.append(map_item)

        # Attach the users array to each noting object (as an attribute, not in the database)
        noting.users = users_array
        noting.noting_map_detail = noting_detail_array 

    noting_counts = get_noting_counts()  # Assuming this function is defined elsewhere
    data = {
        'section': "monitoring_noting",
        'notings': notings,
        'noting_counts': noting_counts
    }
    return render(request, 'admin/noting.html', data)





def search_noting_view(request, noting_id):
    uid = request.session.get('user_id')
    if noting_id:
        # Query the Noting object
        noting = Noting.objects.get(id=noting_id)

        # Query the NotingUserMap related objects
        notings_map = NotingUserMap.objects \
            .filter(noting_id=noting_id) \
            .select_related('noting', 'from_user', 'to_user') \
            .values(
                'id', 'is_opened', 'message', 'is_forwarded', 'status', 'digital_signature',
                'noting__id', 'noting__noting_no', 'noting__filename_doc', 'noting__filename_dak_doc',
                'noting__comment', 'noting__digital_signature', 'noting__status', 'noting__title',
                'noting__user_id', 'noting__selected_user_id', 'noting__role_id',
                from_user_name=F('from_user__username'),
                to_user_name=F('to_user__username')
            )

        # Extract file extensions
        file_doc_extension = os.path.splitext(noting.filename_doc)[1][1:] if noting.filename_doc else ""
        file_dak_doc_extension = os.path.splitext(noting.filename_dak_doc)[1][1:] if noting.filename_dak_doc else ""

        noting_with_extension = {
            'noting': noting,
            'file_doc_extension': file_doc_extension,
            'file_dak_doc_extension': file_dak_doc_extension,
        }
    else:
        noting_with_extension = None
        notings_map = []
    
  
    data = {
        'section': "search_noting_view", 
        'noting_with_extension': noting_with_extension, 
        'notings_map': notings_map,
    }

    return render(request, 'admin/noting.html', data)



@check_session_exists 
def view_noting_map(request, noting_user_map_id): 
    uid = request.session.get('user_id')

    if request.method == 'POST':
        noting_id = request.POST.get('noting_id')
        noting_map_id = request.POST.get('noting_map_id')
        noting_comments = request.POST.get('add_comment')
        digital_sign = request.POST.get('add_digital_sign')
        selected_role = request.POST.get('selected_role')
        selected_user = request.POST.get('selected_roles_users')
          
        # Retrieve the Noting instance
        noting_instance = get_object_or_404(Noting, pk=noting_id)

        # Create the NotingUserMap instance
        NotingUserMap.objects.create(
            noting=noting_instance,
            from_user_id=uid,
            to_user_id=selected_user,
            is_opened=0,
            is_forwarded=0,
            message=noting_comments,
            digital_signature=digital_sign 
        )
        update_noting_forward_value(noting_user_map_id)      
        messages.success(request, 'Noting Forwarded Successfully.') 

    
    if uid is None: 
        return render(request, 'noting.html', {'section': "incoming_noting", 'notings': []})
    
    notings = NotingUserMap.objects \
        .filter(id=noting_user_map_id) \
        .select_related('noting', 'from_user', 'to_user') \
        .values(
            'id', 'is_opened', 'message', 'is_forwarded', 'status',
            'noting__id', 'noting__noting_no', 'noting__filename_doc', 'noting__filename_dak_doc',
            'noting__comment', 'noting__digital_signature', 'noting__status', 'noting__title', 
            'noting__user_id', 'noting__selected_user_id', 'noting__role_id',
            from_user_name=F('from_user__username'),
            to_user_name=F('to_user__username')
        )
    
    # Handling the case where the ID might not exist.
    if not notings.exists():
        return render(request, 'noting.html', {'section': "view_noting_map", 'notings': [], 'error': "No data found"})
    
    # Prepare the data with file extensions
    notings_with_extension = []
    for noting in notings:
        file_doc_extension = os.path.splitext(noting['noting__filename_doc'])[1][1:]  # Extract extension without the dot
        file_dak_doc_extension = os.path.splitext(noting['noting__filename_dak_doc'])[1][1:]  # Extract extension without the dot
        notings_with_extension.append({
            'noting': noting,
            'file_doc_extension': file_doc_extension,
            'file_dak_doc_extension': file_dak_doc_extension,
        })
    
    update_noting_open_value(uid,noting_user_map_id)    
    roles = Role.objects.filter(role_name__in=['co', 'go', 'do', 'hos'])

 
    data = {'section': "view_noting_map", 'notings_with_extension': notings_with_extension, 'roles': roles}  
    return render(request, 'noting.html', data)



def update_noting_open_value(uid,noting_user_map_id): 
    NotingUserMap.objects.filter(id=noting_user_map_id).exclude(from_user_id=uid).update(is_opened=1)

def update_noting_forward_value(noting_user_map_id):     
    NotingUserMap.objects.filter(id=noting_user_map_id).update(is_forwarded=1) 


def get_noting_counts():   
    total = Noting.objects.filter().count()
    forwarded = NotingUserMap.objects.filter().count() 
    corr_count = {'total' : total,'forwarded':forwarded} 
    return corr_count  