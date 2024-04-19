```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new PBEStringEncryptor();
        pbeStringEncryptor.setPassword("mysecretpassword");
    }

    public String encodePassword(String password) {
        return pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(StrongTextEncryptor textEncryptor) {
        pbeStringEncryptor.setAlgorithm(textEncryptor.getAlgorithm());
        pbeStringEncryptor.setProviderName(textEncryptor.getProviderName());
        pbeStringEncryptor.setSaltGenerator(textEncryptor.getSaltGenerator());
        pbeStringEncryptor.setKeyObtentionIterations(textEncryptor.getKeyObtentionIterations());
        pbeStringEncryptor.setPoolSize(textEncryptor.getPoolSize());
        pbeStringEncryptor.setProvider(textEncryptor.getProvider());
        pbeStringEncryptor.setIvGenerator(textEncryptor.getIvGenerator());
        pbeStringEncryptor.setSaltSizeBytes(textEncryptor.getSaltSizeBytes());
        pbeStringEncryptor.setDigest(textEncryptor.getDigest());
        pbeStringEncryptor.setRegisteredName(textEncryptor.getRegisteredName());
        pbeStringEncryptor.setStringOutputType(textEncryptor.getStringOutputType());
        pbeStringEncryptor.setConfig(textEncryptor.getConfig());
    }
}
```