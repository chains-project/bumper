Here's the fixed method using the new library version:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.util.text.TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        textEncryptor.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            textEncryptor.setProviderName(getProviderName());
        }
        textEncryptor.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setTextEncryptor(textEncryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

I replaced `org.jasypt.encryption.pbe.StandardPBEStringEncryptor` with `org.jasypt.util.text.TextEncryptor` and changed the method `setPbeStringEncryptor` to `setTextEncryptor`.