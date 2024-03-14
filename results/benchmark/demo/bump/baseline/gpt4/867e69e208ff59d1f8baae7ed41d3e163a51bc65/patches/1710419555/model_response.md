It seems like the error is due to the missing Thrift library in your project's classpath. You need to make sure that the Thrift library is correctly added to your project dependencies. If you are using Maven, you can add the following dependency to your pom.xml file: 

```xml
<dependency>
    <groupId>org.apache.thrift</groupId>
    <artifactId>libthrift</artifactId>
    <version>0.12.0</version>
</dependency>
```

Once the library is correctly added, the import statement should work fine:

```java
import org.apache.thrift.transport.TFramedTransport;
```