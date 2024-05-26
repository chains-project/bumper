```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder() {
        setPassword("mypassword");
    }

    public void setAlgorithm(String algorithm) {
        setAlgorithm(algorithm);
    }

    public void setKeyObtentionIterations(int keyObtentionIterations) {
        setKeyObtentionIterations(keyObtentionIterations);
    }

    public void setPoolSize(int poolSize) {
        setPoolSize(poolSize);
    }

    public void setProviderName(String providerName) {
        setProviderName(providerName);
    }

    public void setSaltGeneratorClassName(String saltGeneratorClassName) {
        setSaltGeneratorClassName(saltGeneratorClassName);
    }

    public void setStringOutputType(String stringOutputType) {
        setStringOutputType(stringOutputType);
    }

    public void setRegisteredName(String registeredName) {
        setRegisteredName(registeredName);
    }

}
```