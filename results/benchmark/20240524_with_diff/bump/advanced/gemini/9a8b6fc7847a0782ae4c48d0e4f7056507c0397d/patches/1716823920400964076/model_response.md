```java
import org.jasypt.encryption.pbe.StandardPBEByteEncryptor;
import org.jasypt.encryption.pbe.config.PBEConfig;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEByteEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEByteEncryptor();
        PBEConfig config = new PBEConfig();
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations(1000);
        encryptor.setConfig(config);
    }

    public String encodePassword(String password, Object salt) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.decrypt(encPass).equals(rawPass);
    }
}
```