Here's a possible patch to fix the error:

```java
import eu.europa.esig.dss.model.DSSException;

// ...

try {
    // Your existing code that uses CertificationPermission
} catch (DSSException e) {
    // Handle the exception appropriately
}
```

This patch imports the `DSSException` class, which is a part of the `dss-common` library that contains the `CertificationPermission` class. By catching this exception, you can handle any issues that may arise when using the `CertificationPermission` class.

Note that this patch assumes that your code is using the `CertificationPermission` class within a try-catch block. If this is not the case, you may need to modify your code accordingly.