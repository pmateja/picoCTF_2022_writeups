# Search source

This one is really basic: go to url http://saturn.picoctf.net:58133/ and do some digging in page sources. 

Flag is in: http://saturn.picoctf.net:58133/css/style.css. As you already know the flag pattern (picoCTF{.*}), you can find it in no time:

```css

}
/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8} **/
 .carousel-indicators li {
     width: 20px;
     height: 20px;
     border-radius: 11px;
     background-color: #070000;
}
```