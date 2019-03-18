from mysite import site

if __name__ == "__main__" :
    site.app.run(debug=True, host='0.0.0.0', port=80)