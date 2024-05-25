Here's a patch for the failing client code:

```java
import static org.apache.commons.lang3.StringUtils.isAllEmpty;

// ...

@Override
public CreateJFrogInstanceStep executeStep(StepContext context) throws IOException, InterruptedException {
    // ...
    if (isAllEmpty(jfrogInstanceId, url, apiKey, apiSecret, verifyCertificates, trustAllCerts)) {
    // ...
}
```

The `isAllBlank` method has been replaced with `isAllEmpty` to resolve the dependency issue. The method behavior is similar, but it checks for null or empty strings instead of whitespace-only strings.

Confidence: 90%

In case there are specific cases in which you need to check for whitespace-only strings, you can update the condition as follows:

```java
if (isAllEmpty(jfrogInstanceId, url, apiKey, apiSecret, verifyCertificates, trustAllCerts)
        || hasOnlyWhitespace(jfrogInstanceId, url, apiKey, apiSecret, verifyCertificates, trustAllCerts)) {
    // ...
}

// ...

private static boolean hasOnlyWhitespace(String... strings) {
    for (String str : strings) {
        if (str != null && !str.trim().isEmpty()) {
            return true;
        }
    }
    return false;
}
```

Confidence: 80% (depending on the specific requirements of the code)