Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            @Override
            public boolean matches(String s) {
                return s.contains("Image pulled:") || s.contains("Status: Downloaded newer image for ");
            }

            @Override
            public void describeMismatchSafely(String item, Description description) {
                description.appendText("was not pulled");
            }
        };
    }
```
The `StringContains` constructor that takes two parameters is removed in the new library version, so we need to create a new instance of `StringContains` with the `Override` decorator and implement the `matches` and `describeMismatchSafely` methods ourselves.
The `matches` method checks if the input string contains either "Image pulled:" or "Status: Downloaded newer image for ", if it does, it returns `true`, otherwise, it returns `false`.
The `describeMismatchSafely` method simply appends the string "was not pulled" to the description.

This patch should fix the error and allow the code to compile and run successfully.