It seems that the `CertificationPermission` class is not available in the `org.openpdfsign` package. This could be due to a missing dependency or a version conflict.

To resolve this issue, you can try adding the following dependency to your `pom.xml` file (if you're using Maven) or your `build.gradle` file (if you're using Gradle):
```xml
<dependency>
    <groupId>org.openpdfsign</groupId>
    <artifactId>openpdfsign-core</artifactId>
    <version>1.0.0</version>
</dependency>
```
Alternatively, you can also try importing the `CertificationPermission` class from the `java.security` package, like this:
```java
import java.security.CertificationPermission;
```
This should allow you to use the `CertificationPermission` class in your code without any issues.