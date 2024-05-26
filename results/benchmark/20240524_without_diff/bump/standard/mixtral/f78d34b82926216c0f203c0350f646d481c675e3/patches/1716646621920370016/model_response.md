Here's the proposed patch for the failing client code:
```java
import org.apache.commons.text.RandomStringGenerator;

...

private static final String randomString = new RandomStringGenerator.Builder()
                                                .withinRange('a', 'z')
                                                .build()
                                            .generate(10);
```
This patch replaces the usage of `org.apache.commons.lang3.RandomStringUtils` with `org.apache.commons.text.RandomStringGenerator`, as the former has been removed in the latest version of the library. The new class provides similar functionality, allowing you to generate random strings within a specific range of characters.