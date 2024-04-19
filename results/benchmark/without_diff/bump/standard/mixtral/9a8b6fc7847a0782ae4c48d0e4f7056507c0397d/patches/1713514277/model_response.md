Here's a fixed version of the code that removes the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);`:

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
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        // no need to scramble password here
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
Note: The `scramble` method is only called on the `chars` array, so it's safe to remove it from the `password` array.