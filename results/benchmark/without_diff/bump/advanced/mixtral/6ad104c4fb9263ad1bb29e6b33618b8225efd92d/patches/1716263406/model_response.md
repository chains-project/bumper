Here's a proposed patch for the client code:
```java
import org.bouncycastle.tls.AlertDescription;
```
Note that I replaced `org.bouncycastle.crypto.tls` with `org.bouncycastle.tls`. This is because the `AlertDescription` class has been moved to the `org.bouncycastle.tls` package in newer versions of the Bouncy Castle library.

Additionally, you might need to update the version of the Bouncy Castle library that you are using. If the updated package import doesn't work, you can try adding the following dependency to your `pom.xml` file:
```xml
<dependency>
    <groupId>org.bouncycastle</groupId>
    <artifactId>bcpkix-jdk15on</artifactId>
    <version>1.70</version>
</dependency>
```
This adds the Bouncy Castle library version 1.70 to your project, which should include the `AlertDescription` class in the `org.bouncycastle.tls` package.