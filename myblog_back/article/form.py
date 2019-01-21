from django import forms






class CateFrom(forms.Form):
    name = forms.CharField(max_length=20,
                           required=True,
                           error_messages={
                               'required': '栏目名称不能为空'
                           })
    alias = forms.CharField(max_length=20)
    fid = forms.CharField(max_length=20,
                           required=True,
                           error_messages={
                               'required': '父节点不能为空'})
