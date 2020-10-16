# 使用Python库ass对字幕作出调整

大多数情况下，字幕异常的小不是因为ass文件中字体设置的过小，而是字幕字体设置好后又用aegisub打开过，这将设置PlayResX和PlayResY两个参数，影响播放器显示字体的大小。在这种情况下，只要删掉这两个参数就可以了。

'''
A sample of ass style key value pair
Style(
        name='Default',
        fontname='Arial',
        fontsize=16.0,
        primary_color=Color(r=0xff, g=0xff, b=0xff, a=0x00),
        secondary_color=Color(r=0xff, g=0xff, b=0xff, a=0x00),
        outline_color=Color(r=0x00, g=0x00, b=0x00, a=0x00),
        back_color=Color(r=0x00, g=0x00, b=0x00, a=0x00),
        bold=False,
        italic=False,
        underline=False,
        strike_out=False,
        scale_x=100.0,
        scale_y=100.0,
        spacing=0.0,
        angle=0.0,
        border_style=1,
        outline=1.0,
        shadow=0.0,
        alignment=2,
        margin_l=10,
        margin_r=10,
        margin_v=10,
        encoding=0
)
'''

## Reference

 - [python-ass](https://github.com/chireiden/python-ass)
