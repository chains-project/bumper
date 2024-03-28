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
                " Pulled"
            )
        );
    }
```
The error is caused by the fact that the `StringContains` constructor takes two parameters of the same type, and the compiler can't infer the types correctly. We can fix this by using the `AllOf` class from the same package, which takes two matchers as arguments and returns a matcher that matches both. We create two `StringContains` matchers, one for the "Status: Downloaded newer image for" string and one for the " Pulled" string, and pass them to the `AllOf` constructor. This should fix the error and make the code compile.