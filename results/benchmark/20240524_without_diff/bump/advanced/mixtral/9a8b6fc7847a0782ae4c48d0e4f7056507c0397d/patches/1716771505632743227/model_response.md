Here's the fixed version of the failing method:
```java
import org.jasypt.util.password.ConfigurablePasswordEncoder;

import java.util.Locale;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private ConfigurablePasswordEncoder passwordEncoder;

    @Override
    public String encode(CharSequence rawPassword) {
        if (passwordEncoder == null) {
            passwordEncoder = new ConfigurablePasswordEncoder("MD5");
        }
        return passwordEncoder.encodePassword(rawPassword.toString(), null);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncoder.matches(rawPassword, encodedPassword);
    }

    @Override
    public boolean upgradeEncoding(String encodedPassword) {
        return false;
    }

    public void setEncodeAlgorithm(String encodeAlgorithm) {
        if (passwordEncoder == null) {
            passwordEncoder = new ConfigurablePasswordEncoder(encodeAlgorithm);
        } else {
            passwordEncoder.setAlgorithm(encodeAlgorithm);
        }
    }

    public void setTruncateOverlongPasswords(boolean truncateOverlongPasswords) {
        passwordEncoder.setTruncateOverlongPasswords(truncateOverlongPasswords);
    }

    public void setStringOutputType(String stringOutputType) {
        passwordEncoder.setStringOutputType(stringOutputType);
    }

    public void setEncodeHashAsBase64(boolean encodeHashAsBase64) {
        passwordEncoder.setEncodeHashAsBase64(encodeHashAsBase64);
    }

    public void setCharEncoding(String charEncoding) {
        passwordEncoder.setCharEncoding(charEncoding);
    }

    public void setSaltGenerator(org.jasypt.salt.SaltGenerator saltGenerator) {
        passwordEncoder.setSaltGenerator(saltGenerator);
    }

    public void setIterationCount(int iterationCount) {
        passwordEncoder.setIterationCount(iterationCount);
    }
}
```
In this fixed version, I replaced the non-existent `org.jasypt.spring.security.PasswordEncoder` with `org.jasypt.util.password.ConfigurablePasswordEncoder` from the `jasypt` library.

The `encode`, `matches`, `upgradeEncoding` methods were updated accordingly.

The `setEncodeAlgorithm`, `setTruncateOverlongPasswords`, `setStringOutputType`, `setEncodeHashAsBase64`, `setCharEncoding`, `setSaltGenerator`, `setIterationCount` methods were added to configure the new `ConfigurablePasswordEncoder`.