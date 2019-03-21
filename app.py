from flask import Flask, render_template, request, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/request-counter', methods=["GET", "POST", "DELETE"])
def request_counter():
    counters = data_manager.get_statistics()
    counters[request.method] += 1

    data_manager.write_statistics(counters)

    return redirect("/")


@app.route('/statistics')
def show_statistics():
    counters = data_manager.get_statistics()
    return render_template("statistics.html", counters=counters)


if __name__ == '__main__':
    app.run(debug=True)
