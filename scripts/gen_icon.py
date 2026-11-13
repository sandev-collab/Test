import random, os

r = random.Random()
col = lambda: "#%06X" % r.randint(0, 0xFFFFFF)
shapes = [
    "M54,24 a30,30 0 1,0 0.01,0 z",
    "M54,18 L90,54 L54,90 L18,54 z",
    "M30,30 H78 V78 H30 z",
]
xml = f'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="{col()}" android:pathData="M0,0H108V108H0z"/>
    <path android:fillColor="{col()}" android:pathData="{r.choice(shapes)}"/>
</vector>
'''
d = "app/src/main/res/drawable"
os.makedirs(d, exist_ok=True)
open(d + "/ic_launcher.xml", "w").write(xml)
print("Icon generated")