Sobre
==========
O GDG Pros And Cons é uma aplicação web/mobile para que seja mais efetiva a captação de feedback em tempo real dos encontros mensais do GDG-Sp.
Este repositório trata da implementação server-side utilizado [Google App Engine](https://developers.google.com/appengine/) para Python.
[Meetup GDG-Sp](http://www.meetup.com/GDG-SP/)
[Repositório app Android](https://github.com/cirocosta/gdg-pros-and-cons-android)


Wiki
===========
O [wiki](http://cirocosta.github.io/gdg-pros-and-cons-gae) há de ser elaborado em breve.


Serviços
===========
[Channel API](https://developers.google.com/appengine/docs/python/channel/)
[Cron](https://developers.google.com/appengine/docs/python/config/cron)
[Google Cloud Endpoints](https://developers.google.com/appengine/docs/python/endpoints/)
[Google Cloud Messaging](http://developer.android.com/google/gcm/server.html)


External
============
Faz-se uso da API do [Meetup.com](www.meetup.com) para a obtenção de dados referentes aos encontros do grupo:

- https://api.meetup.com/2/groups?&sign=true&group_urlname=GDG-SP&page=20
- https://api.meetup.com/2/events?&sign=true&group_id=8562442&page=20
