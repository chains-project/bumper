It seems that the `CertificationPermission` class is not available in the `org.openpdfsign` package. This could be due to a missing dependency or a version conflict.

To fix this issue, you can try adding the following dependency to your `pom.xml` file (if you're using Maven):
```xml
<dependency>
    <groupId>org.openpdfsign</groupId>
    <artifactId>openpdfsign-core</artifactId>
    <version>1.4.0</version>
</dependency>
```
Alternatively, you can try importing the `CertificationPermission` class from the `java.security` package:
```java
import java.security.CertificationPermission;
```
If you're still encountering issues, you may need to update the version of the `openpdfsign` library you're using, or try using a different library for PDF signing.