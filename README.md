# stubilous
A plain simple Python http stub server inspired by https://github.com/dreamhead/moco

[![Build Status](https://travis-ci.org/CodersOfTheNight/stubilous.svg?branch=master)](https://travis-ci.org/CodersOfTheNight/stubilous)

Installing
==========
`pip install stubilous`

Requirements
============
Tested on Python 2.7, 3.4 and 3.5 versions

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
