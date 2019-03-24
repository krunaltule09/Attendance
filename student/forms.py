from django import forms


class StudentAttendanceForm(forms.Form):
	code=forms.IntegerField(label="code")