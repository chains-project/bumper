Here's a possible patch for the failing client code. This solution adds a Maven dependency for Bouncy Castle library to the project's `pom.xml` file.

First, add the following dependency to the `<dependencies>` section of your `pom.xml` file:
```xml
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcpkix-jdk15on</artifactId>
    <version>1.71</version>
</dependency>
```

Then, you can keep the existing Java code unchanged:
```java
import org.bouncycastle.crypto.tls.AlertDescription;

// existing code...
```

This solution assumes that the client code is using Maven as a build tool. If it's not the case, you might need to adjust the solution accordingly.