Here's a fixed version of the `createStringEncoder` method that uses an alternative way to instantiate `PBEStringEncryptor` since `StandardPBEStringEncryptor` seems to be unavailable:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.PooledPBEStringEncryptor();
        ((org.jasypt.encryption.pbe.PooledPBEStringEncryptor) stringEncrypter).setPoolSize(1);
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PBEPasswordEncoder encoder = new org.jasypt.spring.security.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

This version uses `PooledPBEStringEncryptor` instead of `StandardPBEStringEncryptor` and sets the pool size to 1. This should resolve the "cannot find symbol" error.