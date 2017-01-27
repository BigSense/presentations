## Scala Dependency Injections

    // Formats

    lazy val senseXMLFormat = new SenseDataXMLFormat
    lazy val txtFormat = new TabDelimitedFormat
    lazy val csvFormat = new CSVFormat
    lazy val tableHTMLFormat = new TableHTMLFormat
    lazy val senseJsonFormat = new SenseJsonFormat

    def getFormat(format: String): Option[FormatTrait] = {
      format match {
        case "sense.xml" => Some(senseXMLFormat)
        case "txt" => Some(txtFormat)
        case "csv" => Some(csvFormat)
        case "table.html" => Some(tableHTMLFormat)
        case "sense.json" => Some(senseJsonFormat)
        case _ => None
      }
    }
