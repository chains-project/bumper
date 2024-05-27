Here's a proposed patch for the client code:
```java
import org.bouncycastle.tls.AlertDescription;
```
Note that the import statement has been changed to use the fully qualified class name `org.bouncycastle.tls.AlertDescription`. This assumes that the required Bouncy Castle library is available on the classpath at runtime.

Additionally, you may need to add the following Maven dependency to your `pom.xml` file if it is not already present:
```xml
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcpkix-jdk15on</artifactId>
    <version>1.69</version>
</dependency>
```
This will ensure that the required Bouncy Castle library is available at runtime.