from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name') 
      result['StudentNumber'] = request.form.get('StudentNumber')
      # 성별
      result['Gender'] = request.form.get('Gender')
      # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨.
      result['Programing Languague'] = " "
      lst = ["Python", "Java", "HTML", "C++"]
      lst2 = []
      for x in lst:
         if request.form.get(x):
            lst2.append(x)
      result['Programing Languague'] = ', '.join(lst2)
      
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
