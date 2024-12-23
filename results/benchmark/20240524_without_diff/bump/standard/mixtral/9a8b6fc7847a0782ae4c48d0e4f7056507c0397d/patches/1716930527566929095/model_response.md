Here's a fixed version of the code that replaces the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password)` with an alternative implementation using `java.util.Arrays.fill`:

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
        Arrays.fill(password, (byte) 0); // clear the password
        Arrays.fill(chars, '\u0000'); // clear the char array
    }
}
```

Note that this implementation clears the `password` and `chars` arrays using `Arrays.fill` instead of the removed `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble` method. This should prevent any potential security issues caused by leaving sensitive data in memory.