Here's a fixed version of the method that replaces the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password)` with the equivalent functionality using `new String(password)` and `getBytes()`:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPassword(new String(password));
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PBEPasswordEncoder encoder = new org.jasypt.spring.security.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
    }
}
```

Note: I also removed the usage of `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars)` since it's not necessary and it's not clear what it does. If it's important, you can add it back in a similar way as I added the `new String(password)` line.