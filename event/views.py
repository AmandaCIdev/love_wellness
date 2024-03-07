from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Event, Reviews
from .forms import ReviewsForm

class EventList(generic.ListView):
    queryset = Event.objects.all()
    template_name = "event/index.html"
    paginate_by = 6

def event_detail(request, slug):
<<<<<<< HEAD
    queryset = Event.objects.filter(slug=slug)
=======
    queryset = Event.objects.filter(status=1)
>>>>>>> c96785c (register, signin, signout, basic styling, change title and head/logo, connect home and about, js file for reviews, event_detail.html creation, add functions to event views)
    event = get_object_or_404(queryset, slug=slug)
    reviews = event.reviews.all().order_by("-created_on")
    review_count = event.reviews.filter(approved=True).count()
    if request.method == "POST":
        print("Received a POST request")
        reviews_form = ReviewsForm(data=request.POST)
        if reviews_form.is_valid():
            review = reviews_form.save(commit=False)
            review.author = request.user
            review.event = event
            review.save()
            messages.add_message(request, messages.SUCCESS, "Your review is submitted and awaiting verification")
    reviews_form = ReviewsForm()

    return render(
            request,
            "event/event_detail.html",
            {"event": event, "reviews": reviews,
            "review_count": review_count, "reviews_form": reviews_form,},
            
    )


def review_edit(request, slug, review_id):
        """
        view to edit comments
        """
        if request.method == "POST":

<<<<<<< HEAD
            queryset = Event.objects.all()
=======
            queryset = Event.objects.filter(status=1)
>>>>>>> c96785c (register, signin, signout, basic styling, change title and head/logo, connect home and about, js file for reviews, event_detail.html creation, add functions to event views)
            event = get_object_or_404(queryset, slug=slug)
            review = get_object_or_404(Reviews, pk=review_id)
            review_form = ReviewsForm(data=request.POST, instance=review)

            if review_form.is_valid() and review.author == request.user:
                review = review_form.save(commit=False)
                review.event = event
                review.approved = False
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating review!')

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
<<<<<<< HEAD
    queryset = Event.objects.all()
=======
    queryset = Event.objects.filter(status=1)
>>>>>>> c96785c (register, signin, signout, basic styling, change title and head/logo, connect home and about, js file for reviews, event_detail.html creation, add functions to event views)
    event = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Reviews, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[slug]))