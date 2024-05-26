Here's the proposed patch for the failing method:
```java
import org.apache.commons.text.RandomStringGenerator;

// ...

public static String generateRandomString(int length) {
    RandomStringGenerator generator = new RandomStringGenerator.Builder()
            .withinRange('0', 'z')
            .build();
    return generator.generate(length);
}
```
In this patch, I replaced the usage of `org.apache.commons.lang3.RandomStringUtils` with `org.apache.commons.text.RandomStringGenerator` since the former has been removed. This new class provides similar functionality for generating random strings.