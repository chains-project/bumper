```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

import org.springframework.security.authentication.encoding.PasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;
    private TextEncryptor textEncryptor;

    // -- public PBEPasswordEncoder org.jasypt.spring.security.PBEPasswordEncoder()

    // -- public java.lang.String org.jasypt.spring.security.PBEPasswordEncoder.encodePassword(java.lang.String,java.lang.Object)

    // -- public bool org.jasypt.spring.security.PBEPasswordEncoder.isPasswordValid(java.lang.String,java.lang.String,java.lang.Object)

    // -- public void org.jasypt.spring.security.PBEPasswordEncoder.setPbeStringEncryptor(org.jasypt.encryption.pbe.PBEStringEncryptor)

    // -- public void org.jasypt.spring.security.PBEPasswordEncoder.setTextEncryptor(org.jasypt.util.text.TextEncryptor)

    // -- public PasswordEncoder org.jasypt.spring.security.PasswordEncoder()

    // -- public java.lang.String org.jasypt.spring.security.PasswordEncoder.encodePassword(java.lang.String,java.lang.Object)

    // -- public bool org.jasypt.spring.security.PasswordEncoder.isPasswordValid(java.lang.String,java.lang.String,java.lang.Object)

    // -- public void org.jasypt.spring.security.PasswordEncoder.setPasswordEncryptor(org.jasypt.util.password.PasswordEncryptor)

    // -- public void org.jasypt.spring.security.PasswordEncoder.setStringDigester(org.jasypt.digest.StringDigester)

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public String encodePassword(String rawPass, Object salt) {
        return pbeStringEncryptor.encrypt(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return pbeStringEncryptor.decrypt(encPass).equals(rawPass);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setAlgorithm(java.lang.String)
    public void setAlgorithm(String algorithm) {
        pbeStringEncryptor.setAlgorithm(algorithm);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setPassword(java.lang.String)
    public void setPassword(String password) {
        pbeStringEncryptor.setPassword(password);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setProviderName(java.lang.String)
    public void setProviderName(String providerName) {
        pbeStringEncryptor.setProviderName(providerName);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setSaltGenerator(org.jasypt.salt.SaltGenerator)
    public void setSaltGenerator(SaltGenerator saltGenerator) {
        pbeStringEncryptor.setSaltGenerator(saltGenerator);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setSaltSizeBytes(int)
    public void setSaltSizeBytes(int saltSizeBytes) {
        pbeStringEncryptor.setSaltSizeBytes(saltSizeBytes);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setStringOutputType(java.lang.String)
    public void setStringOutputType(String stringOutputType) {
        pbeStringEncryptor.setStringOutputType(stringOutputType);
    }

    // ++ public void org.jasypt.encryption.pbe.PBEStringEncryptor org.jasypt.encryption.pbe.PBEStringEncryptor.setKeyObtentionIterations(int)
    public void setKeyObtentionIterations(int keyObtentionIterations) {
        pbeStringEncryptor.setKeyObtentionIterations(keyObtentionIterations);
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }
}
```