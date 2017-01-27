## Scala Dependency Injections

    // Actions

    lazy val aggregateAction = new AggregateAction {validator = new AggregateActionValidator}
    lazy val imageAction = new ImageAction {validator = new ImageActionValidator}
    lazy val queryAction = new QueryAction {validator = new QueryActionValidator}
    lazy val sensorAction = new SensorAction {validator = new SensorActionValidator}
    lazy val statusAction = new StatusAction {validator = new StatusActionValidator}

    def getAction(action: String): Option[ActionTrait] = {
      action match {
        case "Aggregate" => Some(aggregateAction)
        case "Image" => Some(imageAction)
        case "Query" => Some(queryAction)
        case "Sensor" => Some(sensorAction)
        case "Status" => Some(statusAction)
        case _ => None
      }
    }
