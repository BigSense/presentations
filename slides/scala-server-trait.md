## BigSense Server 

```
trait ServerTrait {

  lazy val httpPort = BigSenseServer.config.options("httpPort").toInt

  def startServer()
  def stopServer()

}
 ```