Here's the fixed version of the method using `java.util.Base64` to replace the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password)`:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = new String(java.util.Base64.getDecoder().decode(new String(password))).toCharArray();
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PBEPasswordEncoder encoder = new org.jasypt.spring.security.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        java.util.Arrays.fill(password, (byte) 0);
        java.util.Arrays.fill(chars, '0');
    }
}
```

This code assumes that the `lookupPasswordFromKeyStore()` method returns a base64 encoded password. If that's not the case, you might need to modify the code accordingly. I also added scrambling of the `password` and `chars` arrays in the `finally` block using `java.util.Arrays.fill()`.