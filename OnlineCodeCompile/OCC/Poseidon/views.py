from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm
import tempfile,subprocess

def compile_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            with tempfile.NamedTemporaryFile(mode='w',suffix='.cpp') as f:
                f.write(code)
                f.flush()
                process = subprocess.Popen(['g++', f.name, '-o', 'a.out'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if process.returncode == 0:
                    process = subprocess.Popen(['./a.out'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    return HttpResponse(stdout.decode().replace('\n','<br>'))
                else:
                    return HttpResponse(stderr.decode())
    else:
        form = CodeForm()
    return render(request, 'compile.html', {'form': form})

