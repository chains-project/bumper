```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private final PBEStringEncryptor pbeStringEncryptor;
    private final PasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder(PBEStringEncryptor pbeStringEncryptor, PasswordEncryptor passwordEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
        this.passwordEncryptor = passwordEncryptor;
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor.setAlgorithm(pbeStringEncryptor.getAlgorithm());
        this.pbeStringEncryptor.setPassword(pbeStringEncryptor.getPassword());
        this.pbeStringEncryptor.setSaltGenerator(pbeStringEncryptor.getSaltGenerator());
        this.pbeStringEncryptor.setPoolSize(pbeStringEncryptor.getPoolSize());
        this.pbeStringEncryptor.setIvGenerator(pbeStringEncryptor.getIvGenerator());
        this.pbeStringEncryptor.setStringOutputType(pbeStringEncryptor.getStringOutputType());
        this.pbeStringEncryptor.setProviderName(pbeStringEncryptor.getProviderName());
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.pbeStringEncryptor.setAlgorithm(textEncryptor.getAlgorithm());
        this.pbeStringEncryptor.setPassword(textEncryptor.getSecretKey());
        this.pbeStringEncryptor.setSaltGenerator(textEncryptor.getSaltGenerator());
        this.pbeStringEncryptor.setPoolSize(textEncryptor.getPoolSize());
        this.pbeStringEncryptor.setIvGenerator(textEncryptor.getIvGenerator());
        this.pbeStringEncryptor.setStringOutputType(textEncryptor.getStringOutputType());
        this.pbeStringEncryptor.setProviderName(textEncryptor.getProviderName());
    }
}
```