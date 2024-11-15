```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("password");
    }

    public String encodePassword(String password) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor encryptor) {
        this.encryptor = encryptor;
    }

    public void setTextEncryptor(StrongTextEncryptor textEncryptor) {
        encryptor.setAlgorithm(textEncryptor.getAlgorithm());
        encryptor.setSaltGenerator(textEncryptor.getSaltGenerator());
        encryptor.setKeyObtentionIterations(textEncryptor.getKeyObtentionIterations());
        encryptor.setIvGenerator(textEncryptor.getIvGenerator());
        encryptor.setProviderName(textEncryptor.getProviderName());
        encryptor.setProvider(textEncryptor.getProvider());
        encryptor.setStringOutputType(textEncryptor.getStringOutputType());
    }
}
```