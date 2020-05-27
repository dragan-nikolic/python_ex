from selene.api import *

browser.open_url('https://todomvc4tasj.herokuapp.com')
s("#new-todo").should(be.blank)
s("#new-todo").set_value(1).press_enter()
ss("#todo-list>li").should(have.exact_texts("1"))