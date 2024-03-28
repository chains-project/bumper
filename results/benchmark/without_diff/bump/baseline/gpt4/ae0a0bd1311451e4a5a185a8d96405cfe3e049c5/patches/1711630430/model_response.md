```java
private Matcher<String> layersAlreadyExist() {
    return new TypeSafeMatcher<String>() {
        @Override
        protected boolean matchesSafely(String item) {
            return item.contains(String.format("%s: Layer already exists", image.layer()));
        }

        @Override
        public void describeTo(Description description) {
            description.appendText("a string containing 'Layer already exists'");
        }
    };
}
```