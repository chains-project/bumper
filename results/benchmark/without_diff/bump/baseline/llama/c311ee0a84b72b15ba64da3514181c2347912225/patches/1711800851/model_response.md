```
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                false,
                "image pulled"
            )
        );
    }
```
The `StringContains` class has been replaced with `AllOf`, which is a class from the Hamcrest library that allows combining multiple matchers. The `StringContains` matcher has been split into two separate matchers, each with its own `StringContains` matcher. The first `StringContains` matcher checks for the presence of the phrase "Status: Downloaded newer image for" followed by the image name, while the second `StringContains` matcher checks for the presence of the phrase "image pulled". Both matchers are combined using the `AllOf` class to create a single matcher that matches both conditions. This should fix the error caused by the external dependency.