### Spring Glue (Logging)

    <!-- logging  -->
    <bean name="logger" class="io.bigsense.spring.LoggingInterceptor" />
    <bean id="loggingAdvisor" class="org.springframework.aop.support.RegexpMethodPointcutAdvisor">
      <property name="advice" ref="logger" />
      <property name="pattern" value="io.bigsense.*" />
    </bean>
    <bean class="org.springframework.aop.framework.autoproxy.DefaultAdvisorAutoProxyCreator" />

