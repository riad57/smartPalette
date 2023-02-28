#! /usr/bin/env /home/riad/pycode/test_env/bin/python3
# -*- coding: utf8 -*-

import streamlit as st
from PIL import Image
import kmeans

@st.cache_data
def convert(im, n) :
    im.thumbnail((100, 100))
    data = list(im.getdata())
    pal = set(data)
    pixels = [[i, data.count(i)] for i in pal]
    centers = kmeans.kmeans(pixels, n)
    return centers
    

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    im = Image.open(uploaded_file).convert('RGB')
    st.image(im, caption='Your image')
    nc = st.slider('number of colors', min_value=2, max_value=12, value=6)
    pal = sorted(convert(im, nc))
    if len(pal) > 0 :
        col = st.columns(len(pal))
        for i, j in enumerate(col) :    
            with j :
                hex_val = '#%02x%02x%02x' % tuple(pal[i])
                st.color_picker(hex_val, hex_val)

