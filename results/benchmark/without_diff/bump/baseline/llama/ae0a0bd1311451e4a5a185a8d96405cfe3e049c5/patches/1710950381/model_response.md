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
The patch creates a new `AllOf` matcher that combines two `StringContains` matchers. The first `StringContains` matcher checks for the presence of "Status: Downloaded newer image for" followed by the image name, and the second `StringContains` matcher checks for the presence of " Pulled". By combining these two matchers, the `imagePulled` method will only return a match when both conditions are met, which should fix the error.


Note that the `StringContains` constructor that takes a single string argument has been removed in the latest version of the Hamcrest library, which is why the error message mentions that the constructor cannot be applied to the given types. The `AllOf` class is a better choice in this case, as it allows combining multiple matchers in a more readable way.