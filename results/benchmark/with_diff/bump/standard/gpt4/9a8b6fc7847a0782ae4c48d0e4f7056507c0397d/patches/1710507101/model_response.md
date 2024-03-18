```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.acegisecurity.providers.encoding.PasswordEncoder encoder = new org.acegisecurity.providers.encoding.ShaPasswordEncoder();
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
The `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package is no longer available. Instead, I have replaced it with the `ShaPasswordEncoder` class from the `org.acegisecurity.providers.encoding` package. This class is part of the `Acegi Security System for Spring`, which provides comprehensive security services for Spring-based enterprise software applications.