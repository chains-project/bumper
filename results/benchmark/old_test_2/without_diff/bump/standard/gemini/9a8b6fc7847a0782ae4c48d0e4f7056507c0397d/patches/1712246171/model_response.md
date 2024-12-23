```java
import it.geosolutions.geostore.core.security.password.SecurityUtils;
import it.geosolutions.geostore.core.security.password.PBEPasswordEncoder;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.springframework.security.providers.encoding.PasswordEncoder;

@java.lang.Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = SecurityUtils.toChars(password);
    try {
        StandardPBEStringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        PBEPasswordEncoder encoder = new PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        SecurityUtils.scramble(password);
        SecurityUtils.scramble(chars);
    }
}
```