## Jetty Server

```
class JettyServer extends ServerTrait {

  val server = new Server()
  val connector = new ServerConnector(server)
  connector.setPort(httpPort)
  server.setConnectors(Array(connector))

  val context = new ServletContextHandler()
  context.setContextPath(BigSenseServer.webRoot)
  context.addServlet(new MasterServlet().getClass, "/*")
  context.addEventListener(new DBUpdateListener())

  val fileContext = new WebAppContext()
  fileContext.setContextPath(BigSenseServer.contentRoot)
  fileContext.setResourceBase(BigSenseServer.getClass.getResource("/io/bigsense/web").toExternalForm)

  val handlers = new HandlerCollection()
  handlers.setHandlers(Array( fileContext, context, new DefaultHandler()))
  server.setHandler(handlers)
  ...
 ```