from django.shortcuts import render, get_object_or_404
from .models import Review
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import tensorflow as tf

def index(request):   
    review_class = ''
    review_text = ''
    review_stars = ''
    if request.method == 'POST':
        review_text = request.POST['review']
        loaded_model = tf.keras.models.load_model('export_model')
        review_class = loaded_model.predict([review_text])[0][0]>=0.5
        loaded_model1 = tf.keras.models.load_model('export_model1')
        review_stars = int(loaded_model1.predict([review_text])[0][0] + (0.5))
        print(review_class)
    context = {'review_class' : review_class,
               'review_text' : review_text,
               'review_stars': review_stars
               }
    return render(request, 'review/index.html', context)