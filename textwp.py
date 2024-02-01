import textwrap
txt="""The textwrap module offers tools to format and wrap plain text within a specified width, enhancing readability and visual appeal."""
    
txtw=textwrap.wrap(txt,width=60)
for i in txtw:
    print(i)