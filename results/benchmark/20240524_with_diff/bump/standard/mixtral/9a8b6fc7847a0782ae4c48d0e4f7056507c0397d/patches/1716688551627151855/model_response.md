Here is a possible patch for the given client code:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    org.jasypt.util.text.TextEncryptor stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
    stringEncrypter.setPasswordCharArray(chars);
    if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
        stringEncrypter.setProviderName(getProviderName());
    }
    stringEncrypter.setAlgorithm(getAlgorithm());
    org.jasypt.spring.security3.PBEPasswordEncoder encoder = new org.jasypt.spring.security3.PBEPasswordEncoder();
    encoder.setStringEncryptor(stringEncrypter);
    return encoder;
}
```

This patch uses the new `org.jasypt.spring.security3.PBEPasswordEncoder` class and `org.jasypt.util.text.TextEncryptor` interface introduced in the new library version. It also removes the `try-finally` block since it is not necessary in this case.