# Roboto Sans

Every time while enumerating a web page, it is a good practice to taka a look at the *robots.txt* file.

http://saturn.picoctf.net:65352/robots.txt:

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

We can see, that the gibberish inside looks like base64 code, so using CyberChef we can decode:

ZmxhZzEudHh0 from base64: flag1.txt  

anMvbXlmaWxlLnR4dA== from base64: **js/myfile.txt**

Now go to url http://saturn.picoctf.net:65352/js/myfile.txt for a flag.