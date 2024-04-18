I've analyzed the issue and found a solution. Here's the fixed version of the failing method:

```java
import org.apache.commons.text.RandomStringGenerator;

...

@Test
@Override
public void testRandomStringGeneration() throws Exception {
    final int length = 10;
    final RandomStringGenerator generator = new RandomStringGenerator.Builder()
        .withinRange('a', 'z')
        .build();
    final String randomString = generator.generate(length);
    assertTrue(randomString.length() == length);
}
```

In this solution, I replaced the usage of the removed `RandomStringUtils` class from Apache Commons Lang with the `RandomStringGenerator` class from Apache Commons Text. This class provides similar functionality and can generate random strings, which fixes the issue caused by the removed method.