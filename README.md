# stubilous
A plain simple Python http stub server

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
