from flask import Flask, request
import random, math
app = Flask(__name__)


@app.route('/')
def index():
    f = open("main.html", "r")
    page = f.read()
    return page
@app.route('/display', methods = ['POST'])
def display():
   global x,d,l,y
   if request.method == 'POST':
      x = int(request.form['distance'])
      d = int(request.form['debris_height'])
      l = int(request.form['debris_length'])
      y= int(request.form['debris_relative_height'])

      
      ydis = [y, y+9, y-1, y+7, y-9, y+1, y+7, y+4, y-2, y-1]
      xdis = [x, x+4, x-9, x+4, x-2, x+1, x+8, x+5, x-6, x-1]

      ysum = 0
      for i in ydis:
          ysum += i

      xsum = 0
      for i in xdis:
          xsum += i
  
      ysum = ysum/len(ydis)
      xsum = xsum/len(xdis)
  
      angleChange = ((ysum*x-y*xsum)/x**2)*(1/(1+(y/x)**2))*180*(1/math.pi)
  
      if angleChange > 0:
         result = -(d-y)/x
      else:
         result = y/x
      output = f"{result} degrees for {l+x+1} miles"
   f2 = open("display.html", "r")
   page = f2.read()
   page = page.replace("{output}", output)
   return page
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
