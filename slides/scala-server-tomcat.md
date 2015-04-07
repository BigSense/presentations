## Tomcat Server

```
class TomcatServer extends ServerTrait {

  val tomcat = new Tomcat()
  tomcat.setPort(httpPort)
  val tmp = new File(System.getProperty("java.io.tmpdir"))

  val ctx = tomcat.addContext(BigSenseServer.webRoot,tmp.getAbsolutePath)
  Tomcat.addServlet(ctx,"bigsense",new MasterServlet())
  ctx.addServletMapping("/*","bigsense")

  new DBUpdateListener().contextInitialized(null)

  val cCtx = tomcat.addContext(BigSenseServer.contentRoot,tmp.getAbsolutePath)
  Tomcat.addServlet(cCtx,"static",new StaticContentServlet)
  cCtx.addServletMapping("/*","static")
  ...
 ```