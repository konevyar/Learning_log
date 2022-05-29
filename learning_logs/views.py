from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    """Home page."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """List of topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """All entries in one selected topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic.owner, request)
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Creating new topic."""
    if request.method != 'POST':
        # If user sent blank form, he'll get blank form in return
        form = TopicForm()
    else:
        # If user sent filled form, data will be processed
        form = TopicForm(data=request.POST)
        if form.is_valid(): # Checking required fields
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    
    # Return of blank form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry on selected topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic.owner, request)
    
    if request.method != 'POST':
        # If user sent blank form, he'll get blank form in return
        form = EntryForm()
    else:
        # If user sent filled form, data will be processed
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Creating entry without saving in database
            new_entry = form.save(commit=False)
            # Connection with Topic, received earlier
            new_entry.topic = topic
            # Saving entry with link to the topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Output an empty form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Editing of entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic.owner, request)
    
    if request.method != 'POST':
        # Initial query; form is filled with the data of the current record
        form = EntryForm(instance=entry)
    else:
        # Sending POST; processing entered data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(owner, request):
    """Checking owner of the topic."""
    if owner != request.user:
        raise Http404

