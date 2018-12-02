from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        searchContent = request.form['searchContent']
        print(searchContent)
    return render_template("index.html")


@app.route('/result', methods =['GET','POST'])
def result():
    if request.method == 'POST':
        searchContent = request.form['searchContent']
        print(searchContent)
        selectedLink = request.args.get('discuss')
        print(selectedLink)
    problems = [
        {
            'title': '3sum problem',
            'tags': ['tag1', 'tag2'],
            'difficulty': 'hard',
            'recommendations': [
                {'title': 'integer to english words', 'link': 'https://leetcode.com/problems/integer-to-english-words/'},
                {'title': 'integer to english words', 'link': 'https://leetcode.com/problems/integer-to-english-words/'},
            ],
            'discussions': [
                {'discussion_title': 'test discussion', 'url': 'https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand'},
                {'discussion_title': 'test discussion', 'url': 'https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand'},
                {'discussion_title': 'test discussion', 'url': 'https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand'},
            ],
        },
        {
            'title': '3sum problem',
            'tags': ['tag1', 'tag2'],
            'difficulty': 'hard',
            'discussions': [
                {'discussion_title': 'test discussion', 'url': 'https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand'},
            ],
        },
        {
            'title': '3sum problem',
            'tags': ['tag1', 'tag2'],
            'difficulty': 'hard',
            'discussions': [
                {'discussion_title': 'test discussion', 'url': 'https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand'},
            ],
        },
    ]
    return render_template("result.html", problems = problems)

if __name__ == '__main__':

    app.run(debug=True)
