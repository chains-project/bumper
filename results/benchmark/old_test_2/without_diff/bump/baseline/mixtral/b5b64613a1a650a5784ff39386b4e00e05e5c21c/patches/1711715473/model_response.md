Here is a fixed version of the method that should resolve the error:
```java
import static org.apache.commons.lang3.StringUtils.isBlank;

@Override
public CreateJFrogInstanceStepExtension step(StepContext context) {
    String url = context.get(URL_CONTEXT_KEY);
    String apiKey = context.get(API_KEY_CONTEXT_KEY);
    String apiKeySecret = context.get(API_SECRET_CONTEXT_KEY);
    String verifySsl = context.get(VERIFY_SSL_CONTEXT_KEY);
    String verifyFingerprints = context.get(VERIFY_FINGERPRINTS_CONTEXT_KEY);
    String connectTimeout = context.get(CONNECT_TIMEOUT_CONTEXT_KEY);
    String readTimeout = context.get(READ_TIMEOUT_CONTEXT_KEY);
    String proxyHost = context.get(PROXY_HOST_CONTEXT_KEY);
    String proxyPort = context.get(PROXY_PORT_CONTEXT_KEY);
    String nonProxyHosts = context.get(NON_PROXY_HOSTS_CONTEXT_KEY);
    String trustAllCerts = context.get(TRUST_ALL_CERTS_CONTEXT_KEY);

    if (isBlank(url)) {
        throw new MissingRequiredContextVar(URL_CONTEXT_KEY);
    }

    if (isBlank(apiKey)) {
        throw new MissingRequiredContextVar(API_KEY_CONTEXT_KEY);
    }

    if (isBlank(apiKeySecret)) {
        throw new MissingRequiredContextVar(API_SECRET_CONTEXT_KEY);
    }

    boolean verifySslValue = Boolean.parseBoolean(verifySsl);
    boolean verifyFingerprintsValue = Boolean.parseBoolean(verifyFingerprints);
    boolean trustAllCertsValue = Boolean.parseBoolean(trustAllCerts);

    int connectTimeoutValue = Integer.parseInt(connectTimeout);
    int readTimeoutValue = Integer.parseInt(readTimeout);

    Proxy proxy = createProxy(proxyHost, proxyPort, nonProxyHosts);

    return new CreateJFrogInstanceStepExtension(url, apiKey, apiKeySecret, verifySslValue,
            verifyFingerprintsValue, connectTimeoutValue, readTimeoutValue,
            proxy, trustAllCertsValue);
}
```
In this version, I replaced the usage of `isAllBlank` with `isBlank`, which is still present in the `org.apache.commons.lang3.StringUtils` class. This should resolve the "cannot find symbol" error you were encountering.