# KafkaPyClient
https://zhuanlan.zhihu.com/p/156812909

There are three python lib for kafka:
- kafka-python: The first on the scene, a Pure Python Kafka client with robust documentation and an API 
                that is fairly faithful to the original Java API. This implementation has the most stars on GitHub, 
                the most active development team (by number of committers) but also lacks a connection to the fast C 
                library. I’ll admit that I didn’t spend enough time on this project to judge it well because of this.
- PyKafka: The second implementation chronologically. This library is maintained by Parse.ly a web analytics company 
            that heavily uses both streaming systems and Python. PyKafka’s API is more creative and designed to 
              follow common Python idioms rather than the Java API. PyKafka has both a pure Python implementation 
             and connections to the low-level C library for increased performance.librdkafka
- Confluent-kafka: Is the final implementation chronologically. It is maintained by Confluent, the primary 
              for-profit company that supports and maintains Kafka. This library is the fastest, but also the least 
               accessible from a Python perspective. This implementation is written in CPython extensions, and 
               the documentation is minimal. However, if you are coming from the Java API then this is entirely 
               consistent with that experience, so that documentation probably suffices.

official doc for kafka-python: https://kafka-python.readthedocs.io/en/master/apidoc/modules.html