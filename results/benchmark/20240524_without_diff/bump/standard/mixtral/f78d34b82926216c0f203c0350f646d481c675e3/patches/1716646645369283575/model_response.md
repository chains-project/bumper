Here's the updated code to fix the failure:
```java
import org.apache.commons.text.RandomStringGenerator;

// ...

private static final String GENERATE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

// ...

public static String generateRandomString(final int length) {
    final RandomStringGenerator randomStringGenerator = new RandomStringGenerator.Builder()
            .withinRange(33, 126)
            .usingChars(GENERATE_ALPHABET)
            .build();

    return randomStringGenerator.generate(length);
}
```
The `org.apache.commons.lang3.RandomStringUtils` has been replaced with `org.apache.commons.text.RandomStringGenerator` from Apache Commons Text 1.9.0 or later. Also, the method `generateRandomString` has been updated to use the new `RandomStringGenerator` class.