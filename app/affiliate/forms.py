# from django import forms
# from .models import Comment
# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ['name','email', 'comment']
#         labels = {'name':'enter name', 'email':'enter valid email', 'comment':'enter Comment'}
#         error_messages = {

#             'name':{'required':'name is required'},
#             'email':{'required':'email is required'},
#             'comment':{'required':'Commnet is required','max_length':'100'}
#         }

#         widgets = {
#             'name':forms.TextInput(attrs={'class':'email-field'}),
#             'email':forms.EmailInput(attrs={'class':'email-field'}),

#             'comment':forms.Textarea(attrs={'class':'email-field', 'cols':70, 'placeholder':'Enter Your Comment...'})

#         }

