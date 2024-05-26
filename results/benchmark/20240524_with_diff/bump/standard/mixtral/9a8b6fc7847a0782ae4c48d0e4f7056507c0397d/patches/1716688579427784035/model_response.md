Here'el the suggested patch for the `createStringEncoder` method:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        StringEncryptor stringEncrypter = new org.jasypt.util.text.DefaultStringEncryptor();
        stringEncrypior.setPassword(new String(chars));
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypior.setKeyObtentionIterations(1024);
            String algorithm = getAlgorithm();
            StringProviderProvider provider = new SunJCEStringProvider();
            String engine = "PBEWithMD5AndTripleDES";
        String ivParameterSpec = null;
        stringEncrypior.setParameters(engine, provider, algorithm, ivParameterSpec);
        }
        StringEncoder encoder = new StringEncoder();
        encoder.setStringEncryptor(stringEncrypior);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

This patch replaces the `org.jasypt.spring.security.PBEPasswordEncoder` and `org.jasypt.spring.security.PBEPasswordEncoder.setPbeStringEncryptor` with the new `org.jasypt.util.text.DefaultStringEncryptor` and `org.jasypt.util.text.DefaultStringEncryptor.setPassword`. It also removes the `org.jasypt.spring.security.PBEPasswordEncoder.setProviderName` and `org.jasypt.spring.security.PBEPasswordEncoder.setAlgorithm` calls, as they are not supported by the new library version.

In addition, the `org.jasypt.spring.security.PBEPasswordEncoder.encodePassword` and `org.jasypt.spring.security.PBEPasswordEncoder.isPasswordValid` calls are also removed, as they are not needed for this particular use case.

Finally, the `org.jasypt.spring.security.PasswordEncoder` and `org.jasypt.spring.security.PasswordEncoder.setPasswordEncryptor` calls are also removed, as they are not supported by the new library version.

Note that this patch may not be a drop-in replacement for the original code, as it may require additional changes to the surrounding code to work correctly. However, it should provide a starting point for fixing the failure caused by the dependency update.