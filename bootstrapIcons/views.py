from django.shortcuts import render, redirect
from .models import Bootstrap_icons
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
import time


# Create your views here.

def BSicons(request):
    if not request.user.is_anonymous:
        icons = Bootstrap_icons.objects.all()
        paginator = Paginator(icons, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"icon": icons, "page_obj": page_obj}
        return render(request, "bootstrap/bootstrapicons.html", context)
    return redirect('login-user')


def BSiconsPagination(request):
    if not request.user.is_anonymous:
        icons = Bootstrap_icons.objects.all()
        paginator = Paginator(icons, 100)  # Display 100 icons per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            data = []
            for icon in page_obj:
                data.append({
                    "name": icon.name,
                    "path": icon.path,
                    "category": icon.category,
                    "svgname": icon.svgname
                })
            return JsonResponse({"data": data})
    return redirect('login-user')

@cache_page(60 * 2)
def BSiconsSearch(request):
    if not request.user.is_anonymous:
        query = request.GET.get('search')
        search_terms = query.split() if query else []
        allSearchTag = Bootstrap_icons.objects.all()

        if query is not None and len(query) != 0:
            if search_terms:
                searchedItems = allSearchTag.filter(searchtag__icontains=search_terms[0])  # Using the first search term initially
                for term in search_terms[1:]:  # Remaining search terms
                    searchedItems = searchedItems.filter(searchtag__icontains=term)

            # Measure the execution time of the query
            start_time = time.time()
            results = list(searchedItems)  # Execute the query and fetch results
            end_time = time.time()
            query_time = end_time - start_time
            if query_time == 0:
                query_time = "0.0001"
            else:
                pass
            if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
                data = []
                for icon in results:
                    data.append({
                        "name": icon.name,
                        "path": icon.path,
                        "category": icon.category,
                        "svgname": icon.svgname,
                        "found_searches": len(searchedItems),
                        "found_searches_time": round(query_time, 4),
                    })
                return JsonResponse({"data": data})
            return JsonResponse({"data": None})
        else:
            return JsonResponse({"data": "null"})
    return redirect('login-user')