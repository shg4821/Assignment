from django import forms
# 폼 컨트롤 정의 클래스


class jusoF(forms.Form):
    state_val = forms.CharField(widget=forms.HiddenInput())
    # 도로명검색어(도로명으로)
    juso = forms.CharField(label='도로명검색어', required=True, widget=forms.TextInput(
        attrs={'placeholder': '도로명검색어', 'style': 'width:200px', 'class': 'form-control'}))
    # 도로명결과 select
    ADDR = (
        ('1', '검색하세요'),
    )
    state = forms.ChoiceField(choices=ADDR, label='검색도로명')
    # 도로명으로 상세도로명
    juso_datail = forms.CharField(label='상세도로명', required=True, widget=forms.TextInput(attrs={'placeholder':'상세도로명 (빌라/아파트동호수)', 'class': 'form-control'}))
    # 내용 텍스트에어리어
    comment = forms.CharField(label='내용', widget=forms.Textarea(
        attrs={'placeholder': '내용', 'class': 'form-control'}))
