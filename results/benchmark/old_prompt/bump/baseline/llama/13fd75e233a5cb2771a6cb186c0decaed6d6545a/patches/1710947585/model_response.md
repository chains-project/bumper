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
                "pullImage"
            )
        );
    }
```
The error was caused by trying to create a `StringContains` matcher with a boolean value as its second argument. The `StringContains` constructor takes a substring to search for, not a boolean value.

Instead, we can create an `AllOf` matcher that combines two `StringContains` matchers: one that looks for the substring "Status: Downloaded newer image for" and another that looks for the substring "pullImage". This should match the expected output format of the "docker pull" command.

Note that I removed the `Override` annotation as it's not necessary and can be safely removed.