flask run

py.test -sv

py.test -sv
py.test --cov --cov-report html .
py.test --cov-report term-missing --cov=rentomatic
