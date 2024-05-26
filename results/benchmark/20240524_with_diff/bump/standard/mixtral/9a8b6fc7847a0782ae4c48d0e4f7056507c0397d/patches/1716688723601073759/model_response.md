Here is the updated code to fix the error:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypeter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes are:

1. Replace `new org.jasypt.spring.security.PBEPasswordEncoder()` with `new org.jasypt.spring.security.PasswordEncoder()`.
2. Replace `encoder.setPbeStringEncryptor(stringEncrypter)` with `encoder.setPasswordEncryptor(stringEncrypter)`.

The reason for these changes is that the `PBEPasswordEncoder` class has been removed in the new version of the library and its functionality has been absorbed into the `PasswordEncoder` class.