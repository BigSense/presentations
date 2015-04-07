## Tomcat Server (Static Content Servlet)

```
class StaticContentServlet extends HttpServlet {

  override def doGet(req : HttpServletRequest, resp : HttpServletResponse) {

    val resourcePath = "/io/bigsense/web/%s".format(req.getPathInfo.stripPrefix("/"))

    val resource = getClass.getResource(resourcePath)

    if(resource == null) {
      resp.setContentType("text/plain")
      resp.setStatus(HttpServletResponse.SC_NOT_FOUND)
      resp.getWriter.write("Not Found")
      resp.getWriter.close
    }
    else {
      resp.setContentType( getContentType(req.getPathInfo) )
      ByteStreams.copy(getClass.getResourceAsStream(resourcePath), resp.getOutputStream)
      resp.getOutputStream.close
    }
  }
  ...
 ```