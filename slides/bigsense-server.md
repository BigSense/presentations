## Web Applications
- Traditional Tomcat/WAR deployment
- Embedded Jetty
- Embedded Tomcat

```
try {
    config.options("server") match {
      case "tomcat" => new TomcatServer().startServer()
      case "jetty" => new JettyServer().startServer()
      case _ => {
        log.fatal("Unknown server type: %s. (Was expecting tomcat or jetty)")
        System.exit(4)
      }
    }
  }
 ```