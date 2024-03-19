Based on the information provided, it seems the issue is caused by a missing dependency for the `TFastFramedTransport` class. To resolve this issue, you can add the necessary dependency to your project.

If you are using Maven, you can add the following dependency to your `pom.xml`:

```xml
<dependency>
  <groupId>org.apache.thrift</groupId>
  <artifactId>thrift-transport-java</artifactId>
  <version>0.13.0</version>
</dependency>
```

If you are using a different build system, you will need to add the dependency in the appropriate format for that system.

Assuming the rest of the code in the class is correct, the failing method in `AppenderUtils.java` should look something like this:

```java
private static TFramedTransport newFramedTransport(TTransport transport) {
  return new TFastFramedTransport(transport, MAX_FRAME_SIZE, MAX_FRAME_SIZE);
}
```

Make sure to replace any other occurrences of `TFramedTransport` with `TFastFramedTransport` in the rest of the code, as the former is likely deprecated or not included in the version of the library you are using.