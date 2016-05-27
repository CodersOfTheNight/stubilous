# stubilous
A plain simple Python http stub server
[![Build Status](https://travis-ci.org/CodersOfTheNight/stubilous.svg?branch=master)](https://travis-ci.org/CodersOfTheNight/stubilous)

Installing
==========
`pip install stubilous`

Requirements
============
Python 3.5+ version

Example config
==============
```yaml
---
server:
  port: 80
  host: localhost
  routes:
      - desc: A test route
        method: GET
        path: /test
        body: Hello!
        status: 200
      - desc: Advanced route
        method: GET
        path: /test/<name>
        body: Hello {{name}}!
        status: 200
```

How to use it
=============
Launch `python -m stubilous --config example.yaml`
