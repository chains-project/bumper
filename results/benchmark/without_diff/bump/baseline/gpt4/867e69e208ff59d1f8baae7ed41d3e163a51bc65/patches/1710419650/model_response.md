It seems like the library that contains the class TFramedTransport is missing from your classpath. You need to include the Apache Thrift library in your project dependencies. 

If you are using Maven, you can include it in your pom.xml file like this:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.thrift</groupId>
        <artifactId>libthrift</artifactId>
        <version>0.12.0</version>
    </dependency>
</dependencies>
```

After adding the dependency, your import statement should work:

```java
import org.apache.thrift.transport.TFramedTransport;
```

Please note that the version of the library might vary. Make sure to use the version that is compatible with your project.