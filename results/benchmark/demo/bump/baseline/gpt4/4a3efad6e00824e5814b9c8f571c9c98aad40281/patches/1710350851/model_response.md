The error message indicates that the compiler is unable to find the symbol 'CertificationPermission' in the package 'eu.europa.esig.dss.pades'. This could be due to a number of reasons such as:

1. The class 'CertificationPermission' does not exist in the package 'eu.europa.esig.dss.pades'.
2. The package 'eu.europa.esig.dss.pades' does not exist.
3. The class 'CertificationPermission' is not public or has been removed in an update of the library.

Without knowing the exact reason, it's hard to provide a definitive fix. However, assuming that the 'CertificationPermission' class has been moved to a different package in an updated version of the library, you could try importing it from its new location. 

If the 'CertificationPermission' class has been removed or replaced, you will need to find an alternative way to achieve the same functionality. This could involve using a different class or method from the library, or implementing the functionality yourself.

Here is a general patch that could fix the issue, but it will depend on the specifics of your situation:

```java
  import eu.europa.esig.dss.pades.signature.PAdESSignatureParameters;
  import eu.europa.esig.dss.model.pades.SignatureImageParameters.VisualSignatureAlignmentHorizontal;
```

In this patch, I replaced the 'CertificationPermission' import with the 'PAdESSignatureParameters' and 'VisualSignatureAlignmentHorizontal' imports. These classes might provide similar functionality to the 'CertificationPermission' class. However, you will need to adjust your code to use these classes instead. 

Please note that you might need to adjust this patch based on the actual changes in the library and the specifics of your code.