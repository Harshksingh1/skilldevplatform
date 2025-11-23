from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Skill, SkillCategory


def skill_list(request):
    """List all skills"""
    skills = Skill.objects.filter(is_active=True)
    categories = SkillCategory.objects.filter(is_active=True)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        skills = skills.filter(category_id=category_id)
    
    # Search
    query = request.GET.get('q')
    if query:
        skills = skills.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    # Filter by difficulty
    difficulty = request.GET.get('difficulty')
    if difficulty:
        skills = skills.filter(difficulty_level=difficulty)
    
    context = {
        'skills': skills,
        'categories': categories,
        'current_category': category_id,
        'current_difficulty': difficulty,
        'search_query': query,
    }
    return render(request, 'skills/skill_list.html', context)


def skill_detail(request, pk):
    """Detail view for a skill"""
    skill = get_object_or_404(Skill, pk=pk, is_active=True)
    related_skills = Skill.objects.filter(category=skill.category, is_active=True).exclude(pk=pk)[:4]
    
    context = {
        'skill': skill,
        'related_skills': related_skills,
    }
    return render(request, 'skills/skill_detail.html', context)
