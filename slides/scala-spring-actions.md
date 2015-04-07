    ## Spring Glue (Actions)

    <!-- Actions -->

	<bean id="BaseAction" name="BaseAction" class="io.bigsense.action.ActionTrait" abstract="true">
		<property name="dbHandler" ref="serviceDataHandler" />
	</bean>

	<bean id="ActionSensor" name="ActionSensor" class="io.bigsense.action.SensorAction" parent="BaseAction">
		<property name="validator" ref="SensorActionValidator" />	
	</bean>
	
	<bean id="ActionQuery" name="ActionQuery" class="io.bigsense.action.QueryAction" parent="BaseAction">
		<property name="validator" ref="QueryActionValidator" />
	</bean>
	
	<bean id="ActionStatus" name="ActionStatus" class="io.bigsense.action.StatusAction" parent="BaseAction">
		<property name="validator" ref="StatusActionValidator" />
	</bean>

	<bean id="ActionAggregate" name="ActionAggregate" class="io.bigsense.action.AggregateAction" parent="BaseAction">
		<property name="validator" ref="AggregateActionValidator" />
	</bean>
	
	<bean id="ActionImage" name="ActionImage" class="io.bigsense.action.ImageAction" parent="BaseAction">
		<property name="validator" ref="ImageActionValidator" />
