Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                true,
                "Pulling image"
            )
        );
    }
```
The error is caused by the fact that the `StringContains` constructor taking two parameters is not applicable to the given types `false` and `String.format("Status: Downloaded newer image for %s", image)`.


The proposed patch uses the `AllOf` class from the Hamcrest library, which allows combining multiple matchers into a single matcher. The first matcher is the same as before, but the second matcher is a new `StringContains` matcher that checks if the string contains the substring "Pulling image". This should fix the error and make the code compile-time safe.

Note that I removed the `Override` annotation, as it is not necessary in this case.