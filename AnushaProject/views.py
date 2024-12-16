from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    params = {'Name':'Anusha', 'Place':'India', 'Age':33}
    return render(request, 'index.html', params)

# def removepunc(request):
#     return HttpResponse('removepunc 12345')
#
# def removeCapital(request):
#     return HttpResponse('removed Capital Letters')
#
# def removeSpace(request):
#     return HttpResponse('removed Space')
#
# def characterCount(request):
#     return HttpResponse('removed Character Count')
#
# def newlineremover(request):
#     return HttpResponse('removed new Line')



def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    convertUppertoLower = request.GET.get('convertUppertoLower', 'off')
    add22toOriginalString = request.GET.get('add22toOriginalString', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (removeExtraSpace == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (removeExtraLines == "on"):
        newline = '''\n'''
        analyzed = ""
        for char in djtext:
            if char not in newline:
                analyzed = analyzed + char
        params = {'purpose':'Remove extra line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    #
    # elif (convertUppertoLower == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         analyzed = analyzed + char.lower()
    #     params = {'purpose': 'Convert upper to Lower', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)
    #
    # elif (addition22 == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         analyzed = analyzed + char.lower()
    #     params = {'purpose': 'MathematicalCalculation', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)

    elif (add22toOriginalString == "on"):
        # Given string
        # Extract the numeric part from the string
        numeric_part = int(''.join(filter(str.isdigit, djtext)))
        # Add 22 to the numeric part
        new_numeric_part = numeric_part + 22

        # Combine the non-numeric part with the new numeric part
        analyzed = ''.join(filter(str.isalpha, djtext)) + str(new_numeric_part)
        params = {'purpose':'Add 22 to Original String', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")



