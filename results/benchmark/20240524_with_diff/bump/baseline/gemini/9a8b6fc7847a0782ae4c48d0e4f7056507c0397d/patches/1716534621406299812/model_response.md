```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.StrongTextEncryptor;

public StandardPBEStringEncryptor pbeStringEncryptor = new StandardPBEStringEncryptor();
public StrongTextEncryptor textEncryptor = new StrongTextEncryptor();

public GeoStorePBEPasswordEncoder(String password) {
    pbeStringEncryptor.setPassword(password);
    textEncryptor.setPassword(password);
}

public String encode(String password) {
    return pbeStringEncryptor.encrypt(password);
}

public boolean matches(String rawPassword, String encodedPassword) {
    return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
}

public void setAlgorithm(String algorithm) {
    pbeStringEncryptor.setAlgorithm(algorithm);
}

public void setKeyObtentionIterations(int keyObtentionIterations) {
    pbeStringEncryptor.setKeyObtentionIterations(keyObtentionIterations);
}

public void setPoolSize(int poolSize) {
    pbeStringEncryptor.setPoolSize(poolSize);
}

public void setSaltGenerator(org.jasypt.salt.SaltGenerator saltGenerator) {
    pbeStringEncryptor.setSaltGenerator(saltGenerator);
}

public void setStringOutputType(String stringOutputType) {
    pbeStringEncryptor.setStringOutputType(stringOutputType);
}

public void setProviderName(String providerName) {
    pbeStringEncryptor.setProviderName(providerName);
}

public void setProvider(org.jasypt.encryption.pbe.PBEStringEncryptor.PBEProvider provider) {
    pbeStringEncryptor.setProvider(provider);
}

public void setConfig(org.jasypt.encryption.pbe.config.PBEConfig config) {
    pbeStringEncryptor.setConfig(config);
}

public void setRegisteredName(String registeredName) {
    pbeStringEncryptor.setRegisteredName(registeredName);
}

public void setEncryptionParameters(String encryptionParameters) {
    pbeStringEncryptor.setEncryptionParameters(encryptionParameters);
}

public void setSaltSizeBytes(int saltSizeBytes) {
    pbeStringEncryptor.setSaltSizeBytes(saltSizeBytes);
}

public void setPassword(String password) {
    pbeStringEncryptor.setPassword(password);
}

public void setDigest(String digest) {
    pbeStringEncryptor.setDigest(digest);
}

public void setDigestAlgorithm(String digestAlgorithm) {
    pbeStringEncryptor.setDigestAlgorithm(digestAlgorithm);
}

public void setStringDigester(org.jasypt.digest.StringDigester stringDigester) {
    pbeStringEncryptor.setStringDigester(stringDigester);
}

public void setIvGenerator(org.jasypt.iv.IvGenerator ivGenerator) {
    pbeStringEncryptor.setIvGenerator(ivGenerator);
}

public void setIvSizeBytes(int ivSizeBytes) {
    pbeStringEncryptor.setIvSizeBytes(ivSizeBytes);
}

public void setKeyLength(int keyLength) {
    pbeStringEncryptor.setKeyLength(keyLength);
}

public void setInputProvider(String inputProvider) {
    pbeStringEncryptor.setInputProvider(inputProvider);
}

public void setOutputProvider(String outputProvider) {
    pbeStringEncryptor.setOutputProvider(outputProvider);
}

public void setAlgorithm(String algorithm) {
    textEncryptor.setAlgorithm(algorithm);
}

public void setKeyObtentionIterations(int keyObtentionIterations) {
    textEncryptor.setKeyObtentionIterations(keyObtentionIterations);
}

public void setPoolSize(int poolSize) {
    textEncryptor.setPoolSize(poolSize);
}

public void setSaltGenerator(org.jasypt.salt.SaltGenerator saltGenerator) {
    textEncryptor.setSaltGenerator(saltGenerator);
}

public void setStringOutputType(String stringOutputType) {
    textEncryptor.setStringOutputType(stringOutputType);
}

public void setProviderName(String providerName) {
    textEncryptor.setProviderName(providerName);
}

public void setProvider(org.jasypt.util.text.TextEncryptor.TextEncryptorProvider provider) {
    textEncryptor.setProvider(provider);
}

public void setConfig(org.jasypt.encryption.pbe.config.PBEConfig config) {
    textEncryptor.setConfig(config);
}

public void setRegisteredName(String registeredName) {
    textEncryptor.setRegisteredName(registeredName);
}

public void setEncryptionParameters(String encryptionParameters) {
    textEncryptor.setEncryptionParameters(encryptionParameters);
}

public void setSaltSizeBytes(int saltSizeBytes) {
    textEncryptor.setSaltSizeBytes(saltSizeBytes);
}

public void setPassword(String password) {
    textEncryptor.setPassword(password);
}

public void setDigest(String digest) {
    textEncryptor.setDigest(digest);
}

public void setDigestAlgorithm(String digestAlgorithm) {
    textEncryptor.setDigestAlgorithm(digestAlgorithm);
}

public void setStringDigester(org.jasypt.digest.StringDigester stringDigester) {
    textEncryptor.setStringDigester(stringDigester);
}

public void setIvGenerator(org.jasypt.iv.IvGenerator ivGenerator) {
    textEncryptor.setIvGenerator(ivGenerator);
}

public void setIvSizeBytes(int ivSizeBytes) {
    textEncryptor.setIvSizeBytes(ivSizeBytes);
}

public void setKeyLength(int keyLength) {
    textEncryptor.setKeyLength(keyLength);
}

public void setInputProvider(String inputProvider) {
    textEncryptor.setInputProvider(inputProvider);
}

public void setOutputProvider(String outputProvider) {
    textEncryptor.setOutputProvider(outputProvider);
}

```