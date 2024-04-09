It seems that the `CertificationPermission` class is not available in the `org.openpdfsign` package. This could be due to a missing dependency or a version conflict.

To fix this issue, you can try adding the following dependency to your `pom.xml` file (if you're using Maven):
```xml
<dependency>
    <groupId>org.openpdfsign</groupId>
    <artifactId>openpdfsign-core</artifactId>
    <version>1.4.0</version>
</dependency>
```
Alternatively, you can also try updating the version of the `openpdfsign-core` dependency to a newer version that includes the `CertificationPermission` class.

Once you've updated the dependency, you should be able to compile the code without any issues.