Here's the proposed patch for the failing method:
```java
import java.util.Random;
import java.util.StringJoiner;

public static String generateRandomString(int length) {
    Random random = new Random();
    StringJoiner stringJoiner = new StringJoiner("");
    for (int i = 0; i < length; i++) {
        stringJoiner.add(Character.toString((char) ('a' + random.nextInt(26))));
    }
    return stringJoiner.toString();
}
```
This code replaces the usage of `RandomStringUtils` from Apache Commons Lang3 library with a custom implementation using `StringJoiner` and `Random` from Java Standard Library. The implementation generates a random string of length `length` by selecting a random character from 'a' to 'z'.