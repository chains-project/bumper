```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor stringEncryptor;
    private final ConfigurablePasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        stringEncryptor = new StandardPBEStringEncryptor();
        passwordEncryptor = new ConfigurablePasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        passwordEncryptor.setStringEncryptor(stringEncryptor);
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        passwordEncryptor.setStringEncryptor(stringEncryptor);
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor pbeStringEncryptor) {
        stringEncryptor.setPassword(pbeStringEncryptor.getPassword());
        stringEncryptor.setAlgorithm(pbeStringEncryptor.getAlgorithm());
        stringEncryptor.setKeyObtentionIterations(pbeStringEncryptor.getKeyObtentionIterations());
        stringEncryptor.setPoolSize(pbeStringEncryptor.getPoolSize());
        stringEncryptor.setProviderName(pbeStringEncryptor.getProviderName());
        stringEncryptor.setSaltGenerator(pbeStringEncryptor.getSaltGenerator());
        stringEncryptor.setStringOutputType(pbeStringEncryptor.getStringOutputType());
    }

    public void setTextEncryptor(StandardPBEStringEncryptor textEncryptor) {
        setPbeStringEncryptor(textEncryptor);
    }
}
```