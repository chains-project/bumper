Sure, I understand the requirements. Here's a possible patch for the failing code:
```java
import org.apache.commons.lang3.RandomStringGenerator;
import org.apache.commons.lang3.text.WordUtils;

public static String generateRandomString(int length) {
    RandomStringGenerator generator = RandomStringGenerator.builder()
        .withinRange('A', 'z')
        .build();
    return WordUtils.capitalizeFully(generator.generate(length));
}
```
Explanation:

* I replaced the usage of `RandomStringUtils` with `RandomStringGenerator` from the same library version.
* I also added an import statement for `WordUtils` from the same library version, which can be used to capitalize the first letter of the generated string.
* The function signature remains unchanged.
* I created a new variable `generator` to generate random strings of the given length.
* I used `WordUtils.capitalizeFully()` to capitalize the first letter of the generated string.
* The function returns the capitalized string.

Note: This is just one possible solution. There might be other ways to fix the code while meeting the given requirements.