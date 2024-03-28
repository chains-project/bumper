Based on the information provided, it seems the issue is caused by a missing symbol import. Here's a patch for the failing method in `AppenderUtils.java`. I am assuming that the missing symbol is `TFastFramedTransport` from the `org.apache.thrift.transport` package.

The error message suggests that the class cannot be found, so I'll make sure the class is properly imported. If the class is already imported and the issue still persists, please provide more context or information.

```java
-  private static void validateThriftTransportFactory(LoggerContext loggerContext, Appender appender) {
+  private static void validateThriftTransportFactory(LoggerContext loggerContext, Appender<ILoggingEvent> appender) {
    if (appender instanceof ThriftAppender) {
-      TFramedTransport.Factory transportFactory = (TFramedTransport.Factory) appender.getParameters().getTransportFactory();
+      TFastFramedTransport.Factory transportFactory = (TFastFramedTransport.Factory) appender.getParameters().getTransportFactory();
    }
  }
```

This patch assumes that the original issue was caused by an incorrect import of `TFramedTransport` instead of `TFastFramedTransport`. This should resolve the "cannot find symbol" error. If the issue is not resolved, please provide more context or information.