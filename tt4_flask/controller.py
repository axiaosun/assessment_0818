#!/usr/bin/env python3

from flask import Flask, render_template,request,session,redirect
import json
import requests
import model
import sqlite3
import operator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bruhhh'

@app.route('/terminal')
def menu():
    return render_template('index.html')

@app.route('/terminal/register', methods=['GET','POST']) #tells you which methods are accepted
def create_account():
	if request.method =='GET':
		return render_template('create_account.html')
	else:
		submitted_username = request.form['username']
		submitted_password = request.form['password']
		submitted_balance = request.form['balance']
		model.create(submitted_username,submitted_password,submitted_balance)
		return redirect('/terminal/login')

@app.route('/terminal/login',methods=['GET','POST'])
def login():
	if request.method =='GET':
		return render_template('log_in.html')
	else:
		submitted_username = request.form['username']
		submitted_password = request.form['password']
		if model.log_in(submitted_username,submitted_password):
			session['username'] = submitted_username
			session['password'] = submitted_password
			return redirect('/terminal/mainmenu')
		else:
			return redirect('/terminal/login')
	return ''' 
	<form action = "/terminal/login" method='POST'>
	<p><input type = text name = username></p>
	<p><input type = text name = password></p>
	<p><input type = submit value = Login></p>
	</form>
	'''

@app.route('/terminal/leaderboard', methods=['GET', 'POST'])
def leaderboard():
	if request.method =='GET':
		return render_template('log_in.html')
	else:
		submitted_username = request.form['username']
		submitted_password = request.form['password']
		if submitted_username == 'admin' and submitted_password == 'bruhhh':
			userlist = model.getUser()
			return_list = model.calculateLeaderBoard(userlist) #list of tuples
			return_list.sort(reverse = True, key = operator.itemgetter(1))
			return render_template('leaderboard.html',return_list=return_list)
		else:
			return redirect('/terminal')

@app.route('/terminal/mainmenu')
def main_menu():
    return render_template('main_menu.html')

@app.route('/terminal/quote', methods=['GET','POST'])
def quote():
    if request.method == 'GET':
        return render_template('quote.html')
    else:
        submitted_symbol = request.form['ticker_symbol']
        result = model.quote_last_price(submitted_symbol)
        return render_template('quote.html',result=result)

@app.route('/terminal/lookup', methods=['GET','POST'])
def lookup():
    if request.method == 'GET':
        return render_template('lookup.html')
    else:
        submitted_company_name = request.form['company_name']
        result = model.lookup_ticker_symbol(submitted_company_name)
        return render_template('lookup.html',result=result)

@app.route('/terminal/account')		
def check_balance():
	result = model.get_user_balance(session['username'])
	result = "${0:.2f}".format(result)
	return render_template('account.html',result=result)

@app.route('/terminal/trade', methods=['GET','POST'])
def trade():
	if request.method == 'GET':
		return render_template('trade.html')
	else:
		submitted_ticker_symbol = request.form['ticker_symbol']
		submitted_trade_volume = request.form['trade_volume']
		submitted_order_type = request.form['order_type']
		if submitted_order_type == 'Buy':
			#calculate , display confirmation message with preview of trade, and execute if yes selected
			(confirmation, return_list) = model.buy(session['username'],submitted_ticker_symbol,submitted_trade_volume)
			if confirmation:
				model.buy_db(return_list)
			else:
				pass
				#User doesn't have enough balance
		else:
			#result = model.sell()
			(confirmation, return_list) = model.sell(session['username'],submitted_ticker_symbol,submitted_trade_volume)
			if confirmation:
				model.sell_db(return_list)
			else:
				pass
		return render_template('trade.html')

@app.route('/terminal/portfolio')
def portfolio():
	result2 = model.calculateHoldings_byTicker(session['username'])  #value of current holdings based on last price by ticker
	result3 = model.get_user_balance(session['username'])  #cash balance
	result1 = model.calculateHoldings(session['username']) + result3 #value of current holdings based on last price + cash balance
	result4 = model.calculateHoldings(session['username']) - model.calculateHistory(session['username'])
	result1 = "${0:.2f}".format(result1)
	result3 = "${0:.2f}".format(result3)
	result4 = "${0:.2f}".format(result4)
	return render_template('portfolio.html', result1=result1, result2=result2, result3=result3, result4=result4)
	
@app.route('/terminal/logout', methods=['GET'])
def logout():
	if session:
		session.clear()
	return redirect('/terminal')


app.run(debug=True)
